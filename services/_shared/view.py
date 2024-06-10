from http.client import CREATED, NO_CONTENT, NOT_FOUND
from typing import OrderedDict

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import views, viewsets
from rest_framework.exceptions import APIException, ValidationError

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

        elif isinstance(exc, ObjectDoesNotExist):
            return make_error_response(
                message='Not found',
                status=NOT_FOUND
            )

        else:
            raise exc

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except (AttributeError, KeyError):
            return [permission() for permission in self.permission_classes]


class BaseViewSet(viewsets.ModelViewSet):
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
