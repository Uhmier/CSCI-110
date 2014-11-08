### read a file, create a list of strings, print pheon number to console,
### name ; email ; number
### name ; email ; number
### output:
import myfunction

def get_numbers_from_file(tfile) :
    a = open(tfile, 'r')
    for user in a.readlines() :
        b = user.split(';')
        number = b[2].strip('\n')
        if myfunction.is_number(number) :
            print number
        
    

get_numbers_from_file('testtfile.txt')
