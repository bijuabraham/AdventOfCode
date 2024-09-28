import os
import pdfplumber
import re
from datetime import datetime

def extract_data_from_pdf(file_path):
    data = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Extract transactions using regex
            transactions = re.findall(r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+([-]?\$[\d,]+\.\d{2})', text)
            for transaction in transactions:
                date, description, amount = transaction
                amount = float(amount.replace('$', '').replace(',', ''))
                data.append({
                    'date': datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d'),
                    'description': description.strip(),
                    'amount': amount,
                    'type': 'credit' if amount > 0 else 'debit',
                    'source_file': os.path.basename(file_path)
                })
    return data

def process_pdf_files(folder_path):
    all_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            try:
                file_data = extract_data_from_pdf(file_path)
                all_data.extend(file_data)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    return all_data