from .ai_engines import OpenAIEngine
from .common import EngineInterface
def create()-> EngineInterface:
    return OpenAIEngine("gpt-3.5-turbo")
