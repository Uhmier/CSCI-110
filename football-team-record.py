###files
##f = open(fake_file.dat, 'r')
##f.write()
##pies = ['apple', 'pumpkin', 'oatmeal']
##for current_pies in pies:
##    print current_pie + 'pie'
##
##    
sports_teams = ['eagles', '49ers', 'ravens', 'titans']
for names in sports_teams:
    print names
response = raw_input('would you like to add to this list').lower().strip()
while response != 'no':
    sports_teams.append(raw_input('what is the teams name you\'d like to add'))
    response = raw_input('Enter no if you would like to stop').lower().strip()
teams_records = {}
response = raw_input('would you like to give records to teams?').lower().strip()
while response != 'no':
    teams_records[raw_input("what is the team's name?")] = (raw_input('wins'),
                                                      raw_input('losses'))
    print teams_records
    response = raw_input('would you like to continue?')
team_names = teams_records.keys()
for name in team_names :
    i=0
    a = teams_records
    record = float ((a[name])[0]) / (float((a[name])[1]) + float((a[name])[0]) )
    i+=1
    print name + str(record)

