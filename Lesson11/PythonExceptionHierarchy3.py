try:
   age = eval( input("Please enter your age: ") )
   ten_years = age + 10
   print ("In 10 years, you'll be", ten_years)
except Exception:
   print ("Something unexpected has happened")
except NameError:
   print ("A NameError has occurred")


print ("Have a nice day. Goodbye.")
