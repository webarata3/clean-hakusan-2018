import sys
import os
import json
import datetime
import calendar

def checkArg(args):
    if len(args) != 4:
        print('usage: year in_filename out_filename')
        sys.exit()

    print('処理するファイル>>> ' + args[2])

    if not os.path.exists(args[2]):
        print('ファイルを指定してください')
        sys.exit()

    if os.path.isdir(args[2]):
        print('ファイルを指定してください（ディレクトリです）')
        sys.exit()

##### ファイル確認

args = sys.argv
checkArg(args)
year = int(args[1])
inputfilename = args[2]
outputfilename = args[3]

indexregion = 0
indexday = 1
indexmonth = 2
indexother = 3

##### ファイル読み込み

# 大きいファイルじゃないので全部読む
lines = []
with open(inputfilename, 'rt', encoding='utf-8') as fin:
    lines = fin.readlines()

# 行の最後の改行文字を消す
for row in lines:
    row = row.rstrip()

# 1行目の地域を取得する
resultjson = {}
regionlist = lines[indexregion].split(',')
resultjson['regionNo'] = regionlist[0]
resultjson['region'] = regionlist[1]

# 3行目の月を取得する
# 先頭は空なので無視する
monthlist = list(map(lambda x: int(x), lines[indexmonth].split(',')[1:]))

# 結果のリスト
garbagelist = []
resultjson['garbageList'] = garbagelist

# 2行目の曜日を処理する
daylist = list(lines[indexday].replace('\n', ''))

DAY_DICT = {
         '日': calendar.SUNDAY,
         '月': calendar.MONDAY,
         '火': calendar.TUESDAY,
         '水': calendar.WEDNESDAY,
         '木': calendar.THURSDAY,
         '金': calendar.FRIDAY,
         '土': calendar.SATURDAY
         }

burnlist = []
for day in daylist:
    dayOfWeek = DAY_DICT[day]
    for month in monthlist:
        calyear = year if month >= 4 else year + 1
        datelist = [x[dayOfWeek] for x in calendar.monthcalendar(calyear, month)]
        # カレンダーから取るので日付0があるためそれを取り除く
        datelist = filter(lambda x: x != 0, datelist)
        for date in datelist:
            burnlist.append('{0:04d}{1:02d}{2:02d}'.format(calyear, month, date))
burnlist.sort()
garbagelist.append({
    'garbageTitleList': ['燃える一般ごみ', '毎週 ' + ''.join(daylist)],
    'garbageDateList': burnlist
    })

# 4行目以降
for row in lines[indexother:]:
    garbage = {}
    garbagelist.append(garbage)
    garbagedatelist = []
    garbage['garbageDateList'] = garbagedatelist
    for index, column in enumerate(row.split(',')):
        if index == 0:
            titlelist = column.split('$')
            garbage['garbageTitleList'] = titlelist
        else:
            calyear = year if monthlist[index - 1] >= 4 else year + 1
            date = '{0:04d}{1:02d}{2:02d}'.format(calyear, monthlist[index - 1], int(column))
            garbagedatelist.append(date)

with open(outputfilename, 'wt') as fout:
    fout.write(json.dumps(resultjson, ensure_ascii=False, indent=2))

