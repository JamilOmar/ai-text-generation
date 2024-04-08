from ai import app
import os
import dotenv
dotenv.load_dotenv()
ai_app= app.create()
request = input("Define a request you would like to have: ")
result = ai_app.execute(request)
print(result)