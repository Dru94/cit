from genericpath import exists


dic = input()
print("Enter questions and answer dictionary: " + dic)

if not exists:
    file = open('answer.txt', 'w')
    for qn, ans in dic:
        file.write(qn, "<<<>>>", ans)
    file.close()

print("Content")

c = open("answer.txt", r)

print(c.read())
