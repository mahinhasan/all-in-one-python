LabComputer = dict()

class Computer:
    def getComputer(self):
        self.__id = input("Enter pc Number : ")
        self.__os = input("Enter Which os is runnig: ")
        self.__status = input("Enter Status of this pc: ")
        
    
    def addPC(self):
        LabComputer['id'][]
    def printAllPcInfomation(self):
        print("Pc Number : ",self.__id)
        print("Pc Os : ",self.__os)
        print("Pc Status : ",self.__status)

    
LabComputer = dict()

#n = int(input("Enter Pc"))

for i in range(5):
    C = Computer()
    pc = C.getComputer()
    LabComputer.setdefault(pc,C)
    
    C.printAllPcInfomation()   