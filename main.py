import os
import openai
from dotenv import load_dotenv

MAX_TOKENS = 100
CHATGPT_MODEL = 'text-davinci-003'

load_dotenv()

# Get from .env file
openai.api_key = os.getenv('OPENAI_API_KEY')
# Global key for OpenAI
openai.organization = 'org-r95rDmiPDWBEwR7J2VM9AEnd'

# Wait for Prompt
in_prompt = input("Enter prompt: ")

# Receive response given prompt
response = openai.Completion.create(
  model=CHATGPT_MODEL,
  prompt=in_prompt,
  max_tokens=MAX_TOKENS,
  temperature=0
)

print(response.choices[0].text)
print(f'Total Tokens: {response.usage.total_tokens}')