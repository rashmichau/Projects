# print("Hello world")
# Match an Email Address: Write a regex pattern to check if a string is a valid email address.
import re
# s=input("enter any mail id :")
# match =re.fullmatch(r"\w[a-zA-Z0-9._][a-zA-Z0-9]*@gmail.com", s)
# if match !=None:
#     print("valid email address")
# else :
#     print("Invalid email address")

# s = "gdsdx 9870654098 bdfdhjg 9087605430 gjhkiuy 8907654908"
# find = re.finditer(r'(0|91)?[987][0-9]{9}', s)
# for i in find:
#     print(i)

# s="gdsdx 9870654098 bdfdhjg 9087605430 gjhkiuy 8907654908"
# find=re.findall(r"[0|91]?[\s][987]([0-9]{9})",s)
# print(find)

'''print("Hello world")
import re
s=input("enter any mail id :")
match =re.fullmatch("\w[a-zA-Z0-9._]*@gmail.com", s)
if match != None:
    print("valid email address")
else :
    print("Invalid email address")

#A password must contain at least one uppercase, one lowercase, one digit, one special character, and be at least 8 characters long
s="Aw3@lddm"
match=re.findall(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',s)

if match!=None:
    print("it is fully find")
else:
    print("it is not find")'''

# Extract all dates in DD-MM-YYYY or DD/MM/YYYY format from a given text
# Test="02-05-2021 and we will get 03/12/1997 after this we will get 09/11/1220"
# match=re.findall("\b\d{2}[-|/]\d{2}[-|/]\d{4}\b","Test")
# print(match)

# str=" 123 jnsjg 456 kjffjsb 67.89 kdfhi"
# match=re.finditer("\d+(.\d+)","str")
# for i in match:
#     print(i)

