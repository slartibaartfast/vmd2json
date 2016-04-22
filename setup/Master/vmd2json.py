# encoding='utf-8'
"""
    vmd2json.py
    for creating a json structure given a vmd structure
"""
import json
import xmltodict
#from xmlutils.xml2json import xml2json

from argparse import ArgumentParser
import os.path


def is_valid_file(parser, arg):
    # see if the file exists.  better as try catch
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg  # return a file

if __name__ == "__main__":
    parser = ArgumentParser(description="description")
    parser.add_argument("-in", dest="input_file", required=True,
                    help="Input file of type vmp or xml.", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))

    # let them specify the output file
    #parser.add_argument("-out", dest="output_file", required=False,
    #                help="Output file of type JSON", metavar="FILE")
    args = parser.parse_args()

    # for python 3, need to convert xml to binary
    with open(args.input_file, "rb") as f:
        output_dict = xmltodict.parse(f, xml_attribs=True)
        json.dumps(output_dict, indent=4)
        print('output ', output_dict)

    #with open(args.input_file, "rb") as output_file:
    #    output_dict = xmltodict.parse(f, xml_attribs=True)
    with open('data-out.json', 'w') as file:
        json.dump(output_dict, file)
	
