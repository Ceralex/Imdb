import pandas as pd

# The mapping dictionary
categories_dict = {
    'self': 1,
    'director': 2,
    'cinematographer': 3,
    'composer': 4,
    'producer': 5,
    'editor': 6,
    'actor': 7,
    'actress': 8,
    'writer': 9,
    'production_designer': 10,
    'archive_footage': 11,
    'archive_sound': 12
}

def convert_category_to_id(input_file, output_file, column_name):
    # Read the file into a DataFrame
    df = pd.read_csv(input_file, sep='\t', encoding='utf-8')

    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Map the column to the corresponding IDs
        df[column_name] = df[column_name].map(categories_dict, na_action='ignore')
    else:
        print(f"Column '{column_name}' not found in the file.")
        return

    # Save the modified DataFrame to a new file
    df.to_csv(output_file, sep='\t', index=False, encoding='utf-8')

# Define your input and output file paths and the column to be converted
input_file = 'tsv_data/title.principals.tsv'
output_file = 'title.principals.id.tsv'
column_name = 'category_id'  # The column you want to convert

# Run the function
convert_category_to_id(input_file, output_file, column_name)
