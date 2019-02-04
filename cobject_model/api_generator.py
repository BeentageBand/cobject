class APIGenerator:
    def __init__(self, data):
        self.data = data
        self.upper_case_name = data.name.upper()
        self.lower_case_name = data.name.lower()
    def print_api(self):
        print '#ifndef %s_H_' % (self.upper_case_name)
        print '#define %s_H_' % (self.upper_case_name)
        print '#include "cobject.h"'
        self.print_api_obj()
        print ''
        self.print_api_class()
        print ''
        print 'extern %s_Class_T _private %s_Class;' % (self.data.name, self.data.name)

        print '#endif /*%s_H_*/' % (self.upper_case_name)
    def print_api_obj(self):
        print 'typedef union %s' % (self.data.name)
        print '{'
        print '    %s_Class_T _private * _private vtbl;' % (self.data.name)
        print '    struct'
        print '    {'
        if self.data.isa is '':
            print '        struct Object Object;'
        else:
            print '        union %s %s;' % (self.data.isa)
        self.print_api_members()
        print '    }'
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
        for method in self.data.methods:
            print '    %s (*_private %s)(union %s * const %s%s);' % (method.return_t, \
                                                                     method.name, \
                                                                     self.data.name, \
                                                                     self.lower_case_name, \
                                                                     self.print_api_params(method.params))
    def print_api_params(self, params = []):
        param_out = ''
        for param in params:
            param_out = param_out + ', %s %s %s' % (param.type_t, param.ref_t, param.name)
        return param_out

