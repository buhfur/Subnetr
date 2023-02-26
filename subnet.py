#!/usr/bin/env python3 
# Ryan McVicker 2/25/2023
import sys 


#TODO: allow reading IP packets and perform the translation there 
''' 

This is a very basic implementation of what I think a Network 
address translation tool is.

Problem I want to solve : given an IPv4 address and a subnet mask , 
 calculate the network address , range, and available hosts on the network

 '''


''' my own little method to convert UTF-8 string ip addresses
to a list of binary numbers '''
def ip4_to_binary(x):

    binary_octet_list = []
    for octet in x.split('.'):
        binary_octet_list.append(bin(int(octet)))  # appends as string
    return binary_octet_list
        
''' function that returns the identified IPv4 network address in binary 
'''


def get_net_addr(ip , mask, literal=None):
    net_addr = [] 
    ip = ip4_to_binary(ip)
    mask = ip4_to_binary(mask)

    for x in range(len(ip)): 
        net_addr.append(bin( int(ip[x], 2)  & int(mask[x], 2)))


    #TODO : change this to use command line arguments instead
    if literal: 
        # strips out the '0b' in front of every binary number 
        s_net_addr = [] # array containing stripped values
        for y in net_addr: 
            s_net_addr.append(y[2:])

        return s_net_addr
    else:
        for x in range(len(net_addr)): 
            net_addr[x] = str(int(net_addr[x], 2 ))

        
    return (".".join(net_addr)) 

    
    
    


''' 
IN : IPv4 address
OUT: octet output of all 
'''

def get_net_range(net_addr, mask):

    return 

def get_net_avail_hosts(ip):
    return 



if __name__ == '__main__':

    if sys.argv[1] and sys.argv[2]:
        print(f"\nIP address:\n\t{sys.argv[1]}\nSubnet Mask:\n\t{sys.argv[2]}\nNetwork Address:\n\t{get_net_addr(sys.argv[1], sys.argv[2])}\n")

    net_addr = get_net_addr(sys.argv[1], sys.argv[2])

