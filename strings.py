#stirng is collection of characters
from http.cookiejar import uppercase_escaped_char

from variables import firstname

text = "hello world"
course = "WEB DEVELOPMENT"
print(text[6],text[7])
#accessing an element in a string
#length of string
print(len(text))
#modifying a string
print(course.lower())
print(text.upper())
#string concatenation -joining string
greeting = "how are you"
firstname = "vitalis"
print(greeting + " "  + firstname)