from openai import OpenAI
from asyncio import run
import datetime
import os
import json
import re

OPENAI_API_KEY = "Paste OpenAI API key here."
MODEL_NAME = "unused"

# Locally hosted server endpoint
PORT = 1234
API_ENDPOINT = f"http://localhost:{PORT}/v1"

# Location for files used by the program
RESOURCE_FOLDER = 'resource_files/'
OUTPUT_FOLDER = 'output_files/'

async def main():
    client = OpenAI(base_url=API_ENDPOINT, api_key=OPENAI_API_KEY)

    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    prep = open(f'{RESOURCE_FOLDER}preprompt.md', 'r')        # Preprompt can be customized to whatever you want.
    preprompt = prep.read()
    preprompt = ""
    
    while True: # Main loop

        cont = open(f'{RESOURCE_FOLDER}bot_context.md', 'r')
        # TODO: Upgrade to more robust context storage method. This was mainly developed this way so a user could see exactly what was going on.
        context = cont.read()
        
        query = input("👦: ")
        
        if query.upper() == 'QUIT':                     
            # Detects if a user wants to quit the program from the CLI
            old_context = open(f'{RESOURCE_FOLDER}bot_context.md', 'r')   
            print(old_context.read())                   # Prints bot_context.md to the terminal and then erases it for the next cycle.
            erase_bot_context(f'{RESOURCE_FOLDER}bot_context.md')
            await documentation_generator('unused', client)
            break
        try:                                            
            # Completes chat response
            resp = await create_completion(MODEL_NAME, (f'{preprompt}\n{query}\n For context: {context}'), client)
            print(f"🤖: {resp}")
            append_to_markdown_file(f'{RESOURCE_FOLDER}chat_history.md',f'\n### {timestamp} Query: {query} \n Response: {resp}\n')
            output_code_to_file(resp, 'test')
        except Exception as e:
            print(f"🤖: {e}")
        try:
            # Compresses the output in an attempt to save on tokens for sending the entire chat
            # TODO: This was originally a very hacky way to do this, need to figure out an actual better way.
            #       Ideally, this would be pipelined to run while the user is writing a response.

            compression_prompt = "Compress the following text in a way that fits in a tweet (ideally) and such that you (GPT-4) can reconstruct the intention of the human who wrote text as close as possible to the original intention. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, unicode symbols, or any other encodings or internal representations is all permissible, as long as it, if pasted in a new inference cycle, will yield near-identical results as the original text:"
            topic_prompt = "Based on this response, decide what the topic of the thread is. Only return one or two words."
            encoded_output = await create_completion(MODEL_NAME, (f'{compression_prompt} \n {resp}'), client)
            topic_output = await create_completion(MODEL_NAME, (f'{topic_prompt} \n {resp}'), client)
            print(topic_output)
            append_to_markdown_file(f'{RESOURCE_FOLDER}bot_context.md',f'\n{encoded_output}')
        
        except Exception as e:
            print(f"🤖: {e}")

async def create_completion(MODEL_NAME, prompt, client):
    """Asynchronous create_completion method."""
    # TODO: Need to update this method so that it's more aligned with openAI's example code.

    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=[
          {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
          {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        )
    response = completion.choices[0].message
    return response.content

def append_to_markdown_file(file_name, string_to_append):
    """Appends string to Markdown file."""
    with open(file_name, 'a') as file:
        file.write(f'\n{string_to_append}')

def erase_bot_context(file_path):
    """Erases content in the chatbot's context file."""
    with open(file_path, 'w') as file:
        file.write('')

def output_code_to_file(response, title):
    """Detects Python scripts in the output and then writes it to 'latest.py' for users to test."""
    # TODO: Allow the option for titling the output file something other than 'latest.py'

    with open(f'{OUTPUT_FOLDER}latest.py', 'w') as f:
        code_list = re.findall(r"```python(.*?)```", json.dumps(response), re.DOTALL)
        for code in code_list:
            # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
            # and remove leading/trailing whitespaces
            code = code.replace("\\n", "\n").replace('\\"', '"').strip()
            f.write("%s\n" % code)

async def documentation_generator(file_path, client):
    script = open(f'{OUTPUT_FOLDER}latest.py', 'r')
    code = script.read()
    documentation_prompt = "Generate supplementary documentation for this Python script. Make sure to describe what the code is doing. Also list its input variables, output variables, and how they interact with each other in a table in Markdown format."
    documentation = await create_completion(MODEL_NAME, (f'{documentation_prompt} \n {code}'), client)
    append_to_markdown_file(f'{OUTPUT_FOLDER}Documentation.md', documentation)

run(main())