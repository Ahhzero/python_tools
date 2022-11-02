# coding=utf-8
import sys
from c_scan import C_scan
from optparse import OptionParser
if __name__ == '__main__':
    banner = """
       version v1.0.1          author:ly
          ___   ___  ___ __ _ _ __  
         / __| / __|/ __/ _` | '_ \ 
        | (__ _\__ \ (_| (_| | | | |
         \___(_)___/\___\__,_|_| |_|
       """
    print(banner)
    parser = OptionParser()
    parser.add_option("-i", "--ipc", dest="ipc", help=" eg:-i 192.168.1.0/24  Please enter the IP address block to query")
    parser.add_option("-t", "--threads", dest="threads",default=10,help=" threads, the default value is recommended. If you want to change -t plus the number of threads")
    (options, args) = parser.parse_args()
    if options.ipc is None:
        parser.print_help()
        print("EEROR: The parameter cannot be empty!")
    else:
        scan = C_scan(options.ipc,int(options.threads))
        scan.start()
        print("The build succeeded！Check out the pwd folder!")
