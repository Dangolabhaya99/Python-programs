class Customer():
    def __init__(self,cid,name,address):
        self.cid = cid
        self.name = name
        self.address = address

    #Getter
    def getCID(self):
        return self.cid
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

    #Setter
    def setCID(self,cid):
        self.cid = cid
    def setName(self,name):
        self.name = name
    def setAddress(self,address):
        self.address = address

    #str
    def __str__(self):
        return str(self.cid)+","+self.name+","+self.address