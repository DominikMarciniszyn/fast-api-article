from fastapi import FastAPI


app = FastAPI()


def ping():
    return {'result': 'Service is alive...'}


async def example_endpoint():
    return {'result': 'Example'}
