# Word2Vec as a service [![Build Status](https://travis-ci.org/vampolo/word2vec-service.svg?branch=master)](https://travis-ci.org/vampolo/word2vec-service)

# Why this project ?

Word2Vec is a popular model family used in datascience. To be meaningful, it requires a model of millions of words. Loading those models in a normal laptop can take a hit on ram usage.
Why not providing a word2vec implementation trained on the [ GoogleNews-vectors-negative300 ](https://code.google.com/archive/p/word2vec/) dataset as a service ?
Just hit the `/word2vec?word=something` of this service ad you will get your word vector

# Run it

```
docker pull vampolo/word2vec-service
docker run -P vampolo/word2vec-service
```

Go to http://localhost:8000/word2vec?word=something and you will get the array of the word you selected.

## Docker Compose

Since building this project takes quite a bit of time and resources, you can leverage `docker-compose` to dowload published image

```
docker-compose pull
docker-compose up
```

Then go to http://localhost:8000/word2vec?word=something and you will get the array of the word you selected.
