# coding=utf-8
"""JSON数据
JavaScript Object Notation
已经成为通过HTTP请求在Web浏览器和其他应用程序之间发送数据的标准格式之一
"""
import numpy as np
import pandas as pd
import json
obj = """
{"name":"Wes",
"place_lived":["United State", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age":25, "pet": "Zuko"},
                {"name": "Katie", "age":33, "pet": "Cisco"}]
}
"""

"对象中所有的键都必须是字符串"
"通过json.loads可以将JSON字符串转为Python格式"
result = json.loads(obj)
print(result)
"json.dumps 将python对象转为JSON格式"
asjson = json.dumps(result)
print(asjson)
