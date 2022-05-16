# -*- coding: UTF-8 -*-

import sys
import os
import csv

sys.path.append("..")
from libs import XmlFileUtil

LINE_COUNT = 0


def ParseCsvAndWriteAndroid(filePath, targetPath):
    global LINE_COUNT
    reload(sys)
    sys.setdefaultencoding('utf-8')
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        keys = []
        for i, rows in enumerate(reader):
            if i == 0:
                header_row = rows
            else:
                keys.append(rows[0])
        if len(header_row) == 1:
            print 'localizable not null'
            sys.exit(-1)

        if i > 0:
            LINE_COUNT = i + 1
        header_row.pop(0)
        for inx, loc in enumerate(header_row):
            if loc == "en":
                locDir = "values"
            else:
                locDir = "values-" + loc
            targetDir = os.path.join(targetPath, locDir)
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)

            with open(filePath, 'rb') as ff:
                r = csv.reader(ff)
                next(r)
                values = [row[inx + 1] for row in r]

            XmlFileUtil.writeToFile(
                keys, values, targetDir, "strings.xml")

        print "\n**************************"
        print("\n %d lines write successful \n" % LINE_COUNT)
        print "**************************"


def ParseCsvAndWriteIos(filePath, targetPath):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        keys = []
        for i, rows in enumerate(reader):
            if i == 0:
                header_row = rows
            else:
                keys.append(rows[0])
        if len(header_row) == 1:
            print 'localizable not null'
            sys.exit(-1)

        if i > 0:
            LINE_COUNT = i + 1
        header_row.pop(0)
        for inx, loc in enumerate(header_row):
            locDir = loc + ".lproj"
            targetDir = os.path.join(targetPath, locDir)
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)

            content = ""
            with open(filePath, 'rb') as ff:
                r = csv.reader(ff)
                next(r)
                # values = [row[inx + 1] for row in r]
                for i, v in enumerate(r):
                    content += "\"" + v[0] + "\" " + \
                               "= " + "\"" + v[inx + 1] + "\";\n"
                open(os.path.join(targetDir, "Localizable.strings"), "wb").write(content)

        print "\n**************************"
        print("\n %d lines write successful \n" % LINE_COUNT)
        print "**************************"
