import xlrd
import xlwt


def read_excel():
    workbook = xlrd.open_workbook('/root/Desktop/b.xlsx')
    # print workbook.sheet_names()
    wifis = ['302', '404', '1233', 'cs309', 'CS411',
             'cs417', 'c', 'h', '3', '5']
    # wifis = ['3']

    positions = []
    for i in range(1, 6):
        for j in range(1, 7):
            temp = "(%s,%s)" % (i, j)
            positions.append(temp)
    print positions
    sheet1 = workbook.sheet_by_index(0)
    # sheet1 = workbook.sheet_by_name('Sheet1')

    # print sheet1
    # print sheet1.row(0)[2].value
    # print sheet1.row(0)[0].ctype  #type
    print sheet1.nrows, sheet1.ncols
    # print type(sheet1.row(0)[0].value)
    i = 0

    content = []
    for each in wifis:
        i += 1
        # j = 0
        print 'i = %d' % i
        for item in positions:
            # j += 1
            # print 'j = %d' % j
            for index in range(sheet1.nrows):
                a = sheet1.row(index)[0].value
                if type(a) == float:
                    a = str(int(a))
                b = sheet1.row(index)[2].value
                if a == each and b == item:
                    # name = each + '_' + item
                    content.append(sheet1.row_values(index))

    # for each1 in content:
    #     print each1
    print len(content)
    dic = dict.fromkeys(wifis) #dong tai  #{'CS411': None, 'c': None, 'h': None, 'cs417': None, '3': None, '5': None, 'cs309': None}
    temp = []
    for each2 in wifis:
        for item2 in content:
            if type(item2[0]) == float:
                item2[0] = str(int(item2[0]))
            if each2 == item2[0]:
                # dic[temp].append(item[0])
                temp.append(item2)
                # temp1 = list(set(temp)) # qu chong
        dic[each2] = temp
        temp = []
    print dic['cs309']
    print len(dic['1233'])
    # print dic['3']
    # print len(dic['3'])

    # f = xlwt.Workbook()
    # s = f.add_sheet('Sheet1')
    for name in wifis:
        f = xlwt.Workbook()
        s = f.add_sheet('Sheet1')
        file_name = '/root/Desktop/' + name + '.xls'
        source = dic[name]
        # print source[0][1]
        print len(source)
        for i in range(len(source)):#row
            temp = len(source[i])
            for j in range(temp):#col
                s.write(i, j, source[i][j])

        f.save(file_name)

if __name__ == '__main__':
    read_excel()
