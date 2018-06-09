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

def get_region(region_line):
    region_list = region_line.split(',')
    return (region_list[0], region_list[1])

def get_day_list(day_line):
    return list(day_line.replace('\n', ''))

def get_month_list(month_line):
    # 先頭は空白なので無視する
    return list(map(lambda x: int(x), month_line.split(',')[1:]))

def get_day_date_list(year, month, day_of_week):
    cal_year = year if month >= 4 else year + 1
    date_list = [x[day_of_week] for x in calendar.monthcalendar(cal_year, month)]
    # カレンダーから取るので日付0があるためそれを取り除く
    date_list = filter(lambda x: x != 0, date_list)
    day_date_list = []
    for date in date_list:
        # 1/1〜1/3は除外する
        if month == 1 and (1 <= date and date <= 3):
            continue
        day_date_list.append('{0:04d}{1:02d}{2:02d}'.format(cal_year, month, date))
    return day_date_list

def get_burn_list(day_list, month_list, year):
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
        day_of_week = DAY_DICT[day]
        for month in month_list:
            day_date_list = get_day_date_list(year, month, day_of_week)
            burn_list += day_date_list
    burn_list.sort()
    return burn_list

def get_garbage(row, year, month_list):
    garbage = {}
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
    return garbage

def csv_to_json(input_file_name):
    INDEX_REGION = 0
    INDEX_DAY = 1
    INDEX_MONTH = 2
    index_other = 3

    ##### ファイル読み込み

    # 大きいファイルじゃないので全部読む
    lines = []
    with open(input_file_name, 'rt', encoding='utf-8') as fin:
        lines = list(map(lambda s: s.rstrip(), fin.readlines()))

    # 1行目の地域を取得する
    result_json = {}
    result_json['regionNo'], result_json['region'] = get_region(lines[INDEX_REGION])
    print('    ' + result_json['region'])

    # 結果のリスト
    garbage_list = []
    result_json['garbageList'] = garbage_list

    # 2行目の曜日を処理する
    day_list = get_day_list(lines[INDEX_DAY])

    # 3行目の月を取得する
    month_list = get_month_list(lines[INDEX_MONTH])

    # 燃えるゴミ
    burn_list = get_burn_list(day_list, month_list, year)

    garbage_list.append({
        'garbageTitleList': ['燃える一般ごみ', '毎週 ' + ''.join(day_list)],
        'garbageDateList': burn_list
        })

    # 4行目以降
    for row in lines[index_other:]:
        garbage = get_garbage(row, year, month_list)
        garbage_list.append(garbage)

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

