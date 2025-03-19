import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    colname = f'getNthHighestSalary({N})'
    array_values = sorted(employee['salary'].unique(), reverse = True)
    if N >= 1 and len(array_values) >= N :
        return pd.DataFrame({colname: [array_values[N-1]]})
    
    return pd.DataFrame({colname: [None]})