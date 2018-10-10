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
    if l == prev:
        l = getLang(langs, prev)
    return l
def genPath(langs, len, start, end):
    p = start
    prev = start
    for i in range(1, len-2):
        nxt = getLang(langs, prev)
        p += '\n' + nxt
        prev = nxt
    p += '\n' + end
    return p
def t(f, t, s):
    return getJSON(u = 'https://translate.googleapis.com/translate_a/single', p = {'client':'gtx', 'sl':f, 'tl':t, 'dt':'t', 'q':s})[0][0][0]
def follow(path, txt):
    path = path.split('\n')
    prev = path[0]
    for i in range(1, len(path)):
        txt = t(prev, path[i], txt)
        prev = path[i]
def loadCFG(fname):
    return json.loads(r(fname))
def transLoop(cfg):
    txt = r(cfg['input'])

    if cfg['useDefinedPathIfAvail'] and r(cfg['path']) != '':
        w(cfg['output'], follow(r(cfg['path']), txt))
    else:
        path = genPath(r(cfg['genPath']['langs']).split(','), cfg['genPath']['length'], cfg['genPath']['start'], cfg['genPath']['end'])
        w(cfg['path'], path)
        w(cfg['output'], follow(path, txt))

def main():
    cfg = loadCFG('res/cfg.json') # change the file path if something else is used
    if cfg['mode'] == 'transLoop':
        transLoop(cfg)
    elif cfg['mode'] == 'genPath':
        w(cfg['path'], genPath(r(cfg['genPath']['langs']).split(','), cfg['genPath']['length'], cfg['genPath']['start'], cfg['genPath']['end']))
    else:
        print('[ERROR] Invalid mode')

if __name__ == '__main__':
    main()
