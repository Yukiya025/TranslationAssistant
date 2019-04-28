# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
import re
import csv

downloadtxt = open('source.txt', 'r', encoding = 'utf-8-sig')
texts = downloadtxt.read()
texts = re.sub('[.,?!()\'—]', ' ', texts)
texts = texts.split()
# print(texts)
print(len(texts)) # 105
# ここからレマ化
lemma_list = []
for text in texts:
    if text not in lemma_list:
        lemma_list.append(wn.morphy(text))

# 重複をなくす
no_dup = []
for l in lemma_list:
    if l not in no_dup:
        no_dup.append(l)
no_dup = [e for e in no_dup if e is not None] # リスト内からNoneを除去。内包表記
print("Duplications deleted")
print(len(no_dup))

# アルファベット順にソート
no_dup.sort()
with open('source.csv', 'w', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, lineterminator = '\n')
    for n in range(0, len(no_dup)):
        writer.writerows([[no_dup[n]]])
