import csv

import os.path
'''

'''
def firstime_setup():
    with open("hashedusers.csv", 'w', newline='') as file:
        fields = ['ID', 'Hashed_Name', 'Hashed_Password']
        
        writer = csv.writer(file)

        writer.writerow(fields)

# If the files for storing aircraft and user data have not been initialized,
# then 
if not (os.path.isfile("hashedusers.csv") and os.path.isfile("aircraft.csv")):
    firstime_setup()