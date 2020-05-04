## often times when performing string searching, especially with file names
## it can be tough to differentiate between new line or other escape characters
## '\n' and file directory names
## for this reason, you can either add an extra backslash to enforce that 
## something is not an escape character, and is actually meant to be \n or \t
## in the string, or you can "turn off" escape characters by stating 
## explicitly that the string is raw