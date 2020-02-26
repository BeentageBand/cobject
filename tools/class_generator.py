from class_parser import *
class CInterfaceGenerator:
    def __init__(self, data):
        self.class_parser = ClassParser(data)
        self.constructor_parser = ConstructorParser(data)
        self.methods_parser = MethodParser(data)
        self.fmt = {}
        self.fmt['upper'] = data.name.upper()
        self.fmt['lower'] = data.name.lower()
        self.fmt['name'] = data.name
        isa = data.isa[-2].name.lower()
        self.fmt['isa'] = 'cobject' if isa in 'object' else isa
    def generate(self):
        fmt = self.fmt
        fmt['class'] = self.class_parser.get_decl()
        fmt['class_method'] = self.class_parser.get_class_method_decl()
        fmt['constructors'] = self.constructor_parser.get_decl()
        fmt['methods'] = self.methods_parser.get_decl()
        return '#ifndef %(upper)s_H\n\
#define %(upper)s_H\n\
#include "%(isa)s.h"\n\
\n\
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
#endif /* %(upper)s_H */' % (fmt)

class CInnerIntGenerator:
    def __init__(self, data):
        self.class_parser = ClassParser(data)
        self.constructor_parser = ConstructorParser(data)
        self.methods_parser = MethodParser(data)
        self.fmt = {}
        self.fmt['upper'] = data.name.upper()
        self.fmt['lower'] = data.name.lower()
        self.fmt['name'] = data.name
    def generate(self):
        fmt = self.fmt
        fmt['class_method'] = self.class_parser.get_class_method_impl()
        fmt['methods'] = self.methods_parser.get_impl()
        return '#ifndef %(upper)s_INT_H\n\
#define %(upper)s_IMPLEMENTATION\n\
\n\
#include "%(lower)s.h"\n\
\n\
static void %(lower)s_override(union %(name)s_Class * const %(lower)s);\n\
static void %(lower)s_delete(union %(name)s * const %(lower)s);\n\
\n\
%(class_method)s\n\
%(methods)s\n\
#endif /* %(upper)s_INT_H */\n' % (fmt)
