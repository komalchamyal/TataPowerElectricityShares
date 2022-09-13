total_amt= float(input("Total bill amount: "))
units= float(input("Total units: "))
unit_total= float(input("Total units amount: "))
people=int(input("How many people: "))
div= list(map(float, input("Enter unit amounts (space seperated): ").strip().split()))

def total_tax(total_amt, unit_total):
  diff= total_amt-unit_total
  tax= diff/unit_total
  tax*=100
  print(f"Total Tax on your bill = {round(tax)}")
  return tax

def input_units():
  individual_units=dict()
  tot=0
  print("Only add values in increasing order. Any other order will give wrong output!")
  for i in range(1,people+1):
    unit=float(input(f"Units for person {i}: "))
    individual_units[i]=unit
    tot+=unit
  if tot<units:
    print("All your units are less than total units in bill.\nDividing rest of the units amongst the people")
    diff= units-tot
    diff=diff/people
    for i in range(1,people+1):
      individual_units[i]+=diff
  if tot>units:
    print("Units provided do not add upto total units of", units)
    individual_units=input_units()
  return individual_units

def input_breakdown():
  usage=dict()
  tot=0
  for i in div:
    unit=float(input(f"Rs.{i} units= "))
    usage[i]=unit
    tot+=unit
  if tot!=units:
    print("Units provided do not add upto total units of", units)
    usage= input_breakdown()
  return usage

def calc_shares(people):
  usage=input_breakdown()
  people_units=input_units()
  n=people
  amount={}
  flag=[]
  for i in range(1, people+1):
    amount[i]=0.0
  for i in div:
    if n!=0:
      for j in range(1,people+1):
        if j in flag:
          continue
        pp=usage[i]/n
        if pp>people_units[j]:
          pp= people_units[j]
          amount[j]+=pp*i
          usage[i]-=pp
          flag.append(j)
          n-=1    
        else:
          people_units[j]-=pp
          amount[j]+=pp*i
  return amount

tax=total_tax(total_amt, unit_total)
individual_shares=calc_shares(people)

for i in range(1,people+1):
  amt=individual_shares[i]+ individual_shares[i]*tax/100
  print(f"Amount for Person {i} = {round(amt)}")