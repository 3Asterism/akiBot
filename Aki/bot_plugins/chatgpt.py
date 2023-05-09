import openai
from nonebot import on_command


@on_command('chatgpt', permission=lambda sender: sender.is_superuser)
async def getPic(session):
    openai.api_key = "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"

    messages = []
    while True:
        content = (await session.aget(prompt='User:')).strip()
        if content == "stop":
            break
        messages.append({"role": "user", "content": content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion
        answer = chat_response.choices[0].message.content
        await session.send(f'ChatGPT: {answer}')
        print(answer)
        messages.append({"role": "assistant", "content": answer})
