conversion = float(input("please enter your number of poeple who visited your website and decided to purchase your service or product?: "))
interactions = float(input("please enter the number of people who visited your webste: "))
revenue = float(input("please enter your weekly revenue revenue: "))
cost = float(input("What is your total weekly cost?: "))
service = float(input(" How much do you charge for your service or product?: "))
adbudget = float(input("What is your weekly ad budget: "))
def conversion_calc():
  global equation
  equation = conversion/interactions*100
  print("your conversion rate is: " + str(equation) + "%" )


conversion_calc()

def profit():
  money = revenue - cost
  print("Your profit is : " + str(money))

profit()



def desired_conversion():
  people = cost/service
  totalimp = adbudget*1000/4.99
  cpm = 500/totalimp/1000
  ans = conversion/interactions
  final = ans * totalimp
  print("You will get "+ str(totalimp) +(" Impressions and ") + " You will convert " + str(final) + " Out of those impressions")
  if final <= people:
    print("Your budget is not enough, maybe spend more or increase your conversion rate.")
  elif final == people:
    print("Your budget is just enough")
  else:
    print("Your making money!!!")



desired_conversion()



def profit_margin():
 c2 = revenue-cost
 c3= c2/revenue
 print("Your profit margin is: " + str(c3) + "%")
 
profit_margin()








