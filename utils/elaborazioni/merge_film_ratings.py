import pandas as pd

# Caricare il primo file TSV
ratings = pd.read_csv('title.ratings.tsv', sep='\t')

# Caricare il secondo file TSV
titles = pd.read_csv('title.basics.tsv', sep='\t')

# Unire i due DataFrame sulla base di 'tconst'
merged = pd.merge(titles, ratings, on='tconst', how='left')

# Convertire i valori non-nulli di 'averageRating' in float
merged['averageRating'] = pd.to_numeric(merged['averageRating'], errors='coerce')

# Sostituire i valori NaN con '\N' in 'averageRating'
merged['averageRating'].fillna('\\N', inplace=True)

# Sostituire i valori NaN con 0 in 'numVotes' e convertirli in int
merged['numVotes'] = merged['numVotes'].fillna(0).astype(int)

# Salvare il DataFrame unito in un nuovo file TSV
merged.to_csv('title.basics_rated.tsv', sep='\t', index=False)
