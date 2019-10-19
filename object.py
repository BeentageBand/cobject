import xml.etree.ElementTree as ET
import xml.etree.ElementInclude as EI
from class_data import *
from class_generator import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-o', '--output', dest='output', help='output path')
parser.add_option('-c', '--class', dest='classname', help='class name to generate')
parser.add_option('-i', '--input', dest='input', help='xml with domain')

(options, args) = parser.parse_args()

if None is options.input:
    parser.error('--input is mandatory')
if None is options.output:
    parser.error('--output is mandatory')
if None is options.classname:
    parser.error('--class is mandatory')

tree = ET.parse(options.input)
root = tree.getroot()
EI.include(root)
domain_data = DomainData(root)
class_data = domain_data.get_class(options.classname)

c_interface = CInterfaceGenerator(class_data)
c_inner_int = CInnerIntGenerator(class_data)
'''
c_inner_impl = CInnerImplGenerator(class_data)
c_implementation = CImplementationGenerator(class_data)
'''

interface_filename = options.output + '/' + options.classname.lower() + '.h'
inner_filename = options.output + '/' + options.classname.lower() + '-internal.h'

interface_file = open(interface_filename, 'w')
inner_file = open(inner_filename, 'w')

try:
    print 'Writing ' + interface_filename
    interface_file.write(c_interface.generate())
    print 'Writing ' + inner_filename
    inner_file.write(c_inner_int.generate())
finally:
    interface_file.close()
    inner_file.close()

print 'End Processing'
