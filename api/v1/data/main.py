#!/usr/bin/python3
"""states"""
from . import app_data
from flask import jsonify, abort, jsonify
from flask import request, Response
from models import storage
from models.accounts import account
from datetime import datetime
import json

def GetObject(clc, id):
    if id is not None:
        return storage.get(clc, int(id))
    if 'info' in request.json:
        info = request.json.get('info')
        objs = storage.getDict(clc, info)
        if objs:
            return objs[0]
    return None

@app_data.route('/gen/<clc>/', methods=['GET'])
@app_data.route('/gen/<clc>/<id>', methods=['GET'])
def get_object(clc=None, id=None):
    obj = GetObject(clc, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())

@app_data.route('/gen/<clc>/', methods=['DELETE'])
@app_data.route('/gen/<clc>/<id>', methods=['DELETE'])
def delete_object(clc=None, id=None):
    obj = GetObject(clc, id)
    if obj is None:
        abort(404)
    obj.delete()
    return {'status':"deletet complate"}, 200


@app_data.route('/gen/<clc>/', methods=['POST'])
def add_object(clc=None, id=None):
    
    if 'info' not in request.json:
        return {'status': 'no info to add'}, 400
    info = request.json.get('info')
    obj = storage.add(clc, info)
    if obj is None:
        return {'status': 'couldn\'t add object'}, 400
    obj.save()
    return {'status':"added complate"}, 200


@app_data.route('/gen/<clc>/', methods=['PUT'])
@app_data.route('/gen/<clc>/<id>', methods=['PUT'])
def edit_object(clc=None, id=None):
    obj = GetObject(clc, id)
    if obj is None:
        abort(404)
    if 'attach' not in request.json:
        return {'status': 'no attach to add'}, 400
    attach = request.json.get('attach')
    for key, val in attach.items():
        code = f"obj.{key}=attach[\'{key}\']"
        exec(code)

    storage.save()
    return {'status':"eddit complate"}, 200

@app_data.route('/gen/', methods=['GET'])
def rrr():
    '''main api data routing'''
    return ''
