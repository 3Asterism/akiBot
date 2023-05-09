import openai

openai.api_key = "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"

messages = []
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion
    answer = chat_response.choices[0].message.content
    print(f'ChatGPT: {answer}')
    messages.append({"role": "assistant", "content": answer})
