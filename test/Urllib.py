import urllib.parse


def parse(word):
    return urllib.parse.quote(word)


print(urllib.parse.urlencode({'你好': 'ok'}))
print(parse("你好"))

