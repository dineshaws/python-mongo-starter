from fastapi import FastAPI

app = FastAPI()


@app.get('/', status_code=200)
def get_root():
    return {'Foo': 'BAR'}