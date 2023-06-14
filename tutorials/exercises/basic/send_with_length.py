#!/usr/bin/env python3
import random
import socket
import sys

from scapy.all import IP, TCP, Ether, get_if_hwaddr, get_if_list, sendp, UDP


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def get_payload_with_length(length):
    msg = f"{length}ThisIsASamplePayloadWithLength{length}"
    msg_length = len(msg)
    if length < msg_length:
        return msg[:length]
    ret = ""
    for i in range(length // msg_length):
        ret += msg
    ret += msg[:length - len(ret)]
    return ret

def main():

    if len(sys.argv) < 4:
        print('pass 3 arguments: <destination> "<message_length> <TCP/UDP>"')
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    print("sending on interface %s to %s" % (iface, str(addr)))
    pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    if sys.argv[3] == "TCP":
        pkt = pkt /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / get_payload_with_length(int(sys.argv[2]))
    elif sys.argv[3] == "UDP":
        pkt = pkt /IP(dst=addr) / UDP(dport=1234, sport=random.randint(49152,65535)) / get_payload_with_length(int(sys.argv[2]))
    else:
        print('pass 3 arguments: <destination> "<message_length> <TCP/UDP>"')
        exit(1)
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
