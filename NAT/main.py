#!eusr/bin/env python3 
from subnet import * 
import argparse 


#TODO: parse output for correctness in testing
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



'''
IN : None 
OUT: 0 or 1 ( 0 indicating success ) 
'''
def test_get_net_addr() -> int:  
    # use list of generated IP addresses 
    get_net_addr()

    return 1



''' 
IN: <class 'int'> -> specifies how many addresses you want to generate

OUT: <class 'list'> -> list of generated IP addresses 

TODO: enable the user to specify whether they want the 
same network address for all 

TODO: enable to user to specify only private IP addresses 
'''
def test_ip4_gen(n):

    ip4_gen()

def test_ip4_to_binary(): 
    addr = "192.168.1.1"
    print(ip4_to_binary(addr, literal=True))


if __name__ == '__main__':
    test_ip4_to_binary()


