from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

# Registering App Routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# For Debuging Purpose
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)