#shot  = [player , distace from target]
#I understand github!



import random

def dist_to_target(shot):
    return(shot[1])

def still_in(shot,players_list,shots_list):
    if shot[1] < min(shot_list,key = dist_to_target)[1]:
        pass
    else:
        players_list.remove(shot[0])


A = 0
B = 0
C = 0
D = 0
for i in range(10000000000):
    players = ["A","B","C","D"]
    shot_list = [["A",random.uniform(0,1)]]
    turn = 0
    while len(players) != 1:
        shot = [players[turn%len(players)],random.uniform(0,1)]
        still_in(shot,players,shot_list)
        turn+=1
    print(players)
    if players[0] == "A":
        A +=1
    elif players[0] == "B":
        B +=1
    elif players[0] == "C":
        C +=1
    elif players[0] == "D":
        D +=1
    print(A,B,C,D)
    print(D/(A+B+C+D))
