from .requests_test import data_for_tg
import gspread

def formatted_packages_list():
    packages = data_for_tg()

    current_p1 = ''
    current_p2 = ''

    next_p1 = ''
    next_p2 = ''

    current_total_p1 = 0
    current_total_p2 = 0

    next_total_p1 = 0
    next_total_p2 = 0

    for package_list in packages:
        package_list[0] = package_list[0].split("|")[0]
        
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



# Запись данных в Google Sheets

def gsheet_package(parts=None):
    packages = data_for_tg()

    current_p1 = []
    current_p2 = []

    next_ = []

    """Разделение по неделям и партиям"""
    for package in packages:
        if package[-2] == 'Current: part #1':
            if int(package[-1]) > 1:
                current_p1.append([f'{package[-1]}шт {package[0]}',package[1],package[2],package[3],package[4]])
            else:
                current_p1.append([package[0],package[1],package[2],package[3],package[4]])
        elif package[-2] == 'Current: part #2':
            if int(package[-1]) > 1:
                current_p2.append([f'{package[-1]}шт {package[0]}',package[1],package[2],package[3],package[4]])
            else:
                current_p2.append([package[0],package[1],package[2],package[3],package[4]])

        elif package[-2] == 'Next: part #1':
            if int(package[-1]) > 1:
                next_.append([f'{package[-1]}шт {package[0]}',package[1],package[2],package[3],package[4]])
            else:
                next_.append([package[0],package[1],package[2],package[3],package[4]])

        elif package[-2] == 'Next: part #2':
            if int(package[-1]) > 1:
                next_.append([f'{package[-1]}шт {package[0]}',package[1],package[2],package[3],package[4]])
            else:
                next_.append([package[0],package[1],package[2],package[3],package[4]])


    """Авторизация"""
    sa = gspread.service_account()
    sh = sa.open("MacPython")
    wks = sh.worksheet('Список посылок')
    wks.batch_clear(['A1:G60'])

    current_p1_count = len(current_p1) if len(current_p1) != 0 else 1
    current_p2_count = len(current_p2) if len(current_p2) != 0 else 1

    if parts: # Для раздельной (по партиям записи)
        wks.update("A2", "Товары на этой неделе")
        
        wks.update(f"A3", "Партия №1")
        wks.update(f"A4:E{current_p1_count+4}", current_p1)
        
        wks.update(f"A{current_p1_count+4}", "Партия №2")
        wks.update(f"A{current_p1_count+5}:E{current_p2_count+5+len(current_p2)}", current_p2)
        
        pack_count = current_p1_count + current_p2_count

        wks.update(f"A{pack_count + 7}", "Товары на следующей неделе")

        wks.update(f"A{pack_count + 8}:E{pack_count + 8 + len(next_)}", next_)
    
    else: # Для объедененной записи
        wks.update("A2", "Товары на этой неделе")
        
        wks.update(f"A3:E{current_p1_count + current_p2_count+3}", current_p1+current_p2)

        wks.update(f"A{current_p1_count + current_p2_count+4}:E{current_p1_count + current_p2_count+4}","Товары на следующей неделе" )

        wks.update(f"A{current_p1_count + current_p2_count+5}:E{current_p1_count + current_p2_count+5+len(next_)}", next_)