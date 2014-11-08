#Tennesse Tax calculator
#Request amount of items from user
#set up while loop to accomodate this amount
#Use variable named total in while loop to keep a running total of items
#use variable named subtotal to keep running subtotal
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def convert_to_currency(s) :
    currency = (int(s * 100)) / 100.00
    return currency
    

TN_TAX = 1.09
counter = 1
total = 0
subtotal = 0

num_items= raw_input('How many items do you plan to check out?')
while not is_number(num_items) :
    num_items= raw_input('How many items do you plan to check out?')
if is_number(num_items) :
    num_items = float(num_items)
while counter <= num_items :
    item_price = raw_input('What is the price of this item?')
    while not is_number(item_price):
        item_price = raw_input('ERROR INPUT \n What is the price of this item?')
    if is_number(item_price) :
        item_price = float(item_price)
    counter += 1
    subtotal = convert_to_currency(subtotal + item_price) 
    total = convert_to_currency(total + (item_price * TN_TAX))
    print 'Your current subtotal is \n :: ' + '$' + str(subtotal)
    print 'Your  current total is \n :: ' + '$' + str(total)
    if counter < num_items :
        print ' \n Next item please.'
print 'Thanks you for using my tax calculator'
    




#FUTURE WISHLIST
#Allow user to select a state to reflect tax rates
#Different tax rates for different classificatiosn of items
