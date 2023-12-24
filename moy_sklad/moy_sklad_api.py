from moysklad.api import MoySklad
from moysklad.queries import Filter, Query
from decouple import config


sklad = MoySklad.get_instance(config('login'), config('password'))
client = sklad.get_client()
methods = sklad.get_methods()

response = client.get(
    method=methods.get_list_url('move'),
    query=Query(Filter().eq('applicable', False)
    ),
)


# with open('moy_sklad/data.py', 'w', encoding='utf8') as f:
#     f.write(str(response.rows),)


for document in response.rows:
    print(document['description'].split('\n\n'))
