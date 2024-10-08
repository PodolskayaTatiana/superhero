import requests
import json

def get_superhero(gender, work):

    
    all_sp = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    # Создаем постой список
    suitable_superheroes = []
    # Проходим по общему списку и добавляем в пустой список подходящих героев
    for i in all_sp:
        if work == False:
            if i['appearance'].get("gender") == gender and i['work'].get("occupation") == "-":
                suitable_superheroes.append(i)
        else:
            if i['appearance'].get("gender") == gender and i['work'].get("occupation") != "-":
                suitable_superheroes.append(i)
    
    m = "meters"
    for i in suitable_superheroes:
        if m in i['appearance'].get("height")[1]:
            height = float(i['appearance'].get("height")[1][:-7])
            i['appearance'].get("height")[1] = height*100
        else:
            height = float(i['appearance'].get("height")[1][:-3])
            i['appearance'].get("height")[1] = height

    # Сортируем полученный список по убыванию роста супергероев        
    sorted_suitable_superheroes = sorted(suitable_superheroes, key = lambda x: x['appearance'].get("height")[1], reverse = True)

    if suitable_superheroes == []:
        return sorted_suitable_superheroes
    else:
        return sorted_suitable_superheroes[0]