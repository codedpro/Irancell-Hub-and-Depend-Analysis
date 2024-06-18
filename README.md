# Irancell Hub and Depend Analysis

## Overview

The **Irancell Hub and Depend Analysis** project is a comprehensive tool designed to analyze and process site data for MTN Irancell. This tool includes functionalities for cleaning site data, analyzing hub depends, merging site columns, and adding depend information from one file to another. It helps in effectively managing and understanding the network depends and site information.

## Features

- **Data Cleaning**: Clean site data by extracting specific patterns and standardizing the format.
- **Hub Analysis**: Analyze the hub depends for the cleaned site data.
- **Column Merging**: Merge site information from different Excel files, ensuring no duplicate entries.
- **Depend Addition**: Add depend information from one file to another, updating the main dataset with relevant details.

## Requirements

To run this project, you will need to have Python installed along with the following libraries:

- `pandas`
- `openpyxl`
- `xlsxwriter`

You can install these depends using the provided `requirements.txt` file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/codedpro/Irancell-Hub-And-Depend-Analysis.git
   cd Irancell-Hub-And-Depend-Analysis
   ```

2. **Install Depends**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the Excel Files**: Ensure your input Excel files (e.g., `DepCount-MTNi.xlsx`) are placed in the project directory.

2. **Run the Main Script**:
   ```bash
   python main.py
   ```

### main.py

The main script orchestrates the entire process by calling the functions from the respective modules:

- `cleanDep.py` for cleaning site data.
- `analysehub.py` for analyzing hub depends.
- `merger.py` for merging site columns.
- `depadd.py` for adding depend information.

## Modules

### cleanDep.py

This module cleans the site data by extracting specific patterns and standardizing the format.

### analysehub.py

This module analyzes the hub depends for the cleaned site data.

### merger.py

This module merges site information from different Excel files, ensuring no duplicate entries and updating the main dataset.

### depadd.py

This module adds depend information from one file to another, updating the main dataset with relevant details.

## Example Workflow

1. **Clean the Site Data**:
   - The `cleanDep.py` module processes the input file `DepCount-MTNi.xlsx` and outputs a cleaned file `cleaned_file.xlsx`.

2. **Analyze Hub Depends**:
   - The `analysehub.py` module analyzes the cleaned data and performs the necessary hub depend analysis.

3. **Merge Site Columns**:
   - The `merger.py` module merges site columns from the `output.xlsx` file with the `cleaned_file.xlsx`, creating an updated file `updated_file1.xlsx`.

4. **Add Depend Information**:
   - The `depadd.py` module adds depend information from `DepCount-MTNi.xlsx` to `updated_file1.xlsx`, resulting in the final file `Analyzed DepCount-MTNi.xlsx`.

## Contributing

We welcome contributions to enhance the functionality and usability of this tool. Feel free to open issues or submit pull requests on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

This tool was developed to streamline the process of analyzing and managing site data for MTN Irancell, enabling efficient network management and understanding of depends.