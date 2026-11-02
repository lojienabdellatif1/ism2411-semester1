#exercise 1 building the list 
print("---exercise 1 building the list ---")

inventory=["pen","notebook"]
inventory.append("tape")
inventory.append("stapler")
inventory.append("marker")
print(inventory)
print(len(inventory))  #for len always use (len(varibale))

#exercise 2 index practice 
print("---exercise 2 index practice ---")

print(inventory[0])  #prints the first item in the list
print(inventory[-1]) #prints the last item in the list
middle= len(inventory)//2 #this is the middle of the list
print(inventory[middle]) #prints the middle item in the list

#exercise 3 slicing practice
print("---exercise 3 slicing practice ---")
print(inventory[0:3]) #prints the first 3 items in the list
print(inventory[1:4]) 
print(inventory[-2:]) #last 2 items
print(inventory[::2]) #every other item or every 2 items 

#exercise 4 modify 
print("---exercise 4 modify ---")

inventory.append("envelope")
inventory.append("tape")
inventory.remove("tape")
print(inventory)

inventory.sort() #sorts the list in alphabetical order
print(inventory)

#exercise 5 tuple comparison
print("---exercise 5 tuple comparison ---")

coords=(40.7128, -74.0060) #nyc coordinates 

try:
    coords[0]=99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protetect coordinates from being changed by accident")

#exercise 6 average of a list of sales 
print("---exercise 6 avg of a list of sales---")

sales =[100,250,75,480,200]
total=sum(sales)
count=len(sales)
average= total/count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"average sales: {average}")

#how to find max and min w out functions 
best= sales [0]
worst=sales [0]
for amount in sales:
    if amount> best:
        best=amount
    if amount< worst:
        worst=amount 

print(f"best sale"{best})

#exercise 7: accumulator pattern 
print("---exercise 7: accumulator pattern---")

prices=[9.99,14.99,4.99,24.99,1.99]

discounted= []
for price in prices 
    discounted.append(round(price*0.9,2)) # applys 10% disocunt
print(prices)
print(discounted)

#exercise 8 filter above threshold
print("---exercise 8: filter above threshold")

sales=[340,127,589,204,467,88,731,315,61,490]
high_sales= []

for amount in sales: 
    if amount> 300:
        high_sales.append (amount)

print(high_sales)
print(f"count:{len(high_sales)}")
print(f"average: {amount}")

#Reflections 
#1: I did not know that python lists could be standardized so that important info does not get changed. i found that surprising
#2: I think a business scenario would be running an online business where I sell clothing. it would be must easier to run things through python lists like discounts or shipping prices, as well as edit things as they get updated 