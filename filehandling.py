fo=open("handling.txt","w")
fo.write("\t File Handling \n 6th Class of Python \n in which we are discussing File Handling")

fo.close()

fi=open("handling.txt","r")
fi.read(48)

import os

os.rename("handling.txt","filehandling.txt")

os.remove("filehandling.txt")

"""Class Practice:

Why to learn Python?
    Python is a high level, interpreted, interactive and object-oriented scripting language.

  Python is designed to be highly readable.It uses English keywords
  frequently where as other languages use punctuation,
  and it has fewer syntactical constructions than other languages.
"""

fp= open('Practice.txt','w')
fp.write('Why to learn Python? \n \t \t Python is a high level, interpreted, interactive and object-oriented scripting language. \n \t \t Python is designed to be highly readable. \n \t \t It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.')
fp.close()

with open('Practice.txt','a') as pf:
  pf.write('\n Sub Reh gaya !!')

import os
os.rename('Practice.txt','RenamePractice.txt')