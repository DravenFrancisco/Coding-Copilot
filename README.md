# Coding Copilot
 This is an experimental repo of Python functions that leverage Large Language Models (LLMs) to help users write code, including a code interpreter, documentation writer, and transpiler. 

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgements)
- [To-Do List](#todo)

## Features

The main program `coding_copilot.py` runs a chatbot style interface in the terminal similar to ChatGPT, but with a few extra features:

- Any code enclosed in backticks \`\`\` is immediately written to a new Python file so the user can immediately test it.
- The code file is fed back into the LLM in order to write accompanying documentation.
- All outputs from the chatbot is logged into `chat_history.md` for the user to read later.
- All outputs from the chatbot are also returned to the LLM, accompanied with a compression prompt, so that it can be stored as context that the bot can later call upon.
- Upon specifying a different programming language, the chatbot can be supplied both a code file and the accompanying documentation in order to transpile the code file into another programming language.

## Usage

To use the chatbot, simply run `coding_copilot.py` in an IDE such as Visual Studio Code. Later versions, however, should be possible to run from the command line terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was enabled by the [freeGPT Python package](https://github.com/Ruu3f/freeGPT) created by Ruu3f. While the plan for this project is to be ultimately used with locally installed Large Language Models and have dropin compatibility with OpenAI, freeGPT was used for the purposes of experimenting with prompt engineering.

## Todo

- [ ] Add in the ability for the script to be accessible from the command line terminal, or to interact with a GUI.
- [ ] Specify save and resource directories for all of the files generated and used by `coding_copilot.py`.
- [ ] Seperate functions such as writing documentation, transpiling, etc. into classes so that different preprompts can be used.
- [ ] Integrate locally deployed LLMs into the copilot's functionality.
- [ ] Save chatbot history and context in a more robust and modular way. (Currently they are saved in a Markdown file for users to visually see what is happening, but ideally the context ought to be stored within a JSON file or even an SQL database to enable Tree of Thoughts style prompting). 
