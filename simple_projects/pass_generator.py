import random
import string
def generate_pass(min_len, numbers=True ,special_characters=True):
     letters=string.ascii_letters
     digits=string.digits
     special=string.punctuation
     
     characters=letters
     if numbers:
          characters+=digits
          
     if special_characters:
          characters+=special

     pwd=""
     meet_criteria=False
     has_number=False
     has_special=False

     while not meet_criteria or len(pwd) < min_len:
          new_char=random.choice(characters)
          pwd += new_char

          if new_char in digits:
               has_number = True
          elif new_char in special:
               has_special=True

          meet_criteria = True
          if numbers:
               meet_criteria += has_number
          if special_characters:
               meet_criteria += meet_criteria and has_special
          
     return pwd

min_len=int(input("enter the number"))
has_number=input("do you waant the numbers ? (y/n)").lower() == "y"
has_special=input("do you waant the special characters ? (y/n)").lower() == "y"
pwd=generate_pass(min_len,has_number,has_special)
print("The generated password is :",pwd)


