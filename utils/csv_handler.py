"""Utility functions for CSV file operations"""
import csv
import os
from typing import List, Dict

DATA_DIR = 'data'

def read_csv(filename: str) -> List[Dict]:
    """Read CSV file and return list of dictionaries"""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
    
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename: str, data: List[Dict], fieldnames: List[str]):
    """Write data to CSV file"""
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filename: str, row: Dict, fieldnames: List[str]):
    """Append a row to CSV file"""
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)
    
    file_exists = os.path.exists(filepath)
    with open(filepath, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

