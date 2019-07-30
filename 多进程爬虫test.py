from multiprocessing import Process, Queue

import time
import re
import requests
import os


class DouBanSpider(Process):
    def __init__(self, url, q):
        # 重写写父类的__init__方法
        super(DouBanSpider, self).__init__()
        self.url = url
        self.q = q
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/top250?start=225&filter=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        }
        # self.namee=str(os.getpid())

    def run(self):
        self.parse_page()

    def send_request(self, url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print(u"[INFO]请求url:" + url,time.time())
                time.sleep(0.3)
                return requests.get(url=url, headers=self.headers).content
            except Exception as e:
                print(u'[INFO] %s%s' % (e, url))
                i += 1

    def parse_page(self):

        response = self.send_request(self.url)
        p = re.compile(
            r'<div class="hd">.*?<a href="https://movie.douban.com/subject/(.*?)/"',
            re.S | re.M)
        q = re.findall(p, response)
        for mid in q:
            inner_url='https://movie.douban.com/subject/{}/'.format(mid)
            self.parse_detill(inner_url)
    def parse_detil(self,url):
        response = self.send_request(url)




def main():
    # 创建一个队列用来保存进程获取到的数据
    q = Queue()
    base_url = 'https://movie.douban.com/top250?start={}'
    # 构造所有ｕｒｌ
    url_list = [base_url.format(num)for num in range(0, 225 + 1, 25)]

    # 保存进程
    Process_list = []
    # 创建并启动进程
    for url in url_list:
        p = DouBanSpider(url, q)
        p.start()
        Process_list.append(p)
    print(Process_list)
    # 让主进程等待子进程执行完成
    for i in Process_list:
        i.join()

    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))