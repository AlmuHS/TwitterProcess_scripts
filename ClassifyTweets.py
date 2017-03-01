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


'''
This script classify a tweet set, using key words setted previously as support or reject words extracted from two files.
The support file contains the list of support hashtags, with a hashtag per line
The reject file is similar to support file, but with reject hashtags.

The tweet set is getted from a csv file, which contains the tweet identifier, the text, and your hashtag list, separated with spaces

The script read the hashtag list of each tweet, and set a code to this, based in the contents of your hashtag list
The possible codes are: 1=support, 2=reject, 3=uncertain, 4=unclassificable

support = the tweet only contains hashtags of support file
reject = the tweet only contains hashtags of reject file
uncertains = the tweet contains hashtag of both files
unclassificable = the tweet don't contains any files hashtag

This code is written in a out file, which contains all columns of the csv file, and a new column with the code assigned for each tweet
 '''

import csv
import re
import sys

def ClassifyTweets(csv_filename, support_filename, reject_filename, out_filename):
	
	#Open files
	with open(csv_filename, 'r') as csv_file, open(support_filename, 'r') as support_file, open(reject_filename, 'r') as reject_file, open(out_filename, 'w') as out_file:
		
		#Create dictionary
		code_dict = dict()
		
		#Add words to dictionary, deleting extra characters
		for line in support_file:
			code_dict[re.sub(" *\n", "", line)] = 1
			
		for line in reject_file:
			code_dict[re.sub(" *\n", "", line)] = 2
			
		#get lines from csv file
		refureader = csv.reader(csv_file, delimiter=';')
		
		#Read lines
		for row in refureader:
			tweet = list(row)
					
			#Get hashtag list
			hashtag_list = tweet[2].split(" ")
							
			#At first, all flags are unmarked
			support = False
			reject = False
			uncategorized = False	
					
			#Clasify tweets
			for hashtag in hashtag_list:
				code = -1
				
				try:
					#Search word in dictionary
					code = code_dict[hashtag]
				
				#if the word isn't in dictionary, mark as uncategorized
				except KeyError:
					uncategorized = True
				
				#If the word has code 1, mark as support and unmark as uncategorized
				if code == 1:
					support = True
					uncategorized = False
						
				#if the word has code 2, mark as reject and unmark as uncategorized
				elif code == 2:
					reject = True
					uncategorized = False
					
			#if support and reject flags are marked, set code 3 (uncertain tweet)
			if support and reject:
				code = 3
				
			#if support flag is marked but reject flag isn't, set code 1 (support tweet)
			elif support and not reject:
				code = 1
				
			#if support is unmarked and reject is, set code 2 (reject tweet)
			elif not support and reject:
				code = 2
				
			#if both flags are unmarked, set code 4 (unclasificable tweet)
			elif not support and not reject and uncategorized:
				code = 4
					
			#write tweet with code added			
			out_file.write(tweet[0] + ";" + tweet[1] + ";" + tweet[2] + ";" + str(code) + "\n")
		
#Execute function
if len(sys.argv) < 5:
	print("Error: It needs four parameters")
else:
	ClassifyTweets(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	
