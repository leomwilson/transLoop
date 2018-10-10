import requests
import json
import random

# u is this URL to get. This does NOT include params (e.g. ?foo=bar)
# p is the URL params (e.g. ?foo=bar)
def getJSON(u = 'leomerch.net', p = {}):
    return requests.get(url = u, params = p).json()
def r(fname):
    f = open(fname, 'r')
    co = f.read()
    f.close()
    return co
def w(fname, co):
    f = open(fname, "w")
    f.write(co)
    f.close()
def getLang(langs, prev):
    l = random.choice(langs)
    if(l == prev):
        l = getLang(langs, prev)
    return l;
def genPath(langs, len, start, end):
    p = start;
    for i in range(1, len-2):
        p += '\n' + random.choice(langs)
    p += '\n' + end
def t(f, t, s):
    return getJSON(u = 'https://translate.googleapis.com/translate_a/single', p = {'client':'gtx', 'sl':f, 'tl':t, 'dt':'t', 'q':s})[0][0][0]

cfg = json.loads(r('res/cfg.json')) # change the file path if something else is used
txt = r(cfg['input'])
c = cfg['startingLang']
