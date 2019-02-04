import xml.etree.ElementTree as ET
from class_data import *
from class_data_parser import *
from class_member_data import *
from class_method_data import *
from method_param_data import *

class ClassDataParser:
    def __init__(self, xml):
        self.root = ET.parse(xml)
    def generate(self):
        class_builder = ClassDataBuilder()
        for c in self.root.iter('class'):
            class_builder.with_name(c.attrib['name'])
            class_builder.with_members(self.gen_class_members(c))
            class_builder.with_methods(self.gen_class_methods(c))
            try:
                class_builder.with_isa(c.attrib['isa'])
            except KeyError:
                pass
        return  class_builder.build()
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