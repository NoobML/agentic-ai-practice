import certifi
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent


os.environ['SSL_CERT_FILE'] = certifi.where()
load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
weatherstack_api_key = os.getenv("WEATHERSTACK_API_KEY")


st.set_page_config(
    page_title="Simple Agent",
    page_icon= "🎩",
    layout="centered"
)

st.title("A simple Agent developed through langchain")
st.markdown("An agentic application, which searches weather of a location & provides information on a topic by searching on web-browser")
user_query = st.text_input(
    "Enter your query",
    placeholder="Example: Find latest news on AI"
)

tavily_search = TavilySearchResults(max_results=3)


@tool
def get_weather_data(city:str) -> str:
    """
    This function returns weather information of a city
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={weatherstack_api_key}&query={city}"
    )

    response = requests.get(url)
    data = response.json()

    if 'current' not in data:
        return f"Could not fetch {city} weather data "

    return (
        f"City: {city} \n"
        f"Temperature: {data['current']['temperature']}℃ \n"
        f"Weather: {data['current']['weather_descriptions'][0]} \n"
        f"Humidity: {data['current']['humidity']}% \n"
    )


tools = [tavily_search, get_weather_data]


LLM = ChatGoogleGenerativeAI(
    model='gemini-3.8-flash',
    temperature=0,
    google_api_key=gemini_api_key
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer clearly and concisely. Use short paragraphs or bullet points. Avoid unnecessary details."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent_1 = create_tool_calling_agent(
    llm = LLM,
    tools = tools,
    prompt = prompt
)

agent_executor = AgentExecutor(
    agent = agent_1,
    tools=tools,
    verbose=True
)

if st.button("Run Agent"):
    if user_query:
        with st.spinner("Agent is running, please be patient..."):
            response = agent_executor.invoke({"input": user_query})
            output = response["output"]

        if isinstance(output, list):
            output = "\n".join(
                item["text"]
                for item in output
                if isinstance(item, dict) and item.get("type") == "text"
            )

        st.markdown(output)
    else:
        st.warning("Please enter something")

