from openai import OpenAI
from ..common.engine_interface import EngineInterface

class OpenAIEngine(EngineInterface):
    def __init__(self , model) -> None:
        EngineInterface.__init__(self,"OPEN_AI_ENGINE", model,client =OpenAI())
    
    def execute(self , prompt:str) ->str:
        messages = [{"role":"user" , "content":prompt}]
        completion =self._client.chat.completions.create(model=self._model_name, messages=messages)
        return completion.choices[0].message.content;
        
        
        
    
        
    