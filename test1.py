"""
 * Project name(项目名称)：Python_dict字典及基本操作
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 18:50
 * Version(版本): 1.0
 * Description(描述)： 字典（dict）是一种无序的、可变的序列，它的元素以“键值对（key-value）”的形式存储。
 相对地，列表（list）和元组（tuple）都是有序的序列，它们的元素在底层是挨着存放的。

 主要特征	            解释
通过键而不是通过索引来读取元素	字典类型有时也称为关联数组或者散列表（hash）。它是通过键将一系列的值联系起来的，这样就可以通过键从字典中获取指定项，但不能通过索引来获取。
字典是任意数据类型的无序集合	和列表、元组不同，通常会将索引值 0 对应的元素称为第一个元素，而字典中的元素是无序的。
字典是可变的，并且可以任意嵌套	字典可以在原处增长或者缩短（无需生成一个副本），并且它支持任意深度的嵌套，即字典存储的值也可以是列表或其它的字典。
字典中的键必须唯一	字典中，不支持同一个键出现多次，否则只会保留最后一个键值对。
字典中的键必须不可变	字典中每个键值对的键是不可变的，只能使用数字、字符串或者元组，不能使用列表。

dict name = {'key':'value1', 'key2':'value2', ..., 'key n':value n}
其中 dict name 表示字典变量名，key n : value n 表示各个元素的键值对。需要注意的是，同一字典中的各个键必须唯一，不能重复。

Python 访问字典元素
dict name[key]

其中，dict name 表示字典变量的名字，key 表示键名。

 """

if __name__ == '__main__':
    # 使用字符串作为key
    scores = {'数学': 75, '英语': 69, '语文': 94}
    print(scores)
    print(type(scores))
    # 创建空元组
    dict2 = {}
    print(dict2)
    knowledge = ['语文', '数学', '英语']
    scores = dict.fromkeys(knowledge, 68)
    print(scores)

    print(scores['数学'])
    print(scores.get("数学"))
    print(scores.get("数"))
    print(scores.get("数", "不存在"))
    print(scores)
    del scores['数学']
    print(scores)
    del scores
    # print(scores)

    input()

