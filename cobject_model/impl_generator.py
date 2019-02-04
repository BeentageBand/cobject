class ImplGenerator:
    def __init__(self, data):
        self.data = data
        self.upper_case_name = data.name.upper()
        self.lower_case_name = data.name.lower()
    def print_impl(self):
        print '#define COBJECT_IMPLEMENTATION'
        print '#include "%s.h"' % (self.lower_case_name)
        print ''
        print 'static void %s_delete(struct Object * const obj);'
        self.print_impl_prototypes()
        print '%s_Class_T %s =' % (self.data.name, self.data.name)
        print '{'
        print '    {NULL, %s_delete},' % (self.lower_case_name)
        self.print_impl_methods()
        print '};'
        print ''
        print 'static union %s %s = {NULL};' % (self.data.name, self.data.name)
    def print_impl_prototypes(self):
        for method in self.data.methods:
            print 'static %s %s_%s(union %s * const this%s);' % (method.return_t, self.lower_case_name, method.name, self.data.name, self.print_impl_params(method.params))
    def print_impl_methods(self):
        for method in self.data.methods:
            print '    %s_%s,' % (self.lower_case_name, method.name)
    def print_impl_params(self, params):
        param_out = ''
        for param in params:
            param_out = param_out + ', %s %s %s' % (param.type_t, param.ref_t, param.name)
        return param_out
        


