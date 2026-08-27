from html.parser import HTMLParser

class V(HTMLParser):
    def __init__(s):
        super().__init__()
        s.void = {'meta','img','br','hr','link','area','base','col','embed','source','track','wbr'}
        s.stack = []
        s.errors = []
    def handle_starttag(s, t, a):
        if t not in s.void:
            s.stack.append(t)
    def handle_endtag(s, t):
        if t in s.void:
            return
        if s.stack and s.stack[-1] == t:
            s.stack.pop()
        else:
            s.errors.append('mismatched </%s>' % t)

data = open(r'C:\Users\admin\Desktop\web\index.html', encoding='utf-8').read()
p = V()
p.feed(data)

print('Unclosed tags:', p.stack)
print('Errors:', p.errors)
print('DOCTYPE ok:', data.lstrip().lower().startswith('<!doctype html>'))
print('Has <head>:', '<head>' in data)
print('Has <body>:', '<body>' in data)
print('h1 count:', data.count('<h1'))
print('main count:', data.count('<main'))
print('semantic tags (header/section/footer/main):',
      data.count('<header') + data.count('<section') + data.count('<footer') + data.count('<main'))
print('li count:', data.count('<li>'))
print('img count:', data.count('<img'))
print('external link:', 'href="https://www.vietnam.travel' in data)
