# def main():
#     print("Hello from week-5!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}