# coding=utf-8
from pwd_dict import Generate_pwd_dict
from optparse import OptionParser
import sys

if __name__ == '__main__':
    banner = """
    version v1.0.1          author:ly
                              _ 
             _ ____      ____| |
            | '_ \ \ /\ / / _` |
            | |_) \ V  V / (_| |
            | .__/ \_/\_/ \__,_|
            |_|                 
                                                                                                         
    """
    print(banner)
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Pass in the URL where you want to generate the dictionary")
    (options, args) = parser.parse_args()
    if options.url is None:
        parser.print_help()
        print("EEROR: The parameter cannot be empty!")
    else:
        pwd_dict = Generate_pwd_dict(options.url)
        pwd_dict.generate()
        print("The build succeeded！Check out the pwd folder!")