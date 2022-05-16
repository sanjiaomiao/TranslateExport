# -*- coding:utf-8 -*-

import glob
import csv
import sys

from xlsxwriter.workbook import Workbook


def covert(fPath):
    for csvfile in glob.glob(fPath):
        print csvfile[:-4] + '.xlsx'
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    print c, col
                    worksheet.write(r, c, col)
        workbook.close()
    sys.exit()
