from optparse import OptionParser
from cobject_model.class_data import *
from cobject_model.class_data_parser import *
from cobject_model.class_member_data import *
from cobject_model.class_method_data import *
from cobject_model.method_param_data import *
from cobject_model.api_generator import *
from cobject_model.impl_generator import *

import sys

try:
    xml = sys.argv[1]
except IndexError:
    xml = 'cobject-model.xml'

data_parser = ClassDataParser(xml)
data_objs = data_parser.generate()
for data_obj in data_objs:
    data_obj.print_obj()
    api_gen = APIGenerator(data_obj)
    api_gen.print_api()
    impl_gen = ImplGenerator(data_obj)
    impl_gen.print_impl() 
