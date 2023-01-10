from database.pg_queries import data_read_query, data_delete_query
from database.pg_query_search import django_search_query
from supports.response_module import *


def get_filter_data(request):
    """
     this function used for deleting the data based on id from db

     """
    try:
        id = request.GET.get('id')
        data = django_search_query(data_delete_query.format(id=id))
        # print(data)
        return response_success(data=data)

    # If any kind of exception, response will be forbidden
    except Exception as err:
        return response_exception(err)


