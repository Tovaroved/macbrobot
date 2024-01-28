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

products = {}

for document in response.rows:
    description = document['description'].split('\n\n')
    for element in description:
        if element.startwith('Отправле'):
            send_date = element.split(':')[-1].strip
            products[f'']


