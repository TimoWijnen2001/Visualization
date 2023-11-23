import pandas as pd

df = pd.read_csv("all_data.csv", delimiter=";")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def parse_data(row, attribute_name):
    """Get the value of a cell by specifying the column name and row number, 
    where the row number starts at 0.
    It is assumed that df is already defined."""
    return df.loc[row, attribute_name]
# print(parse_data("Age", 0))


def attribute_distribution(attribute_name):
    """Get the frequency of the values of a column. including empty values.
    It is assumed that df is already defined."""
    print(df[attribute_name].value_counts(
        ascending=True, dropna=False).head(9000))
#print(attribute_distribution("Annual_Income"))


def missing_values_per_attribute():
    """Get the number of missing values per attribute.
    It is assumed that df is already defined."""
    print(df.isnull().sum())
# print(missing_values_per_attribute())


def missing_values_per_entry():
    """Get the number of missing values per entry.
    It is assumed that df is already defined."""
    print(df.isnull().sum(axis=1))
# print(missing_values_per_entry())
