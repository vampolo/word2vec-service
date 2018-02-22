from sanic import Sanic
from sanic.exceptions import abort
from sanic import response
from encoder import json

from fasttext_vecs import model

# LOAD FT HERE
app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/ft_jpn_vec")
async def ft_jpn_vec(request):
    word = request.args['word'][0]

    if word in model:
        return json({ 'data': model[word] })

    return response.json(
        {'message': '404 Not Found'},
        status=404
    )

# CHANGE ROUTE
@app.route('/ft_jpn_vec_list', methods=['POST'])
async def ft_jpn_vec_list(request):
    if 'words' not in request.json:
        return response.json({
            'message': 'Please provide array of words as body'
        }, status=422)

    words = request.json['words']

    res = {x: model[x] if x in model else None for x in words}

    return json(res)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
