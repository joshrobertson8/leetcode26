"""
LeetCode: 2024 11 18 09.48.24 Accepted Runtime 423ms Memory 68.3MB

Algorithm:
Use pandas DataFrame constructor to create a dataframe from the student_data list. Specify column names as "student_id" and "age". The DataFrame constructor automatically converts the list of lists into a structured dataframe.

Time Complexity: O(1)
Space Complexity: O(1)
"""

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    column_names = ["student_id", "age"]

    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe