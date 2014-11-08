# All even values are x's turn
# All odd values are o's turn
# Return values only if turn number is less than 9
# Only spaces between 0-8

#Def current player
turn_num = 0
def current_player(turn_num) :
    if (turn_num <= 8  and turn_num >= 0):
        if turn_num % 2 == 0 :
            marker = 'x'
            return marker
        elif turn_num % 2 == 1 :
            marker = 'o'
            return marker
    else :
        print ' Invalid turn number'

#Board Full

def board_full() : 
    space_num = 0
    while (space_num < 9) and (is_filled(space_num)) :
        space_num += 1
    if space_num == 9 :
        return True
    elif space_num < 9 :
        return False

#Print Board
    
space0 = '0'
space1 = '1'
space2 = '2'
space3 = '3'
space4 = '4'
space5 = '5'
space6 = '6'
space7 = '7'
space8 = '8'

def print_board():
  print space0, space1, space2
  print space3, space4, space5
  print space6, space7, space8

# Has winner
def has_winner():

  if (space0 == space1 and space1 == space2):
    return True
  elif (space3 == space4 and space4 == space5):
    return True
  elif (space6 == space7 and space7 == space8):
    return True
  elif (space0 == space3 and space3 == space6):
    return True
  elif (space1 == space4 and space4 == space7):
    return True
  elif (space2 == space5 and space5 == space8):
    return True
  elif (space0 == space4 and space4 == space8):
    return True
  elif (space2 == space4 and space4 == space6):
    return True
  else:
    return False


# is filled

#space = raw_input('x or o')
#space1 = raw_input('x or o')
#space2 = raw_input('x or o')
#space3 = raw_input('x or o')
#space4 = raw_input('x or o')
#space5 = raw_input('x or o')
#space6 = raw_input('x or o')
#sapce7 = raw_input('x or o')
#space8 = raw_input('x or o')


def is_filled(space_num):
  if space_num == 0:
    if space0 == 'x' or space0 == 'o':
      return True
    else:
      return False
  if space_num == 1:
    if space1 == 'x' or space1 == 'o':
      return True
    else:
      return False
  if space_num == 2:
   if space2 == 'x' or space2 == 'o':
    return True
   else:
    return False
  if space_num == 3:
   if space3 == 'x' or space3 == 'o':
     return True
   else:
     return False
  if space_num == 4:
   if space4 == 'x' or space4 == 'o':
     return True
   else:
     return False
  if space_num == 5:
   if space5 == 'x' or space5 == 'o':
      return True
   else:
      return False
  if space_num == 6:
   if space6 == 'x' or space6 == 'o':
      return True
   else:
      return False
  if space_num == 7:
   if space7 == 'x' or space7 == 'o':
      return True
   else:
      return False
  if space_num == 8:
   if space8 == 'x' or space8 == 'o':
      return True
   else:
      return False

# Place move
    
def place_move(move, marker):
  if move == 0:
    global space0
    space0 = marker
  elif move == 1:
    global space1
    space1 = marker 
  elif move == 2:
    global space2
    space2 = marker 
  elif move == 3:
    global space3
    space3 = marker 
  elif move == 4:
    global space4
    space4 = marker 
  elif move == 5:
    global space5
    space5 = marker 
  elif move == 6:
    global space6
    space6 = marker 
  elif move == 7:
    global space7
    space7 = marker 
  else:
    global space8
    space8 = marker

# get valid move

def get_valid_move():
    valids = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    move = int(raw_input('Please place your move \n >>>'))
    while move not in valids:
        print "your move is not valid.... Please try again"
        move = int(raw_input("Please place your move \n >>>>"))
    return move
  

def play() :
    turn_num = 0
    while (has_winner() == False) and (board_full() == False) :
        print_board()
        place_move(get_valid_move(), current_player(turn_num))
        turn_num +=1
    if board_full == True :
        print ' No winner, game tie'

play()
