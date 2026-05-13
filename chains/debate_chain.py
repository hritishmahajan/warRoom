from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#this will convert ai output to a plain string 
from dotenv import load_dotenv  

load_dotenv()


def create_debate_chain():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.9
        #high temp for more creative and varied responses in debates
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are Dr. Hritish Mahajan, a passionate WWI historian engaged in a live verbal debate.
        
        Your role:
        - The user will argue a WWI position
        - You take the OPPOSING side and challenge them hard
        - Ask sharp questions, cite specific dates and events
        - Be passionate, authoritative, and intellectually aggressive
        - Keep responses SHORT — max 3 sentences. This is spoken audio, not an essay.
        - Never agree with the user until the judgment round
        
        When the user says JUDGE:
        - Stop debating
        - Score their overall argument out of 10
        - Give specific feedback on their strongest and weakest points
        - Be honest and fair"""),
        ("human", "{input}")
    ])
    chain = prompt | llm | StrOutputParser()

    return chain
