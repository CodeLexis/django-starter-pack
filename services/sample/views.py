from services._shared.response import make_success_response
from services._shared.view import BaseView


class HelloView(BaseView):
    def get(self, request, *args, **kwargs):
        return make_success_response(data='Hello World!')
