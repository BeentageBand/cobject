import os
from optparse import OptionParser
from xml.etree import ElementTree, ElementInclude

from .class_data import DomainData
from .class_generator import CInnerIntGenerator, CInterfaceGenerator, CTemplateGenerator, CTemplateInternalGenerator


def write_files_by_generators(output_path, class_data, generators=[], filenames=[]):
    for i in range(len(generators)):
        generator = generators[i](class_data)
        file_path = os.path.join(output_path, filenames[i])
        with open(file_path, 'w') as f:
            try:
                print('Writing ', file_path)
                f.write(generator.generate())
            finally:
                f.close()


usage = 'Usage: tools [options]'
parser = OptionParser(usage=usage)
parser.add_option('-o', '--output', dest='output', help='output path')
parser.add_option('-c', '--class', dest='classname', help='class name to generate')
parser.add_option('-i', '--input', dest='input', help='xml with domain')

(options, args) = parser.parse_args()

if None is options.input:
    parser.print_help()
    parser.error('--input is mandatory')
if None is options.output:
    parser.print_help()
    parser.error('--output is mandatory')
if None is options.classname:
    parser.print_help()
    parser.error('--class is mandatory')

os.chdir(os.path.dirname(os.path.abspath(options.input)))
tree = ElementTree.parse(os.path.basename(options.input))
root = tree.getroot()
ElementInclude.include(root)

domain_data = DomainData(root)
class_data = domain_data.get_class(options.classname)

file_generators = [CInnerIntGenerator, CInterfaceGenerator]
file_names = [class_data.prefix.lower() + '-internal.h', class_data.prefix.lower() + '.h']

if hasattr(class_data, 'typenames'):
    file_generators.append(CTemplateGenerator)
    file_names.append(class_data.prefix.lower() + '-template.h')
    file_generators.append(CTemplateInternalGenerator)
    file_names.append(class_data.prefix.lower() + '-int-template.h')

write_files_by_generators(options.output, class_data, file_generators, file_names)

print
'End Processing'
