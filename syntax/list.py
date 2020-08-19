spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1]) #elephant
print(spam[-3]) #bat

print(spam[0:4]) #['cat', 'bat', 'rat', 'elephant']

print(spam[1:3]) #['bat', 'rat']

print(spam[0:-1]) #['cat', 'bat', 'rat']

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2]) #['cat', 'bat']

print(spam[1:]) #['bat', 'rat', 'elephant']

print(spam[:]) #['cat', 'bat', 'rat', 'elephant']

print([1, 2, 3] + ['A', 'B', 'C']) #[1, 2,  3,  'A',  'B',  'C']

print(['X', 'Y', 'Z'] * 3) #['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

del spam[2] #删除变量  

#输出0,1,2,3
for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

# 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# 'howdy' not in spam

# 多重赋值
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

print(spam.index('hello'))

#原地排序，并不返回新数组
spam.sort() #逆序排序
span.sort(reverse=True) #顺序排序

#如果知道想要删除的值在列表中的下标，del 语句就很好用。
#如果知道想要从列表中删除的值，remove() 方法就很好用

#字符串可以被当成字符数组直接使用
#但字符串跟Java一样是只读的,不可更改
name = 'Zophie'
print(name[0]) #打印Z

#元组相当于final的数组
eggs = ('hello', 42, 0.5)
print(eggs[0])

# [].list() 和[].tuple()分别返回数组的列表和元组形式
