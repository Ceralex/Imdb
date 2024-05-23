import gzip
import os

def extract_and_rename_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.tsv.gz'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(root, file.replace('.gz', ''))
                
                with gzip.open(input_path, 'rb') as f_in:
                    with open(output_path, 'wb') as f_out:
                        f_out.write(f_in.read())
                
                # Get the original file name without the .gz extension
                original_filename = os.path.splitext(file)[0]
                
                # Rename the extracted .tsv file to match the original filename
                new_file_name = os.path.join(root, original_filename)
                os.rename(output_path, new_file_name)
                
                # Remove the original .gz file
                os.remove(input_path)

folder_path = r'D:\Imdb\tsv_data'
extract_and_rename_files(folder_path)
