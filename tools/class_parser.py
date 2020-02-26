from class_data import *
class ClassParser:
    def __init__(self, data):
        self.data = data
    def get_decl(self):
        fmt = {}
        fmt['name'] = self.data.name
        fmt ['union'] = self.get_union_t()
        fmt ['class_t'] = self.get_class_t()
        fmt['isa_t'] = '%s %s %s;\n' % (self.data.isa[-2].type_t, self.data.isa[-2].name, self.data.isa[-2].name)
        fmt['isa_list'] = self.get_cast_decl('')
        fmt['isa_class_t'] = '%s %s_Class %s;\n' % (self.data.isa[-2].type_t, self.data.isa[-2].name, self.data.isa[-2].name)
        fmt['isa_class_list'] = self.get_cast_decl('Class')
        fmt['members'] = self.get_members_decl()
        fmt['methods'] = self.get_methods_decl()

        return '\
%(union)s;\n\
%(class_t)s\n\
{\n\
    %(isa_class_list)s\n\
    struct\n\
    {\n\
    struct Class Class;\n\
    %(methods)s\n\
    };\n\
};\n\n\
%(union)s\n\
{\n\
    %(class_t)s * vtbl;\n\
    %(isa_list)s\
    struct\n\
    {\n\
      union Object Object;\n\
      %(members)s\n\
    };\n\
};' % (fmt)
    def get_union_t(self):
        return 'union %s' % (self.data.name)
    def get_class_t(self):
        fmt = {}
        fmt['type_t'] = self.data.isa[-1].type_t
        fmt['name'] = self.data.name
        return '%(type_t)s %(name)s_Class' % (fmt)
    def get_cast_decl(self, suffix):
        isa_list = ''
        print len(self.data.isa)
        if len(self.data.isa) <= 2:
            return isa_list
        for i in self.data.isa[1:-1]:
            isa_list = '%s %s_%s %s;\n' % (i.type_t, i.name, suffix, i.name)
        return isa_list
    def get_members_decl(self):
        member_list = ''
        for m in self.data.members:
            member_list += '%s _private %s;\n' % (m.type_t, m.name)
        return member_list
    def get_class_method_decl(self):
        fmt = {}
        fmt ['class_t'] = self.get_class_t()
        fmt ['name'] = self.data.name
        return 'extern %(class_t)s * Get_%(name)s_Class(void);\n' % (fmt)
    def get_methods_decl(self):
        method_list = ''
        adapter = FunctionAdapter()
        for m in self.data.methods:
            method_list += adapter.get_cbk_decl(self.data, m.return_t, m.name, m.params)
        return method_list
    def get_class_method_impl(self):
        fmt = {}
        fmt ['name'] = self.data.name
        fmt ['class_t'] = self.get_class_t()
        fmt ['lower_name'] = self.data.name.lower()
        fmt ['isa'] = self.data.isa[-1].name
        return '\
%(class_t)s * Get_%(name)s_Class(void)\n\
{\n\
  static %(class_t)s clazz;\n\
  if (0 != clazz.Class.offset) return &clazz;\n\
  Class_populate(&clazz.Class, sizeof(clazz),\n\
		 (Class_Delete_T)%(lower_name)s_delete,\n\
		 Get_%(isa)s_Class());\n\
  %(lower_name)s_override(&clazz);\n\
  return &clazz;\n\
}' % (fmt)
    def get_methods_impl(self):
        method_list = ''
        adapter = FunctionAdapter()
        for m in self.data.methods:
            method_list += adapter.get_cbk_impl(self.data, m.return_t, m.name, m.params)
        return method_list

class FunctionAdapter:
    def get_extern_decl(self, clazz, return_t, name, params):
        fmt = {}
        fmt ['name'] = clazz.name
        fmt ['lower'] = clazz.name.lower()
        fmt ['return_t'] = return_t
        fmt ['method'] =  '%s_%s' % (clazz.name, name)
        fmt ['param_list'] = self.get_params(params)
        return 'extern %(return_t)s %(method)s(union %(name)s * const %(lower)s%(param_list)s);\n' % (fmt)
    def get_cbk_decl(self, clazz, return_t, name, params):
        fmt = {}
        fmt ['name'] = clazz.name
        fmt ['lower'] = clazz.name.lower()
        fmt ['return_t'] = return_t
        fmt ['method'] =  name
        fmt ['param_list'] = self.get_params(params)
        return '%(return_t)s (* _private %(method)s)(union %(name)s * const %(lower)s%(param_list)s);\n' % (fmt)
    def get_cbk_impl(self, clazz, return_t, name, params):
        fmt = {}
        fmt ['name'] = clazz.name
        fmt ['lower'] = clazz.name.lower()
        fmt ['return_t'] = return_t
        fmt ['method'] =  name
        fmt ['param_list'] = self.get_params(params)
        fmt ['param_values'] = self.get_param_values(params)
        return '\
%(return_t)s %(name)s_%(method)s(union %(name)s * const %(lower)s%(param_list)s)\n\
{\n\
  return %(lower)s->vtbl->%(method)s(%(lower)s%(param_values)s);\n\
}\n' % (fmt)
    def get_params(self, params = []):
        param_list = ''
        for p in params:
            param_list += ', %s const %s' % (p.type_t, p.name)
        return param_list
    def get_param_values(self, params = []):
        param_values = ''
        for p in params:
            param_values += ', %s' % (p.name)
        return param_values

class ConstructorParser:
    def __init__(self, data):
        self.data = data
        self.fmt = {}
        self.fmt ['name'] = data.name
        self.fmt ['lower'] = data.name.lower()
        self.function_adapter = FunctionAdapter()
    def get_decl(self):
        default_constructor = self.function_adapter.get_extern_decl(self.data, 'void', 'populate', self.data.members)
        constructor_list = '%s\n' % (default_constructor)
        for c in self.data.constructors:
            ctor = self.function_adapter.get_extern_decl(self.data, c.return_t, 'populate' + c.name, c.params)
            constructor_list += '%s\n' % (ctor)
        return constructor_list

class MethodParser:
    def __init__(self, data):
        self.data = data
        self.function_adapter = FunctionAdapter()
    def get_decl(self):
        method_list = ''
        for m in self.data.methods:
            method = self.function_adapter.get_extern_decl(self.data, m.return_t, m.name, m.params)
            method_list += '%s\n' % (method)
        return method_list
    def get_impl(self):
        method_list = ''
        for m in self.data.methods:
            method = self.function_adapter.get_cbk_impl(self.data, m.return_t, m.name, m.params)
            method_list += '%s\n' % (method)
        return method_list

