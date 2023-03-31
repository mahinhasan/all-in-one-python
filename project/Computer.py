class Computer:
    def __init__(self, ID, os_name, status, problem):
        self.__os_name = os_name
        self.__ID = ID
        self.__status = status
        self.__problem = problem

    def set_name(self, os_name):
        self.__os_name = os_name

    def set_ID(self, ID):
        self.__ID = ID

    def set_dept(self, status):
        self.__status = status

    def set_problem(self, problem):
        self.__problem = problem

    def get_os_name(self):
        return self.os_name

    def get_ID(self):
        return self.__ID

    def get_status(self):
        return self.__status

    def get_problem(self):
        return self.__problem

    def __str__(self):
        return (f"\n\n\t**********************************\n\t| Computer Details For:  {self.__ID}  \n\t|=======================\n\t| OS Name: {self.__os_name}\n\t| ID Number:  {self.__ID}\n "
                f"\t| Status: {self.__status}\n\t| Problem: {self.__problem}\n\t**********************************\n\n")