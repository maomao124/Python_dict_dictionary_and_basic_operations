"""
 * Project name(项目名称)：Python_dict字典及基本操作
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 19:06
 * Version(版本): 1.0
 * Description(描述)：
 Python字典添加键值对
为字典添加新的键值对很简单，直接给不存在的 key 赋值即可
dict name[key] = value
dict name 表示字典名称。
key 表示新的键。
value 表示新的值，只要是 Python 支持的数据类型都可以。

Python字典修改键值对
Python 字典中键（key）的名字不能被修改，我们只能修改值（value）。

Python字典删除键值对
如果要删除字典中的键值对，还是可以使用 del 语句。
 """

if __name__ == '__main__':
    knowledge = ['语文', '数学', '英语']
    scores = dict.fromkeys(knowledge, 68)
    print(scores)
    scores["历史"] = 89
    print(scores)

    scores["历史"] = 87
    print(scores)

    del scores["历史"]
    print(scores)

    # 判断字典中是否存在指定键值对
    # 判断是否包含名为'数学'的key
    print('数学' in scores)
    # 判断是否包含名为'物理'的key
    print('物理' in scores)

    input()
