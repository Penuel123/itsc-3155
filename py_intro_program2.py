# Start Code Here
items = int(input("Number of items: ")) #
items_and_price = []

#in the loop below, the number of items a user wants to enter determines how many item-price pairs that a user will be
#allowed to enter, as well as how many elements the items_and_price list will hold
for i in range(items): 
    items_and_price.append(input("Input item and price: "))

#this function below compares the prices of each item-and-price pair and then returns a list that is sorted by the price
def sort_by_price(list):
    for a in range(0, len(list) - 1):
        for b in range(0, len(list) - 1 - a):
            #the price variables below are assigned to the 2nd elements of item-price strings that were split. 
            #for example, the item-price string "apple 5" will be split into ["apple", "5"]. 
            #the price variables will hold the integer type-cast value of the 2nd element in ["apple", "5"], which is 5.
            price1 = int(list[b].split()[1]) 
            price2 = int(list[b + 1].split()[1])
            #the if statement below shows how the sort algorithm swaps the each item-price pair based on a 
            #greater-than comparison that is ONLY performed on the prices of the pairs. The pairs will be in ascending order
            #once the inner and outer loops are finished running
            if price1 > price2:
                temp = list[b]
                list[b] = list[b + 1]
                list[b + 1] = temp
    return list


new_items_and_price = sort_by_price(items_and_price)#this new_items_and_price list will hold the sorted item-price pairs
#this for-loop prints each element of item and price on a new line
for i in range(len(items_and_price)):
    print(new_items_and_price[i])
