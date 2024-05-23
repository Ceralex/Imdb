import pandas as pd
import csv

# Dizionario per mappare nomi dei generi agli ID
genre_id_map = {
    'Action': 1,
    'Adult': 2,
    'Adventure': 3,
    'Animation': 4,
    'Biography': 5,
    'Comedy': 6,
    'Crime': 7,
    'Documentary': 8,
    'Drama': 9,
    'Family': 10,
    'Fantasy': 11,
    'Film-Noir': 12,
    'Game-Show': 13,
    'History': 14,
    'Horror': 15,
    'Music': 16,
    'Musical': 17,
    'Mystery': 18,
    'News': 19,
    'Reality-TV': 20,
    'Romance': 21,
    'Sci-Fi': 22,
    'Short': 23,
    'Sport': 24,
    'Talk-Show': 25,
    'Thriller': 26,
    'War': 27,
    'Western': 28
}

# Funzione per processare una riga e aggiungere gli ID dei generi a una lista
def process_row(row, id_column, value_column, output_list):
    if row[value_column] and row[value_column] != '\\N':
        for value in row[value_column].split(','):
            genre_id = genre_id_map.get(value)
            if genre_id is not None:
                output_list.append([row[id_column], genre_id])

# Funzione per processare il file e generare il file TSV
def process_file(input_file, output_file, id_column, value_column):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        output_data = []

        for row in reader:
            process_row(row, id_column, value_column, output_data)

        # Convertire in DataFrame e salvare
        df = pd.DataFrame(output_data, columns=[id_column, 'genre_id'])
        df.to_csv(output_file, sep='\t', index=False)

process_file('tsv_data/title.basics.tsv', 'title.genres.tsv', 'tconst', 'genres')
