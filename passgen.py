import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
quit = 0
while quit == 0:
  print("What Type Of Password Do You Want")
  print("1: Super Secure Password")
  print("2: No Symbol Password")
  print("3: Readable Password")
  print("4: Quit")
  choice = input("")
  if choice == "1":
    passnum = ""
    while isinstance(passnum, str):
      passnum = input("How Many Passwords Do You Want To Generate? ")
      try:
        passnum = int(passnum)
      except:
        print("Please Enter A Number")
        passnum = str(passnum)
      else:
        passnum = int(passnum)

    passcount = 0
    thing1 = [40, 41]
    print("___________________")

    # Generate password using all the characters, in random order # + ....
    while passcount != passnum:
      randsymbol = chr(random.randint(36, 38))
      randsymbol2 = chr(random.randint(36, 38))
      randsymbol3 = chr(random.randint(36, 38))
      randsymbol4 = chr(random.randint(36, 38))
      number = chr(random.randint(48, 57))
      number2 = chr(random.randint(48, 57))
      number3 = chr(random.randint(48, 57))
      number4 = chr(random.randint(48, 57))
      lowercaseletter = chr(random.randint(97, 122))
      lowercaseletter2 = chr(random.randint(97, 122))
      uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
      uppercaseLetter2 = chr(random.randint(65, 90))
      uppercaseLetter3 = chr(random.randint(65, 90))
      uppercaseLetter4 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
      thing = chr(random.choice(thing1))
      password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + randsymbol + randsymbol2 + randsymbol3 + randsymbol4 + number + number2 + number3 + number4 + lowercaseletter + lowercaseletter2 + thing
      password = shuffle(password)
      print(password)
      passcount += 1

      # Ouput
    print("___________________")
    choice = 0
    passnum = 0
    passcount = 0
  if choice == "2":
    passnum = ""
    while isinstance(passnum, str):
      passnum = input("How Many Passwords Do You Want To Generate? ")
      try:
        passnum = int(passnum)
      except:
        print("Please Enter A Number")
        passnum = str(passnum)
      else:
        passnum = int(passnum)

    passcount = 0
    thing1 = [40, 41]
    print("___________________")

    # Generate password using all the characters, in random order # + ....
    while passcount != passnum:
      number = chr(random.randint(48, 57))
      number2 = chr(random.randint(48, 57))
      number3 = chr(random.randint(48, 57))
      number4 = chr(random.randint(48, 57))
      number5 = chr(random.randint(48, 57))
      number6 = chr(random.randint(48, 57))
      lowercaseletter = chr(random.randint(97, 122))
      lowercaseletter2 = chr(random.randint(97, 122))
      lowercaseletter3 = chr(random.randint(97, 122))
      lowercaseletter4 = chr(random.randint(97, 122))
      uppercaseLetter1 = chr(random.randint(65, 90))
      uppercaseLetter2 = chr(random.randint(65, 90))
      uppercaseLetter3 = chr(random.randint(65, 90))
      uppercaseLetter4 = chr(random.randint(65, 90))
      uppercaseLetter5 = chr(random.randint(65, 90))
      password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + number + number2 + number3 + number4 + number5 + number6 + lowercaseletter + lowercaseletter2 + lowercaseletter3 + lowercaseletter4
      password = shuffle(password)
      passcount += 1
      print(password)
    print("___________________")

  if choice == "3":
    howanytogenerate = ""
    passwordsmade = 0
    while howanytogenerate != passwordsmade:
      howanytogenerate = (input)("How Many Passwords Would You Like To Generate: ")
      print("___________________")
      try:
        howanytogenerate = int(howanytogenerate)
        while passwordsmade != howanytogenerate:
          adjective = ["ok", "good", "amazing", "cool", "fast", "slow", "medium", "small", "large", "interested",
                       "maintained",
                       "weird", "lazy", "average", "upsidedown", "joyful", "bright", "sanitery", "clean", "educated",
                       "sourced", "common", "swift", "blue", "green", "red", "yellow"]
          noun = ["sloth", "jellyfish", "cow", "pig", "carpet", "table", "chair", "toaster", "bulb", "fridge",
                  "watermelon",
                  "seeds", "dirt", "bottle", "door", "sky", "star", "planet", "whale", "pillow", "case", "brush",
                  "plate",
                  "bowl", "spy", "cheese" ]
          adjective1 = random.choice(adjective)
          noun1 = random.choice(noun)
          readablenum = random.randint(100, 999)
          readablenum = str(readablenum)
          password = adjective1 + noun1 + readablenum
          print(password)
          passwordsmade += 1
        print("___________________")
      except:
        print("Please Choose A Valid Number")
  if choice == "4":
    quit = 1
quit()


