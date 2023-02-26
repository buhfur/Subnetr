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

Here's how you can determine the network prefix for a given IP address:

Determine the IP address class: 

The IP address class can be determined by looking at the first octet of the IP address. The three common classes of IP addresses are A, B, and C. Class A IP addresses have a first octet range of 1-126, Class B IP addresses have a first octet range of 128-191, and Class C IP addresses have a first octet range of 192-223.

Determine if the IP address is public or private: 

Private IP addresses are reserved for use on private networks and are not routable on the Internet. There are three ranges of private IP addresses: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Public IP addresses, on the other hand, are assigned to devices that are connected to the Internet.

Determine the network prefix: 
Once you know the class and whether the IP address is public or private, 
you can determine the network prefix by looking at the default subnet mask for the IP address class.

The default subnet mask for Class A IP addresses is 255.0.0.0
, for Class B IP addresses it is 255.255.0.0, 

and for Class C IP addresses it is 255.255.255.0. 

If the IP address is a private address, the network prefix will be the same as the default subnet mask.
If the IP address is a public address, the network prefix may be different, depending on how the network is configured.

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
