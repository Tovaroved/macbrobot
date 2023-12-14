from moysklad.api import MoySklad
from moysklad.queries import Expand, Filter, Ordering, Select, Search, Query


sklad = MoySklad.get_instance('admin@gun19', 'rolanddeschain19')
client = sklad.get_client()
methods = sklad.get_methods()

response = client.get(
    method=methods.get_list_url('counterparty'),
    # query=Query(
    #     Filter().exists('email').eq('archived', False),
    #     Search('петров'),
    #     Expand('owner', 'owner.group'),
    #     Ordering().asc('id').desc('name'),
    #     Select(limit=1),
    # ),
)
print(response.data)