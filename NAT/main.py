#!eusr/bin/env python3 
from subnet import * 
import argparse 


#TODO: parse command line args with argparse



'''
Usage: ./main.py  [OPTION]... [IP]...[SUBNET_MASK]

Options: 
    -b : Use python 3 representation for binary numbers ( ex. Removes the "0b" in front of binary strings) 
    -v : Verbose output 
    -n : Only show the network address
    -a SUBMASK : Show the Network Address, Range, and 
    Available hosts for a network 
    -d : Show IPv4 addresses in dot notation

'''


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("")

    parser.add_argument(""
    parser.parse_args() 

'''    if sys.argv[1] and sys.argv[2]:

        ip = sys.argv[1]
        mask = sys.argv[2]
        net_addr = get_net_addr(ip, mask)


        print(f"\nIP address:\n\t{sys.argv[1]}\nSubnet Mask:\n\t{sys.argv[2]}\nNetwork Address:\n\t{net_addr}\n")

        net_range = get_net_range(net_addr, mask)

    else:
        
        '''
