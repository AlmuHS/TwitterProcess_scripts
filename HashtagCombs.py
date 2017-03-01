'''Copyright 2017 Almudena Garcia Jurado-Centurion

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

To execute in console, write: "python HashtagCombs.py csvfile outputfile", replacing csvfile with your csv name 
and outputfile with your output file name
'''

import itertools
import sys

def Gen_HashtagCombs(csv_filename, out_filename):
	
	#Open files
	with open(csv_filename, 'r') as input_file, open(out_filename, 'w') as out_file:

		#Read csv file line to line
		for line in input_file:
			
			#Separate line in hashtag list using ; character as separator
			hashtag_list = line.split(";")
			
			#Remove blank strings from hashtag list
			while hashtag_list.count("") > 0:
				hashtag_list.remove("")
												
			#skip one word line
			if len(hashtag_list) < 2:
				continue
				
			else:
				#generate combs list from hashtag list
				combs = itertools.combinations(hashtag_list, 2)
				
				#Copy combinations to output file
				for word in combs:
						
					#if comb has more than one word, copy to output file
					if word[1] != "\n":
						out_file.write(word[0] + "\t" + word[1] + "\n")
					

#Execute function getting parameters from console
if len(sys.argv) < 3:
	print("Error: It needs two parameters")
else:
	Gen_HashtagCombs(sys.argv[1], sys.argv[2])
