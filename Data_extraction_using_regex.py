'''
Shiivong Kapil Birla - 30046572
Created on - 02/10/2018
Modified on - 11/10/2018

This program cleans the raw files and stores them on a desired file
'''

import glob
import re


def cleaned_file(initial_path, final_path): # passing initial and final path of the raw and cleaned files respectively

 files = glob.glob(initial_path) # storing all text files present in file_path


 for name in files: # looping over all files

    with open(name) as f: # opening files one by one

          file_object = f.read() # reading files one by one
          #print(file_object)
          list_of_matches = re.findall(r'\*CHI:[a-zA-Z0-9\t &=\[\]|<>\\\n().+/?,\'!:*]*', file_object) # finding all lines starting with '*CHI:'


          for line in list_of_matches:


              line = str(line).replace('*CHI:\t','') # replacing '*CHI:' with an empty string


              list_of_brackets = re.findall(r'(?!\[/\]|\[//\]|\[\*\]|\[\* [a-z]:\+[a-z]*\])(\[[^\]]*\])', line) # finding everything inside brackets except '[/]', '[//]' and '[* m:+ed]'
              for brackets in list_of_brackets:
                  line = line.replace(brackets, '') # replacing found strings with null string


              list_of_angular = re.findall(r'<[^>]*>', line) # finding all strings within '<>' (including)
              for angular in list_of_angular:
                  line = line.replace(angular, angular[1:-1]) # replacing '<' and '>' and only retaining the word(s) inside


              list_of_removals = re.findall(r'\[\+ [a-z]*\]', line) # finding all strings starting with '[+'
              for removal in list_of_removals:
                  line = line.replace(removal, '') # replacing found strings with null strings


              list_of_round = re.findall(r'(?!\(\.\))\([^)]*\)', line) # finding all strings within '()' (including)
              for round in list_of_round:
                  line = line.replace(round, round[1:-1]) # replacing '(' and ')' and only retaining the word(s) inside


              print(line) # printing resulting line

              file_object_output = open(final_path, 'a') # appending all filtered lines in the final_path

              file_object_output.write(line) # writing all lines in the ouput file


cleaned_file(initial_path = 'ENNI/SLI/*.txt',
             final_path = 'ENNI_Cleaned/SLI_Cleaned/SLI_Cleaned.txt') # calling cleaned_file() with SLI initial and final path

cleaned_file(initial_path = 'ENNI/TD/*.txt',
             final_path= 'ENNI_Cleaned/TD_Cleaned/TD_Cleaned.txt') # alling cleaned_file() with TD initial and final path





