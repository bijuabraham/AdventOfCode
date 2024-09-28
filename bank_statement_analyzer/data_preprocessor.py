import pandas as pd
from collections import Counter

def preprocess_data(raw_data):
    df = pd.DataFrame(raw_data)
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Ensure amount is numeric
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Determine transaction type (already done in pdf_processor, but let's ensure it's correct)
    df['type'] = df['amount'].apply(lambda x: 'credit' if x > 0 else 'debit')
    
    # Identify recurring transactions
    description_counts = Counter(df['description'])
    df['is_recurring'] = df['description'].apply(lambda x: description_counts[x] > 1)
    
    # Flag transactions above threshold
    threshold = 100  # This should be user-configurable in the future
    df['above_threshold'] = df['amount'].abs() > threshold
    
    # Add month and year columns for easier querying
    df['month'] = df['date'].dt.to_period('M')
    df['year'] = df['date'].dt.year
    
    return df

def generate_summary(df):
    summary = {
        'total_transactions': len(df),
        'total_credit': df[df['type'] == 'credit']['amount'].sum(),
        'total_debit': abs(df[df['type'] == 'debit']['amount'].sum()),
        'avg_transaction': df['amount'].mean(),
        'max_transaction': df.loc[df['amount'].abs().idxmax()],
        'min_transaction': df.loc[df['amount'].abs().idxmin()],
        'recurring_transactions': df['is_recurring'].sum(),
        'transactions_above_threshold': df['above_threshold'].sum(),
    }
    return summary