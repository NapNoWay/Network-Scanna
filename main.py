from scapy.all import *
import sys
import res

targetPorts = []


def syn_scan(target_ip, target_ports):
    for port in target_ports:








for i in range(1024):

    port = i
    targetPorts.append(port)
    i + 1








for i in range(len(sys.argv)):


    if sys.argv[i] == "-p":
        port = sys.argv[i+1]

    elif sys.argv[i] == "-syn":
        from src.modules.synscan import synScan
        synScan()

    elif sys.argv[i] == "pscan":
        from src.modules.pingSweep import pingSweep
        pingSweep()
    




