from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/") # inside the cotation is the path operator
async def root():
    return {'massage' : 'welcome to my api'}

# so the app is our api instance 
# .get is the https method
# ("/") inside we can specify the path

@app.get("/posts")
def get_posts():
    return {"post" : "this is my post"}

# post is like like giving data to the api
@app.post("/createpost")
def post(payload: dict = Body(...)):
    print(payload)
    # return {'Massage' : 'The post was created successfully'}
    return {'New post' : f'Title:{payload['Title']}, Content:{payload['content']}'}