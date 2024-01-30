## Database Scraping 🐍

Due to the Database of Accredited Postsecondary Institutions and Programs (DAPIP) having a 
well-organized/clean database, we can make a lot of generalizations in this code that will likely hold.
In the 'Address' column, we can make that data into a string variable (holds characters including
letters and numbers) and essentially pick out the third-to-last word which should be the city name!)

## How to set-up:

1. Open folder that CONTAINS .csv files and this .py files in VSCode (can use any text editor/compiler/python IDE, but further steps may not apply)
2. CTRL + SHIFT + P -> Python: Create Environment -> <select your Python>
3. CTRL + SHIFT + P -> Python: Create Terminal -> get to work!


# CONSIDERATIONS (primarily for code contributors):

1. Not all cities are one word, ie College Station, so we can attempt to splice the string with the
commas since the commas separate columns, but we can splice with spaces for zip codes!!

2. We must first compare the DAPIP database to the TRIO database first before we separate the address
into a string variable, because once we separate into a string variable, we lose the university name!

3. There are some institutions where the data is blank (noted by '-') in the database for the 'ParentName'
column, so we can try to look at the 'LocationName' column instead, yet there still may be errors! Such
examples include how TAMU Galveston has no institution name, so it should not get a city if we only
use the 'ParentName' column, may be in the inevitable clean-up
