# Getting Started

See the README for general setup instructions.

## SOC Classification Library

This utility provides functions for classifying the Standard Occupational Code, used by the **Survey Assist API** hosted in **Google Cloud Platform (GCP)**.

### Features

- SOC Lookup
- SOC Classification with LLM

### Installation

To use this code in another repository using ssh:

```bash
poetry add git+ssh://git@github.com/ONSdigital/soc-classification-library.git@v0.1.4
```

or https:

```bash
poetry add git+https://github.com/ONSdigital/soc-classification-library.git@v0.1.4
```

### Usage

Example code that uses the SOC lookup and SOC meta functionality is available in `src/occupational_classification/lookup/soc_lookup_example.py`. Run it with:

```bash
poetry run python src/occupational_classification/lookup/soc_lookup_example.py
```
