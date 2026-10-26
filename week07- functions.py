#AI DISCLOSUR: I used AI to help me with debugging
#exercise 1 calculate_tax function 
def calculate_tax(price,rate): #defines a function
    return price*rate
#calling the function 
tax1 = calculate_tax(100, 0.07)
tax2= calculate_tax(250,0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

print(f"tax for $350 at 5%: ${calculate_tax(350,0.05):.2f}") #the function is in the f string
#however if we do it this way then it isnt saved and we cant use it again 

#exercise 2 setting up discount function
gold = 0.15
silver = 0.10
bronze = 0.05
def apply_discount(price,tier):
    if tier==gold:
        return price*0.85
    elif tier==silver:
        return price*0.90
    elif tier==bronze:
        return price*0.95
    else: 
        return price

    #cslling the function
    orginal_price=200
    for tier in["gold","silver","bronze","none"]:
        print(f"{tier}: ${apply_discount(original_price,tier):.2f}")
#this sets up aoutomation the conditionals and the whole thing is in a loop in the f string 

#exercise 3 composing
def final_price(price,tax_rate,discount_tier):
    discounted_price=apply_discount(price,discount_tier)
    tax=calculate_tax(discounted_price,tax_rate)
    return discounted_price+tax

#calling the function
print(f"final_price (200,""0.07,'gold'):${final_price(200,0.07,'gold'):.2f}")
#prints out that the function is = to a certain dollar amount 

#exercise 4 
orders=[(200, "gold"),(150, "silver"),(80, "bronze"),(500,"none")]

         
for price,tier in orders:
    total=final_price(price,0.07,tier)
    print(f'Price: ${price} Tier: {tier} Final Price: ${total:.2f}')

#exercise 6 
x=100 #global x 
def double_it():
    x= 999 #local x
    return x*2

print(x)
print(double_it())
print(x)

#exercise 5 fix broken file 
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    #total = sale #this is a silent bug because instead of printing the real value it shows 
    # the total again, it should be +=
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales: #add : to make this statement into a function
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #this < is correct because it asks for an item that exists.our list 
    #has 5 items but in this loop once it reaches 5 it still looks for more. 
    # remember python lists start at 0 so we change <= to just < 
    print(sales[i])
    i += 1

#exercise 6 
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # prints 100 which is the global x
print(double_it()) # prints 1998 which is the local x doubled
print(x)           # no it hasent because the global x and local x 
#are not the same thing. unless we use the global keyword to change the global x then it will stay the same.

#self assesment 
#1 the first bug i was able to spot was on my own using the traceback and it
#  was the fact that the function didnt have a : at the end. i think so far that 
# my debugging skills are okay since i was able to find the clear bugs. 
# but i had trouble finxing the one that didnt give an error message, and had to use ai for help 
#2 apply_discount(price,tier) is a function and it applys a given dicount to a given price and tier. 
# it basically tells us what discount to apply based on these inputs
#3 yes i used AI to help me with debugging the file beacuse at first i didnt understand the indexerror, 
# and then i had trouble finding the last bug. so i ussed the AI to help me, 
# and i think that it helped my understanding. not shortcutted it
