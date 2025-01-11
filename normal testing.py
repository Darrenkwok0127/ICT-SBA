def get_data():
    global x1
    f = open(r"C:\Users\Kwok\Documents\python\ICT SBA\Junior_hw_log\1C_assessments_hw_log.txt", "r")
    x1 = f.readlines()
    for i in range(len(x1)):
        x1[i] = x1[i].strip("\n")
get_data()
x2 = []
inp = input("Search: ").upper()
inp = inp.replace(" ", "")
if inp != "":
    for i in range(len(x1)):
        find = x1[i].find(inp)
        if find == -1:
            pass
        else:
            x2.append(x1[i])
if len(x2) != 0:
    for j in range(len(x2)):
        print(x2[j])
else:
    print("Empty")