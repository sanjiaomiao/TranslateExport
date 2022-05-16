# -*- coding:utf-8 -*-

import sys

sys.path.append("..")
from libs.ParseCsvAndWrite import ParseCsvAndWriteAndroid
import os
import time
from optparse import OptionParser


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--fileDir",
                      help="Xls files directory.",
                      metavar="fileDir")

    (options, args) = parser.parse_args()

    return options


def convertFromMultipleForm(fileDir, targetDir):
    for _, _, filenames in os.walk(fileDir):
        csvFiles = [fi for fi in filenames if fi.endswith(".csv")]
        for file in csvFiles:
            ParseCsvAndWriteAndroid(fileDir + "/" + file, targetDir)


def startConvert(options):
    fileDir = options.fileDir

    if fileDir is None:
        print "xls files directory can not be empty! try -h for help."
        return

    targetDir = "output/android" + \
                "_" + time.strftime("%Y%m%d")
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    convertFromMultipleForm(fileDir, targetDir)


def main():
    options = addParser()
    startConvert(options)

main()
