'''Copyright 2017 Almudena Garcia Jurado-Centurion
Developed with the help of the Python España community

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''


'''This script generate a two columns text file, with the combinations two to two of tweets' hashtag
extracted from csv file

The csv file contains the hashtag list from differents tweets, with a tweet per line
The script performs the combinational of words two to two in each line from csv file, and copy the results in a new file

To execute in console, write: "python HashtagCombs_csv.py csvfile outputfile", replacing csvfile with your csv name 
and outputfile with your output file name
'''


import itertools
import csv
import sys

def Gen_HashtagCombs(csv_filename, out_filename):
	
	#Open files
    with open(csv_filename, 'r') as input_file, open(out_filename, 'w') as out_file:
       
		#get lines from csv file
        refureader = csv.reader(input_file, delimiter=';')
        
        #Read lines one by one
        for row in refureader:
			
			#Get hashtag list without blank lines
            hashtag_list = list(filter(None, row))

			#if hashtag list have less than two words, skip line
            if len(hashtag_list) < 2:
                continue

			#get combinations list 
            combs = itertools.combinations(hashtag_list, 2)

			#copy combinations to output file
            for word in combs:
                out_file.write('\t'.join(word) + "\n")
                

#Execute function getting parameters from console
if len(sys.argv) < 3:
	print("Error: It needs two parameters")
else:
	Gen_HashtagCombs(sys.argv[1], sys.argv[2])
