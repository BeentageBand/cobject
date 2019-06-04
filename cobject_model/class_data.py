class ClassData:
    def __init__(self, name, isa = None , constructors = [], members = [], methods = []):
        self.name = name
        self.isa = isa
        self.constructors = constructors
        self.members = members
        self.methods = methods 
    def print_obj(self):
        print 'class:', self.name
        print 'inherits:', '' if self.isa is None else self.isa.name
        isa_members = []
        isa_methods = []
        isa = self.isa

        while isa is not None:
            isa_members += isa.members
            isa_methods += isa.methods
            isa = isa.isa

        for constructor in self.constructors:
            constructor.print_obj()
        for member in (isa_members + self.members):
            member.print_obj()
        for method in (isa_methods + self.methods):
            method.print_obj()
class ClassDataBuilder:
    def __init__(self):
        self.name = None
        self.isa = None 
        self.constructors = []
        self.members = []
        self.methods = []
    def with_name(self, name):
        self.name = name
    def with_isa(self, isa):
        self.isa = isa
    def with_constructors(self, constructors):
        self.constructors = constructors
    def with_members(self, members):
        self.members = members
    def with_methods(self, methods):
        self.methods = methods
    def build(self):
        return ClassData(name = self.name, isa = self.isa, constructors = self.constructors, members = self.members, methods = self.methods)
