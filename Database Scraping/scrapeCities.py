import csv

source_file = 'InstitutionCampusAlt.csv' # change this file to the DAPIP InstitutionCampus...csv file on your machine if running for self
trio_file = 'TRIOUniversityCities.csv' # file only contains university names, will be updated to have cities

city_dict = {} # creates dictionary to hold { university name : city } data from read section to use in wrting section

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
                    city = address_list[-2] # index 0 gets street, index -1 gets state & zip code, index -2 gets city

                    if row_T['Student Support Services(SSS) Grantees'] not in city_dict:
                        city_dict[row_T['Student Support Services(SSS) Grantees']] = city # created dictionary for comparisons
                    
                elif row_T['Student Support Services(SSS) Grantees'] == row_I['ParentName']:

                    address = str(row_I['Address'])
                    address_list = address.split(',') # FORM OF DATA IN ADDRESS : " street , city , state & zip code "
                    city = address_list[-2] # index 0 gets street, index -1 gets state & zip code, index -2 gets city

                    if row_T['Student Support Services(SSS) Grantees'] not in city_dict:
                        city_dict[row_T['Student Support Services(SSS) Grantees']] = city # created dictionary for comparisons
        
        trio_csv.seek(0)
        trio_read = csv.DictReader(trio_csv)
        trio_rows = list(trio_read)

        for row in trio_rows:
            name_check = row['Student Support Services(SSS) Grantees']
            if name_check in city_dict:
                row['City'] = city_dict[name_check]
        
        input_csv.close()
    trio_csv.close()

with open(trio_file, 'w') as trio_csv:

    fieldnames_requirement = ['Student Support Services(SSS) Grantees', 'City']
    trio_write = csv.DictWriter(trio_csv, fieldnames=fieldnames_requirement)
    
    trio_write.writeheader()
    trio_write.writerows(trio_rows)
    
trio_csv.close()
