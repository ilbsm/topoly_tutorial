#!/usr/bin/python3
import sys

from topoly_preprocess import chain_read
from topoly_preprocess import close_chain_2points

if __name__ == "__main__":
    # arg 1 - input file path
    # arg 2 - output file path
    print("Testing PY KnotFinder")
    chain, unable = chain_read('t31_numbered_cut.xyz'.encode('utf-8'))

    print("unable: " + str(unable))
    print(str(chain))

    res, chain_out = close_chain_2points(chain)
    print("close result: " + str(res))
    print(str(chain_out))
