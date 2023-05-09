import json
import requests
import jsonpath

json1 = '''{
    "error": "",
    "data": [
        {
            "pid": 82152381,
            "p": 0,
            "uid": 1549112,
            "title": "蓮華ちゃん～【本命】",
            "author": "K.Yuuka",
            "r18": false,
            "width": 1416,
            "height": 1447,
            "tags": [
                "美少女万華鏡",
                "美少女万华镜",
                "蓮華",
                "莲华",
                "制服",
                "uniform",
                "黒タイツ",
                "黑裤袜",
                "黒スト",
                "黑丝袜",
                "セーラー服",
                "水手服",
                "魅惑のふともも",
                "魅惑的大腿",
                "パンツ",
                "内裤",
                "蓮華(美少女万華鏡)"
            ],
            "ext": "jpg",
            "aiType": 0,
            "uploadDate": 1591502738000,
            "urls": {
                "original": "https://i.pixiv.re/img-original/img/2020/06/07/13/05/38/82152381_p0.jpg"
            }
        }
    ]
}'''
































page = json.loads(json1)
print(jsonpath.jsonpath(page["data"], "$..original")[0])


























