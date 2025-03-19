import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    
    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.nlargest(2).iloc[-1]
    else:
        second_highest = None
       
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    return result_df