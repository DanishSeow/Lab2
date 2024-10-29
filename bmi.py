def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    
    # Classify BMI
    if bmi < 18.5:
        classification = "Under Weight"
    elif 18.5 <= bmi < 25.0:
        classification = "Normal Weight"
    else:
        classification = "Over Weight"
    
    # Return both BMI and classification
    return bmi, classification  

# Usage
bmi, classification = calculate_bmi(weight=57, height=1.73)

print(f"Your BMI is: {bmi:.2f}")
print(f"You are: {classification}")
