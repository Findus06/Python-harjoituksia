import random


Noppa = []
while len(Noppa) < 6:
    num = random.randint(1,7)
    Noppa.append(num)
    



score = []
for i in range(len(Noppa)):
    score.append(0)
    for k in range(len(Noppa)):
        if Noppa[i] == Noppa[k]:
            score[i] += 1
            

suurin = 0
for i in range(len(score)):
    if score[i] > suurin:
        suurin = score[i]
print(suurin)

    