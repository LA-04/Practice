import json
import openai
from config import *

openai.api_key = API_KEY

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="50 typical python developer interview questions with multiple answers",
#   temperature=0.5,
#   max_tokens=3090,
#   top_p=1.0,
#   frequency_penalty=0.5,
#   presence_penalty=0.0
# )
#
# with open(f'answer.json', 'w', encoding='utf8') as ans:
#   json.dump(response, ans, indent=2, ensure_ascii=False)
# answer = response

response = openai.Image.create(
  prompt="Facades in the style of Mario Botta",
  n=3,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(response)