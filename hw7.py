'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

'''
import json

profit_dict = {}
looser_dict = {}
average_profit = {}
profit_list = []

with open('text_7.txt', 'r', encoding='utf-8') as file:
    for i in file:
        company, property_type, revenue, costs = i.rsplit()
        if int(revenue) - int(costs) >= 0:
            profit_dict[f"{property_type} '{company}'"] = int(revenue) - int(costs)
        else:
            looser_dict[f"{property_type} '{company}'"] = int(revenue) - int(costs)
    average_profit['average_profit'] = sum(profit_dict.values()) / len(profit_dict.keys())
    profit_dict.update(looser_dict)
    profit_list.append(profit_dict)
    profit_list.append(average_profit)
    print(profit_list)

with open('file_7.json', 'w', encoding='utf-8') as js_file:
    json.dump(profit_list, fp=js_file, sort_keys=False, indent=4, ensure_ascii=False)

