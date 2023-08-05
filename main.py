import os
import pandas as pd
import numpy as np
import torch


def main():
    sd = pd.Series([1,2,3])
    print(sd)

def test(*args):
    for i in args:
        print(i)

if __name__ == "__main__":
    main()
