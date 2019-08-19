from pickle import load
from gensim.models.word2vec import Word2Vec
print('pleace wait a minute')
model = load(open('word2vec', 'rb'))
print('ready to input')
while True:
	positive = input('pleace input positive word if you wont) write with space  ').split()
	negative = input('pleace input negative word if you wont) write with space  ').split()
	if len(negative) and len(positive):
		out = model.wv.most_similar(positive=positive, negative=negative)
	elif len(positive):
		out = model.wv.most_similar(positive=positive)
	else:
		out = model.wv.most_similar(negative=negative)

	
	for o in out:
		print(o[0])