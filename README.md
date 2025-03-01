# VDR Analysis Team

This repository contains the work of the VDR Analysis Team, focusing on the structural and functional analysis of the Vitamin D Receptor (VDR).

## Project Overview

The Vitamin D Receptor (VDR) is a member of the nuclear receptor family of transcription factors. It plays a crucial role in calcium homeostasis and bone metabolism by regulating the expression of target genes in response to vitamin D. Understanding the structure and function of VDR is essential for insights into various physiological processes and potential drug discovery

## Repository Contents

- **Ramachandran/**: Contains Ramachandran plots analyzing the dihedral angles of VDR structures.
- **secondary structure analysis/**: Includes analyses of the secondary structural elements of VDR.
- **species/**: Data related to VDR sequences across different species.
- **structures/**: 3D structural models and related files of VDR.
- **BIOL363 StructBiol 2025 VDR analysis.pdf**: Comprehensive report on VDR analysis conducted in the BIOL363 Structural Biology course, 2025.
- **overview.py**: Python script providing an overview of the VDR analysis.
- **species.xlsx**: Spreadsheet detailing VDR sequences and related information across various species.
- **versions.py**: Script tracking versions of tools and libraries used in the analysis.

## Technologies Used

- **Python (3.12.2)**: Programming language used for automating data retrieval, preprocessing PDB files, and performing various analyses (e.g., computing the mean and standard deviation).
- **Pandas (2.2.1)**: Python library used to create CSV files that store all the PDB files with their averaged phi/psi angles.
- **Sklearn (1.5.0)**: Python library for machine learning, used to perform k-means clustering.
- **Numpy (1.26.4)**: Python library for scientific computing, mainly for computing the mean and standard deviation of phi/psi angles for subgroups.
- **Seaborn (0.13.2)**: Python library used for plotting visualizations, such as the distribution of different species and their subgroups based on averaged phi/psi angles.
