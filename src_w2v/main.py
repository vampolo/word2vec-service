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
        status=404
    )

@app.route('/words2vec', methods=['POST'])
async def words2vec(request):
    if 'words' not in request.json:
        return response.json({
            'message': 'Please provide array of words as body'
        }, status=422)

    words = request.json['words']

    res = {x: model[x] if x in model else None for x in words}

    return json(res)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
