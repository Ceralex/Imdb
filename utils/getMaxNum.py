import pandas as pd

def max_column_integer(tsv_file, column_name):
    max_integer = float('-inf')  # Initialize with negative infinity
    
    # Iterate through the file in chunks
    for chunk in pd.read_csv(tsv_file, delimiter='\t', chunksize=100_000, na_values='\\N'):
        if column_name in chunk.columns:
            # Convert the column to numeric, treating '\N' as NaN
            chunk[column_name] = pd.to_numeric(chunk[column_name], errors='coerce')
            max_integer = max(max_integer, chunk[column_name].max())
    
    return max_integer

# Example usage
tsv_file = 'tsv_data/title.ratings.tsv'  # Update with your TSV file path
column_name = 'num_votes'  # Change to the name of the column you're interested in
max_value = max_column_integer(tsv_file, column_name)
print(f"The maximum value in column '{column_name}' is: {max_value}")
