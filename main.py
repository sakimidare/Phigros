import json
import re
import requests
from bs4 import BeautifulSoup, NavigableString, TemplateString

def go(st):
    if st is None:
        return ""
    else:
        if st:
            return str(st).strip()
        else:
            return "undefined"

def get_stripped_strings(stripped_strings):
    for x in stripped_strings:
        return x
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
mew = requests.get('https://mzh.moegirl.org.cn/Phigros/%E8%B0%B1%E9%9D%A2%E4%BF%A1%E6%81%AF', headers=header)
soup = BeautifulSoup(mew.text,'html.parser')
ul_data = soup.find_all('table', class_='wikitable')
items = (ul_data[0].find_all("td"))
data_list = {}
for idx, item in enumerate(ul_data):
    # print(idx)
    # print(item)
    if idx+1:
        tds = item.find_all('td')
        song = re.sub(r'\[\d+\]','',item.th.get_text(types=(NavigableString, TemplateString)))
        print(song)
        try:
            illustration = tds[0].a.img.get('src')
        except:
            illustration = 'undefined'
        illustration_big = illustration.replace('thumb/','').rsplit('/',1)[0]
        chapter = item.find('td', text="所属章节").find_next("td").get_text(types=(NavigableString, TemplateString))
        bpm = item.find('td', text="BPM").find_next("td").get_text(types=(NavigableString, TemplateString))
        composer = re.sub(r'\[\d+\]','',item.find('td', text="曲师").find_next("td").get_text(types=(NavigableString, TemplateString)))
        get_len = item.find('td', text="时长") or item.find('td', text="长度")
        length = get_len.find_next("td").get_text(types=(NavigableString, TemplateString))
        illustrator = re.sub(r'\[\d+\]','',item.find('td', text="画师").find_next("td").get_text(types=(NavigableString, TemplateString)))
        chart = {}
        if not item.find('td', text="EZ") is None:
            current = item.find('td', text="EZ").find_next('td')
            ez_level = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            ez_difficulty = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            ez_combo = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            ez_charter = re.sub(r'\[\d+\]','',current.get_text(types=(NavigableString, TemplateString)))
            # raise ValueError
            chart["EZ"] = {
                "level": go(ez_level),
                "difficulty": go(ez_difficulty),
                "combo": go(ez_combo),
                "charter": go(ez_charter)
            }
            #print(chart["EZ"])
        else:
            ez_level = 0
            ez_difficulty = 0
            ez_combo = 0
            ez_charter = 0

        if not item.find('td', text="HD") is None:
            current = item.find('td', text="HD").find_next('td')
            hd_level = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            hd_difficulty = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            hd_combo = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            hd_charter = re.sub(r'\[\d+\]','',current.get_text(types=(NavigableString, TemplateString)))

            chart["HD"] = {
                "level": go(hd_level),
                "difficulty": go(hd_difficulty),
                "combo": go(hd_combo),
                "charter": go(hd_charter)
            }
        else:
            hd_level = 0
            hd_difficulty = 0
            hd_combo = 0
            hd_charter = 0

        if not item.find('td', text="IN") is None:
            current = item.find('td', text="IN").find_next('td')
            in_level = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            in_difficulty = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            in_combo = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            in_charter = re.sub(r'\[\d+\]','',current.get_text(types=(NavigableString, TemplateString)))
           
            chart["IN"] = {
                "level": go(in_level),
                "difficulty": go(in_difficulty),
                "combo": go(in_combo),
                "charter": go(in_charter),
            }

        else:
            in_level = 0
            in_difficulty = 0
            in_combo = 0
            in_charter = 0

        if not item.find('td', text="Legacy") is None:
            current = item.find('td', text="Legacy").find_next('td')
            lc_level = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            lc_difficulty = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            lc_combo = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            lc_charter = re.sub(r'\[\d+\]','',current.get_text(types=(NavigableString, TemplateString)))
            chart["Legacy"] = {
                "level": go(lc_level),
                "difficulty": go(lc_difficulty),
                "combo": go(lc_combo),
                "charter": go(lc_charter),
            }

        else:
            lc_level = 0
            lc_difficulty = 0
            lc_combo = 0
            lc_charter = 0
        if not item.find('td', text="AT") is None:
            current = item.find('td', text="AT").find_next('td')
            at_level = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            at_difficulty = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            at_combo = current.get_text(types=(NavigableString, TemplateString))
            current = current.find_next("td")
            at_charter = re.sub(r'\[\d+\]','',current.get_text(types=(NavigableString, TemplateString)))

            chart["AT"] = {
                "level": go(at_level),
                "difficulty": go(at_difficulty),
                "combo": go(at_combo),
                "charter": go(at_charter)
            }
        else:
            at_level = 0
            at_difficulty = 0
            at_combo = 0
            at_charter = 0

        if go(song) == "Another Me":
            if go(composer) == "Neutral Moon":
                song = "Another Me (Rising Sun Traxx)"
            else:
                song = "Another Me (KALPA)"
        if go(song) == "The Mountain Eater from MUSYNC":
            song = "The Mountain Eater"
        if go(song).find('Cipher') != -1:
            song = 'Cipher: /2&//<|0'
        data_list[go(song)] = {
            "song": go(song),
            "illustration": go(illustration),
            "illustration_big": go(illustration_big),
            "chapter": go(chapter),
            "bpm": go(bpm),
            "composer": go(composer),
            "length": go(length),
            "illustrator": go(illustrator),
            "chart": chart
                                                   }
data = json.dumps(data_list, indent=4, ensure_ascii=False)

with open("Phigros.json", 'w+', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write(data)

