def calculate_bmi(height,weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    BMI = weight/ (height * height)
    print("bmi=" + str(BMI))

    if BMI < 18.5 :
        return "Under Weight"
    elif 18.5 <= BMI <= 25.0:
        return "Normal Weight"
    else:
        return "Over Weight"
    
print(calculate_bmi(weight=57, height = 1.73))
