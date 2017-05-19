# coding=utf-8
"""
 TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

 Design the encode and decode methods for the TinyURL service.
 There is no restriction on how your encode/decode algorithm should work.
 You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
 设计URL和tiny URL的编解码算法
"""


# class Codec:
    # def __init__(self):
    #     self.urls = []
    #
    # def encode(self, longUrl):
    #     self.urls.append(longUrl)
    #     #通过自增的urls列表的序号进行编码
    #     return 'http://tinyurl.com/' + str(len(self.urls) - 1)
    #
    # def decode(self, shortUrl):
    #     return self.urls[int(shortUrl.split('/')[-1])]
    #



import random
import string
class Codec:
    """
    使用随机数优化上面的纯整数表示，只用6位code
    """
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))