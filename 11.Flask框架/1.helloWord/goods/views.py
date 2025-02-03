from flask import Flask, request, jsonify, make_response, render_template, abort
from . import goods_bp
@goods_bp.route('/')
def goods_profile():
    return 'goods_profile'


@goods_bp.route('/index', methods=['GET'])
def goods_template():
    return render_template('index.html', my_str='mstr', my_int='mint')

@goods_bp.route('/info', methods=['POST'])
def goods_info():
    btitle = request.args.get('btitle')
    resp = make_response(jsonify({
        btitle: btitle
    }))
    resp.headers["test"] = "Python"
    resp.set_cookie("test", "test01")
    resp.status = "404not found"
    abort(500)
    return resp


@goods_bp.route('/upload', methods=['POST'])
def goods_upload():
    file = request.files.get('file')
    print(file, 'file')
    return {}
