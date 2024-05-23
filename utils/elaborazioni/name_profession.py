import pandas as pd
import csv

# Dizionario per mappare nomi delle professioni agli ID
profession_id_map = {
    'soundtrack': 1,
    'actor': 2,
    'miscellaneous': 3,
    'actress': 4,
    'music_department': 5,
    'writer': 6,
    'director': 7,
    'producer': 8,
    'stunts': 9,
    'make_up_department': 10,
    'composer': 11,
    'assistant_director': 12,
    'camera_department': 13,
    'music_artist': 14,
    'editor': 15,
    'cinematographer': 16,
    'casting_director': 17,
    'script_department': 18,
    'art_director': 19,
    'costume_department': 20,
    'animation_department': 21,
    'art_department': 22,
    'executive': 23,
    'special_effects': 24,
    'production_designer': 25,
    'production_manager': 26,
    'editorial_department': 27,
    'sound_department': 28,
    'talent_agent': 29,
    'casting_department': 30,
    'costume_designer': 31,
    'visual_effects': 32,
    'location_management': 33,
    'set_decorator': 34,
    'transportation_department': 35,
    'manager': 36,
    'publicist': 37,
    'legal': 38,
    'assistant': 39,
    'podcaster': 40,
    'production_department': 41,
    'music_supervisor': 42,
    'choreographer': 43,
    'electrical_department': 44,
    'intimacy_coordinator': 45
}

# Funzione per processare una riga e aggiungere gli ID dei generi a una lista
def process_row(row, id_column, value_column, output_list):
    if row[value_column] and row[value_column] != '\\N':
        for value in row[value_column].split(','):
            profession_id = profession_id_map.get(value)
            if profession_id is not None:
                output_list.append([row[id_column], profession_id])

# Funzione per processare il file e generare il file TSV
def process_file(input_file, output_file, id_column, value_column):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        output_data = []

        for row in reader:
            process_row(row, id_column, value_column, output_data)

        # Convertire in DataFrame e salvare
        df = pd.DataFrame(output_data, columns=[id_column, 'profession_id'])
        df.to_csv(output_file, sep='\t', index=False)

process_file('tsv_data/name.basics.tsv', 'name.profession.tsv', 'nconst', 'primary_profession')
