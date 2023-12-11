from freeGPT import AsyncClient
from asyncio import run
import datetime
import os
import json
import re

model_name = 'gpt4'

async def main():
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    prep = open('preprompt.md', 'r')
    preprompt = prep.read()
    preprompt = ""
    while True:
        cont = open('bot_context.md', 'r')
        context = cont.read()
        query = input("👦: ")
        if query.upper() == 'QUIT':
            old_context = open('bot_context.md', 'r')
            print(old_context.read())
            erase_bot_context('bot_context.md')
            break
        try:
            resp = await AsyncClient.create_completion(model_name, (f'{preprompt}\n{query}\n For context: {context}'))
            print(f"🤖: {resp}")
            append_to_markdown_file('chat_history.md',f'\n### {timestamp} Query: {query} \n Response: {resp}\n')
            output_code_to_file(resp, 'test')
        except Exception as e:
            print(f"🤖: {e}")
        try:
            compression_prompt = "Compress the following text in a way that fits in a tweet (ideally) and such that you (GPT-4) can reconstruct the intention of the human who wrote text as close as possible to the original intention. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible, as long as it, if pasted in a new inference cycle, will yield near-identical results as the original text:"
            topic_prompt = "Based on this response, decide what the topic of the thread is. Only return one or two words."
            encoded_output = await AsyncClient.create_completion(model_name, (f'{compression_prompt} \n {resp}'))
            topic_output = await AsyncClient.create_completion(model_name, (f'{topic_prompt} \n {resp}'))
            print(topic_output)
            append_to_markdown_file('bot_context.md',f'\n{encoded_output}')
        except Exception as e:
            print(f"🤖: {e}")


def append_to_markdown_file(file_name, string_to_append):
    with open(file_name, 'a') as file:
        file.write(f'\n{string_to_append}')

async def summarizer(essay):
    response = await AsyncClient.create_completion(model_name, (f"Summarize the contents of this YouTube video into two paragraphs: {essay}"))
    return response

def erase_bot_context(file_path):
    with open(file_path, 'w') as file:
        file.write('')

def output_code_to_file(response, title):
    with open(f'latest.py', 'w') as f:
        code_list = re.findall(r"```python(.*?)```", json.dumps(response), re.DOTALL)
        for code in code_list:
            # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
            # and remove leading/trailing whitespaces
            code = code.replace("\\n", "\n").replace('\\"', '"').strip()
            f.write("%s\n" % code)

async def documentation_generator(file_path):
    script = open('latest.py', 'r')
    code = script.read()
    documentation_prompt = "Generate supplementary documentation for this Python script. Make sure to describe what the code is doing. Also list its input variables, output variables, and how they interact with each other in a table in Markdown format."
    documentation = await AsyncClient.create_completion(model_name, (f'{documentation_prompt} \n {code}'))
    append_to_markdown_file('Documentation.md', documentation)

async def typescript_transpiler():
    script = open('latest.py', 'r')
    code = script.read()
    documentation_prompt = "Describe what this Python script is doing in as few words as possible. Make sure to list its input and output variables. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible."
    documentation = await AsyncClient.create_completion(model_name, (f'{documentation_prompt} \n {code}'))
    print('Documentation:')
    print(documentation)
    transpiler_prompt = f"You are a software engineer at Google. Using this code: \n {code} \nand this supplying documentation as a base: \n {documentation} \n Generate code in Typescript that matches its functionality and maintains parity with the given Python script."
    transpiled_code = await AsyncClient.create_completion(model_name, (f'{transpiler_prompt}'))
    print('Code transpiled.')
    with open('latest.ts', 'w') as f:
        code_list = re.findall(r"```typescript(.*?)```", json.dumps(transpiled_code), re.DOTALL)
        for code in code_list:
            # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
            # and remove leading/trailing whitespaces
            code = code.replace("\\n", "\n").replace('\\"', '"').strip()
            f.write("%s\n" % code)

async def ruby_transpiler():
    script = open('latest.py', 'r')
    code = script.read()
    documentation_prompt = "Describe what this Python script is doing in as few words as possible. Make sure to list its input and output variables. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible."
    documentation = await AsyncClient.create_completion(model_name, (f'{documentation_prompt} \n {code}'))
    print('Documentation:')
    print(documentation)
    transpiler_prompt = f"You are a software engineer at Google. Using this code: \n {code} \nand this supplying documentation as a base: \n {documentation} \n Generate code in Ruby that matches its functionality and maintains parity with the given Python script."
    transpiled_code = await AsyncClient.create_completion(model_name, (f'{transpiler_prompt}'))
    print('Code transpiled.')
    print(transpiled_code)
    with open('latest.rb', 'w') as f:
        code_list = re.findall(r"```ruby(.*?)```", json.dumps(transpiled_code), re.DOTALL)
        for code in code_list:
            # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
            # and remove leading/trailing whitespaces
            code = code.replace("\\n", "\n").replace('\\"', '"').strip()
            f.write("%s\n" % code)

run(main())
# run(documentation_generator('blank'))
# run(typescript_transpiler())
# run(ruby_transpiler())