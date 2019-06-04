class ClassConstructorData:
    def __init__(self, name, params = []):
        self.name = name
        self.params = params
    def print_obj(self):
        print 'constructor: ', self.name
        for param in self.params:
            param.print_obj()

class ClassConstructorDataBuilder:
    def __init__(self):
        self.name = ''
        self.params = []
    def with_name(self, name):
        self.name = name
    def with_params(self, params):
        self.params = params
    def build(self):
        return ClassConstructorData(self.name, self.params)
