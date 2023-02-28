
# it will only run whre playwright is installed

from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# return the full result
bot.ask("give me only chemical reaction for the production of orthosilicic acid")
bot.ask("convert above reaction into grams of chemicals required")
response=bot.ask("convert above visualisation into csv file")
print(response)

# # return the result in streaming (chunks)
# for chunk in bot.ask_stream("tell me a story about cats and dogs"):
#     print(chunk)