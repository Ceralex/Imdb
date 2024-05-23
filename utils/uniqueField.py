import pandas as pd

# Read the TSV file
df = pd.read_csv('tsv_data/title.principals.tsv', sep='\t')

# Handle missing values (replace '\N' with None)
df = df.replace('\\N', None)

# Split the '' column and stack it to create a single column
professions = df['job'].dropna().str.split(',', expand=True).stack()

# Find unique professions
unique_professions = professions.unique()

# Print unique professions
for profession in unique_professions:
    print(profession)
