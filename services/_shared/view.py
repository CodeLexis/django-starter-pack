from http.client import CONFLICT, CREATED, INTERNAL_SERVER_ERROR, NO_CONTENT, NOT_FOUND
from typing import OrderedDict

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http import Http404

from rest_framework import views, viewsets
from rest_framework.exceptions import APIException, ValidationError

from project import logger
from .exceptions import BaseRequestException
from .pagination import Pagination
from .response import make_error_response, make_success_response


class BaseView(views.APIView):
    @staticmethod
    def get_filter_params_for_object(obj: OrderedDict):
        filter_params = {}
        for key, value in obj.items():
            native_types = (str, int, float, bool, type(None))
            if isinstance(value, native_types):
                filter_params[key] = value

        return filter_params

    def handle_exception(self, exc):
        if type(exc) is ValidationError:
            return make_error_response(
                message=exc.detail,
                status=exc.status_code
            )

        elif isinstance(exc, APIException):
            clean_details = []

            if isinstance(exc.detail, dict):
                for value in exc.detail.values():
                    if isinstance(value, list):
                        clean_details.extend(value)
                    else:
                        clean_details.append(value)

            elif isinstance(exc.detail, str):
                clean_details.append(exc.detail)

            return make_error_response(
                message=clean_details,
                status=exc.status_code
            )

        elif isinstance(exc, BaseRequestException):
            return make_error_response(
                message=exc.message,
                status=exc.status_code
            )

        elif isinstance(exc, ObjectDoesNotExist) or isinstance(exc, Http404):
            return make_error_response(
                message='Not found',
                status=NOT_FOUND
            )
        
        elif isinstance(exc, IntegrityError):
            return make_error_response(message='Resource already exists', status=CONFLICT)

        else:
            logger.exception(exc) # As this could be any error, we want to log it before returning a safe error message

            return make_error_response(
                message='Something went wrong',
                status=INTERNAL_SERVER_ERROR
            )

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except (AttributeError, KeyError):
            return [permission() for permission in self.permission_classes]


class BaseViewSet(BaseView, viewsets.ModelViewSet):
    pagination_class = Pagination

    class Meta:
        abstract = True

    def create(self, request, *args, **kwargs):
        return make_success_response(
            data=super().create(request, *args, **kwargs).data,
            status=CREATED
        )

    def destroy(self, request, *args, **kwargs):
        return make_success_response(
            data=super().destroy(request, *args, **kwargs).data,
            status=NO_CONTENT
        )

    def retrieve(self, request, *args, **kwargs):
        return make_success_response(
            data=super().retrieve(request, *args, **kwargs).data
        )

    def list(self, request, *args, **kwargs):
        return make_success_response(
            data=super().list(request, *args, **kwargs).data
        )
