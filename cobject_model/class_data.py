class ClassData:
    def __init__(self, name, isa = '', members = [], methods = []):
        self.name = name
        self.isa = isa
        self.members = members
        self.methods = methods
    def print_obj(self):
        print 'class:', self.name
        print 'inherits:', self.isa
        for member in self.members:
            member.print_obj()
        for method in self.methods:
            method.print_obj()

class ClassDataBuilder:
    def __init__(self):
        self.name = None
        self.isa = '' 
        self.members = []
        self.methods = []
    def with_name(self, name):
        self.name = name
    def with_isa(self, isa):
        self.isa = isa
    def with_members(self, members):
        self.members = members
    def with_methods(self, methods):
        self.methods = methods
    def build(self):
        return ClassData(name = self.name, isa = self.isa, members = self.members, methods = self.methods)