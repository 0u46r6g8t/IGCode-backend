from dotenv import load_dotenv
import os
from src.config import Debugger
from fastapi import FastAPI

load_dotenv()

class ServerFastapi(Debugger):
    def __init__(self):
        super().__init__()
        
    def __new__(cls) -> FastAPI:
        return FastAPI(
            title=os.environ['TITLE'],
            description=os.environ['DESCRIPTION'],
            version=os.environ['VERSION'],
            summary=os.environ['SUMMARY'],
            swagger_ui_init_oauth=os.environ['SWAGGER_UI_INIT_OAUTH'],            
            swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
        )    
        