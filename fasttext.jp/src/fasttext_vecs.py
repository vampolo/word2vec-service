from gensim.models import KeyedVectors

# Load the word2vec format FasstText model
model = KeyedVectors.load_word2vec_format('/opt/data/wiki.ja.vec',binary=False)
