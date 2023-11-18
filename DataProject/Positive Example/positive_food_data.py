import random
import pandas as pd
import numpy as np

print("Start to read nutritional information......")

excel_file = 'material/nutrition_information.xlsx'
data_frame = pd.read_excel(excel_file, sheet_name='Sheet1')
case_id = np.array(data_frame['case_id'])
nutrition_id = np.array(data_frame['nutrition_id'])
weight = np.array(data_frame['weight'])

print("%d %d %d" % (len(nutrition_id), len(weight), len(case_id)))

# print(data_frame)
# print(nutrition_id)
# print(weight)
# print(case_id)

print("Nutritional information read completely.")

print("Start to read food information......")

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
    # print("%d-id=:%d" % (i, len(food[i])))

# print(food)
# print(food[1][2])
# print(len(food))

print("Food information read completely.")
print("Create food data......")

food_data = [[], [], [], []]

for i in range(len(weight)):
    nutrition_select = nutrition_id[i]
    weight_select = weight[i]
    case_select = case_id[i]

    # print("%d %d %d" % (nutrition_select, weight_select, case_select))

    food_list_select = random.choices(
        food[nutrition_select],
        k=weight_select * 2)
    for j in food_list_select:
        food_data[0].append(case_select)
        food_data[1].append(nutrition_select)
        food_data[2].append(j)
        food_data[3].append(weight_select)

df = pd.DataFrame(
    {'case_id': food_data[0],
     'nutrition_id': food_data[1],
     'food_id': food_data[2],
     'weight': food_data[3]})
print(df)

print("Food data create completely.")
print("Output food data......")

df.to_excel('positive_food_data.xlsx',
            sheet_name='Sheet1',
            na_rep='err',
            index=False)

print("Outputting completely.")

mode = int(input("Select the kind of the dataset of the models:"))
if mode == 1:

    print("(Model1) Divide to train, validation, test dataset......")
    food_data_train = [[], [], [], []]
    food_data_test = [[], [], [], []]
    food_data_validation = [[], [], [], []]
    num = 0

    for i in range(len(food_data[0])):
        case_select = food_data[0][i]
        nutrition_select = food_data[1][i]
        food_select = food_data[2][i]
        weight_select = food_data[3][i]

        if num == 0:
            num = weight_select * 2
        if weight_select == 5 or weight_select == 4:
            if num >= 4:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(nutrition_select)
                food_data_train[2].append(food_select)
                food_data_train[3].append(weight_select)
            elif 3 >= num >= 2:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(nutrition_select)
                food_data_test[2].append(food_select)
                food_data_test[3].append(weight_select)
            elif num == 1:
                num = num - 1
                food_data_validation[0].append(case_select)
                food_data_validation[1].append(nutrition_select)
                food_data_validation[2].append(food_select)
                food_data_validation[3].append(weight_select)
        elif weight_select == 3 or weight_select == 2:
            if num >= 3:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(nutrition_select)
                food_data_train[2].append(food_select)
                food_data_train[3].append(weight_select)
            elif num == 2:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(nutrition_select)
                food_data_test[2].append(food_select)
                food_data_test[3].append(weight_select)
            elif num == 1:
                num = num - 1
                food_data_validation[0].append(case_select)
                food_data_validation[1].append(nutrition_select)
                food_data_validation[2].append(food_select)
                food_data_validation[3].append(weight_select)
        elif weight_select == 1:
            if num >= 2:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(nutrition_select)
                food_data_train[2].append(food_select)
                food_data_train[3].append(weight_select)
            elif num == 1:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(nutrition_select)
                food_data_test[2].append(food_select)
                food_data_test[3].append(weight_select)

    train_data = pd.DataFrame(
        {'case_id': food_data_train[0],
         'nutrition_id': food_data_train[1],
         'food_id': food_data_train[2],
         'weight': food_data_train[3]})
    test_data = pd.DataFrame(
        {'case_id': food_data_test[0],
         'nutrition_id': food_data_test[1],
         'food_id': food_data_test[2],
         'weight': food_data_test[3]})
    validation_data = pd.DataFrame(
        {'case_id': food_data_validation[0],
         'nutrition_id': food_data_validation[1],
         'food_id': food_data_validation[2],
         'weight': food_data_validation[3]})

    print("Divide dataset completely.")

    print("Output dataset......")

    train_data.to_excel('model_1/train_dataset.xlsx', sheet_name='Sheet1', na_rep='err', index=False)
    test_data.to_excel('model_1/test_dataset.xlsx', sheet_name='Sheet1', na_rep='err', index=False)
    validation_data.to_excel('model_1/validation_dataset.xlsx', sheet_name='Sheet1', na_rep='err', index=False)

    print("Dataset1 Outputting completely.")

elif mode == 2:

    print("(Model2) Divide to train, test dataset......")
    food_data_train = [[], []]
    food_data_test = [[], []]
    num = 0

    for i in range(len(food_data[0])):
        case_select = food_data[0][i]
        food_select = food_data[2][i]
        weight_select = food_data[3][i]
        if num == 0:
            num = weight_select * 2
        if weight_select == 5 or weight_select == 4:
            if num >= 4:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(food_select)
            elif 1 <= num <= 3:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(food_select)
        elif weight_select == 3 or weight_select == 2:
            if num >= 3:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(food_select)
            elif 1 <= num <= 2:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(food_select)
        elif weight_select == 1:
            if num >= 2:
                num = num - 1
                food_data_train[0].append(case_select)
                food_data_train[1].append(food_select)
            elif num == 1:
                num = num - 1
                food_data_test[0].append(case_select)
                food_data_test[1].append(food_select)

    train_data = pd.DataFrame(
        {'case_id': food_data_train[0],
         'food_id': food_data_train[1]})
    test_data = pd.DataFrame(
        {'case_id': food_data_test[0],
         'food_id': food_data_test[1]})

    print("Pack the data......")

    food_list_train = [[] for i in range(1018)]
    for i in range(len(train_data['case_id'])):
        case_select = train_data['case_id'][i]
        food_select = train_data['food_id'][i]
        food_list_train[case_select].append(food_select)

    food_list_test = [[] for i in range(1018)]
    for i in range(len(test_data['case_id'])):
        case_select = test_data['case_id'][i]
        food_select = test_data['food_id'][i]
        food_list_test[case_select].append(food_select)

    dict_food_train = {}
    for i in range(1018):
        dict_food_train[i] = food_list_train[i]
    df_train = pd.DataFrame.from_dict(dict_food_train, orient='index')
    df_train = df_train.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    # print(df_train)

    dict_food_test = {}
    for i in range(1018):
        dict_food_test[i] = food_list_test[i]
    df_test = pd.DataFrame.from_dict(dict_food_test, orient='index')
    df_test = df_test.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    # print(df_test)

    print("Start output to the txt......")

    df_train.to_csv('model_2/train_data.txt', sep=' ', header=False)
    df_test.to_csv('model_2/test_data.txt', sep=' ', header=False)

    print("Dataset2 Outputting completely.")

print("OK.")
