# Average of a list


def average(list):
    # for i in range of list add list[i] to temp / len(list)
    temp = 0
    for i in range(len(list)):
        temp += int(list[i])
    return temp/len(list)



