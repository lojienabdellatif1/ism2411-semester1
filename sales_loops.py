#exercise 1 sum a list
sales=[120,80,250,175,90,410,60,215]
total=0
for sale in sales:
    total+=sale
print(f"Total:${total}")

#exercise 2 total,count, and average
total=0
count=0
for sale in sales:
    total+=sale
    count+=1
average= total/count
print(f"Total:${total}")
print(f"Count:{count}")
print(f"Average:${average:.2f}")

#exercise 3 finding max value 
current_max=0
for sale in sales:
    if sale>current_max:
        current_max=sale
print(f"Max sale:${current_max}")

#eercise 4 filtering data to count only qualifying sales
count_over_100=0
total_over_100=0
for sale in sales:
    if sale>100:
        count_over_100+=1
        total_over_100+=sale

print(f"Sales over $100:{count_over_100}")
print(f"Total of sales over $100:${total_over_100}")

#exercise 5 skip or stop 
for sale in sales:
    if sale >400:
        print(f"Alert: outlier found - ${sale}.Stopping.")
        break
    if sale <= 100: 
        continue
    print(f"${sale}")

    #exercise 6 managing the index explicitly
    total=0
    i=0
    while i<len(sales):
        total+=sales[i]
        i+=1
print(f"Total (while loop): ${total}")

#exercise 7 select the discount tier
for sale in sales:
    if sale >= 200:
        discount=0.10
    elif sale >= 100:
        discount=0.05
    else:
        discount=0
    final= sale*(1-discount)
    print(f"Sale: ${sale}, Discount: {discount*100:.0f}%, Final: ${final:.2f}")

    #self reflection questions
    #1: the accumulator pattern is a pattern used to 
    #code loops effectivly, first you initialize 
    # which is like setting up an empty bucket to 
    # hold all the values, next you add the data 
    # that the loop will work on, and then you
    #  write the loop, after ur done the 
    # output will be a clean count of whatever 
    # you were asking the program to count

    #2 the while loop version is much shorter than
    #  the for loop, however it could mess up 
    # the code if we were programming something 
    # where the conditions change. 
    # so the for loop is more reliable but 
    # could take up more lines, and the while l
    # opp is shorter, but not always the cleanest 
    # 
    #3: in the summer i mainly watched
    #  a bunch of youtube videos, and if i were to 
    # work in social media marketing or analytics 
    # I could use these loops and skills i learned
    #  to track subscriber engagemnt and identify high performing contentvtypes.
    #  for example, my data set would include video titles and 
    # the amount of views and new subs that video gave me.then i would use 2 accumulators 
    # dlike total_views and Total_subs_gained. and then print the values for each 
