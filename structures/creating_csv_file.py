import os

directory_path = 'structures'  # path to the directory
pdb_ids = []

# Get list of files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.cif'):
        # Remove the .cif extension to get just the ID
        pdb_id = filename.split('.')[0]
        pdb_ids.append(pdb_id)

print(pdb_ids)