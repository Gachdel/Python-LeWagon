# This file contains useful functions that can be imported from anywhere
def show_type(var, var_name=''):
    print(f"{var_name} type is: {str(type(var).__name__)}")

def show_length(var, var_name=''):
    print(f"{var_name} length is: {len(var)}")


def show_unique_values(pandas_series):
    status_values = pandas_series.unique()
    print(f"{pandas_series.nunique()} possible values: {status_values}")

def show_sorted_values(pandas_series, ascending=False):
    print(pandas_series.sort_values(ascending=ascending))
