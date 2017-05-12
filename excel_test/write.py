import xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style



def write_excel():
    workBook = xlwt.Workbook()
    sheet = workBook.add_sheet('Sheet1')


    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    row0 = [u'yw', u'zt', u'bj', u'sh', u'gz', u'sz', u'xj', u'hj']
    column0 = [u'jp', u'cp', u'hc', u'qc', u'qt']
    status = [u'yj', u'cp', u'tp', u'ywxj']


    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])


    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i + 3, 0, 0)
        sheet1.write_merge(i, i + 3, 7, 7)
        i += 4
        j += 1

    sheet1.write_merge(21, 21, 0, 1, u'hj')


    i = 0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + i + 1, 1, status[j])
        i += 4

    f.save('/root/Desktop/x.xls')


if __name__ == '__main__':
    # generate_workbook()
    # read_excel()
    write_excel()