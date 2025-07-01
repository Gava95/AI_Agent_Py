import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from bcolors import bcolors

# Check if all the require arguments are provided, if not exit the program
if len(sys.argv) < 2:
    # Missing prompt argument
    print(bcolors.WARNING, 
    'Usage: python3 -m main "prompt" (Missing prompt !!!!)', bcolors.ENDC)
    sys.exit(1)

if len(sys.argv) > 3:
    # Missing quotation marks for the prompt argument
    print(bcolors.WARNING, 
    'Usage: python3 -m main "prompt" (Put the prompt between quotation marks --> " ")', bcolors.ENDC)
    sys.exit(1)

# Parse and load .env file variables
load_dotenv()

# API Key from .env files
api_key = os.environ.get("GEMINI_API_KEY")

# Initialization of the AI Agent Client
client = genai.Client(api_key=api_key)

# sys.argv[1] second arguments from the command line define as prompt argument
user_prompt = sys.argv[1]

# List of all the prompts to create a history and enable the conversation mode of the AI Agent
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

# Response from the AI agent given the parameters used
# - model : model of AI used
# - contents : list of the history of prompts
response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)

# AI Agent Response to contents (prompt) 
print('Prompt Response:\n', response.text)

opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]

if '--verbose' in opts:

    # Prompt of the user
    print(f"User prompt: {user_prompt}")

    # Number of tokens used in the prompt
    print('Prompt tokens:', response.usage_metadata.prompt_token_count)

    # Number of tokens used in the response
    print('Response tokens:', response.usage_metadata.candidates_token_count)

    # Total number of tokens used (prompt + response)
    print('Total tokens count:', response.usage_metadata.total_token_count)


