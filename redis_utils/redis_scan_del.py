# encoding: utf-8


"""


@author: tongzhenguo


@time: 2019/1/24 下午9:56


@desc:


"""

import redis


def mcleardb(mhost,mport, mpassword,mdb):
    r = redis.StrictRedis(host=mhost, port=mport, db=mdb, password=mpassword)
    for key in r.scan_iter("*"):
        r.delete(key)

if __name__ == '__main__':
    pass