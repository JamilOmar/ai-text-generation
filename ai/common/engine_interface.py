class EngineInterface:
    _client=''
    _name =''
    _model_name = ''
    def __init__(self, name,model_name,client) -> None:
        self._name =name
        self._model_name = model_name
        self._client = client
        
    def execute(self, prompt:str)->str:
        pass
    def print_client(self) ->str:
        print(self._client)