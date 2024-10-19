# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SpoofDetectorBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, reference_id: str=None, audio_data: str=None, model_version: str=None):  # noqa: E501
        """SpoofDetectorBody - a model defined in Swagger

        :param reference_id: The reference_id of this SpoofDetectorBody.  # noqa: E501
        :type reference_id: str
        :param audio_data: The audio_data of this SpoofDetectorBody.  # noqa: E501
        :type audio_data: str
        :param model_version: The model_version of this SpoofDetectorBody.  # noqa: E501
        :type model_version: str
        """
        self.swagger_types = {
            'reference_id': str,
            'audio_data': str,
            'model_version': str
        }

        self.attribute_map = {
            'reference_id': 'reference_id',
            'audio_data': 'audio_data',
            'model_version': 'model_version'
        }
        self._reference_id = reference_id
        self._audio_data = audio_data
        self._model_version = model_version

    @classmethod
    def from_dict(cls, dikt) -> 'SpoofDetectorBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The spoof_detector_body of this SpoofDetectorBody.  # noqa: E501
        :rtype: SpoofDetectorBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reference_id(self) -> str:
        """Gets the reference_id of this SpoofDetectorBody.


        :return: The reference_id of this SpoofDetectorBody.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id: str):
        """Sets the reference_id of this SpoofDetectorBody.


        :param reference_id: The reference_id of this SpoofDetectorBody.
        :type reference_id: str
        """
        if reference_id is None:
            raise ValueError("Invalid value for `reference_id`, must not be `None`")  # noqa: E501

        self._reference_id = reference_id

    @property
    def audio_data(self) -> str:
        """Gets the audio_data of this SpoofDetectorBody.


        :return: The audio_data of this SpoofDetectorBody.
        :rtype: str
        """
        return self._audio_data

    @audio_data.setter
    def audio_data(self, audio_data: str):
        """Sets the audio_data of this SpoofDetectorBody.


        :param audio_data: The audio_data of this SpoofDetectorBody.
        :type audio_data: str
        """
        if audio_data is None:
            raise ValueError("Invalid value for `audio_data`, must not be `None`")  # noqa: E501

        self._audio_data = audio_data

    @property
    def model_version(self) -> str:
        """Gets the model_version of this SpoofDetectorBody.


        :return: The model_version of this SpoofDetectorBody.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version: str):
        """Sets the model_version of this SpoofDetectorBody.


        :param model_version: The model_version of this SpoofDetectorBody.
        :type model_version: str
        """
        if model_version is None:
            raise ValueError("Invalid value for `model_version`, must not be `None`")  # noqa: E501

        self._model_version = model_version
