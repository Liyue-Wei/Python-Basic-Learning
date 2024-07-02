#串列 list
'''
1. 一維串列  -->  list1 = [obj1, obj2, ...]
2. 二維串列  -->  list2 = [[obj1, obj2, ...], [obj3, obj4, ...]]
'''

#串列取值
'''
list3 = [list3[0], list3[1], list3[2], list3[3]]；等同於
list3 = [list3[-4], list3[-3], list3[-2], list3[-1]]
'''

#串列變數 range()函式  -->  range(起始值, 終止值, 間隔值)

#for迴圈  -->  for (變數 in 串列):

#break與continue用法
'''
1. break用於停止迴圈
2. continue用於跳過某步驟，例:
    for i in range(0, 10):
        if(i==5):
            continue 
        print(i, end=" ")  #0 1 2 3 4 6 7 8 9 
'''

#while迴圈  --> while 條件式:

#串列操作
'''
L*n  -->  L乘以n次
n in L  -->  Bool值，檢測L中是否存在n
L[n1:n2]  -->  取出n1至n2-1的元素
del L[n1:n2]  -->  刪除n1至n2-1的元素
len(L)  -->  取L長度
min(L)  -->  取L最小值 ； max(L)  -->  取L最大值
L.index(n)  -->  取得n在L的位置
L.count(n)  -->  取的n在L出現的次數
L.append(n)  -->  在L最後加入n  -->  [1, 2, 3] + [4, 5] == [1, 2, 3, [4, 5]]
L.extend(x)  --> 在L最後加入x元素  -->  [1, 2, 3] + [4, 5] == [1, 2, 3, 4, 5]
L.insert(n, obj)  -->  在L的n位置插入obj
L.remove(n)  -->  在L中刪除第一個n元素 ； 針對元素刪除
L.pop(n1)  -->  刪除L[n1] ； L.pop()則刪除L[-1] ； 針對位置刪除
L.reverse()  -->  翻轉L
L.sort()  -->  由大到小排序L
'''

#tuple元組  -->  tup(obj1, obj2, obj3, ...)；值不可修改，較快且較安全

#dict字典  -->  dict1 = {"key1":value1, "key2":value2, "key3":value3, ...}
'''
1. 修改與新增字典元素值
    dict1 = {"key1":value1, "key2":value2, "key3":value3}
    dict1["key4"] = value4  #新增key4
    dict1["key1"] = new_value1  #修改key1的value

2. 刪除字典中特定元素，刪除所有元素，刪除字典
    del dict1[key4]  #刪除key4

    dict1.clear()  #清除dict1中所有元素

    del dict1  #刪除dict1
'''

# dict操作
'''
dict1.copy()  -->  複製dict1
keyn in dict1  -->  Bool值，檢測dict1中是否存在keyn
dict1.items()  -->  取得[("key1":value1), ("key2":value2), ...]組合的list
dict1.keys()  -->  取得["key1", "key2", ...]組成的list
dict1.values()  -->  取得["value1", "value2", ...]組成的list
dict1.get(key)  -->  取得dict1中key1的value ； 等同於dict1[key]
dict1.setdefult(key, value)  -->  若key不存在dict1中，則新增key及value
'''
dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
print(dict1.get("key1"))
print(dict1["key1"])
print(dict1)
dict1.setdefault("key4", 114514)
print(dict1)