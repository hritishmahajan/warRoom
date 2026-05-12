from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv() # Loads OPENAI_API_KEY into our environment

#Making a funct that builds and returns our chain
def create_tutor_chain(): #we will call this func from app.py

    #first line creates an instance of GPT model.
    #we use llm since this is a standard var name which we use in LangChain code
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7
        #temp scale is from 0 to 1,
        #higher temp means more creative responses,
        #lower temp means more focused and deterministic responses
    )

    #You can see this is a system prompt which sets the context for the model before
    #the conversation actually starts.
    #also, """ means the string can span multiple lines.
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert WWI historian and tutor named Dr. Hritish Mahajan.
        You have deep knowledge of all aspects of World War 1 including battles,
        political causes, key figures, treaties, and the human cost of the war.
        You explain things clearly, with passion, and use vivid examples.
        When relevant, mention specific dates, names and places to bring history alive.
        If asked something unrelated to WWI, politely redirect the conversation back to WWI."""),
        MessagesPlaceholder(variable_name="chat_history"),
        #this chat history is a placeholder that will be filled with the conversation history from memory.
        ("human", "{question}")
        #human -> this is the user input,
        #and {question} is a variable that will be replaced with the actual question.
    ])

    #LCEL - LangChain Expression Language
    #the | operator pipes the output of one step into the next
    #prompt -> llm -> parse output as string
    chain = prompt | llm | StrOutputParser()

    return chain

#Until now,
#ChatOpenAI -> llm
#ChatPromptTemplate.from_messages -> prompt
#StrOutputParser -> converts llm output to plain string
#chain = prompt | llm | StrOutputParser() -> the modern LCEL pipeline