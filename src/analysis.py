#!/usr/bin/env python
# -*- coding: utf-8 -*-
from newspaper import Article
import newspaper
import os
import numpy as np
import re
import nltk
from textblob import TextBlob
from kitchen.text.converters import getwriter, to_bytes, to_unicode

#for model
import pickle

model_filename = 'finalized_model.sav'

def get_article(url):
	'''make article object
	url: the url of the news article'''
	a = Article(url)
	a.download()
	a.parse()
	# parse out weird chars
	text = ''.join(re.sub('[£—""…\n\"%]', ' ', a.text))
	title = re.sub('[£—""…\n\"%]', ' ',a.title.strip())

	#convert to bytes for text_blob. loses some data potentially, but same process as in training
	text = to_bytes(text, 'utf-8')
	title = to_bytes(title, 'utf-8')

	print(title,text)
	return title,text

def count_char(x):
	'''
	returns number of capital letters
	x: string
	'''
	if isinstance(x,int):
		x = str(x)
	if isinstance(x,float):
		x = str(x)
	return sum(1 for c in x if c.isupper())

def analyze_article(url):

	title,text = get_article(url)

	# prepare the vector
	tb = TextBlob(text.decode('utf-8'))
	test_x = np.array([tb.sentiment.polarity,tb.sentiment[1],len(text),count_char(title)])
	test_x = test_x.reshape(1, -1) 
	print test_x

	result = np.array([0])
	# load the model from disk
	# loaded_model = pickle.load(open(model_filename, 'rb'))
	# result = loaded_model.score(test_x)
	# print(result)
	#test_pred = model.predict(test_x)

	return({'text':text,'title':title,'prediction':result[0]})

if __name__ == '__main__':

	with open('test_urls.txt', 'rb') as f:
		urls = f.readlines()

	for url in urls:
		analyze_article(url)