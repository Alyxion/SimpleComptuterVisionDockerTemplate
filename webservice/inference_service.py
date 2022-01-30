from flask import Blueprint, jsonify, request, Response
from common import *
import numpy as np
import traceback
import redis
import logging
import io
import imghdr
import cv2

REDIS_HOST = "yourredis"
logger = logging.getLogger()


class ClassificationService(Blueprint):
    """
    Provides services to classify an image
    """

    def __init__(self):
        """
        Initializer
        """
        super().__init__('ClassificationService', __name__)
        self.redis_server = self.connect_to_redis()

    def connect_to_redis(self):
        """
        Connects the worker to redis
        """
        logger.info("Connecting to REDIS")
        try:
            redis_server = redis.StrictRedis(host=REDIS_HOST, decode_responses=True)
            redis_server.ping()
            logger.info("REDIS connection successful")
        except:
            logger.error("Error while setting up REDIS connection")

        return redis_server


classification_service = ClassificationService()


@classification_service.route('/inference/classify', methods=["POST"])
def classify_data():
    """
    Classifies a single image

    Awaits a jpg or png image in the request's body / data header

    :return: The detected class as json structure
    """
    try:
        if request.data is None or len(request.data) == 0:
            return {'error': "Missing request data. Please pass a single jpeg or a zip archive of jpegs"}, 400
        format = imghdr.what(io.BytesIO(request.data))
        if format == "jpeg" or format == "png":
            image = cv2.imdecode(np.frombuffer(request.data, dtype=np.uint8), cv2.IMREAD_ANYCOLOR)
            # YOUR classification here, e.g. via redis remote execution
            response_value = jsonify({"class": "banana", "inputShape": list(image.shape)})
        else:
            response_value = Response("No valid data provided. Please provide a single jpeg or png file")
        return make_uncacheable(response_value)
    except:
        print("An  error occurred: " + traceback.format_exc(), flush=True)
        return Response("An error occurred"), 400
