

# More information about this project can be found in a handout on the class
# website. Be sure to read it before you start programming.
import pokemon
import random

# Define a new variable called MOVES that contains a dictionary. As keys, use
# the move variables defined in the pokemon module. The values should be
# 3-tuples. The first value should be a string containing the move name. The
# second value should be the type of the move (use the type variables defined in
# the pokemon module). The third value should be which stat should be targeted
# by the move (HP, attack, defense, or speed... again, use the variables in the
# pokemon module).
MOVES = { pokemon.EMBER : (pokemon.EMBER, pokemon.FIRE, pokemon.HP),
          pokemon.GROWL : (pokemon.GROWL, pokemon.NORMAL, pokemon.ATTACK),
          pokemon.SCARY_FACE : (pokemon.SCARY_FACE, pokemon.NORMAL, pokemon.SPEED),
          pokemon.SCRATCH : (pokemon.SCRATCH, pokemon.NORMAL, pokemon.HP),
          pokemon.TACKLE : (pokemon.TACKLE, pokemon.NORMAL, pokemon.HP),
          pokemon.TAIL_WHIP: (pokemon.TAIL_WHIP, pokemon.NORMAL, pokemon.DEFENSE),
          pokemon.VINE_WHIP : (pokemon.VINE_WHIP, pokemon.GRASS, pokemon.HP),
          pokemon.WATER_GUN : (pokemon.WATER_GUN, pokemon.WATER, pokemon.HP) }



# Define a function called get_all_pokemon that takes one boolean parameter.
# Your function should use the get_new_pokemon function defined in the pokemon
# module to return a list of all possible Pokemon. Use the Pokemon species
# variables defined in the pokemon module as parameters. Additionally, if your
# function's parameter is True, the pokemon returned in the list should be
# wild.
def get_all_pokemon(x):
    charmander = pokemon.get_new_pokemon(pokemon.CHARMANDER
                                         , get_move_set(pokemon.CHARMANDER), x)
    squirtle = pokemon.get_new_pokemon(pokemon.SQUIRTLE
                                       , get_move_set(pokemon.SQUIRTLE), x)
    bulbasaur = pokemon.get_new_pokemon(pokemon.BULBASAUR
                                        , get_move_set(pokemon.BULBASAUR), x)
    all_pokemon = [charmander, squirtle, bulbasaur]    
    return all_pokemon
    


# Define a function called get_move_set that takes one parameter, the ID of a
# Pokemon as defined by the variables in the pokemon module, and returns a list
# of move keys as defined by the variables in the pokemon module. The handout
# describes which Pokemon can perform which moves.
def get_move_set(x):
    if x == pokemon.BULBASAUR :
        return [pokemon.SCARY_FACE, pokemon.TACKLE,
                pokemon.TAIL_WHIP, pokemon.VINE_WHIP]
    if x == pokemon.CHARMANDER:
        return [pokemon.EMBER, pokemon.GROWL,
                pokemon.SCRATCH, pokemon.TAIL_WHIP]
    if x == pokemon.SQUIRTLE :
        return [pokemon.GROWL, pokemon.SCARY_FACE,
                pokemon.TACKLE, pokemon.WATER_GUN]
    


# Define a function called get_npc_move that takes one Pokemon parameter, which
# is the computer's pokemon. Your function should pick a move at random from the
# Pokemon's move list and return its tuple.
def get_npc_move(x):
  a = x.get_moves()
  b = random.choice(a)
  return MOVES[b]

# Define a function called get_npc_pokemon that returns a random wild Pokemon.
def get_npc_pokemon():
    rand_poke = random.choice(get_all_pokemon(True))
    return rand_poke

# Define a function called get_user_choice that takes two parameters. The first
# parameter should be a list of string options to present to the user. The
# second should be a prompt that single string. Your function should output
# prompt and the choices in the following format and return an index when a user
# has selected a valid option.
# Example: get_user_choice(['Option1', 'Option2', 'Option3'], 'Select one.')
# should output:
# 
# Select one. 
#    0: Option1
#    1: Option2
#    2: Option3
# :: 
def get_user_choice(a,b):
    while True :
        print b
        c = 0
        for d in a :
            print '   ' + (str(c)).capitalize() + ': ' + d
            c += 1
        choice =  int(raw_input(':: ' ))
        if choice < len(a)  and choice >= 0:
            return choice


# Define a function called get_user_move that takes one Pokemon parameter and
# uses your get_user_choice function to allow the user to select one of the
# Pokemon's moves. Your function should return the selected move's tuple.
def get_user_move(x):
    choice = get_user_choice(x.get_moves(), 'What will ' + x.get_name() + ' do?')
    e = x.get_moves()
    f = e[choice]
    return MOVES[f]

# Define a function called get_user_pokemon that takes no parameters. Your
# function should use your get_all_pokemon function to allow the user to select
# a Pokemon. Your function should return the selected Pokemon object.
def get_user_pokemon():
    b = [ a.get_name() for a in get_all_pokemon(False) ]
    c = get_user_choice(b, 'Select a Pokemon.')
    d = get_all_pokemon(False)
    return d[c]

# Define a function called print_hp_meter that takes one Pokemon parameter and
# prints out its hit points (HP). The meter should be thirty characters long and
# adjust based on the percentage of the Pokemon's HP that remains. You can use
# the MAX_HP variable in the pokemon module. The HP meter should be output in
# the following format:
# [               xxxxxxxxxxxxxxx] (50/100)
def print_hp_meter(x):
    xit = int(30 * x.get_hp() / pokemon.MAX_HP)
    spaceit = 30 - xit
    state = (((x.get_name()).upper()) + ': [' +(' ' * spaceit)
             + ('x' * xit) + '] (' + str(x.get_hp()) + '/' + str(pokemon.MAX_HP) + ')')
    if x.is_wild() :
        print 'WILD ' + state
    else :
        print state


# Define a function called print_move_result that takes three parameters. The
# first parameter should be a boolean value indicating whether or not the move
# was successful. The second parameter should be a Pokemon object, the Pokemon
# on which the move was performed. The third parameter should be the 3-tuple
# that defines the move itself. If the move was unsuccessful, your function
# should print out: "But it failed!" Your function should print out an
# explanation of the result of running the move. If the move included a damage
# multiplier (according to the get_multiplier function defined in the pokemon
# module), then your function should print out "It's super effective!". Then it
# should print out: "[Wild ]POKEMON NAME's STAT fell!" where "Wild" appears if
# the Pokemon is wild, POKEMON NAME is the name given by the Pokemon object, and
# STAT is the name of the stat effected by the move.
def print_move_result(boo, poke, move):
    if not boo:
        print 'But it failed!'
    elif boo:
        if pokemon.get_multiplier(move[1], poke.get_type()) == 1.5 :
            print " It's super effective!"
        if poke.is_wild():
            print 'WILD ' + poke.get_name().upper() +"'s " + pokemon.get_stat_name(move[2]).upper() + ' fell!'
        else :
            print poke.get_name().upper() +"'s " + pokemon.get_stat_name(move[2]).upper()  + ' fell!'

            
# Define a function called play that runs a Pokemon battle. The user should
# select a Pokemon and so should the computer player. Then the user and and
# computer player should each select moves until one Pokemon faints. Your
# function should also output the appropriate messages according to the handout.
# Remember: you can use all of the functions and variables defined in the
# pokemon module!
def play():
   pp = get_user_pokemon()
   npp = get_npc_pokemon()
   print ' WILD ' + (npp.get_name()).upper() + ' appeared! Go! ' + (pp.get_name()).upper()
   while not pp.is_fainted() and not npp.is_fainted() :
       print_hp_meter(pp)
       print_hp_meter(npp)
       pp_move = get_user_move(pp)
       npp_move = get_npc_move(npp)
       if pp.is_faster_than(npp):
           print (pp.get_name()).upper() + ' used ' + pp_move[0].upper() + '!'
           print_move_result(pp.attack(npp, pp_move), npp, pp_move)
           print 'WILD' + (npp.get_name()).upper() + ' used ' + npp_move[0].upper() + '!'
           print_move_result(npp.attack(pp, npp_move), pp, npp_move)          
       else :
           print (pp.get_name()).upper() + ' used ' + pp_move[0].upper() + '!'
           print_move_result(pp.attack(pp, npp_move), npp, pp_move)
           print 'WILD ' + (npp.get_name()).upper() + ' used ' + npp_move[0].upper() + '!'
           print_move_result(npp.attack(npp, pp_move), pp, npp_move)
   if pp.is_fainted() :
        print pp.get_name().upper() + 'has fainted!'
   else :
        print 'WILD ' + npp.get_name().upper() + ' has fainted'
           

