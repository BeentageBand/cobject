class ClassParser(object):
    def __init__(self, data):
        self.data = data

    def get_decl(self):
        fmt = {'name': self.data.name, 'union': self.get_union_t(), 'class_t': self.get_class_t(),
               'isa_t': '%s %s %s;\n' % (self.data.isa[-2].type_t, self.data.isa[-2].name, self.data.isa[-2].name),
               'isa_list': self.get_cast_decl(''), 'isa_class_t': '%s %s_Class %s;\n' % (
                self.data.isa[-2].type_t, self.data.isa[-2].name, self.data.isa[-2].name),
               'isa_class_list': self.get_cast_decl('_Class'), 'members': self.get_members_decl(),
               'methods': self.get_methods_decl()}

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
};' % fmt

    def get_union_t(self):
        return 'union %s' % self.data.name

    def get_class_t(self):
        fmt = {'type_t': self.data.isa[-1].type_t, 'name': self.data.name}
        return '%(type_t)s %(name)s_Class' % fmt

    def get_cast_decl(self, suffix):
        isa_list = ''
        print(len(self.data.isa))
        if len(self.data.isa) <= 2:
            return isa_list
        for i in self.data.isa[1:-1]:
            isa_list = '%s %s%s %s;\n' % (i.type_t, i.name, suffix, i.name)
        return isa_list

    def get_members_decl(self):
        member_list = ''
        for m in self.data.members:
            member_list += '%s _private %s;\n' % (m.type_t, m.name)
        return member_list

    def get_class_method_decl(self):
        fmt = {'class_t': self.get_class_t(), 'name': self.data.name}
        return 'extern %(class_t)s * Get_%(name)s_Class(void);\n' % fmt

    def get_methods_decl(self):
        method_list = ''
        adapter = FunctionAdapter()
        for m in self.data.methods:
            method_list += adapter.get_cbk_decl(self.data, m.return_t, m.name, m.params)
        return method_list

    def get_class_method_impl(self):
        fmt = {'name': self.data.name, 'class_t': self.get_class_t(), 'lower_name': self.data.name.lower(),
               'isa': 'NULL' if self.data.isa[-2].name == 'Object' else '&Get_%s_Class()->Class' % self.data.isa[
                   -2].name}
        return '\
%(class_t)s * Get_%(name)s_Class(void)\n\
{\n\
  static %(class_t)s clazz = {};\n\
  if (0 != clazz.Class.offset) return &clazz;\n\
  Class_populate(&clazz.Class, sizeof(clazz), %(isa)s);\n\
  %(lower_name)s_override(&clazz);\n\
  return &clazz;\n\
}' % fmt

    def get_methods_impl(self):
        method_list = ''
        adapter = FunctionAdapter()
        for m in self.data.methods:
            method_list += adapter.get_cbk_impl(self.data, m.return_t, m.name, m.params)
        return method_list

    def get_guard(self, suffix=None):
        if suffix is not None:
            suffix = '_' + suffix
        fmt = {'upper': self.data.name.upper(), 'suffix': suffix if suffix else ''}
        return '#ifndef %(upper)s%(suffix)s_H\n#define %(upper)s%(suffix)s_H' % fmt

    def get_guard_end(self, suffix=None):
        if suffix is not None:
            suffix = '_' + suffix
        fmt = {'upper': self.data.name.upper(), 'suffix': suffix if suffix else ''}
        return '#endif /*%(upper)s%(suffix)s_H*/' % fmt


class TemplateParser(ClassParser):
    def __init__(self, data):
        super(TemplateParser, self).__init__(data)

    def get_template_def(self, lower_case=False):
        fmt = {'name': self.data.name, 'name_lower': self.data.name.lower(), 'prefix': self.data.prefix,
               'prefix_lower': self.data.prefix.lower()}
        output = '#define %(name)s TEMPLATE(%(prefix)s, %(prefix)s_Params)\n' % fmt
        output += '#define %(name)s_Class TEMPLATE(%(prefix)s, %(prefix)s_Params, Class)\n' % fmt
        output += '#define Get_%(name)s_Class TEMPLATE(Get, %(prefix)s, %(prefix)s_Params, Class)\n' % fmt

        for m in self.data.methods:
            fmt['method'] = m.name
            output += '#define %(name)s_%(method)s TEMPLATE(%(prefix)s, %(prefix)s_Params, %(method)s)\n' % fmt

        if lower_case:
            fmt['method'] = 'override'
            output += '#define %(name_lower)s_%(method)s template(%(prefix_lower)s, %(prefix)s_Params, \
%(method)s)\n' % fmt
            fmt['method'] = 'delete'
            output += '#define %(name_lower)s_%(method)s template(%(prefix_lower)s, %(prefix)s_Params, \
        %(method)s)\n' % fmt
        for m in self.data.methods if lower_case else []:
            fmt['method'] = m.name
            output += '#define %(name_lower)s_%(method)s TEMPLATE(%(prefix_lower)s, %(prefix)s_Params, \
%(method)s)\n' % fmt

        fmt['populate'] = 'populate'
        output += '#define %(name)s_%(populate)s TEMPLATE(%(prefix)s, %(prefix)s_Params, %(populate)s)\n' % fmt

        return output

    def get_template_undef(self, lower_case=False):
        fmt = {'name': self.data.name}
        output = ''
        output += '#undef %(name)s\n#undef %(name)s_Class\n#undef Get_%(name)s_Class\n' % fmt

        for m in self.data.methods:
            output += '#undef %s_%s\n' % (self.data.name, m.name)

        if lower_case:
            output += '#undef %s_override\n' % self.data.name.lower()
            output += '#undef %s_delete\n' % self.data.name.lower()

        for m in self.data.methods if lower_case else []:
            output += '#undef %s_%s\n' % (self.data.name.lower(), m.name)

        output += '#undef %s_%s\n' % (self.data.name, 'populate')
        return output

    def get_typenames_def(self):
        fmt = {'name': self.data.name, 'prefix': self.data.prefix}

        i = 0
        output = ''
        for t in self.data.typenames:
            i += 1
            fmt['i'] = i
            fmt['typename'] = t
            output += '#define %(typename)s T_Param(%(i)i, %(prefix)s_Params)\n' % fmt
        return output

    def get_typenames_undef(self):
        output = ''
        fmt = {}
        for t in self.data.typenames:
            fmt['typename'] = t
            output += '#undef %(typename)s\n' % fmt
        return output

    def get_constructor_def(self):
        output = ''
        fmt = {'name': self.data.name, 'prefix': self.data.prefix}
        for c in self.data.constructors:
            fmt['constructor'] = c.name
            output += '#define %(name)s_populate_%(constructor)s \
        TEMPLATE(%(prefix)s, %(prefix)s_Params, populate, %(constructor)s)' % fmt
        return output

    def get_constructor_undef(self):
        output = ''
        fmt = {'name': self.data.name}
        for c in self.data.constructors:
            fmt['constructor'] = c.name
            output += '#undef %(name)s_populate_%(constructor)s' % fmt
        return output


class FunctionAdapter:
    def __init__(self):
        pass

    def get_extern_decl(self, clazz, return_t, name, params):
        fmt = {'name': clazz.name, 'lower': clazz.name.lower(), 'return_t': return_t,
               'method': '%s_%s' % (clazz.name, name), 'param_list': self.get_params(params)}
        return 'extern %(return_t)s %(method)s(union %(name)s * const %(lower)s%(param_list)s);\n' % fmt

    def get_cbk_decl(self, clazz, return_t, name, params):
        fmt = {'name': clazz.name, 'lower': clazz.name.lower(), 'return_t': return_t, 'method': name,
               'param_list': self.get_params(params)}
        return '%(return_t)s (* _private %(method)s)(union %(name)s * const %(lower)s%(param_list)s);\n' % fmt

    def get_cbk_impl(self, clazz, return_t, name, params):
        fmt = {'name': clazz.name, 'lower': clazz.name.lower(), 'return_t': return_t, 'method': name,
               'param_list': self.get_params(params), 'param_values': self.get_param_values(params)}
        return '\
%(return_t)s %(name)s_%(method)s(union %(name)s * const %(lower)s%(param_list)s)\n\
{\n\
  return %(lower)s->vtbl->%(method)s(%(lower)s%(param_values)s);\n\
}\n' % fmt

    @staticmethod
    def get_define(self, clazz, name):
        return '#define %(name)s_%(method)s TEMPLATE(%(name)s_ \n\n'

    @staticmethod
    def get_params(params=None):
        if params is None:
            params = []
        param_list = ''
        for p in params:
            param_list += ', %s const %s' % (p.type_t, p.name)
        return param_list

    @staticmethod
    def get_param_values(params=None):
        if params is None:
            params = []
        param_values = ''
        for p in params:
            param_values += ', %s' % p.name
        return param_values


class ConstructorParser:
    def __init__(self, data):
        self.data = data
        self.fmt = {'name': data.name, 'lower': data.name.lower()}
        self.function_adapter = FunctionAdapter()

    def get_decl(self):
        default_constructor = self.function_adapter.get_extern_decl(self.data, 'void', 'populate', self.data.members)
        constructor_list = '%s\n' % default_constructor
        for c in self.data.constructors:
            ctor = self.function_adapter.get_extern_decl(self.data, c.return_t, 'populate_' + c.name, c.params)
            constructor_list += '%s\n' % ctor
        return constructor_list


class MethodParser:
    def __init__(self, data):
        self.data = data
        self.function_adapter = FunctionAdapter()

    def get_decl(self):
        method_list = ''
        for m in self.data.methods:
            method = self.function_adapter.get_extern_decl(self.data, m.return_t, m.name, m.params)
            method_list += '%s\n' % method
        return method_list

    def get_impl(self):
        method_list = ''
        for m in self.data.methods:
            method = self.function_adapter.get_cbk_impl(self.data, m.return_t, m.name, m.params)
            method_list += '%s\n' % method
        return method_list

    def get_define(self):
        method_list = ''
        for m in self.data.methods:
            method = self.function_adapter.get_define(self.data, m.name)
