def climbingLeaderboard(ranked, player):
    player_pos = []
    ranked = [*set(ranked)]
    for i in player :  
        ranked.append(i) 
        ranked.sort(reverse =True)
        x = ranked.index(i) + 1
        player_pos.append(x)
        ranked.remove(i)
    return player_pos

if __name__ == '__main__':

    ranked = list(map(int, input().rstrip().split()))

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)