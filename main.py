from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Return a message and 200 with doctest
    >>> from fastapi.testclient import TestClient
    >>> client = TestClient(app)
    >>> response = client.get("/")
    >>> response.status_code
    200
    >>> response.json()
    {'msg': 'Hello World'}
    """

    return {"msg": "Hello World"}
