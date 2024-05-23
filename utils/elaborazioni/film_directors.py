import pandas as pd
import csv

# Funzione per processare una riga e aggiungere i dati a una lista
def process_row(row, id_column, value_column, output_list):
    if row[value_column] and row[value_column] != '\\N':
        for value in row[value_column].split(','):
            output_list.append([row[id_column], value])

# Funzione per processare il file e generare il file TSV
def process_file(input_file, output_file, id_column, value_column):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        output_data = []

        for row in reader:
            process_row(row, id_column, value_column, output_data)

        # Convertire in DataFrame e salvare
        df = pd.DataFrame(output_data, columns=[id_column, value_column.rstrip('s')])
        df.to_csv(output_file, sep='\t', index=False)

# Processare e salvare i dati per directors e writers
process_file('tsv_data/title.crew.tsv', 'el.film.directors.tsv', 'tconst', 'directors')
process_file('tsv_data/title.crew.tsv', 'el.film.writers.tsv', 'tconst', 'writers')
