#Create new file
file=open("data1.txt","w")
file.write("host='localhost', user='root', password='',port='3306', database='level4d'")
file.close()

#Apeend on file
# file=open("data.txt","a")
# file.write("Good\n")
# file.close()

#Read file
file=open("Data.txt","r")
contents=file.readlines()
print(contents)