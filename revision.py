print("Happy 2021!!")
secret_of_life = 42
gst_percentage = 0.07
sentence = "The quick brown fox jumps over the lazy dog"
is_raining = True
# BMI Calculator
print("2021 New Year Resolution BMI Calculator")

weight = float(input("please enter your weight in kg "))
height = float(input("please enter your height in m "))
bmi = weight / (height * height)
print("Your BMI is", bmi)

if bmi < 18.5:
    print("underweight")
elif bmi <= 24.9:
    print("normal weight")
elif bmi < 29.9:
    print("overweight")
else:
    print("obese")
