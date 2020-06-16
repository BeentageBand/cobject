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
#define %(upper)s_H\n\
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
%(guard_end)s' % fmt


class CInnerIntGenerator(object):
    def __init__(self, data):
        self.class_parser = ClassParser(data)
        self.constructor_parser = ConstructorParser(data)
        self.methods_parser = MethodParser(data)
        self.fmt = {'upper': data.name.upper(), 'lower': data.name.lower(), 'name': data.name}

    def generate(self):
        fmt = self.fmt
        fmt['class_method'] = self.class_parser.get_class_method_impl()
        fmt['methods'] = self.methods_parser.get_impl()
        fmt['guard'] = self.class_parser.get_guard('INT')
        fmt['guard_end'] = self.class_parser.get_guard_end('INT')
        return '%(guard)s\n\
#define %(upper)s_IMPLEMENTATION\n\n\
#include "%(lower)s.h"\n\n\
static void %(lower)s_override(union %(name)s_Class * const %(lower)s);\n\n\
%(class_method)s\n\
%(methods)s\n\
%(guard_end)s\n' % fmt


class CTemplateGenerator(CInterfaceGenerator):
    def __init__(self, data):
        super(CTemplateGenerator, self).__init__(data)
        self.template_parser = TemplateParser(data)

    def generate(self):
        return '#if !defined(%(upper)s_H) || defined(%(name)s_Params)\n\
#include "%(lower)s.h"\n\n\
#ifndef %(name)s_Params\n#error "%(name)s_Params is not defined"\n#endif\n\n\
#endif /* %(upper)s_H */' % self.fmt
