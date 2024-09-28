# Bank Statement Analyzer

This application processes bank statement PDFs, extracts transaction data, and provides a chatbot interface for querying the data using natural language.

## Features

- Extracts transaction data from multiple PDF bank statements
- Preprocesses and analyzes the extracted data
- Provides a chatbot interface for querying the data
- Generates summaries and comparisons across months
- Identifies recurring transactions and flags transactions above a specified threshold

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/bank-statement-analyzer.git
   cd bank-statement-analyzer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

1. Prepare your bank statements:
   - Collect your bank statement PDFs
   - Place them in a folder on your computer

2. Run the main script:
   ```
   python main.py
   ```

3. Follow the prompts:
   - Enter the path to the folder containing your bank statement PDFs
   - Wait for the application to process the PDFs and initialize the chatbot

4. Interact with the chatbot:
   - Ask questions about your bank statements in natural language
   - Type 'exit' to quit the application

## Example Questions

You can ask the chatbot questions like:

- What are my expenses above $100?
- Show me a summary of all transactions.
- What are my recurring transactions?
- Compare my expenses across months.
- What was my total income for the past six months?

## Note

This application is for personal use and demonstration purposes only. Always ensure the security and privacy of your financial information when using such tools.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/bank-statement-analyzer/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)