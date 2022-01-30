from flask import Blueprint, Response
from common import *


class IndexService(Blueprint):
    def __init__(self):
        """
        Initializer
        """
        super().__init__('IndexService', __name__)


index_service = IndexService()


@index_service.route("/")
def index():
    """
    Just a demo landing page.
    :return: A simple text
    """
    return make_uncacheable(Response("Hello world! How are you doing?"))

@index_service.route("/OK")
def ok_check():
    """
    Just a demo health page.
    :return: OK
    """
    return make_uncacheable(Response("OK"))

@index_service.route("/version")
def version_check():
    """
    Returns the server's version
    :return: The version
    """
    return make_uncacheable(Response("1.234"))
