import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:root@localhost:5432/imdb')
chunk_size = 100_000

def truncate_string(value, length=128):
    return value[:length] if isinstance(value, str) else value

def clean_title_basics(chunk):
    chunk = chunk.replace('\\N', None)

    if 'is_adult' in chunk.columns:
        chunk['is_adult'] = chunk['is_adult'].astype(bool)

    for col in ['primary_title', 'original_title']:
        chunk[col] = chunk[col].apply(truncate_string)

    return chunk

def clean_name_basics(chunk):
    chunk = chunk.replace('\\N', None)

    for col in ['primary_name']:
        chunk[col] = chunk[col].apply(truncate_string)

    return chunk

def format_array(array_str):
    # Check if the value is a string that represents an array
    if isinstance(array_str, str) and array_str.startswith('"[') and array_str.endswith(']"'):
        try:
            # Remove the [" at the start and "] at the end
            array_str = array_str[2:-2]

            # Split the string into individual elements
            array_list = array_str.split('","')

            # Process each element in the list
            formatted_array = []
            for item in array_list:
                # Remove unnecessary double quotes from each element
                formatted_item = item.replace('""', '"')
                formatted_array.append(formatted_item)

            # Join the list into a PostgreSQL array format
            return "{" + ",".join(formatted_array) + "}"
        except (ValueError, SyntaxError):
            # In case of parsing error, return the original string
            return array_str
    else:
        # If it's not an array string, return it as is
        return array_str


   

def clean_title_principals(chunk):
    chunk = chunk.replace('\\N', None)
    
    # Convert and format the 'characters' column as a PostgreSQL array
    if 'characters' in chunk.columns:
        chunk['characters'] = chunk['characters'].apply(format_array)

    print(chunk['characters'])
    return chunk



def insert_data(file_path, table_name, engine, clean_func, columns=None):
    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size, usecols=columns, quoting=3):
        cleaned_chunk = clean_func(chunk)

        # Insert data into the database
        cleaned_chunk.to_sql(table_name, engine, if_exists='append', index=False)

def process_files(file_path, table_name, columns, clean_func):
    print(f'Inserting data from {file_path} into {table_name}...')

    insert_data(file_path, table_name, engine, clean_func, columns)

# Main Execution
if __name__ == "__main__":
    pass
    # Process each file with its specific cleaning function
    # process_files('tsv_data/title.basics.tsv', 'title_basics', ['tconst', 'title_type', 'primary_title', 'original_title', 'is_adult', 'start_year', 'end_year', 'runtime_minutes'], clean_title_basics)    
    # process_files('tsv_data/name.basics.tsv', 'name_basics', ['nconst', 'primary_name', 'birth_year', 'death_year'], clean_name_basics)
    process_files('tsv_data/title.principals.id.tsv', 'title_principals', ['tconst', 'ordering', 'nconst', 'category_id', 'job', 'characters'], clean_title_principals)
