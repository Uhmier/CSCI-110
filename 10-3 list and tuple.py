#list and tuple stuff 10-3

#list functions

one = [0,2,4,5]
two = one.pop(1)
print two
three = one.remove(5)
print three
three = one.remove(4)
four = one.pop()
print four
print one

# tuples- cannot add, doesnt use string functions

student_info = ('Amier', 'Freshman', 3.35)
onetuple = ('onetuple',)
print student_info

#dictionaries
dictionary = {}
top_movie_by_year = { 2013: 'Frozen', 2012 : 'The Avengers' }
#value_by_key
#add
top_movie_by_year [2011] = 'Harry Potter'
# value_by_key[key] = 'value'
#delete dictionary values with del
del top_movie_by_year[2011]


#immutable - not able to change



