import os
import openai
from openai import ChatCompletion
import gradio
from flask import Flask

client = ChatCompletion(api_key=os.environ.get("OPENAI_API_KEY"))

def api_calling(question, history):
    try:
        s = list(sum(history, ()))
        s.append(question)
        inp = ' '.join(s)
        response = client.create(
            messages=[
                {
                    "role": "user",
                    "content": inp
                }
            ],
            model="ft:gpt-3.5-turbo-0125:personal::9AKjioqu",
            temperature=0,
            max_tokens=1024,
            n=1,
            stop=None
        )
        message = response.choices[0].message.content
    except Exception as e:
        message = f"An error occurred: {str(e)}"
    return message

def update_chat(new_message, history):
    history = history or []
    output = api_calling(new_message, history)
    history.append((new_message, output))
    return history, None

app = Flask(__name__)

block = gradio.Blocks(theme=gradio.themes.Monochrome())

with block:
    gradio.Markdown("""<h1><center>Mental Health Chatbot</center></h1>""")
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(label="Type your message here")
    state = gradio.State()

    message.submit(update_chat, [message, state], [chatbot, state])

if __name__ == "__main__":
    app.run(debug=True)
    block.launch(debug=True)