import requests, bs4

def create_csv(region, no):
    print('>>> ' + region.text)
    base = region.parent.parent.parent.parent
    table1 = base.next_sibling.next_sibling.select('table')
    # print(table1)

    gomilist = []
    # 地域を先頭行に置く
    gomilist.append(['{0:02d}'.format(no), region.text])

    # 燃えるゴミ
    burn = base.next_sibling.next_sibling.next_sibling.next_sibling
    while (True):
        if burn
            print('>>>>>>>' + str(burn))
            break
        burn = burn.next_sibling
    print(burn)

    gomilist.append([burn.select('td')[1].text.replace('毎週　', '').replace('・', '')])
    for i, tr in enumerate(table1[0].select('tr')):
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
    with open('{0:02d}'.format(no) + '.csv', 'wt') as fout:
        for data in gomilist:
            fout.write(','.join(data))
            fout.write('\n')

# res = requests.get('http://www.city.hakusan.ishikawa.jp/shiminseikatsubu/kankyo/4r/gomi_nittei.html')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.content, 'html5lib')
html = ''
with open('gomi.html', encoding='utf-8') as fin:
    html = fin.read()
soup = bs4.BeautifulSoup(html, 'lxml')
no = 1
for a in soup.select('a[name]'):
    for region in a.parent('span'):
        # 地区
        create_csv(region, no - 1)
    no += 1
    if no == 11: break

