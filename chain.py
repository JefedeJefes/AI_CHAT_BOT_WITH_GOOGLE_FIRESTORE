from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


llm = ChatOpenAI(model="gpt-4o-mini",
                 temperature = 0.6,)


prompt_template = ChatPromptTemplate.from_messages(
    [
      ("system" , "You are a fact expert and gives fact about {animal}."),
      ("human", "Tell me  {fact_count} facts")
])


chain = prompt_template | llm | StrOutputParser()



result = chain.invoke({"animal" : "Tiger" , "fact_count" : 3})

print(result)