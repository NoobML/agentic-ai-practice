# LangChain AI Agent

A simple AI agent built with **LangChain**, Google's Gemini API, Tavily Search, Weatherstack, and Streamlit.

The agent can answer user queries, search the web for relevant information, and retrieve current weather data for different cities through an interactive web interface.

## Features

- **AI-powered responses:** Uses Google Gemini to understand queries and generate answers.
- **Web search:** Uses Tavily to search the internet for relevant information.
- **Weather information:** Uses Weatherstack to retrieve current weather data for different cities.
- **Interactive interface:** Uses Streamlit to provide a simple web interface.
- **Loading indicator:** Shows a message while the agent processes a query.
- **Configurable search results:** Allows the number of search results to be adjusted, if enabled in the application.

## Technologies Used

- Python 3.11
- LangChain
- Google Gemini API
- Tavily Search API
- Weatherstack API
- Streamlit
- Requests
- Python Dotenv

## APIs and Accounts

### 1. Google Gemini API

Gemini is the language model that powers the agent. It helps interpret user queries, generate responses, and decide when to use available tools.

Get an API key: https://aistudio.google.com/api-keys

### 2. Tavily Search API

Tavily enables the agent to search the web and retrieve relevant information.

Create an account: https://app.tavily.com/home

### 3. Weatherstack API

Weatherstack provides current weather information for different cities.

Create an account: https://weatherstack.com/

**Note:** These services may offer free usage with certain limits. Check their websites for current pricing, availability, and usage restrictions.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NoobML/agentic-ai-practice.git
cd agentic-ai-practice/Langchain-Agent
```

### 2. Create and Activate a Conda Environment

```bash
conda create -n agent python=3.11
conda activate agent
```

You can use another Python environment manager if you prefer.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

The project includes an `.env.example` file showing the required environment variables.

1. Create a file named `.env` in the `Langchain-Agent` directory.
2. Copy the contents of `.env.example` into `.env`.
3. Replace the placeholder values with your own API keys.

Your `.env` file should contain:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

**Security:** Never commit or share your actual `.env` file. It contains private API keys. The `.env` file should remain excluded by `.gitignore`, while `.env.example` can be committed with placeholder values.

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Open the local URL displayed in your terminal to access the application in your browser.

## How to Use

1. Open the application in your browser.
2. Enter a query in the input field.
3. Click **Run Agent**.
4. Wait while the agent processes your query.
5. Read the response displayed on the page.

Example queries:

- `Search the web for recent developments in artificial intelligence.`
- `What is the current weather in Peshawar?`
- `Find recent news about machine learning.`

## Project Structure

```text
agentic-ai-practice/
├── Langchain-Agent/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
```

This structure reflects the expected project layout. Adjust it if your actual files differ.

## Learning Objectives

This project was developed to practise:

- Building an AI agent using LangChain.
- Connecting a language model to external tools.
- Integrating web search and weather APIs.
- Managing API keys through environment variables.
- Creating an interactive AI application using Streamlit.
- Understanding Python data types and processing model responses.

## Future Improvements

- Improve error handling for API failures.
- Add conversation history.
- Improve response quality and formatting.
- Add more tools and capabilities.
- Expand the user interface.

## License

See the [LICENSE](../LICENSE) file for licensing information.
