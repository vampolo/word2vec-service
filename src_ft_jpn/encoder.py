from sanic.response import json as sanic_json
import numpy

def is_iterable(x):
    try:
        iter(x)
        return True
    except TypeError:
        return False


def map_anything(x, fn):
    if isinstance(x, str):
        return fn(x)
    if isinstance(x, dict):
        return {k: map_anything(v, fn) for k, v in x.items()}
    if is_iterable(x):
        return [map_anything(ele, fn) for ele in x]
    return fn(x)


def prepare_for_json(val):
    if isinstance(val, numpy.int32):
        return int(val)
    if isinstance(val, numpy.int64):
        return int(val)
    if isinstance(val, numpy.number):
        return str(val)
    if isinstance(val, numpy.ndarray):
        return [str(v) for v in val]
    return val


def json(data, **kwargs):
    # cls not supported by ujson
    # https://github.com/esnme/ultrajson/issues/124
    return sanic_json(map_anything(data, prepare_for_json), **kwargs)
