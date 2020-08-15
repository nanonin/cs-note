# -*- coding: utf-8 -*-

import PIL.Image as pilImage
import dlib
import numpy

import dlib_models


face_detector = dlib.get_frontal_face_detector()

predictor_68_point_model = dlib_models.pose_predictor_model_location()
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

predictor_5_point_model = dlib_models.pose_predictor_five_point_model_location()
pose_predictor_5_point = dlib.shape_predictor(predictor_5_point_model)

cnn_face_detection_model = dlib_models.cnn_face_detector_model_location()
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)

face_recognition_model = dlib_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


# face_aligner = opface.AlignDlib(predictor_68_point_model)


def _rect_to_css(rect):
    """
    Convert a dlib 'rect' object to a plain tuple in (top, right, bottom, left) order

    :param rect: a dlib 'rect' object
    :return: a plain tuple representation of the rect in (top, right, bottom, left) order
    """
    return rect.top(), rect.right(), rect.bottom(), rect.left()


def _css_to_rect(css):
    """
    Convert a tuple in (top, right, bottom, left) order to a dlib `rect` object

    :param css:  plain tuple representation of the rect in (top, right, bottom, left) order
    :return: a dlib `rect` object
    """
    return dlib.rectangle(css[3], css[0], css[1], css[2])


def _trim_css_to_bounds(css, image_shape):
    """
    Make sure a tuple in (top, right, bottom, left) order is within the bounds of the image.

    :param css:  plain tuple representation of the rect in (top, right, bottom, left) order
    :param image_shape: numpy shape of the image array
    :return: a trimmed plain tuple representation of the rect in (top, right, bottom, left) order
    """
    return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)


def face_distance(faces, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.

    :param faces: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A numpy ndarray with the distance for each face in the same order as the 'faces' array
    """
    if len(faces) == 0:
        return numpy.empty(0)

    return numpy.linalg.norm(faces - face_to_compare, axis=1)


def load_image_file(file, mode='RGB'):
    """
    载入图片 Loads an image file (.jpg, .png, etc) into a numpy array

    :param file: 文件名或文件流
    :param mode: 格式转化 RGB | L（黑白）
    :return: image contents as numpy array
    """
    im = pilImage.open(file)
    if mode:
        im = im.convert(mode)
    return numpy.array(im)


def _raw_face_locations(img, number_of_times_to_upsample=1, model="hog"):
    """
    Returns an array of bounding boxes of human faces in a image

    :param img: An image (as a numpy array)
    :param number_of_times_to_upsample: How many times to upsample the image looking for faces.
      Higher numbers find smaller faces.
    :param model: Which face detection model to use. "hog" is less accurate but faster on CPUs. "cnn" is a more accurate
                  deep-learning model which is GPU/CUDA accelerated (if available). The default is "hog".
    :return: A list of dlib 'rect' objects of found face locations
    """
    if model == "cnn":
        return cnn_face_detector(img, number_of_times_to_upsample)
    else:
        return face_detector(img, number_of_times_to_upsample)


def face_locations(img, number_of_times_to_upsample=1, model="hog"):
    """
    返回使用面部识别器识别的面部坐标

    :param img: 面部图片(as a numpy array)
    :param number_of_times_to_upsample: 数字越高，可找到越小的脸
    :param model: 使用模式 "hog" 更快速 "cnn" 可GPU/CUDA加速，使用神经网络更加精确
    :return: （顶部、左侧、底部、右侧） 以右上为0坐标
    """
    if model == "cnn":
        return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in
                _raw_face_locations(img, number_of_times_to_upsample, "cnn")]
    else:
        return [_trim_css_to_bounds(_rect_to_css(face), img.shape) for face in
                _raw_face_locations(img, number_of_times_to_upsample, model)]


def _raw_face_locations_batched(images, number_of_times_to_upsample=1, batch_size=128):
    """
    返回使用面部识别器识别的面部坐标

    :param images: 面部图片(as a numpy array)
    :param number_of_times_to_upsample: 数字越高，可找到越小的脸
    :return: （顶部、右侧、底部、左侧）
    """
    return cnn_face_detector(images, number_of_times_to_upsample, batch_size=batch_size)


def batch_face_locations(images, number_of_times_to_upsample=1, batch_size=128):
    """
    批处理 返回使用cnn面部识别器识别的面部坐标
    可GPU加速，GPU可以同时处理批量图像。如果不使用GPU不要用这个函数

    :param images:面部图片(as a numpy array)
    :param number_of_times_to_upsample: 数字越高，可找到越小的脸
    :param batch_size: 在每个GPU处理批次中包含多少图像
    :return: （顶部、右侧、底部、左侧）中的面部特征点位置
    """

    def convert_cnn_detections_to_css(detections):
        return [_trim_css_to_bounds(_rect_to_css(face.rect), images[0].shape) for face in detections]

    raw_detections_batched = _raw_face_locations_batched(images, number_of_times_to_upsample, batch_size)

    return list(map(convert_cnn_detections_to_css, raw_detections_batched))


def _raw_face_landmarks(face_image, faces_locations=None, model="large"):
    if faces_locations is None:
        faces_locations = _raw_face_locations(face_image)
    else:
        faces_locations = [_css_to_rect(face_location) for face_location in faces_locations]

    # 模式 small（5个） 或 large（68个）
    pose_predictor = pose_predictor_68_point
    if model == "small":
        pose_predictor = pose_predictor_5_point

    return [pose_predictor(face_image, face_location) for face_location in faces_locations]


def face_landmarks(face_image, faces_locations=None, model="large"):
    """
    返回图像中每个面部的特征点位置（眼睛、鼻子等）的.

    :param face_image: 图片
    :param faces_locations: 面部位置
    :param model: 模式 large（默认）或 small（只返回5点，但速度更快）
    :return: 面部的特征点位置
    """
    landmarks = _raw_face_landmarks(face_image, faces_locations, model)
    landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

    # For a definition of each point index, see https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png
    if model == 'large':
        return [{
            "chin": points[0:17],
            "left_eyebrow": points[17:22],
            "right_eyebrow": points[22:27],
            "nose_bridge": points[27:31],
            "nose_tip": points[31:36],
            "left_eye": points[36:42],
            "right_eye": points[42:48],
            "top_lip": points[48:55] + [points[64]] + [points[63]] + [points[62]] + [points[61]] + [points[60]],
            "bottom_lip": points[54:60] + [points[48]] + [points[60]] + [points[67]] + [points[66]] + [points[65]] + [
                points[64]]
        } for points in landmarks_as_tuples]
    elif model == 'small':
        return [{
            "nose_tip": [points[4]],
            "left_eye": points[2:4],
            "right_eye": points[0:2],
        } for points in landmarks_as_tuples]
    else:
        raise ValueError("Invalid landmarks model type. Supported models are ['small', 'large'].")


def face_encodings(face_image, known_face_locations=None, num_jitters=3):
    """
    返回面部图片的128维编码

    :param face_image: 面部图片（至少一个面部）
    :param known_face_locations: 面部位置
    :param num_jitters: 重采样次数
    :return: A list of 128-dimensional face encodings (one for each face in the image)
    """
    # TODO align

    raw_landmarks = _raw_face_landmarks(face_image, known_face_locations)
    return [numpy.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for
            raw_landmark_set in raw_landmarks]


def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    """
    将已知面部编码与未知编码进行比较，以查看它们是否匹配。

    :param known_face_encodings: 已知面部编码列表
    :param face_encoding_to_check: 未知面部编码
    :param tolerance: 阈值
    :return: 结果集（true|false）
    """
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)
