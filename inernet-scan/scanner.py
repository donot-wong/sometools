import ping


class LivePcScan():
    def __init__(self, target):
        self.target = target

    def getPing(self):
        for i in self.target:
            pinger = ping.Pinger(i)
            result = pinger.ping()
            if result:
                print(i + " Live")
            else:
                print(i + " Down")


class PortScan():
    def __init__(self, target):
        self.target = target

    def test():
        pass


if __name__ == '__main__':
    test = LivePcScan(['127.0.0.1', '10.10.100.100', 'baidu.com'])
    test.getPing()
