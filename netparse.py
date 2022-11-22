#!/usr/bin/python3

#
# netparse.py
# pentesting-scanautomation
#

import sys
from typing import List

import xml.etree.ElementTree as ET

# Nessus xml tree (unused subtrees excluded)
"""
            root
            /  \
        Policy  Report
                    \
                    ReportHost, ReportHost, ...
                    /       \
        HostProperties      ReportItem, ReportItem, ...
"""

class Host:
    def __init__(self, ip, tcpPorts, udpPorts) -> None:
        self.ip = ip
        self.tcpPorts = tcpPorts
        self.udpPorts = udpPorts


    def __str__(self) -> str:
        return "%s\n\tTCP Ports: %s\n\tUDP Ports: %s" % (self.ip, self.tcpPorts, self.udpPorts)


def findTag(tags, key):
    '''Search a list of xml tag elements for one with the name key'''
    for t in tags:
        if t.attrib['name'] == key:
            return t
    
    return None


def parseHosts(root) -> List[Host]:
    '''Given the root node of a nessus xml report parse out info about the hosts'''
    reports = list(root[1])
    hosts = []

    for report in reports:
        hostProperties = list(report)[0]
        try:
            hostIP = findTag(list(hostProperties), "host-ip").text
        except AttributeError:
            continue

        tcpPorts = []
        udpPorts = []
        for item in list(report[1:]):
            if item.attrib["port"] != '0':
                portNo = item.attrib["port"]
                if item.attrib["protocol"] == "tcp" and not portNo in tcpPorts:
                    tcpPorts.append(portNo)
                elif item.attrib["protocol"] == "udp" and not portNo in udpPorts:
                    udpPorts.append(portNo)

        host = Host(hostIP, tcpPorts, udpPorts)
        hosts.append(host)
        
    return hosts



def main():
    inputFile = ""
    outPrefix = ""

    # Process command line arguments
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-if":
            # Specify input file: -if <file>
            i += 1
            inputFile = sys.argv[i]
        elif sys.argv[i] == "-of":
            # Specify output file prefix: -of <prefix>
            i += 1
            outPrefix = sys.argv[i]
        else:
            print("Unrecognized argument")
            sys.exit(1)
        
        i += 1

    if inputFile == "":
        print("No input file specified")
        sys.exit(1)

    baseName = ""
    if outPrefix != "":
        baseName = outPrefix + "_"
    
    # Parse tree from nessus xml file
    tree = ET.parse(inputFile)
    root = tree.getroot()

    # Parse host info from the tree
    hosts = parseHosts(root)

    # Build output lists

    # Hosts list
    ips = []
    for h in hosts:
        if not h.ip in ips:
            ips.append(h.ip)

    ips.sort()
    with open(baseName + "Live_Hosts.txt", 'w+') as file:
        for ip in ips:
            file.write(ip)
            file.write('\n')


    # Port lists
    tcpMap = {}

    for h in hosts:
        for p in h.tcpPorts:
            if not p in tcpMap:
                tcpMap[p] = []

            tcpMap[p].append(h.ip)

    for p in tcpMap:
        with open(baseName + "tcp%s_Open.txt" % p, 'w+') as file:
            for ip in tcpMap[p]:
                file.write(ip)
                file.write('\n')


    udpMap = {}

    for h in hosts:
        for p in h.udpPorts:
            if not p in udpMap:
                udpMap[p] = []

            udpMap[p].append(h.ip)

    for p in udpMap:
        with open(baseName + "udp%s_Open.txt" % p, 'w+') as file:
            for ip in udpMap[p]:
                file.write(ip)
                file.write('\n')


if __name__ == "__main__":
    main()
