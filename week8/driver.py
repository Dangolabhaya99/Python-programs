class Driver():
    def __init__(self, did=0, name=None, licenseno=None):
        self.did = did
        self.name = name
        self.licenseno = licenseno

    # Getters
    def getDID(self):
        return self.did
    def getName(self):
        return self.name
    def getLicenseNo(self):
        return self.licenseno

    # Setters
    def setDID(self, did):
        self.did=did
    def setName(self, name):
        self.name=name
    def setLicenseNo(self, licenseno):
        self.licenseno=licenseno
    # str
    def __str__(self):
        return str(self.did)+", "+self.name+", "+self.licenseno