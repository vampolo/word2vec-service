from gensim.models import KeyedVectors

# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
model = KeyedVectors.load_word2vec_format('/opt/data/GoogleNews-vectors-negative300.bin', binary=True)
