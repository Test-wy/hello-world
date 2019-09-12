import re
#a = "C0C++9Java7Python"
#print(a.index("Python")>-1)  #如果字符串中包含python，则打印true
#print("Python" in a)

#正则
#result = re.findall("Python",a)  #在a字符串中找python字符串，返回一个列表，没有则返回[]
#result = "".join(result)
#print(result)

# result = re.findall("\d",a)
# print(result)

#借助普通字符定界
#s = "abc,acc,adc,aec,afc,ahc"  #找出s中中间字符未c或者f的的单词
#r = re.findall("a[^c-f]c",s)      #[]取或，^取非，-：c到f
#print(r)


#概括字符集：
# \d,\D,数字类型，和非数字类型[0-9]
#\w：匹配数字，字母，下划线[A-Za-z0-9_],\W：非单词字符
#\s匹配空白字符  [" ","\t","\n","\r"]   \S,非
#.匹配除换行符之外其他所有字符

#数量词
import re
#a = "python 1111java678php"
#r = re.findall("[a-z]{3,6}",a)  #匹配3~6个字符
#print(r)

#贪婪和非贪婪{3,6}:按最多数量比配，{3,6}？：按最小数量匹配

#*匹配字符*前面的字符0次或者无限次
# a = "pytho0python1pythonn2"
# r = re.findall("python*",a)  #n出现0次或者多次
# print(r)
# #+匹配1次或者无线多次
# r = re.findall("python+",a)
# print(r)
# #?匹配0次或者1次
# r = re.findall("python?",a)
# print(r)


#边界匹配^,$

#让一个字符串以重复多次方式匹配
a = "pythonpythonpythonpythonpythonpythonpython"
r = re.findall("(python){3}",a)
print(r)