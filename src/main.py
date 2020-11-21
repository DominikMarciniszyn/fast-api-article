from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def ping():
    return {'result': 'Service is alive...'}


@app.get('/example')
async def example_endpoint():
    return {'result': 'Example'}
