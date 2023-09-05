import requests
import time
import hashlib
import json
import pandas as pd

# 获取查询企业列表
df = pd.read_excel('路径/文件名.xlsx')
column_data = df['列名'].tolist()

#  请求参数
appKey = "appKey"
secretKey = "secretKey"
encode = 'utf-8'

# Http请求头设置
timespan = str(int(time.time()))
token = appKey + timespan + secretKey;
hl = hashlib.md5()
hl.update(token.encode(encoding=encode))
token = hl.hexdigest().upper();
print('MD5加密后为 ：' + token)

#设置请求Url-请自行设置Url
reqInterNme = "http://api.qichacha.com/XXXXXX"
paramStr = "keyword=企查查科技有限公司"
url = reqInterNme + "?key=" + appKey + "&" + paramStr;
headers={'Token': token,'Timespan':timespan}
response = requests.get(url, headers=headers)

#结果返回处理
print(response.status_code)
resultJson = json.dumps(str(response.content, encoding = encode))
# convert unicode to chinese
resultJson = resultJson.encode(encode).decode("unicode-escape")
print(resultJson)