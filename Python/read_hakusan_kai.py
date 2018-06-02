import requests, bs4

def getregionlist(soup):
    regionlist = []
    notfound = True
    for strong in soup.find_all('strong'):
        for span in strong.select('span > span'):
            if not span.text.isdigit():
                if span.text.find('松任地区のごみ収集日程') != -1:
                    notfound = False
                    continue
                if notfound: continue
                if span.text.find('収集日程') != -1:
                    continue
                regionlist.append(span.text)
    return regionlist

def getburntable(soup):
    burntable = []
    for table in soup.select('td[align=left] div table'):
        if table.text.find('燃やす一般ごみ') != -1:
            burntable.append(table)
    return burntable

def getothertable(soup):
    othertable = []
    for table in soup.select('td[align=left] div table'):
        if table.text.find('収集月') != -1:
            othertable.append(table)
    return othertable

# res = requests.get('http://www.city.hakusan.ishikawa.jp/shiminseikatsubu/kankyo/4r/gomi_nittei.html')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.content, 'html5lib')
html = ''
with open('gomi.html', encoding='utf-8') as fin:
    html = fin.read()
soup = bs4.BeautifulSoup(html, 'lxml')

regionlist = getregionlist(soup)
burntablelist = getburntable(soup)
othertablelist = getothertable(soup)

def writeburn(gomilist, burn):
    gomilist.append([burn.select('td')[1].text.replace('毎週　', '').replace('・', '')])

def writeother(gomilist, other):
    for i, tr in enumerate(other.select('tr')):
        row = []
        gomilist.append(row)
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
                row.append(td.text)

i = 0
for region in regionlist:
    print('>>> ' + region)
    gomilist = []

    # 地域を先頭行に置く
    gomilist.append(['{0:02d}'.format(i), region])

    # 燃える一般ごみ
    writeburn(gomilist, burntablelist[i])

    # その他ゴミ
    writeother(gomilist, othertablelist[i])

    # 書き出す
    with open('{0:02d}'.format(i + 1) + '.csv', 'wt') as fout:
        for data in gomilist:
            fout.write(','.join(data))
            fout.write('\n')
    if i == 11:
        break
    i += 1


