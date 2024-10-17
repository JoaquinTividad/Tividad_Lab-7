#name Joaquin Tividad 
#section IT 101
#90.89
#75.01
#85.25

name =(input("Insert your Name Here:"))
section=(input("Insert your Section Here:"))

prelim = float(input("Insert your Prelim Grade Here:"))
midterm = float(input("Insert your Midterm Grade Here:"))
final = float(input("Insert your Final Grade Here:"))

prelimcomp = 0.3333 * prelim
midtermcomp = 0.3333 * midterm
finalcomp = 0.3333 * final
computation = prelimcomp + midtermcomp + finalcomp
finale = round(computation)
if(prelim>=40 and prelim<=100 and midterm>=40 and midterm<=100 and final>=40 and final<=100):
    if(finale>=99 and finale<=100):
        print("Final Grade is:", finale)
        print("Your GPA is 1.00.")
    elif(finale>=96 and finale<=98):
        print("Final Grade is:", finale)
        print("Your GPA is 1.25.")
    elif(finale>=93 and finale<=95):
        print("Final Grade is:", finale)
        print("Your GPA is 1.50.")
    elif(finale>=90 and finale<=92):
        print("Final Grade is:", finale)
        print("Your GPA is 1.75.")
    elif(finale>=87 and finale<=89):
        print("Final Grade is:", finale)
        print("Your GPA is 2.00.")
    elif(finale>=84 and finale<=86):
        print("Final Grade is:", finale)
        print("Your GPA is 2.25.")
    elif(finale>=81 and finale<=83):
        print("Final Grade is:", finale)
        print("Your GPA is 2.50.")
    elif(finale>=77 and finale<=80):
        print("Final Grade is:", finale)
        print("Your GPA is 2.75.")
    elif(finale>=75 and finale<=77):
        print("Final Grade is:", finale)
        print("Your GPA is 3.00.")
    elif(finale<75):
        print("Final Grade is:", finale)
        print("You failed.")
       
else:
    print("Invalid Computation or Input of Grades. Plese try again.")


