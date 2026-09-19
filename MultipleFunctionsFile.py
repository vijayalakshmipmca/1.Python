#class classname(): -- Case sensitive -- indentation is requried
class multifunction():
    
 #Age Calculation : without parameters   
    def agecalc():
        age = int(input("Enter your Age : "))
        if age < 0 :
            print("Invalid age")
            message = "Invalid age"
        elif (age >0 and age < 18):
            print("Minor")
            message = "Minor"
        elif age < 35:
            print("Adult")
            message  = "Adult"
        elif age < 60:
            print("Middle-aged")
            message = "Middle-aged"
        else:
            print("Senior Citizen")
            message = "Senior Citizen"
        return message

     
#BMI Calculation : without parameters
    def bmicalc():
        bmi = int(input("Enter the BMI Index:"))
        if bmi <= 18 :
            print("Underweight")
            msg = "Underweight"
        elif bmi <= 25 :
            print("Normal")
            msg = "Normal"
        elif bmi <= 40 :
            print("Very Overweight")
            msg = "Very Overweight"
        else :
            print("Obese")
            msg = "Obese"
        return msg

#addtion : with parameters
    def addition (num1, num2) :
        add = num1+num2
        return add
        
#subtraction : with parameters        
    def subtraction (num1, num2) :
        sub = num1-num2
        return sub  
        
#multiplication : with parameters        
    def Multiple (num1, num2) :
        mul = num1 * num2
        return mul  
        
#list out the items in the list
    def Subfields() :
        print ("Sub-fields in AI are:" )
        SubFieldsList = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for temp in SubFieldsList :
            print(temp)

#Odd Even check
    def OddEven():
        num = int(input("Enter a number:"))
        if num % 2 == 1 :
            print (num ,"is Odd number")
        else :
            print (num, "is Even number")

# Elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def Elegible() :
        gender = input ("Your Gender:")
        age = int(input("Your Age:"))
        if gender.lower() == "male":
            if age >= 21:
                print ("ELIGIBLE")
            else:
               print ("NOT ELIGIBLE")
        elif gender.lower() == "female":
            if age >= 18:
                print ("ELIGIBLE")
            else:
                print ("NOT ELIGIBLE")
        else:
            print ("Invalid data")

 # calculate the percentage of your 10th mark
    def percentage() :
        Subject1 = int(input("Subject1="))
        Subject2 = int(input("Subject2="))
        Subject3 = int(input("Subject3="))
        Subject4 = int(input("Subject4="))
        Subject5 = int(input("Subject5="))
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        percentage = (total /500) * 100
        print ("Total :", total)
        print ("Percentage :", percentage)      

#print area and perimeter of triangle using functions
    def triangle() :
        Height = int(input ("Height:"))
        Breadth = int(input ("Breadth:"))
        print ("Area formula: (Height*Breadth)/2")
        Area = (Height * Breadth ) / 2
        print ("Area of Triangle:", Area)
        Height1 = int(input ("Height1:"))
        Height2 = int(input ("Height2:"))
        Breadth1 = int(input ("Breadth:"))
        print ("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1 + Height2  + Breadth1
        print ("Perimeter of Triangle:", Perimeter)