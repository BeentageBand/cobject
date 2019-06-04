import xml.etree.ElementTree as ET
from class_data import *
from class_data_parser import *
from class_member_data import *
from class_constructor_data import *
from class_method_data import *
from method_param_data import *

class ClassDataParser:
    def __init__(self, xml):
        self.tree= ET.parse(xml)
        self.root = self.tree.getroot()
        self.domain = {}
        for item in self.root:
            print item.tag, item.attrib
    def generate(self):
        classes = []
        for c in self.root.findall('class'):
            try:
                clazz = self.gen_class(c.attrib['name'])
                classes.append(clazz)
            except KeyError:
                pass
        return classes
    def gen_class(self, key):
        clazz = self.domain.get(key)
        if clazz is not None:
            return clazz
        query = "./class[@name='%s']" % (key)
        c = self.root.find(query)
        class_builder = ClassDataBuilder()
        try:
            class_builder.with_name(c.attrib['name'])
            class_builder.with_isa(self.gen_class(c.attrib['isa']))
        except KeyError:
            pass
        class_builder.with_constructors(self.gen_class_constructors(c))
        class_builder.with_members(self.gen_class_members(c))
        class_builder.with_methods(self.gen_class_methods(c))
        clazz = class_builder.build()
        self.domain[key] = clazz
        return clazz
    def gen_class_constructors(self, given_class):
        class_constructors = []
        for constructor in given_class.iter('constructor'):
            constructor_builder = ClassConstructorDataBuilder()
            constructor_builder.with_name(constructor.attrib['name'])
            constructor_builder.with_params(self.gen_method_params(constructor))
            class_constructors.append(constructor_builder.build())
        return class_constructors
    def gen_class_members(self, given_class):
        class_members = []
        for member in given_class.iter('member'):
            member_builder = ClassMemberDataBuilder()
            member_builder.with_name(member.attrib['name'])
            member_builder.with_type_t(member.attrib['type_t'])
            try:
                member_builder.with_access(member.attrib['access'])
            except:
                pass
            try:
                member_builder.with_ref_t(member.attrib['ref_t'])
            except:
                pass
            class_members.append(member_builder.build())
        return class_members
    def gen_class_methods(self, given_class):
        class_methods = []
        for method in given_class.iter('method'):
            method_builder = ClassMethodDataBuilder()
            method_builder.with_name(method.attrib['name'])
            method_builder.with_return_t(method.attrib['return_t'])
            method_builder.with_params(self.gen_method_params(method))
            try:
                method_builder.with_qualifier(method.attrib['qualifier'])
            except KeyError:
                pass
            class_methods.append(method_builder.build())
        return class_methods
    def gen_method_params(self, given_method):
        method_params = []
        for param in given_method.iter('param'):
            method_param_builder = MethodParamDataBuilder()
            method_param_builder.with_name(param.attrib['name'])
            method_param_builder.with_type_t(param.attrib['type_t'])
            try:
                method_param_builder.with_ref_t(param.attrib['ref_t'])
            except KeyError:
                pass
            method_params.append(method_param_builder.build())
        return method_params
