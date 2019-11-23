#!/usr/bin/python
import csv
import json
import pandas as pd
import numpy as np

def createDF(filepath):
  return pd.read_csv(filepath)

#convert categorical data to numerical
def categories_to_numbers(values):
  values.sort()
  replacements = {}
  for i in range(len(values)):
    replacements[vales[i]] = i
  return replacements

def process_data(df):
  labels = df.Label.unique()
  labels_replacements = categories_to_numbers(labels)
  df['Label'].replace(labels_replacements, inplace=True)
  
  dest_port = 

