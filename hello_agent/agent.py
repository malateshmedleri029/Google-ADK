from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="hello_agent",
    description="A simple Hello World agent.",
    instruction="You are a friendly assistant. Greet users and respond briefly.",
)
