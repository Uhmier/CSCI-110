# Define four variables called BLUE, GREEN, RED, and YELLOW that contain string
# values you can use to test user input.
# 10 Points
BLUE = 'blue'
GREEN = 'green'
RED = 'red'
YELLOW = 'yellow'


# Define a function called get_fortune that takes one parameter named
# fortune_num. The parameter should be an integer between 1 and 8, inclusively.
# For each valid value, the function should return a different fortune in a
# string. If the any value other the parameter is anything other than an integer
# between 1 and 8, the function should return the following string:
# 'Invalid fortune number.'
# 30 Points
def get_fortune(fortune_num) :
    if fortune_num == 1 :
        return 'The answer to your question is yes.'
    elif fortune_num == 2 :
        return 'This could be true.'
    elif fortune_num == 3 :
        return 'Probably not.'
    elif fortune_num == 4 :
        return 'Definitely a no.'
    elif fortune_num == 5 :
        return "Whirlybird doesn't know."
    elif fortune_num == 6 :
        return 'Ask again later.'
    elif fortune_num == 7 :
        return 'Chuck Norris knows this.'
    elif fortune_num == 8 :
        return 'Pray about it.'
    else :
        return 'Invalid fortune number.'


# Define a function called get_number_selection that takes one parameter named
# smaller_numbers. The parameter will be a boolean value. The function should
# prompt the user to enter an integer and return their selection as an integer.
# If smaller_numbers is True, the user should be prompted to input a number
# between 1 and 4, inclusively. If smaller_numbers is False, the user should be
# prompted to input a number between 5 and 8, inclusively. No other input values
# should ever be allowed and only valid values should be returned.
# 20 Points
def get_number_selection(smaller_numbers) :
    if smaller_numbers == True :
        number_selection = int(raw_input('Select a number between 1 and 4 \n :: '))
        while number_selection < 1 or number_selection > 4 :
           number_selection = int(raw_input('Select a number between 1 and 4 \n :: '))
        return number_selection
    if smaller_numbers == False :
        number_selection = int(raw_input('Select a number between 5 and 8 \n :: '))
        while number_selection < 5 or number_selection > 8 :
            number_selection = int(raw_input('Select a number between 5 and 8 \n :: '))
        return number_selection
    


# Define a function called get_color_selection that takes no parameters. The
# function should prompt the user to enter one of the colors defined at the
# beginning of the file. The user's input should not be case sensitive. Only the
# four colors defined at the beginning of the program should be considered valid
# input and only valid values should be returned.
# 30 Points
def get_color_selection() :
    valid_colors = ['green', 'yellow', 'red', 'blue']
    color_selection = (raw_input(
        ' Please select a color, RED, GREEN, BLUE, or YELLOW?')).lower()
    while color_selection not in valid_colors :
        color_selection = (raw_input(
        ' Please select a color, RED, GREEN, BLUE, or YELLOW?')).lower()
    return color_selection.lower()
        
    


# Define a function called play that takes no parameters. The function should
# use the other functions you have defined to handle the overall logic of the
# whirlybird. First, the user should be prompted to enter a question for the
# whirlybird. The user should be prompted to choose a color. If there are an
# even number of letters in that color, the user should be prompted to select a
# number on [1, 4]. If there are an odd number of letters in their color, the
# user should be prompted to select a number on [5, 8]. If the number they
# select is even, they should be presented with the same numbers again; if the
# number they select is odd, they should be presented with the other set of
# numbers. The second number the user selects should determine the fortune they
# recieve. Finally, the user's question and their fortune should be printed out.
# 30 Points
def play():
    usr_ques = raw_input('What would you like to ask whirlybird? \n :: ')
    color_selection = get_color_selection()
    smaller_numbers = (len(color_selection) % 2 == 0)
    first_choice = get_number_selection(smaller_numbers)
    if first_choice % 2 == 0 :
        fortune_num = get_number_selection(smaller_numbers)
    elif first_choice % 2 == 1 :
        smaller_numbers = (len(color_selection) % 2 == 1 )
        fortune_num = get_number_selection(smaller_numbers)
    print usr_ques
    print get_fortune(fortune_num)
    



