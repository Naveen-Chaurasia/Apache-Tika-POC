
# it will only run whre playwright is installed

from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# return the full result
response = bot.ask("tell me 5 cat names")
print(response)

# return the result in streaming (chunks)
for chunk in bot.ask_stream("tell me a story about cats and dogs"):
    print(chunk)