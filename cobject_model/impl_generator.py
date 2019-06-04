class ImplGenerator:
    def __init__(self, data):
        self.data = data
        self.class_t = 'struct' if self.data.isa is '' else 'union'
        self.upper_case_name = data.name.upper()
        self.lower_case_name = data.name.lower()
    def print_impl(self):
        print '#define COBJECT_IMPLEMENTATION'
        print '#include "%s.h"' % (self.lower_case_name)
        print ''
        self.print_impl_class()
        print 'typedef %s %s_Class' % (self.class_t, self.data.name)
        print '{'
        print ''
        print 'static void %s_delete(struct Object * const obj);' % (self.lower_case_name)
        print 'static void %s_populate(union %s * const %s);' % (self.lower_case_name, self.data.name, self.lower_case_name)
        print 'static void %s_class(%s %s_Class const * %s_class)' % (self.lower_case_name, \
                                                                      self.class_t, \
                                                                      self.data.name, \
                                                                      self.lower_case_name) 
        self.print_impl_prototypes()
        print ''
        print 'struct Class * %s_Class(void)' % (self.data.name)
        print '{'
        print '    static %s_Class_T clazz = {NULL, NULL, sizeof(%s_Class_T)};' % (self.data.name, self.data.name)
        if self.data.isa is not '':
            print '    if (NULL == clazz.parent)'
            print '        Class_Init(&clazz.Class,%s_Class());' % (self.data.isa)
        print '    %s_class(&clazz);' % (self.lower_case_name)
        print '    return &clazz.Class;'
        print '}'
    def print_impl_class(self):
        print 'typedef %s %s_Class' % (self.class_t, self.data.name)
        print '{'
        if self.data.isa is '':
            print '    struct Class Class;'
            self.print_impl_methods('    ')
        else:
            print '    struct'
            print '    {'
            print '        struct Class Class;'
            self.print_impl_methods('        ')
            print '    };'
        print '}%s_Class_T' % (self.data.name)
    def print_impl_prototypes(self):
        for method in self.data.methods:
            print 'static %s %s_%s(union %s * const this%s);' % (method.return_t, \
                                                                 self.lower_case_name, \
                                                                 method.name, \
                                                                 self.data.name, \
                                                                 self.print_impl_params(method.params))
    def print_impl_methods(self, identation):
        for method in self.data.methods:
            print '%s(*%s)(%s %s * const%s)' % (identation, \
                                                method.name, \
                                                self.class_t, \
                                                self.data.name, \
                                                self.print_impl_params(method.params))
    def print_impl_params(self, params):
        param_out = ''
        for param in params:
            param_out = param_out + ', %s %s %s' % (param.type_t, param.ref_t, param.name)
        return param_out
