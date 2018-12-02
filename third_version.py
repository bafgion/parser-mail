#!/usr/bin/env python
#-*- coding:utf-8 -*-
import gzip, re
from collections import Counter

sp = []
di = {}

class gzopen(gzip.GzipFile):  # создаём класс для работы с gzip-файлами
    def __enter__(self):
        if self.fileobj is None:
            raise ValueError("I/O operation on closed GzipFile object")
        return self

    def __exit__(self, *args):
        self.close()


class regular:
    @staticmethod
    def mail_to(line):
        line = str(line)
        global sp
        test = re.search(r':+\s+\w+: ', line)
        from_login = re.search(r'from=<?\w+@\w+.\w+>', line)
        if from_login and test:
            test = re.sub(r': ', r'', test[0])
            from_login = re.sub(r'from=', r'', from_login[0])
            sp.append(from_login)
            return sp

class parser:
    def test(self):
        with gzopen('maillog.gz') as file:
            for line in file:
                from_login = regular.mail_to(line)
            from_login = Counter(from_login)
            from_login = dict(from_login)
            print(from_login)
        return from_login


class output_info:# отправитель | ошибок | доставленных
    def __init__(self):
        print("""\t\t\t\t\t\t  Сводная таблица
        --------------------------------------------------\n
        |               |                |                \t|\n
        |  Отправитель\t| Кол сообщений\t|  Кол-во ошибок\t |\n
        |               |                |                \t|\n
        --------------------------------------------------\n""")

    def table_info(self):
        from_login = parser().test()
        for key in from_login:
            print("""
            |               |               |                |\n
            |%s\t|%d\t|0|\n
            |               |               |                |\n
            --------------------------------------------------\n""" % (key, from_login[key]))

output_info().table_info()

"""
def garp(line):
    line = str(line)
    global sp
    test = re.search(r':+\s+\w+: ', line)
    from_login = re.search(r'from=<?\w+@\w+.\w+>', line)
    if from_login and test:
        test = re.sub(r': ', r'', test[0])
        from_login = re.sub(r'from=', r'', from_login[0])
        sp.append(from_login)
        return sp

def garpe(line):
    line = str(line)
    global di
    test = re.search(r':+\s+\w+: ', line)
    from_login = re.search(r'from=<?\w+@\w+.\w+>', line)
    if from_login and test:
        test = re.sub(r': ', r'', test[0])
        from_login = re.sub(r'from=', r'', from_login[0])
        di['%s' % from_login] = test
        return di

gl = []
def error_mes(sl, pr, line): # собираю ошибки и вывожу их e-mail ошибок
    for key in sl:
        for keys in pr:
            if re.match(r'[2-3]{2}[1-3]{3}', str(line)) and key == keys:
                g = re.search(r'status=\w+\S\b', str(line))
                g = re.sub(r'status=', r'', a[0])
                print(g)
                if g != 'sent':
                    gl.append(key)
    return gl

with gzopen('maillog.gz') as file:
    for line in file:
        a = garp(line)
        b = garpe(line)
    a = Counter(a)
    a = dict(a)
"""