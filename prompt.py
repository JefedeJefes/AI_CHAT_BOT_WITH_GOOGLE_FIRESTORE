from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()



llm = ChatOpenAI(model="gpt-4o-mini",
                 temperature=0.6,)

template = "Write a {tone} email to {company} expression your wish to join at {position} , mentioning {skills} as strengths"


prompt_template = ChatPromptTemplate.from_template(template=template)


prompt = prompt_template.invoke({
    "tone":"thrilled",
    "company":"Microsoft",
    "position":"Python developer",
    "skills":"Python and Flask and Langchain"

})


result = llm.invoke(prompt)

print(result.content)