from sanic import Sanic
from sanic.exceptions import abort
from sanic import response
from encoder import json

from word2vec import model

app = Sanic()

# model = {
#     'dog': 'cat',
#     'bacon': 'prosciutto'
# }

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/word2vec")
async def word2vec(request):
    word = request.args['word'][0]

    if word in model:
        return json({ 'data': model[word] })

    return response.json(
        {'message': '404 Not Found'},
        status=200
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
