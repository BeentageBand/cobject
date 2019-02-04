class ClassMethodData:
    def __init__(self, name, qualifier='', access = '', return_t = 'void', params=[]):
        self.qualifier = qualifier
        self.access = access
        self.return_t = return_t
        self.name = name
        self.params = params
    def print_obj(self):
        print 'method:', self.qualifier, self.access, self.return_t, self.name
        for param in self.params:
            param.print_obj()

class ClassMethodDataBuilder:
    def __init__(self):
        self.qualifier = ''
        self.access = ''
        self.return_t = 'void'
        self.name = None
        self.params = []
    def with_qualifier(self, qualifier):
        self.qualifier = qualifier
    def with_access(self, access):
        self.access = access
    def with_return_t(self, return_t):
        self.return_t = return_t
    def with_name(self, name):
        self.name = name
    def with_params(self, params):
        self.params = params
    def build(self):
        return ClassMethodData(qualifier = self.qualifier, access = self.access, return_t = self.return_t, name = self.name, params = self.params)