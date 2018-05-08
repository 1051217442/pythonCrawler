# -*- coding: UTF-8 -*-
import sys
import urllib
from imp import reload
from urllib import request

import requests

reload(sys)


if __name__ == "__main__":
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://106.15.80.147/index/recommend?sign=72dbec855931194323b61794f8b93677'
    kw = urllib.parse.quote("推荐")
    data = '{"auto":0,"c_types":[1,3,2,8,7,9],"direction":"homebutton","filter":"all","tab":"推荐","h_av":"4.2.2","h_dt":0,"h_os":24,"h_app":"zuiyou","h_model":"BAC-AL00","h_did":"864751033676464_c8:14:51","h_nt":1,"h_m":44001363,"h_ch":"huawei","h_ts":1525760871550,"token":"TcK0N7n8Bckk5AWoX_jIyhC_Q13KPfr626wazTU27RocuinKYCp73mK368VZusoxppAiO","android_id":"774a1f67980eb21d"}'

    head = {}
    # 写入User Agent信息

    headers = {'Request-Type': 'text/json', 'ZYP': 'mid=44001650', 'Host': '106.15.82.26', 'Content-Type': 'text/plain; charset=utf-8',
               'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.8.1'}
    # # 创建Request对象
    # req = request.Request(url, headers=head, data=data)
    # # 传入创建好的Request对象
    # response = request.urlopen(req)
    # #读取响应信息并解码
    # html = response.read().decode('utf-8')
    # data = {"auto":0,"c_types":[1,3,2,8,7,9],"direction":"homebutton","filter":"all","tab":"推荐","h_av":"4.2.2","h_dt":0,"h_os":24,"h_app":"zuiyou","h_model":"BAC-AL00","h_did":"864751033676464_c8:14:51","h_nt":1,"h_m":44001650,"h_ch":"huawei","h_ts":1525749575934,"token":"TeK2N2ZdUU9beCnEu-HgbK-YPMPsW1AbheZVkD4fOBHYU8-nHCmy0inTBBIn7wvbs1L__","android_id":"774a1f67980eb21d"}

    req = requests.post(url=url, headers=headers, data=data.encode("utf-8")).json()
    # 打印信息
    print(req)

