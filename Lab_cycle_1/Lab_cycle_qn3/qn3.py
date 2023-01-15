#function to find gross salary
def gross_salary(bp,da,hra,ma):
  gross_salary = bp+da+hra+ma
  return gross_salary

#function to find deduction
def deduction(pt,pf,it):
  deduction = pt+pf+it
  return deduction

#function to find net salary
def net_salary(gs,d):
  net_salary = (gs - d)
  return net_salary

#function to print payment slip
def payment_slip(name,code,basic_pay):
  if basic_pay<10000:
    da = (5*basic_pay)/100
    hra = (2.5*basic_pay)/100
    ma = 500
    pt = 20
    pf = (8*basic_pay)/100
    it = 0
    Gross_Salary = gross_salary(basic_pay,da,hra,ma)
    Deduction = deduction(pt,pf,it)
    Net_Salary = net_salary(Gross_Salary,Deduction)

  elif basic_pay<30000:
    da = (7.5*basic_pay)/100
    hra = (5*basic_pay)/100
    ma = 2500
    pt = 60
    pf = (8*basic_pay)/100
    it = 0
    Gross_Salary = gross_salary(basic_pay,da,hra,ma)
    Deduction = deduction(pt,pf,it)
    Net_Salary = net_salary(Gross_Salary,Deduction)

  elif basic_pay<50000:
    da = (11*basic_pay)/100
    hra = (7.5*basic_pay)/100
    ma = 5000
    pt = 60
    pf = (11*basic_pay)/100
    it = (11*basic_pay)/100
    Gross_Salary = gross_salary(basic_pay,da,hra,ma)
    Deduction = deduction(pt,pf,it)
    Net_Salary = net_salary(Gross_Salary,Deduction)

  else:
    da = (25*basic_pay)/100
    hra = (7.5*basic_pay)/100
    ma = 5000
    pt = 60
    pf = (12*basic_pay)/100
    it = (20*basic_pay)/100
    Gross_Salary = gross_salary(basic_pay,da,hra,ma)
    Deduction = deduction(pt,pf,it)
    Net_Salary = net_salary(Gross_Salary,Deduction)

  print("\n--- PAYMENT SLIP ---")
  print("Employee name : ",name)
  print("Employee code : ",code)
  print("Employee Basic pay : ",basic_pay)
  print("Employee Gross Salary : ",Gross_Salary)
  print("Employee deduction : ",Deduction)
  print("Employee Net Salary : ",Net_Salary)
  

name = str(input("enter your name : "))
code = int(input("enter your code : "))
basic_pay = int(input("please enter your basic pay : "))

payment_slip(name,code,basic_pay)