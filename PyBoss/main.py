# PyBoss

import os
import csv

# Specify file to read
csvPath = os.path.join("employee_data.csv")

# Lists to store data
emp_id_list = []
name_list = []
first_name_list = []
last_name_list = []
DOB_list = []
modified_DOB_list = []
SSN_list = []
first_5_hidden_SSN_list = []
us_state_list = []
abbrev_us_state_list = []

# Empty space variable for rejoining strings
empty_space = ""

# US State abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#  Read the file
with open(csvPath, newline = '') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader)

    for row in csvReader:

        # Add employee ID data to list
        emp_id_list.append(row[0])

        # Add name data to list
        name_list.append(row[1])
        
        # Add DOB data to list
        DOB_list.append(row[2])
        
        # Add SSN data to list
        SSN_list.append(row[3])

        # Add US state data to list
        us_state_list.append(row[4])

    # Split the Name column into separate First Name and Last Name columns
    for full_name in name_list:
        
        # Split full name
        split_name = full_name.split()

        # Add first name tp list
        first_name_list.append(split_name[0])
        
        # Add last name to list
        last_name_list.append(split_name[1])

    # Convert DOB data from YYYY-MM-DD format to MM/DD/YYYY format
    for date in DOB_list:
        
        date = date.replace("-","/")
        date = list(date)
        date.append(date.pop(4))
        
        for i in range(4):    
            date.extend(date.pop(0))
        
        date = empty_space.join(date)
        modified_DOB_list.append(date)

    # Rewrite the SSN data to hide the first five numbers from view
    for number in SSN_list:
        
        number = list(number)
        
        for i in range(6):
            if number[i] == "-":
                continue
            else:
                for x in range(10):
                    number[i] = number[i].replace(str(x),"*")

        number = empty_space.join(number)
        first_5_hidden_SSN_list.append(number)

    # Change the US state data to simple two-letter abbreviations
    for state in us_state_list:

        state = us_state_abbrev[state]
        abbrev_us_state_list.append(state)

# Zip lists together
cleaned_csv = zip(emp_id_list, first_name_list, last_name_list, modified_DOB_list, first_5_hidden_SSN_list, abbrev_us_state_list)

# ---- Export to new CSV file ----

# Set variable for output file
output_file = os.path.join("employee_data_final.csv")

# Open the output file
with open(output_file, "w", newline="") as dataFile:
    writer = csv.writer(dataFile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)