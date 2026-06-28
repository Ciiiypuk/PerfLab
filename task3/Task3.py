import sys
import json
def make_dict_result(data):
    dict_result = {}
    for key, value in data.items():
        for elem in value:
            dict_result[elem['id']] = elem['value']
    return dict_result
def update_dict_from_result(dict_1, dict_result):
    for key1, value1 in dict_1.items():
        for elem in value1:
            index = value1.index(elem)
            for key2, value2 in elem.items():
                for key_result, value_result in dict_result.items():
                    if key2 == 'id' and value2 == key_result:
                        dict_1[key1][index]["value"] = value_result
                    elif key2 == "values":
                        for elem2 in value2:
                            index2 = value2.index(elem2)
                            for key3, value3 in elem2.items():
                                if key3 == 'id' and value3 == key_result:
                                    dict_1[key1][index]["values"][index2]["value"] = value_result
                                elif key3 == "values":
                                    for elem3 in value3:
                                        index3 = value3.index(elem3)
                                        for key4, value4 in elem3.items():
                                            if key4 == 'id' and value4 == key_result:
                                                dict_1[key1][index]["values"][index2]["values"][index3]["value"] = value_result
                                            elif key4 == "values":
                                                for elem4 in value4:
                                                    index4 = value4.index(elem4)
                                                    for key5, value5 in elem4.items():
                                                        if key5 == 'id' and value5 == key_result:
                                                            dict_1[key1][index]["values"][index2]["values"][index3][
                                                                "values"][index4]["value"] = value_result
    return dict_1
print('Start!')
if len(sys.argv) ==1 or len(sys.argv)>4:
    print('Ошибка!!! \nОжидаю 3 параметр!')
with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)

with open(sys.argv[2], 'r', encoding='utf-8') as f2:
    data2 = json.load(f2)
dict_result = make_dict_result(data2)
dict_report = update_dict_from_result(data1, dict_result)
with open(sys.argv[3], 'w') as f:
    json.dump(dict_report, f)
    print('Done!')