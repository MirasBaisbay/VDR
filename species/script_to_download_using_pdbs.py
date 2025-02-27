import requests
import os

pdb_ids = ['5XPP', '5H1E', '3VTD', '2ZXM', '5XUQ', '5AWK', '5ZWE', '3A2H']

failed_pdbs = []

output_dir = r"species/Rattus norvegicus (rats)/2.5+/pdb_files"
os.makedirs(output_dir, exist_ok=True)


# download cif format and then convert to pdb because script for Ramachandran only accepts pdb
# website for converting cif to pdb: https://project-gemmi.github.io/wasm/convert/cif2pdb.html

# for failed_pdb in failed_pdbs:
#     url = f"https://files.rcsb.org/download/{failed_pdb}.cif"
#     response = requests.get(url)

#     if response.status_code == 200:
#         file_path = os.path.join(output_dir, f"{failed_pdb}.cif")
#         with open(file_path, "wb") as file:
#             file.write(response.content)
#         print(f"Downloaded: {failed_pdb}")
#     else:
#         print(f"Failed to download: {failed_pdb}")

for pdb_id in pdb_ids:
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(output_dir, f"{pdb_id}.pdb")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {pdb_id}")
    else:
        failed_pdbs.append(pdb_id)
        print(f"Failed to download: {pdb_id}")

print("Download complete!")
print(failed_pdbs)
