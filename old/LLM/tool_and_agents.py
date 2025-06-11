from langchain_community.tools import DuckDuckGoSearchResults #google search requires API key
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "you are sherlock holmes to give search for user's query on duckduckgo and keep it concise"),
        ('human', '{user_input}'),
        ('placeholder', '{agent_scratchpad}')
    ]
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

search = DuckDuckGoSearchResults()

tools = [search]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True)

print(agent_executor.invoke({'user_input' : 'international space station'}))