#  Author  Emily Schwartz 
#  github: https://github.com/EmilySchwartz1 
#  date 3/29/23 
#  
#  Description:
#
#  Simple python script to compare if 2 strings are equal  For example
#  to compare 2 if 2 hashes are the same. 
#  Made this a little more complicated than it needs to be to 
#  teach myself python 

#----------------global variables------------------

string1 = ''
string2 = ''
ans = ''


#----------------functions------------------

def getFirstString():
  print("Enter the first string, hash, etc... to compare: ")
  return input()

def getSecondString():
  print("Enter the second string, hash, etc... to compare: ")
  return input()

def stringInfo(_string1, _string2):
  print("string 1 = ", _string1)
  print("string 2 = ", _string2)
  print("string has a length of: ", len(_string1), " chars")
  print("string has a length of: ", len(_string2), " chars")
   
 
def compareStrings(_string1, _string2):
  if _string1 == _string2:
    print('String 1 and 2 are equal')
  elif string1.casefold() == string2.casefold():
    print('string 1 and 2 are equal ignoring case')
  else:
    print('string 1 and 2 do not match')
#----------------main loop------------------

while ans.lower() != 'x':
  string1 = getFirstString()
  string2 = getSecondString()
  stringInfo(string1,string2)
  compareStrings(string1,string2)
  print("Enter y to continue, x to exit: ")
  ans = input()
  print(ans)

exit()
