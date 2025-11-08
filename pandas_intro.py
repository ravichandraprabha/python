from typing import List

import pandas as pd


# ------------- Create df from list -------------
def createDataframe(data: List, columns: List) -> pd.DataFrame:
    return pd.DataFrame(data=data, columns=columns)


list1 = [[1, 15], [2, 11], [3, 11], [4, 20]]
column_names = ["student_id", "age"]
df1 = createDataframe(list1, column_names)
print(f"---------- createDataframe --------------")
print(f"df1 created as \n: {df1}")
print("\n")


# ------------- Get Dataframe size -------------
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


print(f"---------- getDataframeSize --------------")
print(f"Size of df1: {getDataframeSize(df1)}")
print("\n")


# ------------- Get First 3 rows  -------------
def selectFirstRows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


print(f"---------- selectFirstRows --------------")
print(f"First 3 rows:\n {selectFirstRows(df1, 3)}")
print("\n")


# ------------- Get a row based on a filter and selected columns --------
def selectData(students: pd.DataFrame, student_id, columns) -> pd.DataFrame:
    return students.loc[students["student_id"] == student_id, columns]


students_data = [
    [101, 'Michael', 12],
    [102, 'James', 10],
    [103, 'Nancy', 15],
    [104, 'Robert', 14]
]
df_columns = ["student_id", "name", "age"]
df2 = createDataframe(students_data, df_columns)
filter_id = 103
select_columns = ["name", "age"]

print(f"---------- selectData --------------")
print(selectData(df2, filter_id, select_columns))
print("\n")


# ------------- Create a new column  -------------
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees


emp_list = [["Rahul", 23000], ["Mark", 29000], ["Rupert", 12000], ["Janice", 19000]]
emp_df = createDataframe(emp_list, ["name", "salary"])

print(f"---------- createBonusColumn --------------")
print(createBonusColumn(emp_df))
print("\n")


# ------------- Drop duplicates rows based on a column  -------------
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.sort_values(by=["id"], ascending=True).drop_duplicates(subset=["email"], keep="last")


cust_email_list = [
    {"id": "1", "name": "Ella", "email": "emily@example.com"},
    {"id": "2", "name": "David", "email": "dave@example.com"},
    {"id": "3", "name": "Zachary", "email": "zach@example.com"},
    {"id": "4", "name": "Alice", "email": "john@example.com"},
    {"id": "5", "name": "Finn", "email": "john@example.com"},
    {"id": "6", "name": "Violet", "email": "violet@example.com"}
]
cust_df = pd.DataFrame(cust_email_list)
print(f"---------- dropDuplicateEmails --------------")
print(cust_df)
print("\n")
print(dropDuplicateEmails(cust_df))
print("\n")


# ------------- Drop missing data -------------
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])


students_data = [
    {"student_id": 32, "name": "Piper", "age": 5},
    {"student_id": 217, "name": None, "age": 19},
    {"student_id": 779, "name": "Georgia", "age": 20},
    {"student_id": 849, "name": "Willow", "age": 14},
]
students_data_df = pd.DataFrame(students_data)
print(f"---------- dropMissingData --------------")
print(students_data_df)
print("\n")
print(dropMissingData(students_data_df))
print("\n")


# ------------- Modify columns -------------
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"].astype(int) * 2
    return employees


employees_data = [
    ["Jack", "19666"],
    ["Piper", "74754"],
    ["Mia", "62509"],
    ["Ulysses", "54866"]
]
employees_df = pd.DataFrame(data=employees_data, columns=["name", "salary"])
print(f"---------- modifySalaryColumn --------------")
print(employees_df)
print("\n")
print(modifySalaryColumn(employees_df))
print("\n")


# ------------- Rename columns -------------
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    renamed_columns = {"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"}
    return students.rename(columns=renamed_columns)


students_data = [
    [1, "Mason", "King", 6],
    [2, "Ava", "Wright", 7],
    [3, "Taylor", "Hall", 16],
    [4, "Georgia", "Thompson", 18],
    [5, "Thomas", "Moore", 10]
]
students_data_df = pd.DataFrame(data=students_data, columns=["id", "first", "last", "age"])
print(f"---------- renameColumns --------------")
print(students_data_df)
print("\n")
print(renameColumns(students_data_df))
print("\n")


# ------------- ChangeDatatype -------------
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students


students_data = [
    [1, "Ava", 6, 73.0],
    [2, "Kate", 15, 87.0]
]
students_data_df = pd.DataFrame(data=students_data, columns=["student_id", "name", "age", "grade"])
print(f"---------- ChangeDatatype --------------")
print(students_data_df)
print("\n")
print(changeDatatype(students_data_df))
print("\n")


# ------------- fillMissingValues -------------
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(value=0)
    return products


products_data = [
    ["Wristwatch", None, 135],
    ["WirelessEarbuds", None, 821],
    ["GolfClubs", "779", 9319],
    ["Printer", "849", 3051]
]
products_data_df = pd.DataFrame(data=products_data, columns=["name", "quantity", "price"])
print(f"---------- fillMissingValues --------------")
print(products_data_df)
print("\n")
print(fillMissingValues(products_data_df))
print("\n")


# ------------- concatenateTables -------------
def concatenateTables(df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
    # axis=0, row-wise concatenation. axis=1, column-wise concatenation.
    # Use pd.merge for sql like join
    return pd.concat([df_1, df_2], axis=0, ignore_index=True)


student_data_1 = [
    {"student_id": 1, "name": "Mason", "age": 8},
    {"student_id": 2, "name": "Ava", "age": 6},
    {"student_id": 3, "name": "Taylor", "age": 15},
    {"student_id": 4, "name": "Georgia", "age": 17}
]

student_data_2 = [
    {"student_id": 5, "name": "Leo", "age": 7},
    {"student_id": 6, "name": "Alex", "age": 7}
]

student_data_1_df = pd.DataFrame(student_data_1)
student_data_2_df = pd.DataFrame(student_data_2)

print(f"---------- concatenateTables --------------")
print(student_data_1_df)
print("\n")
print(student_data_2_df)
print("\n")
print(concatenateTables(student_data_1_df, student_data_2_df))
print("\n")


# ------------- pivotTable -------------
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(data=weather, index="month", columns="city", values="temperature")


weather_data = [
    ["Jacksonville", "January", 13],
    ["Jacksonville", "February", 23],
    ["Jacksonville", "March", 38],
    ["Jacksonville", "April", 5],
    ["Jacksonville", "May", 34],
    ["ElPaso", "January", 20],
    ["ElPaso", "February", 6],
    ["ElPaso", "March", 26],
    ["ElPaso", "April", 2],
    ["ElPaso", "May", 43],
]
weather_data_df = pd.DataFrame(data=weather_data, columns=["city", "month", "temperature"])
print(f"---------- concatenateTables --------------")
print(weather_data_df)
print("\n")
print(pivotTable(weather_data_df))
print("\n")


# ------------- meltTable -------------
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(frame=report, id_vars=["product"], var_name="quarter", value_name="sales")


wide_data = [
    ["Umbrella", 417, 224, 379, 611],
    ["SleepingBag", 800, 936, 93, 875]
]
wide_data_df = pd.DataFrame(data=wide_data, columns=["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])

print(f"---------- meltTable --------------")
print(wide_data_df)
print("\n")
print(meltTable(wide_data_df))
print("\n")


# ------------- methodChaining -------------
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False, ignore_index=True).filter(
        items=["name"], axis=1)


animals_data = [
    ["Tatiana", "Snake", 98, 464],
    ["Khaled", "Giraffe", 50, 41],
    ["Alex", "Leopard", 6, 328],
    ["Jonathan", "Monkey", 45, 463],
    ["Stefan", "Bear", 100, 50],
    ["Tommy", "Panda", 26, 349]
]
animals_df = pd.DataFrame(data=animals_data, columns=["name", "species", "age", "weight"])
print(f"---------- methodChaining --------------")
print(animals_df)
print("\n")
print(findHeavyAnimals(animals_df))
print("\n")
