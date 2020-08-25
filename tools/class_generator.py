from .class_parser import ClassParser, ConstructorParser, MethodParser, TemplateParser


class CInterfaceGenerator(object):
    def __init__(self, data):
        self.class_parser = ClassParser(data)
        self.constructor_parser = ConstructorParser(data)
        self.methods_parser = MethodParser(data)
        self.fmt = {'upper': data.name.upper(), 'lower': data.name.lower(), 'name': data.name}
        isa = data.isa[-2].name.lower()
        self.fmt['isa'] = 'cobject/cobject' if isa in 'object' else isa

    def generate(self):
        fmt = self.fmt
        fmt['class'] = self.class_parser.get_decl()
        fmt['class_method'] = self.class_parser.get_class_method_decl()
        fmt['constructors'] = self.constructor_parser.get_decl()
        fmt['methods'] = self.methods_parser.get_decl()
        fmt['guard'] = self.class_parser.get_guard()
        fmt['guard_end'] = self.class_parser.get_guard_end()
        return '%(guard)s\n\
#include "%(isa)s.h"\n\n\
#ifdef %(upper)s_IMPLEMENTATION \n\
#define _private\n\
#else\n\
#define _private const\n\
#endif \n\n\
#ifdef __cplusplus\n\
extern "C" {\n\
#endif\n\
\n\
%(class)s\n\n\
%(class_method)s\n\
%(constructors)s\
%(methods)s\
#ifdef __cplusplus\n\
}\n\
#endif\n\
#undef _private\n\
%(guard_end)s' % fmt


class CInnerIntGenerator(object):
    def __init__(self, data):
        self.class_parser = ClassParser(data)
        self.constructor_parser = ConstructorParser(data)
        self.methods_parser = MethodParser(data)
        self.fmt = {'upper': data.name.upper(), 'lower': data.name.lower(), 'name': data.name,
                    'prefix_lower': data.prefix.lower()}

    def generate(self):
        fmt = self.fmt
        fmt['class_method'] = self.class_parser.get_class_method_impl()
        fmt['methods'] = self.methods_parser.get_impl()
        fmt['guard'] = self.class_parser.get_guard('INT')
        fmt['guard_end'] = self.class_parser.get_guard_end('INT')
        return '%(guard)s\n\
#define %(upper)s_IMPLEMENTATION\n\n\
#include "%(prefix_lower)s.h"\n\n\
static void %(lower)s_override(union %(name)s_Class * const %(lower)s);\n\n\
%(class_method)s\n\
%(methods)s\n\
%(guard_end)s\n' % fmt


class CTemplateGenerator(CInterfaceGenerator):
    def __init__(self, data):
        super(CTemplateGenerator, self).__init__(data)
        self.template_parser = TemplateParser(data)
        self.fmt['prefix'] = data.prefix
        self.fmt['lower_prefix'] = data.prefix.lower()
        self.fmt['upper_prefix'] = data.prefix.upper()

    def generate(self):
        fmt = self.fmt
        fmt['template_def'] = self.template_parser.get_template_def()
        fmt['template_undef'] = self.template_parser.get_template_undef()
        fmt['typenames_def'] = self.template_parser.get_typenames_def()
        fmt['typenames_undef'] = self.template_parser.get_typenames_undef()
        fmt['constructor_def'] = self.template_parser.get_constructor_def()
        fmt['constructor_undef'] = self.template_parser.get_constructor_undef()
        return '#if !defined(%(upper_prefix)s_TEMPLATE_H) || defined(%(prefix)s_Params)\n\
#ifndef %(prefix)s_Params\n#error "%(prefix)s_Params is not defined"\n#endif\n\n\
#include "cobject/ctemplate.h"\n\n\
%(template_def)s\n\
%(typenames_def)s\n\
%(constructor_def)s\n\
#include "%(lower_prefix)s.h"\n\n\
%(template_undef)s\n\
%(typenames_undef)s\n\
%(constructor_undef)s\n\
#endif /* %(upper_prefix)s_TEMPLATE_H */' % fmt


class CTemplateInternalGenerator(CInnerIntGenerator):
    def __init__(self, data):
        super(CTemplateInternalGenerator, self).__init__(data)
        self.template_parser = TemplateParser(data)
        self.fmt['prefix'] = data.prefix
        self.fmt['lower_prefix'] = data.prefix.lower()
        self.fmt['upper_prefix'] = data.prefix.upper()

    def generate(self):
        fmt = self.fmt
        fmt['template_def'] = self.template_parser.get_template_def(lower_case=True)
        fmt['template_undef'] = self.template_parser.get_template_undef(lower_case=True)
        fmt['typenames_def'] = self.template_parser.get_typenames_def()
        fmt['typenames_undef'] = self.template_parser.get_typenames_undef()
        fmt['constructor_def'] = self.template_parser.get_constructor_def()
        fmt['constructor_undef'] = self.template_parser.get_constructor_undef()
        return '#ifndef %(prefix)s_Params\n#error "%(prefix)s_Params is not defined"\n#endif\n\n\
%(template_def)s\n\
%(typenames_def)s\n\
%(constructor_def)s\n\
#include "%(lower_prefix)s.c"\n\n\
%(template_undef)s\n\
%(typenames_undef)s\n\
%(constructor_undef)s' % fmt
