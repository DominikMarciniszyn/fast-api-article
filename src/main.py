from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def ping():
    return {'result': 'Service is alive...'}


@app.get('/example')
async def example_endpoint():
    return { 'result': 'Example' }


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return { 'user_id': user_id }

