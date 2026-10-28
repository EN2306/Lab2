def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = (weight/(height**2))
    print(f"BMI = {bmi:.2f}")
    if bmi<18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Overweight")

calculate_bmi(weight=57, height=1.73)
