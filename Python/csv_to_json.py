import sys
import os
import json
import datetime
import calendar
import glob

def check_arg(args):
    if len(args) != 2:
        print('usage: year')
        sys.exit()
    if not args[1].isdigit():
        print('yearは数値を入力して下さい')
        sys.exit()

def csv_to_json(input_file_name):
    index_region = 0
    index_day = 1
    index_month = 2
    index_other = 3

    ##### ファイル読み込み

    # 大きいファイルじゃないので全部読む
    lines = []
    with open(input_file_name, 'rt', encoding='utf-8') as fin:
        lines = list(map(lambda s: s.rstrip(), fin.readlines()))

    # 1行目の地域を取得する
    result_json = {}
    region_list = lines[index_region].split(',')
    result_json['regionNo'] = region_list[0]
    result_json['region'] = region_list[1]

    print('    ' + region_list[1])

    # 3行目の月を取得する
    # 先頭は空なので無視する
    month_list = list(map(lambda x: int(x), lines[index_month].split(',')[1:]))

    # 結果のリスト
    garbage_list = []
    result_json['garbageList'] = garbage_list

    # 2行目の曜日を処理する
    day_list = list(lines[index_day].replace('\n', ''))

    DAY_DICT = {
             '日': calendar.SUNDAY,
             '月': calendar.MONDAY,
             '火': calendar.TUESDAY,
             '水': calendar.WEDNESDAY,
             '木': calendar.THURSDAY,
             '金': calendar.FRIDAY,
             '土': calendar.SATURDAY
             }

    burn_list = []
    for day in day_list:
        day_Of_Week = DAY_DICT[day]
        for month in month_list:
            cal_year = year if month >= 4 else year + 1
            date_list = [x[day_Of_Week] for x in calendar.monthcalendar(cal_year, month)]
            # カレンダーから取るので日付0があるためそれを取り除く
            date_list = filter(lambda x: x != 0, date_list)
            for date in date_list:
                # 1/1〜1/3は除外する
                if month == 1 and (1 <= date and date <= 3):
                    continue
                burn_list.append('{0:04d}{1:02d}{2:02d}'.format(cal_year, month, date))
    burn_list.sort()
    garbage_list.append({
        'garbageTitleList': ['燃える一般ごみ', '毎週 ' + ''.join(day_list)],
        'garbageDateList': burn_list
        })

    # 4行目以降
    for row in lines[index_other:]:
        garbage = {}
        garbage_list.append(garbage)
        garbage_date_list = []
        garbage['garbageDateList'] = garbage_date_list
        for index, column in enumerate(row.split(',')):
            if index == 0:
                title_list = column.split('$')
                garbage['garbageTitleList'] = title_list
            else:
                cal_year = year if month_list[index - 1] >= 4 else year + 1
                for date_column in column.split('$'):
                    date = '{0:04d}{1:02d}{2:02d}'.format(cal_year, month_list[index - 1], int(date_column))
                    garbage_date_list.append(date)

    with open(input_file_name.replace('.csv', '') + '.json', 'wt') as fout:
        fout.write(json.dumps(result_json, ensure_ascii=False, indent=2))

##### ファイル確認

args = sys.argv
check_arg(args)
year = int(args[1])

file_list = glob.glob('*.csv')

for f in file_list:
    print('>>> ' + f)
    csv_to_json(f)

