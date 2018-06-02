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

##### ファイル読み込み

# 大きいファイルじゃないので全部読む
lines = []
with open(args[2], 'rt', encoding='utf-8') as fin:
    lines = fin.readlines()

# 3行目までは同じ書式なので読み込む
# rstripは行の終わりに改行が入るのでそれを取り除くため
gomilist = []
for i in range(2):
    gomilist.append(list(map(lambda x: int(x), lines[i].rstrip().split('\t'))))

# 4行目は曜日2つ
daylist = lines[3].rstrip().split('・')

##### ゴミ日付

# 結果を格納するリスト
garbagelist = []

for i in range(2):
    garbagedatelist = []
    garbagelist.append({
        'key': i + 1,
        'garbageTitleList': ['燃えるゴミ'],
        'garbageDateList': garbagedatelist
        })
    for j in range(12):
        calyear = year if gomilist[0][j] >= 4 else year + 1
        garbagedatelist.append('{0:04d}{1:02d}{2:02d}'.format(calyear, gomilist[0][j], gomilist[i + 1][j]))

garbagelist[0]['garbageTitleList'] = [
    '燃やす粗大ごみ',
    '紙類・古着・布類',
    'ペットボトル',
    '容器包装プラスチック'
    ]

garbagelist[1]['garbageTitleList'] = [
    '燃えないごみ',
    '缶・びん',
    '容器包装プラスチック'
    ]

# 燃えるゴミ
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
for i in range(2):
    dayOfWeek = DAY_DICT[daylist[i]]
    for month in gomilist[0]:
        calyear = year if month >= 4 else year + 1
        datelist = [x[dayOfWeek] for x in calendar.monthcalendar(calyear, month)]
        # カレンダーからとるので日付0があるため、それを取り除く
        datelist = filter(lambda x: x != 0, datelist)
        for date in datelist:
            burnlist.append('{0:04d}{1:02d}{2:02d}'.format(calyear, month, date))

burnlist.sort()
garbagelist.insert(0, {
    'key': 0,
    'garbageTitleList': ['燃やす一般ごみ', '水・土'],
    'garbageDateList': burnlist
    });
gomi = {
        'garbageList': garbagelist
       }

print('出力するファイル>>> ' + args[3])

gomi_json = json.dumps(gomi, ensure_ascii=False, indent=2)
with open(args[3], 'wt') as fout:
    fout.write(gomi_json)

