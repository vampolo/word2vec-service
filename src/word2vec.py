import os
from gensim.models import KeyedVectors

# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
vector_file = os.getenv("VECTOR_FILE",
                        "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz")
binary = bool(os.getenv("BINARY_VECTOR_FILE", "true" if ".bin" in vector_file else "false").lower() == "true")

model = KeyedVectors.load_word2vec_format(
    vector_file,
    binary=binary)
