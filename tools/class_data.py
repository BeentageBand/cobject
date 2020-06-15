from xml.etree import ElementTree


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

    @staticmethod
    def get_params(root):
        params = []
        for p in root.findall('param'):
            param = MemberData(p)
            params.append(param)
        return params


class ClassData(object):
    def __init__(self, root=None, isa=None):
        if isa is None:
            isa = []
        if None is root:
            self.type_t = 'struct'
            self.name = 'Object'
            self.isa = isa
            print('ClassData - ', self.name)
            self.constructors = []
            self.members = []
            self.methods = []
        else:
            self.type_t = 'union'
            self.name = root.get('name')
            self.isa = isa
            self.members = []
            self.methods = []
            print('ClassData - ', self.name)
            self.constructors = self.get_constructors(root)
            for i in isa:
                self.members.extend(i.members)
                self.methods.extend(i.methods)
            self.members.extend(self.get_members(root))
            self.methods.extend(self.get_methods(root))

    @staticmethod
    def get_constructors(root):
        constructors = []
        for m in root.findall('constructor'):
            method = MethodData(m)
            constructors.append(method)
        return constructors

    @staticmethod
    def get_members(root):
        members = []
        for m in root.findall('member'):
            member = MemberData(m)
            members.append(member)
        return members

    @staticmethod
    def get_methods(root):
        methods = []
        for m in root.findall('method'):
            method = MethodData(m)
            methods.append(method)
        return methods


class TemplateData(ClassData):
    def __init__(self, root=None, isa=None):
        print('ping - template data')
        super(TemplateData, self).__init__(root, isa)
        self.typenames = self.get_typenames(root)
        for i in self.isa:
            if hasattr(i, 'typenames'):
                self.typenames.extend(i.typenames)

        self.prefix = self.name
        for t in self.typenames:
            self.name = self.name + '_' + t

    @staticmethod
    def get_typenames(root):
        typenames = []
        for t in root.findall('typename'):
            typenames.append(t.get('name'))
        return typenames


class DomainData:
    def __init__(self, root):
        self.root = root

    def get_class(self, target_class):
        class_roots = []
        target = target_class
        while True:
            class_root = self.find_class(target)
            if None is class_root:
                print(class_root)
                break
            print(ElementTree.tostring(class_root))
            class_roots.append(class_root)
            target = class_root.get('isa')
        class_roots.reverse()
        class_data = [ClassData()]
        for c in class_roots:
            print('ClassData elems: ', len(class_data), c.get('template'))
            clazz = TemplateData(c, class_data) if 'true' == c.get('template') else ClassData(c, class_data)
            class_data.append(clazz)
        return clazz

    def find_class(self, target_class):
        if None is target_class:
            return None
        print('find - ', target_class)
        query = "./class[@name='%s']" % target_class
        return self.root.find(query)
