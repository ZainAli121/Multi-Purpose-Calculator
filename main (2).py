print("Enter 1 for BMI Calculater")
print("Enter 2 for Simple Math Calculations")
print("Enter 3 for Temprature Convertions")
print("Enter 4 for Unit Convertions\n")
res=input("Register your response here: ")

#---------------------BMI Calculater-------------------------------------
if res=='1':
  w=float(input("\nEnter your weight in kilograms: "))
  h=float(input("\nEnter your height in metres: "))
  bmi=w/h**h
  if bmi<18.5:
    print("\nUnderweight")
  elif bmi>=18.5 and bmi<=24.9:
    print("\nHealthy weight")
  elif bmi>=25 and bmi<=29.9:
    print("\nOverweight")
  else:
    print("\nObesity")

#---------------------------Scientific Calculater-------------------------
elif res=='2':
  num1=float(input("\nEnter First Number: "))
  num2=float(input("\nEnter Second Number: "))
  oper=input("\nEnter one of the fllowing operators\n '+','-','*','/','%','**': ")
  if oper=='+':
    sum=num1+num2
    print("\nThe Sum of two given Numbers is: ",sum)
  elif oper=='-':
    diff=num1-num2
    print("\nThe Difference of two given Numbers is: ",diff)
  elif oper=='*':
    pro=num1*num2
    print("\nThe Product of two given Numbers is: ",pro)
  elif oper=='/':
    div=num1/num2
    print("\nThe Division of two given Numbers is: ",div)
  elif oper=='%':
    rem=num1%num2
    print("\nThe Remainder of two given Numbers is: ",rem)
  elif oper=='**':
    sq=num1**num2
    print("\nThe Square of two given Numbers is: ",sq)
  else:
    print("\nInvalid Operater\nKindly check our available list of operaters again")
    

#----------------------------Temperature Calculater-------------------------
elif res=='3':
  print("\nEnter 1 for Celsius to Fahrenheit Conversion")
  print("\nEnter 2 for Fahrenheit to Celsius Conversion")
  res1=input("\nRegister your response here: ")
  if res1=='1':
    cel=float(input("\nEnter the temperature in Celsius degree: "))
    fah=((cel * 9/5) + 32)
    print("\nThe temperature in Fahrenheit is: ",fah)
  elif res1=='2':
    fah_temp=float(input("\nEnter the temperature in Fahrenheit: "))
    cel_temp=(fah_temp -32) * 5/9
    print("\nThe temperature in Celsius is: ",cel_temp)
  else:
    print("\nInvalid Key Entered\nPlease try again!")
    

#----------------------Unit Converter------------------------------
elif res=='4':
  print("\n\nEnter 1 for Kilometres to Metres Convertion")
  print("\nEnter 2 for Metres to Centimetres Convertion")
  print("\nEnter 3 for Foot to Inches Convertion")
  res2=input("\n\nRegister your response here: ")
  if res2=='1':
    km=float(input("\nEnter the Length in Kilometres: "))
    metres=km*1000
    print("\nThe Length in Metres is: ",metres)
  elif res2=='2':
    met=float(input("\nEnter the Length in Metres: "))
    cent=met*100
    print("\nThe Length in Centimetres is: ",cent)
  elif res2=='3':
    foot=float(input("\nEnter the Length in Foots: "))
    inches=foot*12
    print("\nThe Length in Inches is: ",inches)
  else:
    print("\nInvalid Key\nPlease check your response Again!")
else:
  print("\nInvalid Key\nPlease Check and Try Again Later!")