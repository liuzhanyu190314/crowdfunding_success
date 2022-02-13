#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:daniel

from lxml import etree
import requests
import json
import time
import csv
class Tx:
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }
        self.catetag_list = [123,125,126,127,128,129,130,133]

    def get_data(self):
        for cat in self.catetag_list:
            for page in range(0, 12000):
                url = f"https://ssl.gongyi.qq.com/cgi-bin/gywcom_gy_filter?page={str(page)}&pcnt=6&ranktype=time&pstatus=active&rootCate={str(cat)}&catetag=123&token=678902"
                # url = f"https://ssl.gongyi.qq.com/cgi-bin/gywcom_gy_filter?page={str(page)}&pcnt=6&ranktype=time&rootCate=74&ptype=74&token=678902"
                print(url)
                res = requests.get(url, headers=self.headers, verify=False)
                if res.status_code == 200:
                    html = res.text
                    json_html = json.loads(html)
                    print(json_html)
                    print(json_html['data'])
                    self.parse1(json_html)

    def parse1(self,json_html):
        if json_html.get('data'):
            for mm in json_html['data']['projs']:
                uid = mm['id']
                new_uid = uid[-2:]
                if new_uid[0] == '0':
                    new_uid = new_uid[1]
                url = f"https://scdn.gongyi.qq.com/json_data/data_detail/{new_uid}/detail.{str(uid)}.json"
                print(url)
                res = requests.get(url, headers=self.headers, verify=False)
                html = res.text
                json_html = json.loads(html)
                detail = json_html.get('detail')
                desc = detail['desc']
                desc_p = etree.HTML(desc)
                descs = desc_p.xpath('//text()')
                strs = ""
                for i in descs:
                    strs += i
                img = desc_p.xpath('//img/@src')
                imgs = ""
                for j in img:
                    imgs += j.replace('//', 'https://') + "\n"

                project_start_time = json_html.get('base').get('launch_time')
                record_num = json_html.get('base').get('record_num')
                if record_num:
                    record_num = record_num
                else:
                    record_num = ""
                fundname = json_html.get('base').get('fundName')
                pname = json_html.get('base').get('pName')
                funder = json_html.get('base').get('funder')
                donate = json_html.get('base').get('donate').get('needMoney')

                new_url = f"https://ssl.gongyi.qq.com/cgi-bin/ProjInfoQuery.fcgi?id={str(uid)}&type=proj_mini_stat&is_parent=0&token=678902"
                print(url)
                res1 = requests.get(new_url, headers=self.headers, verify=False)
                html1 = res1.text
                json_html1 = json.loads(html1)
                get_money = str(json_html1['msg']['stat']['recvedMoney'])
                defect_money = str(int(donate) - int(get_money))
                record = json_html1['msg']['stat']['donateNum']
                listimg = mm['listImg']
                if "http:" in listimg:
                    listimg = listimg + "/200"
                else:
                    listimg = listimg.replace("//", 'https://') + "/200"
                funder_name = ""
                funder_corp = ""
                funder_intro = ""
                funder_face = ""
                if funder:
                    if funder.get('name'):
                        funder_name = funder['name']
                    else:
                        funder_name = ""
                    if funder.get('corp'):
                        funder_corp = funder['corp']
                    else:
                        funder_corp = ""
                    if funder.get('intro'):
                        funder_intro = funder['intro']
                    else:
                        funder_intro = ""
                    if funder.get('face'):
                        funder_face = funder['intro']
                    else:
                        funder_face = ""

                    if funder_face == "":
                        funder_face = ""
                    else:
                        if "http:" in funder_face:
                            funder_face = funder_face
                        else:
                            funder_face = funder_face.replace("//", 'https://')

                a_donate = list(donate)
                a_donate.insert(len(donate) - 2, '.')
                new_donate = "".join(a_donate)

                a_get_money = list(get_money)
                a_get_money.insert(len(get_money) - 2, '.')
                new_get_money = "".join(a_get_money)

                a_defect_money = list(defect_money)
                a_defect_money.insert(len(defect_money) - 2, '.')
                new_defect_money = "".join(a_defect_money)

                cishu = json_html.get('base').get('count')
                if cishu:
                    process = cishu['process']
                    finance = cishu['finance']
                    if process != 0:
                        process = f"三个月内进展反馈共{str(process)}次"
                    else:
                        process = "未进入执行披露期"

                    if finance != 0:
                        finance = f"2020年至今共进行{str(finance)}次财务披露"
                    else:
                        finance = "未进入执行披露期"
                else:
                    process = ""
                    finance = ""
                new_data = [
                    [uid, mm['cateName'], fundname, listimg, mm['title'],
                     mm['objTagName'] + "|" + mm['cateTagName'], mm['summary'], strs, imgs, project_start_time,
                     record_num, fundname, pname, funder_name,
                     funder_corp,
                     funder_intro,
                     funder_face,
                     new_donate,
                     new_get_money,
                     new_defect_money,
                     record,
                     process,
                     finance]
                ]
                file_name = "demo.csv"
                with open(file_name, 'a+', encoding="gb18030", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(new_data)
                time.sleep(5)
        else:
            pass


if __name__ == "__main__":
    run = Tx()
    run.get_data()