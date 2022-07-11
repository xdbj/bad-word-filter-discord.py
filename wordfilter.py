filtered_words = ["ex 1", "ex 2" "ex 3"]

@bot.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
         await msg.delete()
    await bot.process_commands(msg)
