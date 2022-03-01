# Command line BMI Calculator
# Tanner Hess
# Tmh648


def BMI(feet, inches, pounds):
    kg = pounds  * .45
    total_inches = inches + (feet*12)
    meters = .025 * total_inches
    meters_squared = meters*meters
    bmi = round(kg/meters_squared, 1)

    if bmi < 18.5:
        weight_class = "Underweight"
    elif bmi <= 24.9:
        weight_class = "Normal"
    elif bmi <= 29.9:
        weight_class = "Overweight"
    else:
        weight_class = "Obese"

    return bmi, weight_class

def main():
    run = "1"
    print("Hello user, welcome to te BMI calculator\n")
    while run == "1":
        print("Please enter your body metrics below (Height is presented as feet then inches):")
        feet = input("Height (Feet): ")
        inches = input("Height (Inches): ")
        weight = input("Weight: ")
        bmi, weight_class = BMI(feet,inches,weight)
        print("Your BMI has successfully been calculated to be:"+str(bmi))
        print("Your BMI indicates you weigh in as"+weight_class)
        run=input("Would you like to continue?\n1) Yes\n2) No\nSelection: ")

        
    return 0


main()
