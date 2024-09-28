from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import pandas as pd

class Chatbot:
    def __init__(self, data):
        self.data = data
        self.llm = OpenAI(temperature=0)
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = self.create_vectorstore()
        self.qa_chain = self.create_qa_chain()

    def create_vectorstore(self):
        texts = [
            f"Transaction on {row['date']} for {row['description']} with amount {row['amount']} ({row['type']})."
            for _, row in self.data.iterrows()
        ]
        return FAISS.from_texts(texts, self.embeddings)

    def create_qa_chain(self):
        prompt_template = """
        You are a helpful assistant for analyzing bank statements. Use the following context to answer the user's question:
        {context}
        
        Question: {question}
        Answer: """
        
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": PROMPT}
        )

    def get_response(self, query):
        try:
            if "summary" in query.lower():
                return self.generate_summary()
            elif "compare" in query.lower() and "months" in query.lower():
                return self.compare_months()
            else:
                return self.qa_chain.run(query)
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_summary(self):
        summary = self.data.agg({
            'amount': ['count', 'sum', 'mean', 'min', 'max'],
            'type': lambda x: x.value_counts().to_dict(),
            'is_recurring': 'sum',
            'above_threshold': 'sum'
        }).to_dict()

        return f"""
        Summary of all transactions:
        - Total number of transactions: {summary['amount']['count']}
        - Total amount: ${summary['amount']['sum']:.2f}
        - Average transaction amount: ${summary['amount']['mean']:.2f}
        - Minimum transaction amount: ${summary['amount']['min']:.2f}
        - Maximum transaction amount: ${summary['amount']['max']:.2f}
        - Number of credit transactions: {summary['type']['credit']}
        - Number of debit transactions: {summary['type']['debit']}
        - Number of recurring transactions: {summary['is_recurring']['sum']}
        - Number of transactions above threshold: {summary['above_threshold']['sum']}
        """

    def compare_months(self):
        monthly_summary = self.data.groupby('month').agg({
            'amount': ['count', 'sum'],
            'type': lambda x: x.value_counts().to_dict()
        })
        
        comparison = ""
        for month, data in monthly_summary.iterrows():
            comparison += f"""
            Month: {month}
            - Total transactions: {data['amount']['count']}
            - Total amount: ${data['amount']['sum']:.2f}
            - Credit transactions: {data['type']['credit']}
            - Debit transactions: {data['type']['debit']}
            """
        
        return comparison