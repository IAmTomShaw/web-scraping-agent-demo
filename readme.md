# Bright Data MCP Demo for OpenAI Agents

This project demonstrates how to use the OpenAI Agents framework with Bright Data's MCP (Machine Connection Proxy) Server to create a powerful web scraping agent that can research information about content creators.

## Overview

The application uses the OpenAI Agents SDK to define an AI agent that can search the web and extract specific information about a content creator. The web scraping functionality is powered by Bright Data's MCP Server, which provides robust web access capabilities.

## Prerequisites

- Python 3.8+
- OpenAI API Key
- Bright Data account with:
  - API Token
  - Web Unlocker Zone configuration
  - Scraping Browser authentication credentials

## Installation

1. Clone this repository
2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example` and add your OpenAI API Key:

```sh
cp .env.example .env
```

4. Update the `main.py` file with your Bright Data credentials:
   - `API_TOKEN`
   - `WEB_UNLOCKER_ZONE`
   - `BROWSER_AUTH`

## Usage

Run the application with:

```sh
python main.py
```

The agent will:
1. Initialize the Bright Data MCP Server
2. Create a web scraper agent with specific instructions
3. Search for information about "Tom Shaw Developer"
4. Return the content creator's name, a short bio, and their city
5. Print the results

You can modify the search query by changing the parameter in the `Runner.run()` function call.

## Workflow Tracing

The application generates a trace ID that allows you to monitor the agent's workflow on the OpenAI platform. The trace URL will be printed in the console when you run the application.

## Customization

You can customize the agent's instructions, model parameters, and search queries in the `main.py` file. The agent is configured to use the `gpt-4o-mini` model by default. However, you can change this to any other model supported by OpenAI.