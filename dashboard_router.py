from django.views.decorators.csrf import csrf_exempt

from api_framework.constants import *
from api_framework.operation_apis.delete_data import get_filter_data
from api_framework.operation_apis.read_data import get_operation_data
# from api_framework.operation_apis.update_data import get_updated_data
from supports.response_module import *



@csrf_exempt
def get_dashboard_apis(request):
    if request.method == GET:
        return get_operation_data(request)
    if request.method == DELETE:
        return get_filter_data(request)
    # if request.method == PUT:
    #     return get_updated_data(request)
    else:
        return response_request_wrong()
