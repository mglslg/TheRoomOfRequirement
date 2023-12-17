import sys
import jieba

sys.path.append("..")

with open('stop_words.txt') as fp:
    stop_words = [_.strip() for _ in fp.readlines()]

print(len(stop_words))
print(stop_words)

seg_list = jieba.cut("他来到的网易行研大厦")
print(",".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算机所，后在日本京都大学深造")

# print(",".join(seg_list))

seg_list1 = []
for e in jieba.cut("小明毕业于武汉大学，后来又去了美国深造"):
    if e not in stop_words and not e.isspace():
        seg_list1.append(e.lower())

print(seg_list1)
