#
# from database.pg_queries import data_update_query
# from database.pg_query_modify import django_parameterized_query_update
# from database.pg_query_search import django_search_query
# from supports.response_module import *
# import json
# from api_framework.constants import *
# from django.views.decorators.csrf import csrf_exempt
#
#
# @csrf_exempt
# def get_updated_data(request):
#     try:
#         if request.method != 'PUT':
#             return response_request_wrong()
#         try:
#             i_d = str(request.GET.get('id'))
#             request_body = json.loads(request.body)
#             print(request_body)
#
#             # update_row, err = (
#             #     name,
#             #     i_d)
#             # print(err)
#
#             query = """UPDATE
#             public.dashboard_customer
#             SET
#             name = 'Varsha', id ='2'"""
#
#
#             data = django_search_query(query)
#             print(data)
#
#             # data,err = django_parameterized_query_update(
#             #     update_sql=data_update_query, update_tuple=update_row)
#             # print(err)
#
#             # print('up_row', update_row, data)
#             #
#             # data = {
#             #     "name": update_row[0],
#             # # }
#             # return response_success(data)
#         except Exception as Err:
#             return response_exception(Err)
#     except Exception as err:
#         return response_exception(err)
#
#
#
