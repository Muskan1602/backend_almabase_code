data_read_query = """ select dc.id, dc.name, vehicle_name, customer_id, 
date FROM public.dashboard_customer dc
join public.dashboard_vehicle dv on dc.id = dv.id
where dv.id = '{id}' """

data_delete_query = """select dc.id, dc.name, vehicle_name, customer_id, 
date FROM public.dashboard_customer dc
join public.dashboard_vehicle dv on dc.id = dv.id
where dv.id = '{id}'"""

# data_update_query =""" BEGIN TRANSACTION;
# UPDATE public.dashboard_customer
# SET name = %s
# FROM public.dashboard_customer dc, public.dashboard_vehicle dv
# WHERE dc.id = dv.id
# and dc.id = %s ;
# UPDATE public.dashboard_vehicle
# SET vehicle_name = %s
# FROM public.dashboard_customer dc, public.dashboard_vehicle dv
# WHERE dc.id = dv.id
# and dc.id = %s ;
# commit; """

data_update_query = """ UPDATE public.dashboard_customer SET name = %s
where i_d = %s; """