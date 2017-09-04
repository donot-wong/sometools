#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-03
# @Author  : donot wang.donot@gmail.com
# @Link    : blog.donot.me
# @Version : 1.0

import os
import re
import ip
import platform


def getAllIpAddr():
    osInfo = platform.system()
    # ipStr = '([0-9]{1, 3\.){3}[0-9]{1, 3}'
    if osInfo == "Windows":
        pass
    elif osInfo == "Linux":
        ifconfig_os = os.popen("ifconfig").read()
        result = re.findall(r"inet (.*?)  netmask (.*)  broadcast (.*)", str(ifconfig_os))
        return result
    else:
        print("[*] Warning: Can not detect system info, this....")


def bin2bin(binstr):
    tm = binstr[2:]
    if len(tm) < 8:
        tm = (8 - len(tm)) * '0' + tm
    return tm


def getMinAndMaxIp(inet, netmask):
    inetPart = inet.split(".")
    netmaskPart = netmask.split(".")
    minIp = ""
    maxIp = ""
    for index in xrange(4):
        if netmaskPart[index] == "255":
            minIp += inetPart[index] + "."
            maxIp += inetPart[index] + "."
        else:
            netmaskPart2bin = bin(int(netmaskPart[index]))
            inetPart2bin = bin2bin(bin(int(inetPart[index])))
            numOfnetmaskbin = len(netmaskPart2bin[2:].split('0')[0])

            prePart = inetPart2bin[:numOfnetmaskbin]
            tailPart = (8 - len(prePart)) * '1'
            if len(prePart) < 8:
                prePart += (8 - len(prePart)) * '0'

            minIp += str(int(prePart, base=2)) + '.'
            maxIp += str(int(prePart, base=2) + int(tailPart, base=2)) + '.'
    minIp = minIp[:-1]
    maxIp = maxIp[:-1]
    return minIp, maxIp


def generateTarget(minIp, maxIp):
    target = ip.iplist(minIp, maxIp)
    return target


def portscan(inet, netmask):
    target = generateTarget(inet, netmask)
    return target


def main():
    banner = '''
     ___                 _   _      _     ____
    |_ _|_ __   ___ _ __| \ | | ___| |_  / ___|  ___ __ _ _ __
     | || '_ \ / _ \ '__|  \| |/ _ \ __| \___ \ / __/ _` | '_ \
     | || | | |  __/ |  | |\  |  __/ |_   ___) | (_| (_| | | | |
    |___|_| |_|\___|_|  |_| \_|\___|\__| |____/ \___\__,_|_| |_|

                author: donot email:blog.donot.me
                     usage: python scan.py
    '''
    print(banner)


if __name__ == '__main__':
    # allIpInfo = getAllIpAddr()
    # for net in allIpInfo:
    #     inet, netmask, _ = net
    #     startIp, endIp = getMinAndMaxIp(inet, netmask)
    #     target = generateTarget(startIp, endIp)
    #     for i in target:
    #         print(i)
    main()
