print("The price of the house is $1M.")
condition = False
good_credit = input("Does the buyer has good credit? ")

while condition == False:
  
  good_credit = good_credit.upper()
  if good_credit == "YES":
   good_credit = True
   condition = True
  elif good_credit == "NO":
    good_credit = False
    condition = True
   
  if good_credit == True:
    print("The buyer need to pay down 10%")
  elif good_credit == False:
      print("The buyer need to pay down 20%")
  else:
     print("The answer must be 'yes' ou 'no'.")
     good_credit =input("Please, try again. ")
    