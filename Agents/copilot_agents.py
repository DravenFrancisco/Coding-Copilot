from openai import OpenAI
from asyncio import run
import datetime
import os
import json
import re

class Documenter():
    def __init__():
        pass

class Transpiler():
    def __init__():
        pass
    
# async def ruby_transpiler():
#     script = open('latest.py', 'r')
#     code = script.read()
#     documentation_prompt = "Describe what this Python script is doing in as few words as possible. Make sure to list its input and output variables. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible."
#     documentation = await create_completion(MODEL_NAME, (f'{documentation_prompt} \n {code}'))
#     print('Documentation:')
#     print(documentation)
#     transpiler_prompt = f"You are a software engineer at Google. Using this code: \n {code} \nand this supplying documentation as a base: \n {documentation} \n Generate code in Ruby that matches its functionality and maintains parity with the given Python script."
#     transpiled_code = await create_completion(MODEL_NAME, (f'{transpiler_prompt}'))
#     print('Code transpiled.')
#     print(transpiled_code)
#     with open('latest.rb', 'w') as f:
#         code_list = re.findall(r"```ruby(.*?)```", json.dumps(transpiled_code), re.DOTALL)
#         for code in code_list:
#             # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
#             # and remove leading/trailing whitespaces
#             code = code.replace("\\n", "\n").replace('\\"', '"').strip()
#             f.write("%s\n" % code)
    
# async def typescript_transpiler():
#     script = open('latest.py', 'r')
#     code = script.read()
#     documentations_prompt = "Describe what this Python script is doing in as few words as possible. Make sure to list its input and output variables. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible."
#     documentation = await  create_completion(MODEL_NAME, (f'{documentation_prompt} \n {code}'))
#     print('Documentation:')
#     print(documentation)
#     transpiler_prompt = f"You are a software engineer at Google. Using this code: \n {code} \nand this supplying documentation as a base: \n {documentation} \n Generate code in Typescript that matches its functionality and maintains parity with the given Python script."
#     transpiled_code = await create_completion(MODEL_NAME, (f'{transpiler_prompt}'))
#     print('Code transpiled.')
#     with open('latest.ts', 'w') as f:
#         code_list = re.findall(r"```typescript(.*?)```", json.dumps(transpiled_code), re.DOTALL)
#         for code in code_list:
#             # Replace escaped newlines with actual newlines, escaped double quotes with actual double quotes
#             # and remove leading/trailing whitespaces
#             code = code.replace("\\n", "\n").replace('\\"', '"').strip()
#             f.write("%s\n" % code)