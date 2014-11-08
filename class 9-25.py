#lists notes and testing
string = raw_input('Say what you want to be lowercase \n ::')
print string.lower()

list_of_numbers = [1,1,5,2,3,13,8,21]
print list_of_numbers
print list_of_numbers[5]
list_of_numbers.append('lol') # adds 'lol' to the end
print list_of_numbers
print list_of_numbers.pop() #remove and return last element
print list_of_numbers
print list_of_numbers.pop(0)
print list_of_numbers
index = 0
while index < len(list_of_numbers) : # prints all
    print list_of_numbers[index]
    index += 1
