from handling_data import get_formatted_data
from requests_test import names1

def formatting_packages_lists(names):
    packages=[]
    for name in names:
        with open(f'track_package/html_pages/{name}.html', 'r+') as f:
            html_code = f.read()
            data = get_formatted_data(html_code, name)
            if data:
                packages+=data
            else:
                continue
    return packages


def formatted_packages_list(names):
    all_packages = formatting_packages_lists(names)
    print(all_packages)


formatted_packages_list(names1)

    # packages_list_current = ''
    # packages_list_next = ''
    # total_price_current = 0
    # total_price_next = 0
    # for package_list in all_packages:
        
    #     if package_list[-2] == 'Current week':
    #         total_price_current+=float(package_list[3])
    #         if int(package_list[-1]) > 1:
    #             packages_list_current+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
    #         else:
    #             packages_list_current+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'

    #     elif package_list[-2] == 'Next week':
    #         total_price_next+=float(package_list[3])
    #         if int(package_list[-1]) > 1:
    #             packages_list_next+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
    #         else:
    #             packages_list_next+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
    


    # return [packages_list_current, packages_list_next, f'Общая сумма доставки: ${round(total_price_current,2)}', f'Общая сумма доставки: ${round(total_price_next,2)}']
