# Test if string is a float
#return true if valid
#use simple iff branch to return true or false
def is_valid_gpa(g):
    try:
        float(g)
    except ValueError:
        return False
    if float(g) <= 4.0 and float(g) >= 0.0 :
        return True
    else:
        return False

def get_new_student_info():
    student_name = raw_input()
    student_email = raw_input()
    gpa = raw_input()
    if is_valid_gpa(gpa):
        gpa = float(gpa)
    else:
        while not is_valid_gpa(gpa):
            gpa = raw_input(gpa)
        gpa = float(gpa)
    student_info = (student_name, student_email, gpa)
    return student_info

def load_student_dictionary() :
    if not file_exists(student_file_path):
        return {}
    else :
        f = open(student_file_path, 'r')
        f.split(\n)
        l_of_elements = []
        for element in f :
            element.split(,)
            l_of_elements.append(element)
        counter = 0
        stud_rec = {}
        while counter <= len(l_of_elements) :
            if counter % 3 == 0 :
                stud_rec[l_of_elements[counter]] = (
                    (l_of_elements[counter + 1], l_of_elements[counter + 1]))
            counter += 1
        f.close()
        return student_rec
            
            
        
