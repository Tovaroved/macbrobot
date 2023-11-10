from .requests_test import get_data_from_accounts


def formatted_packages_list():
    packages = get_data_from_accounts()

    current_p1 = ''
    current_p2 = ''

    next_p1 = ''
    next_p2 = ''

    current_total_p1 = 0
    current_total_p2 = 0

    next_total_p1 = 0
    next_total_p2 = 0

    for package_list in packages:
        
        if package_list[-2] == 'Current: part #1':
            current_total_p1+=float(package_list[3])
            if int(package_list[-1]) > 1:
                current_p1+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                current_p1+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'

        elif package_list[-2] == 'Current: part #2':
            current_total_p2+=float(package_list[3])
            if int(package_list[-1]) > 1:
                current_p2+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                current_p2+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'

        elif package_list[-2] == 'Next: part #1':
            next_total_p1+=float(package_list[3])
            if int(package_list[-1]) > 1:
                next_p1+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                next_p1+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'

        elif package_list[-2] == 'Next: part #2':
            next_total_p2+=float(package_list[3])
            if int(package_list[-1]) > 1:
                next_p2+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                next_p2+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'


    az = '--------------------------------------------'
    ag = '############################################'

    two_parts_current = f"""<b>Товары на этой неделе:</b>\n__Партия №1__\n{current_p1}\n\nСумма: {round(current_total_p1,2)}\n\n{az} \n__Партия №2__\n{current_p2}\n\nСумма: {round(current_total_p2,2)}\n\n<b>Итого на этой неделе: {round(current_total_p1 + current_total_p2, 2)}</b>"""
    two_parts_next = f"""<b>Товары на следующей неделе:</b>\n__Партия №1__\n{next_p1}\n\nСумма: {round(next_total_p1,2)}\n\n{az} \n\n__Партия №2__\n{next_p2}\n\nСумма: {round(next_total_p2,2)}\n\n<b>Итого на следующей неделе: {round(next_total_p1 + next_total_p2, 2)}</b>"""
    
    one_part_current = f"""<b>Товары на этой неделе:</b>\n{current_p1+current_p2}\n\n<b>Итого на этой неделе: {round(current_total_p1 + current_total_p2, 2)}</b>"""
    one_part_next = f"""<b>Товары на следующей неделе:</b>\n{next_p1+next_p2}\n\n<b>Итого на следующей неделе: {round(next_total_p1 + next_total_p2, 2)}</b>"""
    return (two_parts_current, two_parts_next, one_part_current, one_part_next)
