import os
import re
import pandas as pd
import numpy as np
import xlwt


def transfer(txt_path, save_path):
    with open(txt_path, 'r') as f:
        s = f.readlines()

    ns = []

    for a in s:
        a = a.strip()
        if ' ' in a:
            ns.extend(a.split(' '))
        else:
            ns.append(a)

    s = ns

    sn = []
    it = []
    for a in s:

        if re.match('[0-9]{8,8}', a) and len(a) == 8:
            if len(it) < 12:
                it.insert(2, '0')
            sn.append(it)
            it = []
            it.append(a)

        elif re.match('[0-9]', a) and len(a) == 1:
            if len(it) == 2:
                it.append(a)
        else:
            it.append(a)

    sn = sn[1:]

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')

    for i0, it in enumerate(sn):
        for j0, n in enumerate(it):
            # print(n, end='\t')
            worksheet.write(i0, j0, n)
        # print()


    workbook.save(save_path)


if __name__ == '__main__':
    # https://web.baimiaoapp.com/ 下 点 图片文字提取 ，将结果的txt文件下下来
    # transfer(
    #     '/Users/auro/Downloads/WechatIMG216.txt',
    #     './test.xls')
    
    txt_path = '/Users/auro/Downloads/WechatIMG216.txt'
    save_path = txt_path[:txt_path.rfind('.')]+'.xls'
    print(save_path)
