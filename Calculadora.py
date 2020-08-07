from tkinter import *

class Calculator():

    def __init__(self,first_value=0, second_value=1):
        self.__first_value = first_value
        self.__second_value = second_value

    def get_first(self):
        return self.__first_value

    def get_second(self):
        return self.__second_value

    def set_first(self,new_value):
        self.__first_value = new_value

    def set_second(self,new_value):
        self.__second_value = new_value     

    def sum(self):
        return self.__first_value + self.__second_value

    def subtraction(self):
        return self.__first_value - self.__second_value

    def multiplication(self):
        return self.__first_value * self.__second_value

    def division(self):
        return self.__first_value / self.__second_value

    def mod(self):
        return self.__first_value % self.__second_value

class Interface():

    def __init__(self, interface):

        self.fix_value = ''
        self.dynamic_value = '0'
        self.virgula = False
        self.algoritm = Calculator()
        self.operation = None
        self.hash_button = {
            "%": self.algoritm.mod(),
            "/": self.algoritm.division(),
            "X": self.algoritm.multiplication(),
            "-": self.algoritm.subtraction(),
            "+": self.algoritm.sum()
            }
        self.reset = False

        self.interface = interface

        self.create_calculator()

    def create_calculator(self):

        self.entrada1 = Label(self.interface, bg = "#EBEBEB",width = 18,height = 1,text = self.fix_value,font = ("Calibri","20","bold"),anchor = "se")
        self.entrada1.grid(row = 0, column = 0,sticky = "EW")
        
        self.entrada2 = Label(self.interface, bg = "#EBEBEB",width = 18,height = 2,text = self.dynamic_value,font = ("Calibri","24","bold"),anchor = "se")
        self.entrada2.grid(row = 1, column = 0,sticky = "EW")

        self.bottom_frame = Frame(self.interface,bg = "#D6D6D6", width = 50, height = 5)
        self.bottom_frame.grid(row = 2, column = 0)

        bottons = [
            ["%","CE","C","<-"],
            ["7","8","9","/"],
            ["4","5","6","X"],
            ["1","2","3","-"],
            [".","0","=","+"]
        ]

        commands = [
            ["action","row","reset","backspace"],
            ["add","add","add","action"],
            ["add","add","add","action"],
            ["add","add","add","action"],
            ["vir","add","result","action"]
        ]

        for i in range(5):
            for j in range(4):
                Button(self.bottom_frame,bg = "#EFEFEF",text = bottons[i][j], width = 6, height = 2,command = lambda a = bottons[i][j],b = commands[i][j]: self.SetState(a,b),relief = "flat",font = ("Calibri","16","bold")).grid(row = i,column = j,padx = 2,pady = 2)
                
                

    def SetState(self,text,command):
        if self.reset:
            self.fix_value = ''
            self.dynamic_value = '0'
            self.virgula = False
            self.reset = False
            
        self.entrada2.grid_forget()
        self.entrada1.grid_forget()
        if command == "add":
            if self.dynamic_value != "0" :
                self.dynamic_value += text
            else:
                self.dynamic_value = text

            self.entrada2["text"] = self.dynamic_value
        elif command == "vir":
            if not self.virgula:
                self.dynamic_value += text
                self.virgula = True
                self.entrada2["text"] = self.dynamic_value

        elif command == "action":
            self.virgula = False
            if self.fix_value != '':
                self.cal()
            else:
                self.fix_value = self.dynamic_value
            self.operation = text
            self.entrada1["text"] = self.fix_value
            self.dynamic_value = "0"
            self.entrada2["text"] = self.dynamic_value

        elif command == "result":
            result = self.cal()
            self.fix_value = ''
            self.dynamic_value = result
            self.operation = None
            self.entrada1["text"] = self.fix_value
            self.entrada2["text"] = self.dynamic_value
            self.reset = True

        elif command == "row":
            self.dynamic_value = '0'
            self.entrada2["text"] = self.dynamic_value

        elif command == "reset":
            self.fix_value = ''
            self.dynamic_value = '0'
            self.entrada1["text"] = self.fix_value
            self.entrada2["text"] = self.dynamic_value
            self.virgula = False
            self.reset = False

        elif command == "backspace":
            self.dynamic_value = self.dynamic_value[:-1]
            self.entrada2["text"] = self.dynamic_value

        self.entrada1.grid(row = 0, column = 0,sticky = "EW")
        self.entrada2.grid(row = 1, column = 0,sticky = "EW")

    def cal(self):
        self.algoritm.set_first(float(self.fix_value))
        self.algoritm.set_second(float(self.dynamic_value))

        if self.operation == "%":
            op = self.algoritm.mod()
        elif self.operation == "/":
            op = self.algoritm.division()
                    
        elif self.operation == "X":
            op = self.algoritm.multiplication()
        elif self.operation == "-":
            op = self.algoritm.subtraction()
        elif self.operation == "+":
            op = self.algoritm.sum()
                    
        if op.is_integer():
            self.fix_value = int(op)
        else:
            self.fix_value = float(op)

        return self.fix_value

root = Tk()
root.geometry("320x505")
root["bg"] = "#B6B6B6"
root.resizable(width=False, height=False)
O = Interface(root)
root.mainloop()













        
