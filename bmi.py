import sys

print("Welcome to the BMI Calculator!")
unit_req = input("What system of measurement would you like to use? Metric or Imperial?: ").lower()

if unit_req == 'imperial':
    lbs_in = float(input("Enter your weight: "))
    feet_in, inch_in = map(int, input('Enter your height (ft inch): ').split())

    # Converting given values into REAL units (kg & m)
    mass = lbs_in/2.205 # Mass in kg
    f_height = feet_in/3.281
    i_height = inch_in/39.37
    height = f_height+i_height # Total height in m 
elif unit_req == 'metric':
    mass = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    if height > 3: # In case the user is using cm instead of the preferred m. You are NOT going to be taller than 3 meters so it's ok lolllll
        height/=100
else:
    print("Invalid system.")
    sys.exit(0)

# Actual BMI calculations now
bmi = mass/(height ** 2)

# Disclaimer printing
print('')
print("Disclaimer: Before your BMI is printed, be aware that BMI is merely a screening tool and not a definitive measure of health.")
ans = input("Do you accept? (Y/N): ")

# Checking acceptance
if ans == 'N' or ans == 'n':
    print("Must accept disclaimer to proceed.")
    sys.exit(0)


print('')
print(f"Your BMI is: {bmi:.1f}")
print(f"With a BMI of {bmi:.1f}, you are:")
print('')
# BMI Descriptors
if bmi < 18.5:
    print('You are underweight.')
elif bmi >= 18.5 and bmi < 24.9:
    print('You are a healthy weight.')
elif bmi >= 24.9 and bmi < 29.9:
    print('You are overweight.')
elif bmi >= 29.9:
    print('You are obese.')

sys.exit(0)