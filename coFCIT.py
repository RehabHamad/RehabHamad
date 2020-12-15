

#  this code for competition of FCIT ,2020
# Written by Rehab Hamad
# Anyone can take benefite of it to learn writing "if,else" statements in Python



print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("   Conditions for transferring male and female students from other faculty at KAU to the Faculty of Computing and Information Technology:   ")
print("-------------------------------------------------------------------------------------------------------------------------------------------")


GPA=3.75
#Preparatory courses
Math110=85
CPIT110=80
ELI104=85

#College courses
CPCS202=75
CPCS203=75
CPIT221=80
CPIT201=80


def welcome():
    print("Congratulations, and we hope that you will be from 15 competitors for each class")

sGPA=eval(input("Enter your GPA: "))
sMath110=eval(input("Enter your Math110 score: "))
sCPIT110=eval(input("Enter your CPIT110 score: "))
sELI104=eval(input("Enter your ELI104 score: "))

if sMath110>=Math110 and sCPIT110>=CPIT110 and sELI104>=ELI104:
    wa=(sMath110*3+sCPIT110*3+sELI104*2)/8
    print(welcome(),",and your wighted average is equal =",wa)
    exit();

# if GPA of student >= GPA but, Some of  the materials are less than the minimum acceptable level
elif  (sGPA>=GPA and sELI104>=ELI104) and (sMath110 < Math110 or sCPIT110<CPIT110):
    print("your english is good :) ,but you need to add a CPCS202 to fulfill the conditions ")
    sco=eval(input("if you study CPCS202 enter your score "))
    if sco >= CPCS202:
        wa2 = (  sco * 3 + sELI104 * 2) / 5
        print(welcome(), ",and your wighted average is equal =", wa2)
    elif sco < CPCS202:
        print("Do not give up add CPCS203 to fulfill the conditions ")
        sco2 = eval(input("if you study CPCS203 enter your score "))
    if sco2 >= CPCS203:
        wa3 = (sco2  * 3 + sELI104 * 2) / 5
        print(welcome(), ",and your wighted average is equal =", wa3)
    elif sco2 < CPCS203:
        print("do not  worry there is always another way  ")


#----------------------------------------------------------------------------------------------------
elif sGPA>=GPA and sELI104< ELI104 and sMath110>=Math110 and sCPIT110>=CPIT110:
    print("do not  worry add CPIT201 to fulfill the conditions ")
    sco3 = eval(input("if you study CPIT201 enter your score "))
    if sco3 >= CPIT201:
        wa4 = (sMath110 * 3 + sCPIT110 * 3 + sco3* 3) / 9
        print(welcome(), ",and your wighted average is equal =", wa4)
    elif sco3 <CPIT201:
        print("Do not give up add CPIT221 to fulfill the conditions ")
        sco4 = eval(input("if you study CPIT221 enter your score "))
    if sco4 >= CPIT221:
        wa5 = (sMath110 * 3 + sCPIT110 * 3 +  sco4  * 3) / 9
        print(welcome(), ",and your wighted average is equal =", wa5)
    elif sco4 < CPIT221:
        print("do not worry there is always another way  ")

#-----------------------------------------------------------------------------

elif (sGPA>=GPA and sELI104< ELI104 )and (sMath110<Math110 or sCPIT110<CPIT110):
    print("do not worry add CPIT201 and CPCS202 to fulfill the conditions ")
    print("if you study CPIT201 and CPCS202 enter your score ")
    sco8 = eval(input("Enter your CPCS202  score  "))
    sco88 =eval(input("Enter your CPIT201 score  "))
    if sco8 >= CPCS202 and  sco88 >=CPIT201 :
        wa2 = (sco8* 3 + sco88 * 3) / 6
        print(welcome(), ",and your wighted average is equal =", wa2)
        exit()
 #--------------
    elif (sco8 < CPCS202) and (sco88>=CPIT201):
        print("do't worry add CPCS203 to fulfill the conditions ")
        sco80 = eval(input("if you study CPCS203 enter your score "))
        if sco80 >= CPCS203:
             wa33 = (sco80* 3 + sco88* 3) /6
             print(welcome(), ",and your wighted average is equal =",wa33)
        elif sco80<CPCS203:
           print("do't worry there is always another way  ")
#--------------

    elif (sco88<CPIT201) and (sco8 >=CPCS202):
        print("do not worry add CPIT221 to fulfill the conditions ")
        sco40 = eval(input("if you study CPIT221 enter your score "))
        if sco40 >= CPIT221:
            wa50 = ( sco8*3  + sco40*3) / 6
            print(welcome(), ",and your wighted average is equal =", wa50)
        elif sco40 < CPIT221:
            print("do not  worry there is always another way  ")

#-------------

    elif (sco8 < CPCS202) and (sco88 < CPIT201):
        print("do not  worry add CPIT221 and CPCS203 to fulfill the conditions ")
        print("if you study  CPIT221 and CPCS203 enter your score ")
        sco89 = eval(input("Enter your CPCS203   score  "))
        sco889 = eval(input("Enter your CPIT221 score  "))
        if sco8 >= CPCS203 and sco88 >= CPIT221:
            wa2 = (sco89 * 3 + sco889 * 3) / 6
            print(welcome(), ",and your wighted average is equal =", wa2)

        elif sco8 < CPCS203 or sco88 < CPIT221:
            print("Do not give up there is always another way  ")

#-------------------------------------------------------------------------
# if GPA of student < GPA and some of  the materials are less than the minimum acceptable level
elif (sGPA<GPA and  sELI104>= ELI104) and  (sMath110<Math110 or sCPIT110<CPIT110):
    print( "Your GPA is lower than the GPA for add CPCS202. Submit your justifications to the College Council, good luck.")

elif sGPA < GPA and sELI104< ELI104  and (sMath110>=Math110 and  sCPIT110>=CPIT110):
       print("Your GPA is lower than the GPA for add CPIT201. Submit your justifications to the College Council, good luck.")

elif sGPA<GPA and sELI104< ELI104 and  sMath110<Math110 or sCPIT110<CPIT110:
    print( "Your GPA is lower than the GPA for add CPCS202 and CPIT201 . Submit your justifications to the College Council, good luck.")



else:
     exit()






