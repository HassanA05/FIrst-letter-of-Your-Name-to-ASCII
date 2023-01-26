ASCII = []
letters = ""
moreletters = "y"
totalletters = []



print("Enter first letter of first name")
letters = input()
totalletters.append(letters)
print("This letter in ASCII is:",(ord(letters)))
ASCII.append(ord(letters))

print(" Another letter y or n?")
moreletters = input()

while moreletters == "y": 
   print("Enter next letter of first name")
   letters = input()
   totalletters.append(letters)
   print(ord(letters))
   ASCII.append(ord(letters))

   print(" Another letter y or n?")
   moreletters = input()



print("Your Name:", totalletters)
print("Your name is ASCII characters number is...", ASCII)




