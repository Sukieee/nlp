#-*- coding:utf-8 -*-
import os
import re
import json

def name_in():#获取文件名
    name = input('请输入需要读取的文件名：')
    return name

def name_lst():#制作文件名列表
    existed_name_lst = []
    for i in os.listdir():
        dealed_name = i[:-4]
        existed_name_lst.append(dealed_name)
    return existed_name_lst

def exam_name(name):#检验文件是否存在
    existed_name_lst = name_lst()
    try:
        for i in existed_name_lst:
            if name == i:
                file_name = i
                break
        return file_name
    except:
        print('输入文件名无效！')
        main()

def extract_content(name):
    fpath = name+'.txt'
    f = open(fpath,)
    text = f.read()
    return text

def extract_en(name):
    text = extract_content(name)
    uncn = re.compile(r'[\u0061-\u007a,\u0020]')
    text_en = ''.join(uncn.findall(text.lower()))
    file_en_name = name+'_EN.txt'
    with open(file_en_name, "w",encoding='utf-8') as f:
        json.dump(text_en, f,ensure_ascii=False,indent = 4)
    return ''

def extract_zh(name):
    text = extract_content(name)
    uncn = re.compile(r'[\u4e00-\u9fa5]')
    text_zh = ''.join(uncn.findall(text))
    file_zh_name = name+'_CN.txt'
    with open(file_zh_name, "w",encoding='utf-8') as f:
        json.dump(text_zh, f,ensure_ascii=False,indent = 4)
    return ''

def main():
    name = name_in()
    exam_name(name)
    extract_en(name)
    extract_zh(name)
    return ''

main()