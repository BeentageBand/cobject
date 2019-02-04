class ClassMemberData:
    def __init__(self, name, type_t, access = '', ref_t = ''):
        self.access = access
        self.type_t = type_t
        self.ref_t = ref_t
        self.name = name
    def print_obj(self):
        print 'member:', self.access, self.type_t, self.ref_t, self.name

class ClassMemberDataBuilder:
    def __init__(self):
        self.access = ''
        self.type_t = None
        self.ref_t = ''
        self.name = None
    def with_access(self, access):
        self.access = access
    def with_type_t(self, type_t):
        self.type_t = type_t
    def with_ref_t(self, ref_t):
        self.ref_t = ref_t
    def with_name(self, name):
        self.name = name
    def build(self):
        return  ClassMemberData(access = self.access, ref_t = self.ref_t, type_t = self.type_t, name = self.name)