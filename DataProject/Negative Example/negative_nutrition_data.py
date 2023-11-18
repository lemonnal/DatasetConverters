import pandas as pd
import numpy as np
import random

print("Starting to read nutritional information......")

excel_file = 'material/negative_nutrition_data.xlsx'
data_frame = pd.read_excel(excel_file, sheet_name='Sheet1')
case_id_0 = np.array(data_frame['case_id'])
item_id_0 = np.array(data_frame['item_id'])
flag_0 = np.zeros(len(case_id_0))

print("%d %d %d" % (len(case_id_0), len(item_id_0), len(flag_0)))

print("Selecting items......")

flag_0[0] = 1
for i in range(1, len(case_id_0)):
    if case_id_0[i] == case_id_0[i - 1] and item_id_0[i] == item_id_0[i - 1]:
        flag_0[i] = 0
    else:
        flag_0[i] = 1

case_id_1, item_id_1, flag_1 = \
    case_id_0[flag_0 == 1], item_id_0[flag_0 == 1], flag_0[flag_0 == 1]

print("%d %d %d" % (len(case_id_1), len(item_id_1), len(flag_1)))
print("%s %s %s" % (type(case_id_1), type(item_id_1), type(flag_1)))

print("Creating nutrition data......")

nutrition_list = [[0, 4, 8], [3], [2], [1, 3], [11],
                  [3], [0, 4, 8], [1, 9], [0, 4, 8], [],
                  [13], [14], [16], [17], [11],
                  [12], [18], [19], [21], [22]]

output_nutrition_data = [[], [], [], []]

for i in range(len(case_id_1)):
    case_select = case_id_1[i]
    item_select = item_id_1[i]
    for j in range(len(nutrition_list[item_select])):
        output_nutrition_data[0].append(case_select)
        output_nutrition_data[1].append(item_select)
        output_nutrition_data[2].append(nutrition_list[item_select][j])
        output_nutrition_data[3].append(-1)

df = pd.DataFrame(
    {'case_id': output_nutrition_data[0],
     'item_id': output_nutrition_data[1],
     'nutrition_id': output_nutrition_data[2],
     'weight': output_nutrition_data[3]})

print("Outputting nutrition data......")

df.to_excel('negative_nutrition_data.xlsx',
            sheet_name='Sheet1',
            na_rep='err',
            index=False)

print("Formatting data......")

case_id_2, \
    nutrition_id_2, \
    food_num = \
    output_nutrition_data[0], \
    output_nutrition_data[2], \
    [0 for i in range(len(output_nutrition_data[0]))]

case_id_all_num = 1018
case_id_num = np.zeros(case_id_all_num, dtype=int)
for i in case_id_2:
    case_id_num[i] += 1

food_num_remainder = 100 % case_id_num
for i in range(len(case_id_2)):
    case_select = case_id_2[i]
    food_num[i] = 100 // case_id_num[case_select]
    if food_num_remainder > 0:
        food_num[i] += 1
        food_num_remainder -= 1

# for i in range(len(case_id_2)):
#     print("%d %d %d"
#           % (case_id_2[i],
#              nutrition_id_2[i],
#              food_num[i]))

print("Creating food data......")

print("Start to read food information.")

excel_file = 'material/food_information.xlsx'
food = [[], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], []]

for i in range(25):
    food[i] = pd.read_excel(
        excel_file,
        sheet_name=i)['food_id']
    # print("n-id=%d:%d" % (i, len(food[i])))

print("Food information read completely.")
print("Create food data......")

food_data = [[], [], []]

for i in range(len(case_id_2)):
    case_select = case_id_2[i]
    nutrition_select = nutrition_id_2[i]
    food_num_select = food_num[i]
    food_list_select = random.choices(
        food[nutrition_select],
        k=food_num_select)
    for j in food_list_select:
        food_data[0].append(case_select)
        food_data[1].append(nutrition_select)
        food_data[2].append(j)

# for i in range(len(food_data[0])):
#     print("%d %d %d"
#           % (food_data[0][i],
#              food_data[1][i],
#              food_data[2][i]))

df = pd.DataFrame(
    {'case_id': food_data[0],
     'nutrition_id': food_data[1],
     'food_id': food_data[2]
     })
print(df)

print("Output food data......")

df.to_excel('negative_food_data.xlsx',
            sheet_name='Sheet1',
            na_rep='err',
            index=False)

print("OK.")
