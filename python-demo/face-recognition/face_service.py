# *-* coding=utf-8 *-*
import json
import face_api
# import datetime
# import random

"""
人脸识别service
"""


def get_faces_points(file_stream, hog=True):
    """获取人脸位置"""

    # 图片读取
    image = face_api.load_image_file(file_stream)
    if hog:
        # 使用这种方法相当快速，但不如CNN模型准确，也不能GPU加速。
        face_locations = face_api.face_locations(image)
        return json.dumps(face_locations)
    else:
        # 使用深度学习，CNN模型，更准确，可用GPU加速。
        face_locations = face_api.face_locations(
            image, number_of_times_to_upsample=0, model="cnn"
        )
        return json.dumps(face_locations)


def get_faces_num(file_stream):
    """获取图片中人脸数量"""

    # 图片读取
    image = face_api.load_image_file(file_stream)
    # 使用这种方法相当快速，但不如CNN模型准确，也不能GPU加速。
    face_locations = face_api.face_locations(image)
    # 使用深度学习，CNN模型，更准确，可用GPU加速。
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    return len(face_locations)


def get_face_landmark(file_stream):
    """获取人脸68特征点"""

    # 图片读取
    image = face_api.load_image_file(file_stream)
    face_landmarks = face_api.face_landmarks(image)

    return json.dumps(face_landmarks)


def get_face_encode(file_stream):
    """获取人脸128维嵌入编码"""

    # 图片读取
    image = face_api.load_image_file(file_stream)
    encode = face_api.face_encodings(image, num_jitters=5)
    result = []
    if len(encode) == 0:
        return []
    for i in encode[0]:
        result.append(float(i))
    result = json.dumps(result)
    return result


def get_face_sim(file_stream1, file_stream2):
    """获取人脸相似度"""

    # 图片读取
    image1 = face_api.load_image_file(file_stream1)
    image2 = face_api.load_image_file(file_stream2)
    unknown_face_encode = face_api.face_encodings(image1, num_jitters=3)[0]
    know_face_encode = face_api.face_encodings(image2, num_jitters=3)[0]
    known_faces = [know_face_encode]

    face_distances = face_api.face_distance(known_faces, unknown_face_encode)
    results = ""
    for face_distance in face_distances:
        results = "{:.4}".format(face_distance)

    # results = json.dumps(results)
    return results


def get_face_sims(file_stream, known_encode):
    """ 获取与已知人脸集比较的相似度集合 """

    # Load the uploaded image file
    unknown_image = face_api.load_image_file(file_stream)
    # 提取特征向量
    unknown_face_encode = face_api.face_encodings(unknown_image)[0]
    # 读取已保存的面部模板
    know_face_encode = json.loads(known_encode)
    # 计算相似度
    distances = face_api.face_distance(know_face_encode, unknown_face_encode)
    sims = ""
    for distance in distances:
        sims = sims + "{:.4}".format(distance) + ","

    return sims


# # 保存图片到本地
# def _save_local(image_data):
#     image_save = open("static/save_img/" + create_uuid() + '.jpg', 'wb')
#     image_save.write(image_data)
#     image_save.close()


# 保存 人名:编码
def face_regist(file_stream, name, encode_file_name):
    # Load the uploaded image file
    image = face_api.load_image_file(file_stream)
    encode = face_api.face_encodings(image, None)
    if len(encode) == 0:
        return
    result = []
    for i in encode[0]:
        result.append(str(i))

    new_dict = {name: result}

    json_str = json.dumps(new_dict, ensure_ascii=False)
    file = open(encode_file_name, "a", encoding="utf-8")
    file.write(json_str + "\n")
    file.close()
