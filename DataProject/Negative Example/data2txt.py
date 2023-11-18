import pandas as pd

print("Start read positive data and build dictionary......")
excel_file_1 = '../Positive Example/positive_food_data.xlsx'
df1 = pd.read_excel(excel_file_1, sheet_name='Sheet1')
# print(df1)

case_food_list = [0 for i in range(1018)]
for i in range(len(df1['case_id'])):
    case_select = df1['case_id'][i]
    food_select = df1['food_id'][i]
    if case_food_list[case_select] == 0:
        case_food_list[case_select] = food_select
# print(case_food_list)

idx = ["(%d,%d)" % (i, case_food_list[i]) for i in range(1018)]
# print(idx)
print("Build the dictionary like (case_id,positive food data) successfully.")

print("Start read negative data......")
excel_file_2 = 'negative_food_data.xlsx'
df2 = pd.read_excel(excel_file_2, sheet_name='Sheet1')

food_list = [[] for i in range(1018)]
for i in range(len(df2['case_id'])):
    case_select = df2['case_id'][i]
    food_select = df2['food_id'][i]
    food_list[case_select].append(food_select)

print("Read negative food data successfully.")

print("Pack the data......")
dict_food = {}
for i in range(1018):
    dict_food[idx[i]] = food_list[i]
# print(dict_food)
df = pd.DataFrame(dict_food).T
print(df)

print("Start output to the txt......")
df.to_csv('output.txt', sep='\t', header=False)

print("OK.")
