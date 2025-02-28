
'''
mode=
 r 只读模式
 w 只写模式
 a 追加
'''
file=open(file=r'yamldata.yaml',mode='r',encoding='utf-8')   #只读模式
result=file.read()  #读取
file.close()    #回收open
print(result)


file=open(file=r'yamltest.yaml',mode='w',encoding='utf-8')   #只写模式  如果没有找到该路径下文件就会自动创建一个
file.write("牛逼")  #写入
file.close()    #回收open

file=open(file=r'yamltest.yaml',mode='a',encoding='utf-8')   #追加模式
file.write("牛逼")  #写入
file.close()    #回收open


import yaml

file=open(file=r'yamldata.yaml',mode='r',encoding='utf-8')   #只读模式
result_yaml=yaml.load(stream=file.read(),Loader=yaml.FullLoader)
file.close()    #回收open

print(result_yaml,type(result_yaml),result_yaml["msg"])