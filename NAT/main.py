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



'''
IN : None 
OUT: 0 or 1 ( 0 indicating success ) 
'''
def test_get_net_addr() -> int:  
  
  return 1



''' 
IN: None
OUT: Unknown
'''
def test_ip4_gen():
  
  ip4_gen()



if __name__ == '__main__':
  test_ip4_gen()


