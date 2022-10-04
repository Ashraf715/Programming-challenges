import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0]
        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0]

        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
            dictionary[home][3] += 1
            dictionary[away][3] += 1

        if winner == "H":
            dictionary[home][0] += 3
            dictionary[away][0] = dictionary[away][0]
            dictionary[home][2] += 1
            dictionary[away][4] += 1

        if winner == "A":
            dictionary[away][0] += 3
            dictionary[home][0] = dictionary[home][0]
            dictionary[away][2] += 1
            dictionary[home][4] += 1

        dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)
        dictionary[away][1] = dictionary[away][1] + int(awaygoals) - int(homegoals)

        return dictionary

    file_contents = read_csv(csv_file)
    d_dictionary ={x: y for x, y in sorted(process_results(file_contents).items() ,key = lambda y: y[1][1] and y[1], reverse = True)}

    def premierleague_teams(d_dictionary):
        teams = list(d_dictionary.keys())
        return teams[x]

    def totalpoints(d_dictionary):
        teams = list(d_dictionary.keys())
        points = teams[x]
        return d_dictionary[points][0]

    def goal_differences(d_dictionary):
        teams = list(d_dictionary.keys())
        points = teams[x]
        return d_dictionary[points][1]

    def wins(d_dictionary):
        teams = list(d_dictionary.keys())
        points = teams[x]
        return d_dictionary[points][2]

    def draws(d_dictionary):
        teams = list(d_dictionary.keys())
        points = teams[x]
        return d_dictionary[points][3]

    def losses(d_dictionary):
        teams = list(d_dictionary.keys())
        points = teams[x]
        return d_dictionary[points][4]

    if __name__** "__main__":
        teams = list(d_dictionary.keys())
        print(f"{Team |'}{'Points |'}{'GoalDifferences |'}{'Wins |'}{'Draws |'}{'Losses |'}")
        for x in range (0, len(teams)):
            print(f"{premierleague_teams(d_dictionary)}:({totpoints(d_dictionary)})({goal_differences(d_dictionary)})({wins(d_dictionary)}")
        
