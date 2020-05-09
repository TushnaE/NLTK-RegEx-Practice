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

# ## This example prints 'athan' separately, thinking '\n' is a newline character
# file_name = "C:\projects\nathan"
# print(file_name)

# ## solution #1: double backslash    (removes the extra slash when printing)
# file_name = "C:\projects\\nathan"
# print(file_name)

# ## solution #2: stating the string as 'raw' to "turn off" escape characters
# file_name = r"C:\projects\nathan"
# print(file_name)

###############
# RegEx
###############

## Because regular expressions use many backslashes and there is a tendency
## to mistake them for escape characters, all regexpressions strings you use
## should be set as raw strings

import re   ## built in regex module in python
greeting = "hello world"

# ## searches for the **raw** substring "x" inside the string greeting
# print(re.search(r"x", greeting))
#     # None [no match found]

# ## searches for the **raw** substring "x" inside the raw string "exit"
# ## *Note: not a good use of regex because python does this in itself with "in"
# print(re.search(r"x", r"exit"))
#     # This returns a "match object" because a match was found in the string search
#     # <re.Match object; span=(1, 2), match='x'>

# ## ask if any vowels exist in the string using a "character class"
# print(re.search(r'[aeiou]', r"exit"))
# print(re.search(r'[aeiou]', r"nn"))
# print(re.search(r'[0123456789]', r"$100"))

# ## a range can also be used
# ## the following range represents any ASCII character between 0 & 9 | a-z
# print(re.search(r'[0-9]',r'$100'))
# print(re.search(r'[a-z]',r'$100'))

# ## searching for characters in many ranges, as well as nonranges (_), at once
# print(re.search(r'[a-zA-Z0-9_]',"hello"))


# ## Utilizing the regex output
# output = re.search(r'[o-x]',r'hi there')
# print(output.string)    ## prints 'hi there'
# print(output.re)        ## prints "re.compile('[o-x]')" --> search substring
# print(output.endpos)    ## prints length of incoming string
# print(output.span())    ## prints tuple location of 1st substring item found
# print(output.start())   ## prints start location of 1st substring item found
# print(output.end())     ## prints end location of 1st substring item found

# print('hi there'[output.start():output.end()])

# ## Inversion --> looking for "anything but" using the '^' and '[]'
# print(re.search(r'[^0-9]',"Hello"))

# ## Anchors
# print(re.search(r'^a',"anoshi"))
# print(re.search(r'a$',"anoshi"))
# print(re.search(r'a$',"hiya"))
# print(re.search(r'worst$',"you are the worst"))
# print(re.search(r'^a$',"aa")) ## does this string begin and end with the same 'a' --> No (None)
# print(re.search(r'^a$',"a")) ## does this string begin and end with the same 'a' --> Yes (match object)

## Metacharacters
# print(re.search(r'\[hello\]', "[hello]"))
# print(re.search(r'.',""))
# print(re.search(r'.',"\n"))
# print(re.search(r'a.',"ad"))
# print(re.search(r'a..',"adf"))
# print(re.search(r'a.$', "ag"))

## Patterns
# print(re.search(r'.*a$',"kasjdfal"))

## starts and ends with an 'a'
# print(re.search(r'^a.*a$', "aa"))

## a string of ONLY digits is passed in
print(re.search(r'[0-9]*', "9klk")) ## incorrect; stills counts '9'
print(re.search(r'^[0-9]*$', "23243f56")) ## correct; returns None
    ## this is a string that begins with, and ends with only digits (as 
    ## well as every item in between being a digit)
    ## in this case, the '^' is not an inversion (it's not inside the range)
    ## it is a beginning anchor

## if you don't want an empty string to also pass the match,
## then you must specify that you want at least one character
print(re.search('^[0-9][0-9]*$'))


