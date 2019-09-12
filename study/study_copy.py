#-*-coding:utf-8 -*-



# #注：值：字符串，数字等写死的数据；引用：字典，列表为引用
# import copy
# dict = {"a":"apple","b":{"g":"grape","o":"orange"}}
# dict2 = copy.copy(dict)
# dict2["a"] = "aaa"
# #dict2["b"]["o"] = "0000"
# print(dict)

#
# dict3 = copy.deepcopy(dict)
# dict3["b"]["g"]="gggg"
# print(dict3)



# word = "\thello world\n"
# print("直接输出：",word)
# print("strip()后输出：",word.strip())
# print("lstrip()后输出：",word.lstrip())
# print("rstrip()后输出：",word.rstrip())

#"".join()连接字符串
# str = ["hello","world"]
# result = "".join(str)
# print(result)

# from functools import reduce
# import operator
# strs = ["hello ","world ","hello ","china "]
# result = reduce(operator.add,strs,"")
# print(result)


# word = "hello world"
# print("hello" == word[0:5])
# print(word.startswith("hello"))
#
# print(word.endswith("ld",6,10))

# s = "hello world"
# s = list(s)
# s = "".join(s)
# print(s)

# l = [3,1,4,2]
# print(tuple[-1])
# print(tuple[0:-2])
# print(tuple[2:-2])
# print(tuple[1:-2])
# l.sort(reverse = True)
# print(l)

# dict = {"a":"apple","b":"banana"}
# dict2 = {"c":"grape"}
# dict.update(dict2)
# print(dict2)