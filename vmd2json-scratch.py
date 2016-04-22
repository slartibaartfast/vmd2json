# encoding='utf-8'
"""
    vmd2json.py
    for creating a json structure given a vmd structure
"""
import json
import xmltodict
from xmlutils.xml2json import xml2json

from argparse import ArgumentParser
import os.path


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        #return open(arg, 'r')  # return an open file handle
        return arg  # return a file


#def main(input_file, output_file = None, encoding='utf-8'):

    #parser = ArgumentParser(description="description")
    #parser.add_argument("-i", dest="input-file", required=True,
    #                help="input file in vmp or xml", metavar="FILE",
    #                type=lambda x: is_valid_file(parser, x))
    #args = parser.parse_args()

    # for python 3, need to convert xml to binary
    #def convert3(input_file, xml_attribs=True):
    #with open(input-file, "rb") as f:
    #    output_dict = xmltodict.parse(f, xml_attribs=xml_attribs)
    #   return json.dumps(output_dict, indent=4)

# for python 2
#def convert2
#    converter = xml2json(input_file, output_file, encoding="utf-8")
#    converter.convert()


if __name__ == "__main__":
    # figure out if they are running 2 or 3
    #converter = xml2json(input_file, output_file, encoding="utf-8")
    #converter.convert()
    #converter = vmd2json(self.input_file, self.output_file, encoding="utf-8")
    #converter.convert3()
    #main()
    parser = ArgumentParser(description="description")
    parser.add_argument("-i", dest="input_file", required=True,
                    help="input file in vmp or xml", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()

    # for python 3, need to convert xml to binary
    #def convert3(input_file, xml_attribs=True):
    with open(args.input_file, "rb") as f:
        output_dict = xmltodict.parse(f, xml_attribs=True)
        #return json.dumps(output_dict, indent=4)
        json.dumps(output_dict, indent=4)
        print('output ', output_dict)
