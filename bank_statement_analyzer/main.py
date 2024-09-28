import os
from pdf_processor import process_pdf_files
from data_preprocessor import preprocess_data
from chatbot import Chatbot

def get_pdf_folder():
    while True:
        folder = input("Enter the path to the folder containing your bank statement PDFs: ").strip()
        if os.path.isdir(folder):
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            if pdf_files:
                return folder
            else:
                print("No PDF files found in the specified folder. Please try again.")
        else:
            print("Invalid folder path. Please try again.")

def main():
    print("Welcome to the Bank Statement Analyzer!")
    
    # Get the folder path from the user
    pdf_folder = get_pdf_folder()
    
    print("Processing PDF files...")
    raw_data = process_pdf_files(pdf_folder)
    
    print("Preprocessing data...")
    processed_data = preprocess_data(raw_data)
    
    print("Initializing chatbot...")
    chatbot = Chatbot(processed_data)
    
    print("\nChat interface ready. You can now ask questions about your bank statements.")
    print("Type 'exit' to quit.")
    print("Some example questions you can ask:")
    print("1. What are my expenses above $100?")
    print("2. Show me a summary of all transactions.")
    print("3. What are my recurring transactions?")
    print("4. Compare my expenses across months.")
    print("5. What was my total income for the past six months?")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

    print("Thank you for using the Bank Statement Analyzer. Goodbye!")

if __name__ == "__main__":
    main()