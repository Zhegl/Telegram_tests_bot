# By Aleksandr Zheglov
import telegram.ext


def save_test(name, cor_ans, que, ans):
    try:
        f = open(name + ".data", "rt")
        return -1
    except Exception:
        ans2 = []
        for i in range(len(ans)):
            ans2.append("%".join(ans[i]))
        new_data = name + "*" + "/".join(cor_ans) + "*" + "/".join(que) + "*" + "/".join(ans2)
        f = open(name + ".data", "wt")

        f.write(new_data)
        f.close()
        f = open("tests.list", "rt").readlines()
        f2 = open("tests.list", "wt")
        for el in f:
            f2.write(el)
        f2.write(name)
        f2.close()
        return 0


# save_test("name", ["que1", "que2"], [["ans1", "ans2"], ["ans1", "ans2"]], ["cor1", "cor2"])

def load_test(name):
    if name[-1] == "\n":
        name = name[:-1]
    f = open(name + ".data", "rt")
    main_data = f.readline().split("*")
    name = main_data[0]
    cor_ans = main_data[1].split("/")
    que = main_data[2].split("/")
    ans_temp = main_data[3].split("/")
    ans = []
    for el in ans_temp:
        ans.append(el.split("%"))
    f.close()
    return [name, cor_ans, que, ans]


# print(load_test("Почти легкий тест по информатике"))

def save_player(id, score):
    new_data = id + "*" + score
    f = open(id + ".dataplayer", "wt")
    f.write(new_data)
    f.close()


def load_player(id):
    f = open(id + ".dataplayer", "rt")
    data = f.readline().split("*")
    f.close()
    return data

# save_player("234645", "100")
# print(load_player("234645"))
