import openai
import os


def generate_image(prompt):  
    api_key = os.environ['API_KEY']
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        response_format='b64_json',
        n=1,
        )
        return response.data[0].b64_json
    except openai.BadRequestError as e:
        # Re-try if this error is raised.
        if e.code == 'content_policy_violation':
          response = client.images.generate(
          model="dall-e-3",
          prompt=prompt,
          size="1024x1024",
          quality="standard",
          style=style,
          response_format='b64_json',
          n=1,
          )
          return response.data[0]
    except openai.OpenAIError as e:
        print(e)
        print('Encountered critical error.')
        return None


def generate_prompts(mother_prompt, num_children):
    api_key = os.environ['API_KEY']
    client = openai.OpenAI(api_key=api_key)
    generation_prompt = f'Generate {num_children} prompts for dal e 3 based on the following template prompt: "{mother_prompt}"'
    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'Print direct responses with no extra conversational text.'},
                {'role': 'user', 'content': generation_prompt}
            ]
        )
        response_text = response.choices[0].message.content
        response_list = response_text.split('\n')
        children_prompts = [response_list[i-1][len(str(i))+2:] for i in range(1, num_children+1)]
        return children_prompts
    except openai.OpenAIError as e:
        print(e)