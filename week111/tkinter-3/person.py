class Person():
    def __init__(self, pid, name, address):
        self.pid=pid
        self.name=name
        self.address=address
    def getPID(self):
        return  self.pid
    def getName(self):
        return  self.name
    def getAddress(self):
        return  self.address
    def setPID(self, pid):
        self.pid = pid
    def setName(self, name):
        self.name=name
    def setAddress(self, address):
        self.address = address
    def __str__(self):
        return ("{}, {}, {}".format(self.pid, self.name, self.address))