def cal_bmi(weight, height, unit="metric"):
    if unit == "metric":
        bmi = weight / (height ** 2)
    elif unit == "imperial":
        bmi = 703 * weight / (height ** 2)
    else:
        raise ValueError("Invalid unit, use Metric or Imperial")
    return bmi


def classify_bmi(bmi):
    if bmi < 10.5:
        return "Underweight"
    elif bmi > 25:
        return "Overweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Congrates you have a healthy weight"
    

def main():
    print("Welcome BMI calculator")

    unit = input("Choose unit system (metric/imperial): ").strip().lower()
    if unit == "metric":
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
    elif unit == "imperial":
        weight = float(input("Enter your weight in pounds: "))
        height_ft = float(input("Enter your height in feet: "))
        height_in = float(input("Enter your height in inches: "))

        height= (height_ft * 12) + height_in
    else:
        print("Invalid unit, Please restart the program!")
        return
    
    bmi = cal_bmi(weight, height, unit)
    classification = classify_bmi(bmi)
    print(f"\n Your BMI is: {bmi:.2f}")
    print(f"Health Classification: {classification}")

main()