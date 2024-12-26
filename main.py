"""
Name: Orlando Marin
Date: December 26, 2024

Design a program that lets the user enter the total rainfall for each of 12 
months into a list. The program should calculate and display the total rainfall 
for the year, the average monthly rainfall, the months with the highest and 
lowest amounts.
"""

# create a months list that contains each month of the year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# create an empty monthly rainfall list
monthlyRainfall = []

# print opening message
print("Enter the rainfall, in inches, for each month of the year.")

# iterate thruogh the months list so user can enter rainfall for each month
# append the rainfall for each month to the monthlyrainfall list
for month in months:
    monthlyRain = float(input(f"{month}: "))
    monthlyRainfall.append(monthlyRain)

# print the monthlyrainfall list for confirmation purposes
print(monthlyRainfall)

# calculate the total rainfall for the year
yearRainfall = sum(monthlyRainfall)

# print the results, round to 2 decimal places
print(f"The total rainfall for the year was {yearRainfall:,.2f} inches.")

# calculate the average rainfall for the year
averageRainfall = yearRainfall / len(monthlyRainfall)

# print the results, round to 2 decimal places
print(f"The average monthly rainfall for the year was {averageRainfall:,.2f} inches.")

# find the max rainfall for the year
maxRainfall = max(monthlyRainfall)

# find the index of the max rainfall for the year
maxRainMonthIndex = monthlyRainfall.index(maxRainfall)

# use the index to find the month with the most rain
maxRainMonth = months[maxRainMonthIndex]

# print the result
print(f"The month with the most rain: {maxRainMonth}")

# find the min rainfall for the year
minRainfall = min(monthlyRainfall)

# find the index of the min rainfall for the year
minRainMonthIndex = monthlyRainfall.index(minRainfall)

# use the index to find the month with the least rain
minRainMonth = months[minRainMonthIndex]

# print the result
print(f"The month with the least rain: {minRainMonth}")