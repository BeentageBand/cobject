class APIGenerator:
    def __init__(self, data):
        self.data = data
        self.class_t = 'struct' if self.data.isa is '' else 'union'
        self.upper_case_name = data.name.upper()
        self.lower_case_name = data.name.lower()
    def print_api(self):
        print '#ifndef %s_H_' % (self.upper_case_name)
        print '#define %s_H_' % (self.upper_case_name)
        print '#include "cobject.h"'
        self.print_api_obj()
        print ''
        print 'extern struct Class * %s_Class();' % (self.data.name)
        self.print_api_constructor()
        self.print_api_methods()
        print ''
        print '#endif /*%s_H_*/' % (self.upper_case_name)
    def print_api_constructor(self):
        is_empty = True 
        for constructor in self.data.constructors:
            is_empty = False 
            print 'extern void %s_populate_%s(union %s * const %s%s)' % (self.data.name, \
                                                                     self.data.name, \
                                                                     constructor.name, \
                                                                     self.data.name, \
                                                                     self.lower_case_name, \
                                                                     self.print_api_params(constructor.params))
        if is_empty:
            print 'extern void %s_populate(union %s * const %s%s)' % (self.data.name, \
                                                                  self.data.name, \
                                                                  self.lower_case_name,
                                                                  self.print_api_params(self.data.members))
    def print_api_obj(self):
        print 'typedef union %s' % (self.data.name)
        print '{'
        print '    %s %s_Class _private * _private vtbl;' % (self.class_t, self.data.name)
        print '    struct'
        print '    {'
        if self.data.isa is '':
            print '        struct Object Object;'
        else:
            print '        union %s %s;' % (self.data.isa, self.data.isa)
        self.print_api_members()
        print '    };'
        print '}%s_T;' % (self.data.name)
    def print_api_members(self):
        for member in self.data.members:
            print '        %s %s %s;' % (member.type_t, member.ref_t, member.name)
    def print_api_class(self):
        print 'typedef struct %s_Class' % (self.data.name)
        print '{'
        if self.data.isa is '':
            print '    struct Class Class;'
        else:
            print '    %s_Class_T %s;' % (self.data.isa)
        self.print_api_methods()
        print '}%s_Class_T;' % (self.data.name)
    def print_api_methods(self):
        isa_methods = []
        class_isa = self.data.isa
        while class_isa is not None:
            isa_methods += class_isa.methods
            class_isa = class_isa.isa
        
        for method in (isa_methods + self.data.methods):
            print 'extern %s %s_%s(union %s * const %s%s);' % (method.return_t, \
                                                                     self.data.name, \
                                                                     method.name, \
                                                                     self.data.name, \
                                                                     self.lower_case_name, \
                                                                     self.print_api_params(method.params))
    def print_api_params(self, params = []):
        param_out = ''
        for param in params:
            param_out = param_out + ', %s %s %s' % (param.type_t, param.ref_t, param.name)
        return param_out

