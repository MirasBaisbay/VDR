import pandas as pd

files = [
    ("RamaPlot 1-2 Zebra Fish.txt", "Zebrafish", "1-2"),
    ("RamaPlot 2-2.5 Zebra Fish.txt", "Zebrafish", "2-2.5"),
    ("RamaPlot 2.5+ Zebra Fish.txt", "Zebrafish", "2.5+"),
    ("RamaPlot 1-2 Rat.txt", "Rat", "1-2"),
    ("RamaPlot 2-2.5 Rat.txt", "Rat", "2-2.5"),
    ("RamaPlot 2.5+ Rat.txt", "Rat", "2.5+"),
    ("RamaPlot for 1-2 Human.txt", "Human", "1-2"),
    ("RamaPlot for 2-2.5 Human.txt", "Human", "2-2.5"),
    ("RamaPlot for 2.5+ Human.txt", "Human", "2.5+")
]

data = []

for file_name, species, resolution in files:
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 
            # Expected format: "PDB: <id> | Average phi: <phi> | Average psi: <psi>"
            parts = line.split("|")
            try:
                pdb_id = parts[0].split(":")[1].strip()
                phi = float(parts[1].split(":")[1].strip())
                psi = float(parts[2].split(":")[1].strip())
                data.append({
                    "PDB": pdb_id,
                    "AveragePhi": phi,
                    "AveragePsi": psi,
                    "Species": species,
                    "Resolution": resolution
                })
            except (IndexError, ValueError) as e:
                print(f"Error processing line in {file_name}: {line}")
                continue

master_df = pd.DataFrame(data)

master_df.to_csv("master.csv", index=False)

print(master_df.head())
