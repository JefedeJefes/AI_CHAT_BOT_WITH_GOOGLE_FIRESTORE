from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini",
                   temperature=0.6,)


animal_fact_template = ChatPromptTemplate.from_messages(
      [
        ("system" , "You like telling facts and you give facts about {animal}."),
        ("human" , "Tell me {count} facts."),
    ]
)

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a translator and convert the provide text into {language} "),
        ("human","Translate the following text into {language} : {text}")
    ]
)

prepare_for_translate = RunnableLambda(lambda output : {"text":output,"language":"french" })

chain = animal_fact_template | model | StrOutputParser() | prepare_for_translate | translation_template | model | StrOutputParser()


result = chain.invoke({"animal":"Tiger","count":1})

print(result)