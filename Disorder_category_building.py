'''
Shiivong Kapil Birla - 30046572
Created on - 04/10/2018
Modified on - 11/10/2018

This program counts the strings of the cleaned file based on the regular expressions defined below
'''


import glob
import re


class Analyser: # class definition


   def __init__(self, number_of_retracing_words = 0, number_of_repeating_words = 0, number_of_statements = 0, number_of_grammatical_errors = 0, number_of_pauses = 0, number_of_unique_words = 0): # initializing variables with default values

    self.number_of_retracing_words = number_of_retracing_words # defining variables for each stat
    self.number_of_repeating_words = number_of_repeating_words
    self.number_of_statements = number_of_statements
    self.number_of_grammatical_errors = number_of_grammatical_errors
    self.number_of_pauses = number_of_pauses
    self.number_of_unique_words = number_of_unique_words


   def __str__(self): # printing all six statistics for each group

        print("Number of retracing words '[//]' are : " + str(self.number_of_retracing_words))
        print("Number of repeating words '[/]' are : " + str(self.number_of_repeating_words))
        print("Number of statements '[.!?]' are : " + str(self.number_of_statements))
        print("Number of grammatical errors '[* m:+ed]' are : " + str(self.number_of_grammatical_errors))
        print("Number of pauses '(.)' are : " + str(self.number_of_pauses))
        print("Number of unique words are : " + str(self.number_of_unique_words))



   def analyse_script(self, file_path): # passing file path as an arguement

       self.file_path = file_path

       files = glob.glob(file_path) # storing all text files present in file_path

       for name in files: # looping over all files

            with open(name) as f: # opening files one by one

                file_object = f.read() # reading files one by one

                retracing_statements = re.findall(r'(\[//])', file_object) # finding all '[//]' using regex

                for retracing_statement in retracing_statements:

                    self.number_of_retracing_words+=1 # incrementing '[//]' count for every encounter

                repeating_statements = re.findall(r'(\[/])', file_object) # finding all '[/]' using regex

                for repeating_statement in repeating_statements:

                    self.number_of_repeating_words+=1 # incrementing '[/]' count for every encounter

                grammatical_errors = re.findall(r'\[\* [a-z]:\+[a-z]*\]', file_object) # finding all '[* m:+ed]' using regex

                for grammatical_error in grammatical_errors:

                    self.number_of_grammatical_errors+=1 # incrementing '[* m:+ed]' count for every encounter

                pauses = re.findall(r'\(\.\)', file_object) # finding all '(.)' using regex

                for pause in pauses:

                    self.number_of_pauses+=1 # incrementing '(.)' count for every encounter

                statment_pattern = re.compile(r'[.?!]$', re.MULTILINE) # finding all statements that end with '.', '?' or '!' using regex

                statements = re.findall(statment_pattern, file_object)

                for statement in statements:

                    self.number_of_statements+=1 # incrementing '[.!?]' count for every encounter

                list_of_words = file_object.split() # converting all file_objects to list of words
                set_of_words = set(list_of_words) # converting all list of words into a set to make it unique
                self.number_of_unique_words = len(set_of_words) # finding the length of the defined set

                list_of_categories = [self.number_of_retracing_words, self.number_of_repeating_words,
                                      self.number_of_statements, self.number_of_grammatical_errors,
                                       self.number_of_pauses, self.number_of_unique_words] # storing all stats in one list

                return list_of_categories # returning the stats list


print("SLI Group Stats")
print("--- ----- -----")
SLI_file = Analyser() # making an object for SLI and initializing the class
SLI_file.analyse_script('ENNI_Cleaned/SLI_Cleaned/SLI_Cleaned.txt') # calling the analyse_script with the SLI cleaned file path
SLI_file.__str__() # overiding __str()__ to print SLI stats


print("\nTD Group Stats")
print("-- ----- -----")
TD_file = Analyser() # making an object for TD and initializing the path
TD_file.analyse_script('ENNI_Cleaned/TD_Cleaned/TD_Cleaned.txt') # calling the analyze_script with the TD cleaned file path
TD_file.__str__() # overiding __str()__ to print TD stats


