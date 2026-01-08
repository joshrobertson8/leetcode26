"""
LeetCode: 2024 11 18 09.48.24 Accepted Runtime 423ms Memory 68.3MB

Algorithm:
Process the input directly.

Time Complexity: O(1)
Space Complexity: O(1)
"""

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    column_names = ["student_id", "age"]

    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe