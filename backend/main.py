from fastapi import FastAPI
from groq import Groq
from config import settings

app = FastAPI(tiitle="zoo")
client = Groq(api_key=settings.GROQ_API_KEY)
chat_history = []
system_message = {"role":"system","content":"you are a helpful assistance in zoople technologies where you should convice users to take cources in zoople ,so you should have the knowledge of all the courses and the benefits of taking the courses"}
chat_history.append(system_message)
@app.get("/")
def index():
    return {"ErrorCode":0 ,"Data":{},"message":"succesful"}

@app.get("/query")
def query(q:str):
    user_message = {"role":"user","content":q}
    chat_history.append(user_message)
    chat_completion = client.chat.completions.create(messages=chat_history,model ="llama-3.3-70b-versatile", max_tokens=1024,top_p=1,stream=False,stop=None,)

    answer = chat_completion.choices[0].message.content
    if answer:
        return {"ErrorCode":0 ,"Data":answer,"message":"succesful"}
    else:
        return {"ErrorCode":1 ,"Data":"try later","message":"failed"}

