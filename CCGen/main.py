import argparse
import re
import random
from typing import Generator
import os

def cc_number_generator(cc: str, length=15)->Generator:
    cc=''.join(re.findall('[0-9x]+', cc.lower()))[:length]
    cc+='x'*(length-cc.__len__())
    x = list(re.finditer('x', cc))
    for rg in range(int('1'+'0'*x.__len__())):
        y=list(rg.__str__().zfill(x.__len__()))
        cc_tmp = list(cc)
        for s,w in zip(x, y):
            cc_tmp[s.span()[0]] = w
        yield ''.join(cc_tmp)

def cc_number_random_generator(cc: str, length=15)->Generator:
    cc_= list(cc_number_generator(cc,length=length))
    yield from random.sample(cc_,cc_.__len__())

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('--random', action=argparse.BooleanOptionalAction)
    arg.add_argument('--cc', type=str)
    arg.add_argument('--length', type=int, default=15)
    parser = arg.parse_args()
    if parser.cc:
        if parser.random:
            for i in cc_number_generator(parser.cc, parser.length):
                print(i)
        else:
            for i in cc_number_generator(parser.cc, parser.length):
                print(i)
    else:
        os.system(f'python3 {__file__} --help')