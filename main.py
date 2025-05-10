from agents import Agent, Runner, gen_trace_id, trace, ModelSettings
from agents.mcp import MCPServerStdio, MCPServer

async def run_agent(mcp_server: MCPServer):
  web_agent = Agent(
    name="Web Scraper Agent",
    instructions="""
    You are a research agent that uses Google to find information and scrape data from websites.
    Your task is to retrieve information about a specific content creator using the different search results you find.
    You can scrape these websites to find the information you need.
    You will need to return the following information:
    1. The content creator's name
    2. A short bio
    5. The city they live in
    """,
    model="gpt-4o-mini",
    output_type=str,
    mcp_servers=[mcp_server],
    model_settings=ModelSettings(truncation="auto")
  )

  result = await Runner.run(web_agent, "Tom Shaw Developer")

  print(result.final_output)

async def main():
  async with MCPServerStdio(
    name="Bright Data MCP Server",
    params={
      "command": "npx",
      "args": ["-y", "@brightdata/mcp", "--ui", "--ui-port", "3000"],
      "env": {
        "API_TOKEN": "<YOUR API TOKEN HERE>",
        "WEB_UNLOCKER_ZONE": "<YOUR WEB UNLOCKER ZONE HERE",
        "BROWSER_AUTH": "<YOUR AUTH CREDENTIALS HERE>",
      }
    },
    client_session_timeout_seconds=180
  ) as brightdata_mcp:
    print("MCP server initialized successfully.")
    
    trace_id = gen_trace_id()
    with trace(workflow_name="MCP Bright Data Example", trace_id=trace_id):
      print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")

      await run_agent(brightdata_mcp)

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())