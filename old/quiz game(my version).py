choices = []
answers = ["C", "D", "B", "D"]
def q(a):
    print(Ques[a-1])
    print(options[a-1])
#-------------------------------------------------

Ques = ["Q.1 Name scientist who combined electricity with magnetism?","Q.2 What is a mole?", "Q.3 What is phylum python?","Q.4 Which is the most famous Austrian Painter?"]
options = ["A. Micheal Faraday \nB. Albert Einstein \nC. Maxwell \nD. Heisenberg", "A. 6.022 * 10^-23 atoms\nB. 6.022 * 10^-23 entities\nC. 6.022 * 10^23 atoms\nD. 6.022 * 10^23 entities", "A. mammalia\nB. reptilia\nC. monera\nD. aves", "A. Egon Schiele\nB. Gustav Klimt\nC. Oakar Kokoschka\nD. There is another"]

#----------------------------------------------------

q(1)
x = input("Choose option: ")
choices.append(x)
q(2)
y = input("Choose option: ")
choices.append(y)
q(3)
z = input("Choose option: ")
choices.append(z)
q(4)
w = input("Choose option: ")
choices.append(w)
print("Your choices: ")
print(choices)
print("Correct answers: ")
print(answers)

score = 0
for i in range(0,4):
    if choices[i] == answers[i]:
        score += 25
print("Your score is: ", score, "%")