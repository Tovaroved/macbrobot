from moysklad.api import MoySklad
from moysklad.queries import Expand, Filter, Ordering, Select, Search, Query


sklad = MoySklad.get_instance('admin@gun19', 'rolanddeschain19')
client = sklad.get_client()
methods = sklad.get_methods()

response = client.get(
    method=methods.get_list_url('purchaseorder'),
    # query=Query(
    #     Filter().exists('email').eq('archived', False),
    #     Search('петров'),
    #     Expand('owner', 'owner.group'),
    #     Ordering().asc('id').desc('name'),
    #     Select(limit=1),
    # ),
)
# print(response.data)

import json

with open('moy_sklad/data.json' ,"w",) as f:
    json.dump(response.data, f, indent=3, ensure_ascii=False)