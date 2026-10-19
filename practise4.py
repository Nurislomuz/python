#Practise 4
#Patient Body Temperature Monitoring
#Write a Python program to manage and analyze the body temperature readings (in °C) of 6 patients.

#Instructions:
#1. Ask the user to enter the body temperatures of 6 patients using a loop and store them in a list.
#2. Use a try-except block to catch invalid non-numeric inputs (ValueError)
# and ensure each reading is between 34.0°C and 43.0°C inclusive.
#3. Calculate and display the average body temperature.
#4. Find and display the highest and lowest temperature readings.
#5. Count and display the number of patients with a fever and those with a normal temperature.
# A patient has a fever if their temperature is 37.5°C or above.
#6. Display all temperature readings that are greater than the average temperature.
patients = 0
temperature = []
try:
    patients = int(input('Enter the number of patients: ').strip())
    if patients <0:
        print('Invalid number of patients')
        raise ValueError
    for s in range(patients):
        l = float(input(f'Enter the body temperature (in °C) for patient {s + 1}: '))
        while l < 34.0 or l > 43.0:
            print('Invalid degrees, it should be between 34°C and 43°C')
            l = float(input('Enter the body temperature (in °C): '))

        temperature.append(l)
except ValueError:
    print('ValueError faced')

else:
    average = (sum(temperature))/patients
    highest = max(temperature)
    lowest = min(temperature)
    print('-'*8)
    print(f'Average body temperature: {average}')
    print(f'Highest body temperature: {highest}')
    print(f'Lowest body temperature: {lowest}')
    print('-' * 8)
    high = []
    count = 0
    for j in temperature:
        if j > 37.5:
            count+=1
        if j > average:
            high.append(j)

    print(f'{count} patients have high temperature')
    print(f'Greater than the average temperature: {high}')
