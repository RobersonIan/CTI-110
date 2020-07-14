# Asks the user for a distance in kilometers and converts it to miles.
# 7/14/2020
# CTI-110 P5T1_KilometerConverter
# Ian Roberson
#

kilometers = float(input('Enter the distance in kilometers: '))
milesToKilo = 0.6214
miles = kilometers * milesToKilo

print(kilometers, 'kilometers is', miles, 'miles.')


