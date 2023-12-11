require 'openai'

model_name = 'gpt4'

def add_comments_to_code(code)
  # Set up OpenAI API credentials

  # Generate comments using OpenAI GPT-3
  prompt = "Add descriptive comments to the following Ruby code: \\
" + code
  response = OpenAI.Completion.create(model: model_name, prompt: prompt)

  # Extract the generated comment from the response
  generated_comment = response['choices'][0]['text'].strip

  # Add the comment to the code
  code_with_comment = code + "\\
# " + generated_comment

  return code_with_comment
end

# Example usage
ruby_code = File.read('latest.rb')
code_with_comment = add_comments_to_code(ruby_code)
puts code_with_comment
