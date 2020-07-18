*！/usr/bin/env python
编码：utf-8 |
进口 json

导入 xmind
进口管道


def custom_parse_xmind（工作簿）：
    元素 = {}

    _echo（标记、元素、缩进=0）：
        标题 = 元素。获取标题()
        元素=元素。getID（）] = 标题
        打印（'t' = 缩进，标记， '：'，管道.报价（标题）))

    def dump_sheet（表）：
        root_topic = 工作表。获取根主题()
        _echo（"根主题"， root_topic， 1)

        root_topic 中的主题。获取子主题（）或*：
            _echo（"附加子主题"，主题，2)

        root_topic 中的主题。获取子主题（xmind）。核心。康斯特.TOPIC_DETACHED）或[]：
            _echo（"分离子主题"，主题，2)

        在工作表中为 rel。获取关系（）：
            id1， id2 = rel.getEnd1ID （），rel。获取 End2ID()
            打印（'关系： [%s] --> [%s] % （元素）。获取（id1），元素。获取（id2)))

    用于工作簿中的工作表。获取表（）：
        _echo（"表"，表）)
        dump_sheet（工作表）)


def dict_to_prettify_json（数据）：
    打印（json.转储（数据，缩进=4，分隔符=（'，' ， '：)))


除主（）：
    • 1、您可以将 xmind 文件转换为分写数据或 json 数据
    工作簿 = xmind。负载（"演示.xmind")
    打印（工作簿）。获取数据())
    打印（工作簿）。to_prettify_json())

    • 2、您还可以将工作表转换为分写数据
    工作表 = 工作簿。获取初级工作表()
    dict_to_prettify_json（工作表）。获取数据())

    • 3、以及主题
    root_topic = 工作表。获取根主题()
    dict_to_prettify_json（root_topic.获取数据())

    • 4、以及评论
    评论簿 = 工作簿。评论书
    打印（评论书）。获取数据())

    • 5、自定义提取所需数据
    custom_parse_xmind（工作簿）)


如果__name__ = "__main__"：
    主要()