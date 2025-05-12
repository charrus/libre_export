# libre-export

A Python utility that converts Libre Connect CSV files to YAML format for backfilling glucose data into Home Assistant.

## Overview

This tool reads CSV files exported from Libre Connect glucose monitoring system and converts the readings into a format compatible with Home Assistant's recorder. This allows users to track and visualize their glucose data within their Home Assistant dashboard.

## Installation

This project uses Poetry for dependency management:

```bash
# Clone the repository
git clone https://github.com/yourusername/libre-export.git
cd libre-export

# Install dependencies using Poetry
poetry install
```

## Usage

1. Place your Libre Connect CSV export in the project root directory
2. Run the tool:

```bash
poetry run python -m libre_export
```

The tool will process the CSV file and output formatted data that can be imported into Home Assistant.

## File Format

The tool expects a CSV file with the following columns:
- Device
- Serial Number
- Device Timestamp
- Record Type
- Historic Glucose mmol/L
- Scan Glucose mmol/L
- Various insulin and carbohydrate metrics

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Charlie Rusbridger <charlie@rusbridger.com>
