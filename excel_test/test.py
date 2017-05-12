def test():
    wifis = ['3', '5']
    wifi2 = ['3', '5', '5']
    l = [1, 2]
    dic = dict.fromkeys(wifis)
    print dic

    print dic
    m = []
    temp = []
    for each in wifis:
        for item in wifi2:
            if each == item:

                temp.append(l)

        dic[each] = temp
        temp = []
    print dic





if __name__ == '__main__':
        test()