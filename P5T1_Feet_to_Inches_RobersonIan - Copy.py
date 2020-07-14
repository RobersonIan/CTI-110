# Asks the user for a distance in feet and converts it to inches.
# 7/14/2020
# CTI-110 P5T2_FeetToInches
# Ian Roberson
#

feet = float(input('Enter the distance in feet: '))
feetToInches = 12
inches = feet * feetToInches

if feet == 1:
    print(feet, 'foot is', inches, 'inches.')
else:
    print(feet, 'feet is', inches, 'inches.')

