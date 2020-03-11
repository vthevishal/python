print("---Student grade and attendance generator---")
z=input("enter your name\t ")
while(True):
    try:
        a=int(input("enter grade1\t"))
        break
    except:
        print("try again")
while(True):
    try:
        b=int(input("enter grade2\t"))
        break
    except:
        print("try again")
while(True):
    try:
        c=int(input("enter total number of class\t"))
        if(c!=0): #To avoid divide by zero error
            break
    except:
        print("try again")
while(True):
    try:
     d=int(input("enter total number of absent\t"))
     break
    except:
        print("try again")


f=((c-d)/c)*100                                          #avg_of_attendence
e=(a+b)/2                                                #avg_of_grade
print("Welcome {} Your Result Is".format(z))
print('cummulative of grade is {}'.format(e))
print("The attendance rate is ",(round(f,2)),"%" )
if(f>=80):                                              #chk attendance is above 80%
    if(e>=6):   #chk grade is above 6
        print("You are  approved")
    else:
        print("You are Failed due to Grade")
elif(e>=6):                                             #chk Failed only in attendance and not in Grade
    print("You are Failed due to lack of attendance")
else:
    print("You Failed due to attendance and Grade")
