##list_n = []
##int_a = int(raw_input('?'))
##int_b = int(raw_input('?'))
##int_c = int(raw_input('?'))
##if int_a < int_b:
##   while int_a < int_b :
##      if int_a % 2 == 0 :
##          int_a += 1
##      list_n.append(int_a)
##      int_a += 2
##elif int_a > int_b :
##    while int_b < int_a :
##        if int_b % 2 == 0 :
##            int_b += 1
##        list_n.append(int_b)
##        int_b += 2
##if (((int_a > int_c and int_b < int_c) or (int_a < int_c and int_b > int_c)) and
##    int_c % 2 == 1 ):
##    print "your third number is between first and second"
##else :
##    print 'Your numeb ris not inbetween'
##
##print list_n
gpa_by_name = {}
num_stu= int(raw_input())
counter = 1
while counter <= num_stu :
    student_name = raw_input('What is students name?').capitalize()
    student_gpa = raw_input('What is the students gpa?')
    gpa_by_name[student_name] = student_gpa
    counter += 1
if (raw_input('Would you like to retreive a gpa? yesor no?') == 'yes') :
    student_name = raw_input('What is students name?').capitalize()
    print gpa_by_name[student_name]
    while (raw_input('would you liek to stop? type stop') =! 'stop') :
        
    



         
         

     
