#### Android / IOS 端一起维护一个文件(strings.csv), 使用的时候各自导出相应端的 String 文件

### Origin translation file
```
    translation_files/strings.csv
```

### My Env
    - python: 2.7.18
    - pip: 19.2.3
### install
```
pip install -r ./requirements.txt
```
### csv file to ios string
``` 
python CsvToIos.py -f translation_files
```

### csv file to android string
``` 
python CsvToAndroid.py -f translation_files
```

### Thanks
[Localizable.strings2Excel](https://github.com/CatchZeng/Localizable.strings2Excel)
