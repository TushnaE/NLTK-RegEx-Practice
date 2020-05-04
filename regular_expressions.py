## often times when performing string searching, especially with file names
## it can be tough to differentiate between new line or other escape characters
## '\n' and file directory names
## for this reason, you can either add an extra backslash to enforce that 
## something is not an escape character, and is actually meant to be \n or \t
## in the string, or you can "turn off" escape characters by stating 
## explicitly that the string is raw


#############################
# Introduction [Raw String]
#############################

## This example prints 'athan' separately, thinking '\n' is a newline character
file_name = "C:\projects\nathan"
#print(file_name)

## solution #1: double backslash    (removes the extra slash when printing)
file_name = "C:\projects\\nathan"
#print(file_name)

## solution #2: stating the string as 'raw' to "turn off" escape characters
file_name = r"C:\projects\nathan"
#print(file_name)

###############
# RegEx
###############

## Because regular expressions use many backslashes and there is a tendency
## to mistake them for escape characters, all regexpressions strings you use
## should be set as raw strings

import re   ## built in regex module in python
greeting = "hello world"

## searches for the **raw** substring "x" inside the string greeting
print(re.search(r"x", greeting))
    ## None [no match found]

## searches for the **raw** substring "x" inside the string greeting
print(re.search(r"x", r"exit"))



