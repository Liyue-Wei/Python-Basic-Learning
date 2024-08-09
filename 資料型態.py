#數值、布林值、字串
num1 = 1  #int
num2 = 1.14514  #float

num1 *= 1.0  #convert int to float
 
bol1 = True  #bool

str1 = 'hello world'  #string == hello world
str2 = "hello world"  #string == hello world
str3 = 'hello "world"'  #string include "world" == hello "world"

'''
跳脫字元

單引號 \'  雙引號 \"  反斜線 \\
換行 \n  BackSpace鍵 \b  換頁 \f
'''

#print()函數
'''
1. print基本輸出  -->  print(obj1, obj2, ..., sep="", end="")  
sep == 分隔字元
end == 結束字元；預設為"\n"，""則同列輸出

2. print參數格式化%  -->  print(obj % (參數))
%5d  固定輸出5字元；少於5位數自動空格
%5s  固定輸出5字元；少於5個字元自動空格
%8.2f  固定輸出8字元；(8位元-(2位元+1位元).2位元)=(5位元.2位元)

obj1 = 114.514
print("obj1=%9.4f" % obj1)  #obj1= 114.5140

3. print參數格式化 format()  -->  print(({} {} ...).format(obj1, obj2, ...))
'''

#type()函數  -->  type(obj)
#id()函數，檢查變數記憶體位置  -->  id(obj)

#input()函數
'''
1. 基本輸入  -->  obj = input("提示字串")
2. 一行輸入多個str  -->  i = input().split(' ')
3. 一行輸入多個int  -->  i = map(int, intput().split(' '))
4. 強制轉換輸入型態  -->  obj = int(input())  
'''

obj = int(input())