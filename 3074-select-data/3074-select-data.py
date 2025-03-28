import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    a=students.loc[students['student_id']==101]
    return a[['name','age']]
    