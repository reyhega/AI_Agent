import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
model_name = "gemini-2.0-flash-001"
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
verbose_flag = len(sys.argv) > 2 and sys.argv[2] == "--verbose"
system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

if not sys.argv[1]:
    print("Please provide prompt")
    sys.exit(1)
response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print(response.text)

if verbose_flag:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
