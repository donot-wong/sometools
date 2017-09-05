import ping


class LivePcScan():
    def __init__(self, target):
        self.target = target
        self.result = []

    def getPing(self):
        for i in self.target:
            print("Ping %s" % i)
            pinger = ping.Pinger(i)
            result = pinger.ping()
            if result:
                # print(i + " Live")
                self.result.append(i)
            else:
                # print(i + " Down")
                pass
        return self.result


class PortScan():
    def __init__(self, target):
        self.target = target

    def test():
        pass


# if __name__ == '__main__':
#     test = LivePcScan(['127.0.0.1', '10.10.100.100', 'baidu.com'])
#     liveIp = test.getPing()
