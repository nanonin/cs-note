# -*- coding: utf-8 -*-

"""
dlib模型
下载链接
http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2

"""

basepath = "./"

# from pkg_resources import resource_filename

def pose_predictor_model_location():
    return basepath+"models/shape_predictor_68_face_landmarks.dat"

def pose_predictor_five_point_model_location():
    return basepath+"models/shape_predictor_5_face_landmarks.dat"

def face_recognition_model_location():
    return basepath+"models/dlib_face_recognition_resnet_model_v1.dat"

def cnn_face_detector_model_location():
    return basepath+"models/mmod_human_face_detector.dat"

