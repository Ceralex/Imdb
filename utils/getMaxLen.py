import pandas as pd
import ast

def max_length_in_array_column(tsv_file, column_name):
    max_length = 0

    # Iterate through the file in chunks
    for chunk in pd.read_csv(tsv_file, delimiter='\t', chunksize=500_000):
        if column_name in chunk.columns:
            # Convert string representation of arrays into actual lists
            chunk[column_name] = chunk[column_name].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x)
            
            # Iterate through each array in the column
            for item in chunk[column_name]:
                if isinstance(item, list):
                    current_max = max([len(str(element)) for element in item], default=0)
                    max_length = max(max_length, current_max)
    
    return max_length

# Example usage
tsv_file = 'tsv_data/title.principals.tsv'  # Update with your TSV file path
column_name = 'characters'  # Change to the name of the column you're interested in
max_length = max_length_in_array_column(tsv_file, column_name)
print(f"The maximum length of a string in the arrays of column '{column_name}' is: {max_length}")
