import xml.etree.ElementTree as ET

class MemberData:
    def __init__(self, root):
        self.type_t = root.get('type_t')
        self.name = root.get('name')

class MethodData:
    def __init__(self, root):
        self.return_t = root.get('return_t', 'void')
        self.override = root.get('override', 'false')
        self.name = root.get('name')
        self.params = self.get_params(root)
    def get_params(self, root):
        params = []
        for p in root.findall('param'):
            param = MemberData(p)
            params.append(param)
        return params
        
class ClassData:
    def __init__(self, root = None, isa = []):
        if None is root:
            self.type_t = 'struct'
            self.name = 'Object'
            self.isa = isa 
            print 'ClassData - ', self.name
            self.constructors = []
            self.members = []
            self.methods = []
        else:
            self.type_t = 'union'
            self.name = root.get('name')
            self.isa = isa
            self.members = []
            self.methods = []
            print 'ClassData - ', self.name
            self.constructors = self.get_constructors(root)
            for i in isa:
                self.members.extend(i.members)
                self.methods.extend(i.methods)
            self.members.extend(self.get_members(root))
            self.methods.extend(self.get_methods(root))
    def get_constructors(self, root):
        constructors = []
        for m in root.findall('constructor'):
            method = MethodData(m)
            constructors.append(method)
        return constructors
    def get_members(self, root):
        members = []
        for m in root.findall('member'):
            member = MemberData(m)
            members.append(member)
        return members
    def get_methods(self, root):
        methods = []
        for m in root.findall('method'):
            method = MethodData(m)
            methods.append(method)
        return methods

class DomainData:
    def __init__(self, root):
        self.root = root
    def get_class(self, target_class):
        class_roots = []
        target = target_class
        while True:
            class_root = self.find_class(target)
            if None is class_root:
                print class_root
                break
            print ET.tostring(class_root)
            class_roots.append(class_root)
            target = class_root.get('isa')
        class_roots.reverse()
        class_data = []
        class_data.append(ClassData())
        for c in class_roots:
            print 'ClassData elems: ', len(class_data)
            clazz = ClassData(c, class_data)
            class_data.append(clazz)
        return clazz
    def find_class(self, target_class):
        if None is target_class:
            return None
        print 'find - ', target_class
        query = "./class[@name='%s']" % (target_class)
        return self.root.find(query)
