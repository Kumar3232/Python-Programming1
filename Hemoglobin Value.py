# Program to check if hemoglobin value is low, normal, or high
gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender entered.")