#!/usr/bin/python
import csv
import json
import pandas as pd
import numpy as np
import argparse
from common import preprocess_data

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--infile")
parser.add_argument("--outfile")
args = parser.parse_args()

df = preprocess_data.createDF(args.infile)
#print help(df)
print df.dtypes

