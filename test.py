#!/usr/bin/env python3 
from subnet import * 

# prints out ip address as an indiced list of addresses 
print(ip4_to_binary("192.168.1.1"))




if __name__ == '__main__':


    if sys.argv[1] and sys.argv[2]:

        ip = sys.argv[1]
        mask = sys.argv[2]
        net_addr = get_net_addr(ip, mask)


        print(f"\nIP address:\n\t{sys.argv[1]}\nSubnet Mask:\n\t{sys.argv[2]}\nNetwork Address:\n\t{net_addr}\n")

        net_range = get_net_range(net_addr, mask)

    else:
        
