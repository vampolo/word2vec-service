from gensim.models import Word2Vec

# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
model = Word2Vec.load_word2vec_format('/opt/data/GoogleNews-vectors-negative300.bin', binary=True, norm_only=True)

dog = model['dog']
print(dog.shape)
print(dog[:10])

# Deal with an out of dictionary word: Михаил (Michail)
if 'Михаил' in model:
    print(model['Михаил'].shape)
else:
    print('{0} is an out of dictionary word'.format('Михаил'))

# Some predefined functions that show content related information for given words
print(model.most_similar(positive=['woman', 'king'], negative=['man']))

print(model.doesnt_match("breakfast cereal dinner lunch".split()))

print(model.similarity('woman', 'man'))
