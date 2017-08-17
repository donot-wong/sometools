#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from IPy import IP
import threading
import requests
import bs4
import sys


def _decode_response_text(strs, lang=None):
    languages = ['UTF-8', 'GB2312', 'GBK', 'iso-8859-1', 'big5']
    if lang:
        languages.insert(0, lang)
    for lang in languages:
        try:
            return strs.encode(lang)
        except:
            pass
    raise Exception('Can not decode response text')


def gettile(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2146.0 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    try:
        r = requests.get('http://' + url, headers=headers, timeout=10)
        if r.status_code == 200:
            html = bs4.BeautifulSoup(_decode_response_text(r.text, r.encoding), 'html.parser')
            if html.title is not None:
                return html.title.text
            else:
                return 'None'
        else:
            return 'None', r.status_code
    except Exception as e:
        return "Get Title Error Maybe Server Is Down"


def getIp():
    # print("请输入网段，如：192.168.0.0/24: ")
    # icdr = raw_input()
    icdr = sys.argv[1]
    ip_total = IP(str(icdr))
    return ip_total


def do_scan(ip, ports):
    try:
        nm = NmapProcess(ip, options="-Pn -sV -p{0}".format(ports))
        rc = nm.run()
        if rc != 0:
            print("nmap scan failed: {0}".format(nm.stderr))
        try:
            parsed = NmapParser.parse(nm.stdout)
            for host in parsed.hosts:
                for serv in host.services:
                    if serv.state == "open":
                        url = ip + ":" + ports
                        title = gettile(url)
                        print('ip: %s, 端口%s 状态%s 对应的服务是 %s title是 %s' % (ip, ports, serv.state, serv.service, title.encode('utf-8')))
                    else:
                        print('ip: %s, 端口%s 状态%s' % (ip, ports, serv.state))
        except NmapParserException as e:
            print("Exception raised while parsing scan: {0}".format(e.msg))
    except AssertionError:
        print('端口：%s，识别不了服务' % ports)


if __name__ == '__main__':
    threads = []
    # ports list
    ports = ["80", "8080", "8081", "88", "443"]
    ip = getIp()
    for i in ip:
        for port in ports:
            t = threading.Thread(target=do_scan, args=(str(i), port,))
            threads.append(t)

    for t in threads:
        t.start()
        while True:
            # limit threading number
            if len(threading.enumerate()) < 100:
                break
    # do_scan("219.151.41.10", "80")
