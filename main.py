
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
# from langchain.tools import tool
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


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="Thr agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [TavilySearch()]
# agent = create_agent(model=llm, tools=tools)
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job postings for an SDET engineer using langchain in the Bengaluru & Gurugram on linkedin and list their details"
            )
        }
    )
    print(result)

if __name__ == "__main__":
    main()