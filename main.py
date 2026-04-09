import re
from turtle import mode
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
# from langchain_tavily import TavilySearchResults
from langchain_tavily import TavilySearch

# tavily = TavilyClient()
# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching the web for: {query}")
#     # return "India weather is sunny and give detailed description of the result"
#     return tavily.search(query=query)

#     # """Search the web for information"""
#     # return "I found this information: " + query

# with langchain-tavily we can search the web for information --> we don't need any tool for 
# searching the web if using inbuilt tavily by langchain



llm = ChatOpenAI(model="gpt-4o-mini")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from react-search-agent!")
    # result = agent.invoke({"messages": HumanMessage(content="What is the weather in India?")})
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an SDET engineer using langchain in the Bengaluru & Gurugram on linkedin and list their details")})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()