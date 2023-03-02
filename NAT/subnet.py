#!/usr/bin/env python3 
# Ryan McVicker 2/25/2023
import sys 
import random 
import os
from base64 import b64encode


''' 

This is a very basic implementation of what I think a Network 
address translation tool is.

Problem I want to solve : given an IPv4 address and a subnet mask , 
 calculate the network address , range, and available hosts on the network

 '''


'''
IN: <class 'str'> -> string of IPv4 address in dot notation
OUT: <class 'list'> -> list of python3 binary strings unless 
specified otherwise 

'''
def ip4_to_binary(x, literal=False):

    binary_octet_list = []
    for octet in x.split('.'):
        binary_octet_list.append(bin(int(octet)))  # appends as string

    if literal: 
        s_bin_list = [] 
        for y in binary_octet_list: 
            s_bin_list.append(y[2:]) 
        return s_bin_list

    return binary_octet_list

'''
IN : <class 'int'> -> how many addresses you want to generate
OUT: <class 'list'> -> list of genrated IP addresses 
''' 

def ip4_gen(x): 
    #generate 4 random numbers betwen the range of 10-255
    r_ip_addr = [str(random.randrange(256)) for x in range(4)]
    
    print('.'.join(r_ip_addr))


  
'''
IN : <class 'str'>
OUT: <class 'list'> -> prints out binary string list of 
the network address

get_net_addr(ip , mask, literal=None)

OPTIONS:

    #TODO: add command line arguments to
    
'''

#TODO: format output from get_net_addr into a table which shows all forms of output
def get_net_addr(ip , mask ):
    net_addr = [] 
    ip = ip4_to_binary(ip)
    mask = ip4_to_binary(mask)

    net_addr = [ bin( int(ip[x], 2) & int(mask[x], 2) ) for x in range(len(ip))]

    # strips the "0b" in front of each string
    net_addr = [str(int(net_addr[x], 2 )) for x in range(len(net_addr))]
        
    return (".".join(net_addr)) 

    
    
    


''' 
IN : <class 'list'> -> list of binary strings 
OUT: <class 'int'> -> integer of the iP range? 
'''

def get_net_range(net_addr, mask):
    # bitwise AND the subnet mask and bitwise OR with the net_addr
    mask = ip4_to_binary(mask) 
    # bitwise subnet mask with itself
    a_mask = [ bin( int(mask[x], 2) & int(mask[x], 2) ) for x in range(len(mask))]

    # TODO : convert subnet mask to host mask
    for y in a_mask:
      print(bin(~int(y, 3)))


    


'''

IN: 

'''

def get_net_avail_hosts(ip):
    return 




