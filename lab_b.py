"""
Created by Alicia Nguyen on 6-9-2021.
This program uses a dictionary to organize data. It shows the key is department.
Whereas value is the test. It interacts with a user to get information.

"""

laboratory = {'Hematology': 'Cell_Count', 'Microbiology': 'COVID_19', 'Chemistry': 'Basic_Metabolic_Panel'}

while True:

        department = input(" Enter a department: (leave empty if done)")

        # User did not enter any input. Therefore the program detected empty string which ended While loop executing by
        # break statement.
        if department == "":
            break

        # Comparing user's result with department in variable called laboratory
        if department in laboratory:
            print(laboratory[department] + " performs in " + department + '.')

        # Add and update new information when data is not store in laboratory.
        else:
            print(" This department " + department + " is not listed. ")
            d = input(" Please enter department ")
            test = input(" Please enter test name ")
            laboratory[department] = test
            print(d + " processes " + test + ".")
            print(" New information updated. ")
            print(laboratory)