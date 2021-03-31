print("Marvellous Infosystem by Piyush Kahirnar")

print("Demonstration of Types of Function Arguments")

# Position Arguments

def Batches1(name,fees) :
    print("Batch name is :",name)
    print("Fees are :",fees)

print("Demonstration of Position Argumets")
Batches1('Python',5000)
Batches1(5000,'Angular')

# Keyword Arguments 

def Batches2(name,fees) :
    print("Batch name is :",name)
    print("Fees are",fees)

print("Demonstration of Keyword Arguments")

Batches2(fees = 9000,name = 'PPA')
Batches2(name = 'LB',fees = 7500)

# Default Arguments 

def Batches3(name,fees = 5000) :
    print("Batch name is ",name)
    print("Fees is :",fees)
print("Demonstration of Default Arguments")

Batches3('Angular',7500)
Batches3('Angualr')
Batches3(fees = 9000,name = 'PPA')
Batches3(name = 'LB')

#Variable Number of Arguments

def Add(*no) :
    ans = 0
    for i in no :
        ans = ans + i
    return ans

print("Dmonstration of Variable Arguments")

ret = Add(10,20,30)
print("Addition is :",ret)

ret = Add(10,20,30,40,50,60)
print("Addition is :",ret)

ret =Add(10,20)
print("Addition is :",ret)

# Keyword Variable Number of Arguments

def StudentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

print("Demonstration of Keyword Variable Number of Arguments")

StudentInfo(age = 20,address = "Sinhagad Road",mobile = 7588945488,company = "Marvellous")