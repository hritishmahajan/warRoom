from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def create_quiz_chain():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.8
        #higher temperature than tutor chain
        #because we want more variety in quiz questions
        #so it doesn't ask the same questions every time
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a WWI quiz master. Your job is to:
        1. Generate a challenging but fair WWI quiz question
        2. Provide 4 multiple choice options labeled A, B, C, D
        3. Wait for the user to answer before revealing if they are correct
        
        When generating a question, format it EXACTLY like this:

        QUESTION: [your question here]
        
        A) [option]
        B) [option]
        C) [option]
        D) [option]
        
        Do NOT reveal the correct answer or explanation until the user responds.
        
        When the user gives their answer, THEN respond with:
        - Whether they are correct or incorrect
        - The correct answer
        - A detailed historical explanation
        - Then generate a brand new question"""),
        ("human", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    return chain