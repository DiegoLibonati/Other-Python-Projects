text = input("> ")

emojis = {":D":"😀", "xD":"😆", ":)":"🙂", ":$":"🤑","X_X":"😵"}

while text != "salir":
    for text_emoji,emoji in emojis.items():
        text = text.replace(text_emoji, emoji)

    print(text)
    text = input("> ")