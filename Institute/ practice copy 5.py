from typing import Required
import argparse

par = argparse.ArgumentParser()
par.add_argument("--name",required = True)
par.add_argument("--age",required = True)
par.add_argument("--grade",required = True)
args = par.parse_args()
print(args.name,args.age,args.grade)