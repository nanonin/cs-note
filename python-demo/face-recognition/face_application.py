# *-* coding=utf-8 *-*

import base64
import tempfile

from flask import Flask, request
from face_service import *


"""
人脸识别WebService

"""


app = Flask(__name__)


# 获取图片中人脸数量
@app.route('/face_num', methods=['GET', 'POST'])
def face_num():
    # 判断请求类型
    if request.method == 'POST':

        if "file_date" in request.form:
            if request.form['file_date']:
                image_data = request.form['file_date']
                temp = tempfile.TemporaryFile()
                image_bytes = base64.b64decode(image_data)
                temp.write(image_bytes)
                return str(get_faces_num(temp))

    return 0


# 获取图片中人脸坐标
@app.route('/point', methods=['GET', 'POST'])
def face_point():
    # 判断请求类型
    if request.method == 'POST':

        if "file_date" in request.form:
            if request.form['file_date']:
                image_data = request.form['file_date']
                temp = tempfile.TemporaryFile()
                image_bytes = base64.b64decode(image_data)
                temp.write(image_bytes)
                return get_faces_points(temp)
        elif request.data:  # test
            image_data = request.data
            # image_data = image_data.replace("'","").replace(" ","")
            # 
            image_bytes = base64.b64decode(image_data)
            image_save = open("temp.jpg", "wb")
            image_save.write(image_bytes)
            image_save.close()

            temp = tempfile.TemporaryFile()
            image_bytes = base64.b64decode(image_data)
            temp.write(image_bytes)
            return get_faces_points(temp)
    return ""


# 获取人脸68个特征点
@app.route('/landmark', methods=['GET', 'POST'])
def face_landmark():
    # 判断请求类型
    if request.method == 'POST':

        if "file_date" in request.form:
            if request.form['file_date']:
                image_data = request.form['file_date']
                temp = tempfile.TemporaryFile()
                image_bytes = base64.b64decode(image_data)
                temp.write(image_bytes)
                return get_face_landmark(temp)

    return ""


# 获取人脸128维嵌入向量
@app.route('/encode', methods=['GET', 'POST'])
def face_encode():
    # 判断请求类型
    if request.method == 'POST':
        if "file_date" in request.form:
            if request.form['file_date']:
                image_data = request.form['file_date']
                temp = tempfile.TemporaryFile()
                image_bytes = base64.b64decode(image_data)
                temp.write(image_bytes)
                # save_local(image_bytes)
                return get_face_encode(temp)

    return ""


# 比较人脸相似度 两张图片的base64编码
@app.route('/compare', methods=['GET', 'POST'])
def face_compare():
    # 判断请求类型
    if request.method == 'POST':

        if "file_data1" in request.form and "file_data2" in request.form:
            if request.form["file_data1"] and request.form["file_data2"]:
                image_data1 = request.form['file_data1']
                image_data2 = request.form['file_data2']
                temp1 = tempfile.TemporaryFile()
                temp2 = tempfile.TemporaryFile()
                temp1.write(base64.b64decode(image_data1))
                temp2.write(base64.b64decode(image_data2))
                return get_face_sim(temp1, temp2)

    return ""


# 获取与已知人脸集的相似度比较结果集合
@app.route('/find', methods=['GET', 'POST'])
def face_compare_muti():
    # 判断请求类型
    if request.method == 'POST':

        if "uknown_data" in request.form and "known_encodes" in request.form:
            if request.form["uknown_data"] and request.form["known_encodes"]:
                image_data = request.form['uknown_data']
                knownencodes = request.form['known_encodes']
                temp1 = tempfile.TemporaryFile()
                temp1.write(base64.b64decode(image_data))
                return get_face_sims(temp1, knownencodes)

    return ""

# @app.route('/index', methods=['GET', 'POST'])
# def indexxxxxx():
#     return render_template("index.html")

# nouse
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False,threaded=True)
