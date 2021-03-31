class Division :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Your Class Division")
        self.ch = input()

    def ExamSchedule(self) :
        if self.ch == 'A' :
            print("Your Exam is at 7 Am")
        elif self.ch == 'B' :
            print("Your Exam is at 8.30 Am")
        elif self.ch == 'C' :
            print("Your Exam is at 9.20 Am")
        elif self.ch == 'D' :
            print("Your Exam is at 10.30 Am")
        else :
            print("Please Enter Correct Division")

def main() :
    print("Jay Ganesh........")
    obj = Division()
    obj.Accept()
    obj.ExamSchedule()

if __name__  == "__main__" :
    main()