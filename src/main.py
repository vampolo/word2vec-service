from sanic import Sanic
from sanic.response import json
from word2vec import model

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/word2vec")
async def word2vec(request):
    return json(model['dog'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
