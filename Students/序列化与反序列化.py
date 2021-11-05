import json

dict = {"name":"gight",
        "age":27,
        "address":"shenzhen"}

print('未序列化前的数据类型：',type(dict))
print('未序列化前的数据：',dict)

#对python对象进行序列化操作
str1 = json.dumps(dict)
print('序列化后的数据类型：',type(str1))
print('序列化后的数据：',str1)

#对str1反序列化回来
str2 = json.loads(str1)
print('反序列化后的数据类型：',type(str2))
print('反序列化后的数据：',str2)