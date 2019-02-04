class MethodParamData:
    def __init__(self, type_t, name, ref_t = ''):
        self.type_t = type_t
        self.ref_t = ref_t
        self.name = name
    def print_obj(self):
        print '     ', self.type_t, self.ref_t, self.name

class MethodParamDataBuilder:
    def __init__(self):
        self.type_t = None
        self.ref_t = ''
        self.name = None 
    def with_type_t(self, type_t):
        self.type_t = type_t
    def with_ref_t(self, ref_t):
        self.ref_t = ref_t
    def with_name(self, name):
        self.name = name
    def build(self):
        return  MethodParamData(type_t = self.type_t, ref_t = self.ref_t, name = self.name)