import requests, bs4

def get_region_list(soup):
    region_list = []
    not_found = True
    for strong in soup.find_all('strong'):
        for span in strong.select('span > span'):
            if not span.text.isdigit():
                if span.text.find('松任地区のごみ収集日程') != -1:
                    not_found = False
                    continue
                if not_found: continue
                if span.text.find('収集日程') != -1:
                    continue
                region_list.append(span.text)
    return region_list

def get_burn_table(soup):
    burn_table = []
    for table in soup.select('td[align=left] div table'):
        if table.text.find('燃やす一般ごみ') != -1:
            burn_table.append(table)
    return burn_table

def get_other_table(soup):
    other_table = []
    for table in soup.select('td[align=left] div table'):
        if table.text.find('収集月') != -1:
            other_table.append(table)
    return other_table

def write_burn(gomi_list, burn):
    # 白峰（23番目）にバグがあるのでその対応
    if burn.select('td')[1].text.find('燃やす') != -1:
        gomi_list.append([burn.select('td')[2].text.replace('毎週　', '').replace('・', '')])
    else:
        gomi_list.append([burn.select('td')[1].text.replace('毎週　', '').replace('・', '')])

def write_other(gomi_list, other):
    for i, tr in enumerate(other.select('tr')):
        row = []
        gomi_list.append(row)
        for j, td in enumerate(tr.select('td')):
            if i == 0 and j == 0:
                row.append('')
            elif i == 0 and j == 1:
                row.append(td.text.replace('月', ''))
            elif i != 0 and j == 0:
                t = str(td.contents) \
                        .replace('<br/>', '$') \
                        .replace('[', '') \
                        .replace(']', '')
                temp = bs4.BeautifulSoup(t, 'lxml')
                row.append(temp.text)
            else:
                t = str(td.contents) \
                        .replace('</span><br/><br/><span>', '$') \
                        .replace('[', '') \
                        .replace(']', '')
                temp = bs4.BeautifulSoup(t, 'lxml')
                row.append(temp.text)

# res = requests.get('http://www.city.hakusan.ishikawa.jp/shiminseikatsubu/kankyo/4r/gomi_nittei.html')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.content, 'html5lib')
html = ''
with open('gomi.html', encoding='utf-8') as fin:
    html = fin.read()
soup = bs4.BeautifulSoup(html, 'lxml')

region_list = get_region_list(soup)
burn_table_list = get_burn_table(soup)
other_table_list = get_other_table(soup)

i = 0
for region in region_list:
    print('>>> ' + region)
    gomi_list = []

    # 地域を先頭行に置く
    gomi_list.append(['{0:02d}'.format(i + 1), region])

    # 燃える一般ごみ
    write_burn(gomi_list, burn_table_list[i])

    # その他ゴミ
    write_other(gomi_list, other_table_list[i])

    # 書き出す
    with open('{0:02d}'.format(i + 1) + '.csv', 'wt') as fout:
        for data in gomi_list:
            fout.write(','.join(data))
            fout.write('\n')
    i += 1

