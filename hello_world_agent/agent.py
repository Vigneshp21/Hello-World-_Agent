from google.adk.agents import Agent

root_agent=Agent(
    name="hello_world_agent",
    model="gemini-2.0-flash",
    description="Hello world agent",
    instruction="""
    You are a helpful agent that says 'Hello world!' to the user.
    """,
)
