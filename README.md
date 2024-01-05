# Coding Copilot

This is an experimental repo of Python functions that leverage Large Language Models (LLMs) to help users write code.

## Roadmap

- [ ] replace `bot_context.md` with more robust context storage method
- [ ] pipeline compression and topic output so that it sends those completion requests while user is responding to chatbot
- [ ] add JSON prompt config file to `resource_files` folder so system, compression, and documentation prompts can be edited and experimented with more easily 

## Updates

### 2024-01-05:
- removed dependency on [freeGPT Python package](https://github.com/Ruu3f/freeGPT/)
- switched to OpenAI's Python library for drop-in compatibility
- now operates using locally hosted LLMs using [LM Studio's API endpoint](https://lmstudio.ai/)
- cleaned up folders so that there's clear separation between config files and output files
- upon quitting, chatbot now automatically writes documentation for `latest.py` to `Documentation.md`
- moved transpiler functions to `copilot_agents.py`