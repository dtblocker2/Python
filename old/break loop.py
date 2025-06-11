#stop a loop if a certain condition is met
i = 1
while i <= 100:
    print(i)
    if i == 3:
        break
    i += 1

games = ["minecraft", "pubg", "red dead redemption", "gta 5", "lokicraft", "free fire", "call of duty", "clash of clans"]

kaku_beta = input("search a game")
i = 0
while i <= len(games):
    x = games[i]
    if x == kaku_beta:
        print("yes it is a game")
    else:
        print("finding....")
    if x == kaku_beta:
        break
    i += 1