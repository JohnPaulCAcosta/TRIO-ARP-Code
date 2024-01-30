import csv

""" Explanation (primarily for anyone not familiar with this file): 

Due to the Database of Accredited Postsecondary Institutions and Programs (DAPIP) having a 
well-organized/clean database, we can make a lot of generalizations in this code that will likely hold.
In the 'Address' column, we can make that data into a string variable (holds characters including
letters and numbers) and essentially pick out the third-to-last word which should be the city name!)

CONSIDERATIONS (primarily for code contributors):

1. Not all cities are one word, ie College Station, so we can attempt to splice the string with the
commas since the commas separate columns, but we can splice with spaces for zip codes!!

2. We must first compare the DAPIP database to the TRIO database first before we separate the address
into a string variable, because once we separate into a string variable, we lose the university name!

3. There are some institutions where the data is blank (noted by '-') in the database for the 'ParentName'
column, so we can try to look at the 'LocationName' column instead, yet there still may be errors! Such
examples include how TAMU Galveston has no institution name, so it should not get a city if we only
use the 'ParentName' column, may be in the inevitable clean-up

How to set-up:

1. Open folder that CONTAINS .csv files and this .py files in VSCode
2. CTRL + SHIFT + P -> Python: Create Environment -> <select your Python>
3. CTRL + SHIFT + P -> Python: Create Terminal -> get to work!

"""

source_file = 'InstitutionCampusAlt.csv' # change this file to the DAPIP InstitutionCampus...csv file on your machine if running for self
trio_file = 'TRIOUniversityZipcodes.csv' # file only contains university names, will be updated to have cities

zip_dict = {} # creates dictionary to hold { university name : zipcode } data from read section to use in writing section

with open(trio_file, 'r') as trio_csv:
    
    trio_read = csv.DictReader(trio_csv) # trio_read now has a dictionary with column labels as keys, and corresponding values of the rows
    # ie {   'Name' : "TAMU", "LSU"    }

    with open(source_file, 'r') as input_csv:
        
        input_read = csv.DictReader(input_csv)  # input_read now has a dictionary with column labels as keys, and corresponding values of the rows
        # ie {   'Name' : "TAMU", "LSU"    ,    'Address' : "123 Lane", "456 Hollywood"    }

        # i = int(0) # counts matches

        input_rows = list(input_read) # double for loop will not work if inner loop as dictionary
        # we turn the inner loop dictionary into a list, think of the the row of data as one element in the list of many elements


        for row_T in trio_read:
            for row_I in input_rows:
                # compare DAPIP csv (input_csv/read/rows) to TRIO csv (trio_csv/read) to determine which universities we should look at

                if row_T['Student Support Services(SSS) Grantees'] == row_I['LocationName']:

                    address = str(row_I['Address'])
                    address_list = address.split(',') # FORM OF DATA IN ADDRESS : " street , city , state & zip code "

                    address_for_zip_list = address_list[-1].split() # list of [ state , zipcode ] separated by whitespaces
                    zipcode = address_for_zip_list[-1] # gets zipcode

                    if row_T['Student Support Services(SSS) Grantees'] not in zip_dict:
                        zip_dict[row_T['Student Support Services(SSS) Grantees']] = zipcode
                    
                elif row_T['Student Support Services(SSS) Grantees'] == row_I['ParentName']:

                    address = str(row_I['Address'])
                    address_list = address.split(',') # FORM OF DATA IN ADDRESS : " street , city , state & zip code "

                    address_for_zip_list = address_list[-1].split() # list of [ state , zipcode ] separated by whitespaces
                    zipcode = address_for_zip_list[-1] # gets zipcode

                    if row_T['Student Support Services(SSS) Grantees'] not in zip_dict:
                        zip_dict[row_T['Student Support Services(SSS) Grantees']] = zipcode
        
        trio_csv.seek(0)
        trio_read = csv.DictReader(trio_csv)
        trio_rows = list(trio_read)

        for row in trio_rows:
            name_check = row['Student Support Services(SSS) Grantees']
            if name_check in zip_dict:
                row['Zipcode'] = zip_dict[name_check]
        
        input_csv.close()
    trio_csv.close()

with open(trio_file, 'w') as trio_csv:

    fieldnames_requirement = ['Student Support Services(SSS) Grantees', 'Zipcode']
    trio_write = csv.DictWriter(trio_csv, fieldnames=fieldnames_requirement)
    
    trio_write.writeheader()
    trio_write.writerows(trio_rows)
    
trio_csv.close()