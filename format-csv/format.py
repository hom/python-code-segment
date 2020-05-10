# -*- coding:utf-8 -*-

import csv

# 先按照年份来分类
year_dict = {}
with open('./entry.csv', 'r') as entry:
    reader = csv.reader(entry)
    for row in reader:
        if reader.line_num == 1 or reader.line_num == 2:
            continue

        if reader.line_num == 3:
            print(row)
        # if reader.line_num < 100:
        year = row[1]
        if year not in year_dict:
            year_dict[year] = [row]
        else:
            year_dict.get(year).append(row)

result_list = []
# 按照城市来分类
print(len(year_dict.keys()))
for year in sorted(year_dict.keys()):
    this_year_list = year_dict.get(year)

    this_year_city_key_dict = {}
    for item in this_year_list:
        city = item[0]
        label = int(item[-1])
        if city not in this_year_city_key_dict:
            default_this_year_city = {'name': city, 'year': year, 'A': 0, 'A1': 0, 'A2': 0, 'A3': 0,
                                     'A4': 0,'B': 0,'B1': 0, 'B2': 0,'B3': 0, 'B4': 0, 'C': 0, 'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0}
            if label <= 5:
                A1 = float(item[2])
                A2 = float(item[3])
                A3 = float(item[4])
                A4 = float(item[5])
                default_this_year_city['A']+= 1
                default_this_year_city['A1'] += A1
                default_this_year_city['A2'] += A2
                default_this_year_city['A3'] += A3
                default_this_year_city['A4'] += A4
            elif label >= 6 and label <= 50:
                B1 = float(item[2])
                B2 = float(item[3])
                B3 = float(item[4])
                B4 = float(item[5])
                default_this_year_city['B']+= 1
                default_this_year_city['B1'] += B1
                default_this_year_city['B2'] += B2
                default_this_year_city['B3'] += B3
                default_this_year_city['B4'] += B4
            else:
                C1 = float(item[2])
                C2 = float(item[3])
                C3 = float(item[4])
                C4 = float(item[5])
                default_this_year_city['C']+= 1
                default_this_year_city['C1'] += C1
                default_this_year_city['C2'] += C2
                default_this_year_city['C3'] += C3
                default_this_year_city['C4'] += C4
            this_year_city_key_dict[city] = default_this_year_city
        else:
            if label <= 5:
                A1 = float(item[2])
                A2 = float(item[3])
                A3 = float(item[4])
                A4 = float(item[5])
                this_year_city_key_dict[city]['A']+= 1
                this_year_city_key_dict[city]['A1'] += A1
                this_year_city_key_dict[city]['A2'] += A2
                this_year_city_key_dict[city]['A3'] += A3
                this_year_city_key_dict[city]['A4'] += A4
            elif label >= 6 and label <= 50:
                B1 = float(item[2])
                B2 = float(item[3])
                B3 = float(item[4])
                B4 = float(item[5])
                this_year_city_key_dict[city]['B']+= 1
                this_year_city_key_dict[city]['B1'] += B1
                this_year_city_key_dict[city]['B2'] += B2
                this_year_city_key_dict[city]['B3'] += B3
                this_year_city_key_dict[city]['B4'] += B4
            else:
                C1 = float(item[2])
                C2 = float(item[3])
                C3 = float(item[4])
                C4 = float(item[5])
                this_year_city_key_dict[city]['C'] += 1
                this_year_city_key_dict[city]['C1'] += C1
                this_year_city_key_dict[city]['C2'] += C2
                this_year_city_key_dict[city]['C3'] += C3
                this_year_city_key_dict[city]['C4'] += C4
    for city in this_year_city_key_dict.items():
        result_list.append(city[1])

with open('./result.csv', 'w') as result:
    fieldnames = ['name', 'year', 'A', 'A1', 'A2', 'A3', 'A4', 'B', 'B1', 'B2', 'B3', 'B4', 'C', 'C1', 'C2', 'C3', 'C4']
    writer = csv.DictWriter(result, fieldnames=fieldnames)

    writer.writeheader()
    for city in result_list:
        writer.writerow(city)