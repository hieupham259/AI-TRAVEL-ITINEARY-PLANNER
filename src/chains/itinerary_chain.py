from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini 2.5 Flash model
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

itnineary_prompt = ChatPromptTemplate([
    ("system" , "You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
    ("human" , "Create a itineary for my day trip")
])


def generate_itineary(city:str , interests:list[str]) -> str:
    chain = itnineary_prompt | model
    response = chain.invoke({
        "city": city,
        "interests": interests
    })
    return response.content

if __name__ == "__main__":
    city = "Paris"
    interests = ["art", "history", "Eiffel Tower"]
    itineary = generate_itineary(city, interests)
    print(itineary)