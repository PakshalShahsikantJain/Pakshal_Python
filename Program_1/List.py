print("Marvellous Infosystem By Piyush Khairnar")

print("Demonstration of LIST")

batches = ["PPA","LB","Angular","Python"]

print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

#we can Store Heterogenous Data

data1 = [11,"Marvellous",3.14]
print(data1)

data2 = [21,"Infosystem",6.10]

# We can create list of list 

combined = [data1,data2]
print(combined)

# There are Multiple Methods that we can use to manipuate list

batches.append("Mean")
print(batches)

batches.insert(2,"LSP")
print(batches)

batches.remove("LSP")
print(batches)

batches.pop()
print(batches)

batches.pop(2)
print(batches)

del batches[1:]
print(batches)

batches.extend(["LB","Python","Angular","Mean"])
print(batches)

batches.sort()
print(batches)