from objects import CreateObjetct

class Sequences(CreateObjetct):
    def __init__(self) -> None:
        self.type = "SEQUENCE"
        super().__init__()
    
    
    def all_object(self) -> dict: 
            object_dict = {
                "SQ_CLIENTE": "CREATE SEQUENCE SQ_CLIENTE START WITH 1 INCREMENT BY 1",
                "SQ_ENDERECO": "CREATE SEQUENCE SQ_ENDERECO START WITH 1 INCREMENT BY 1",
                "SQ_TELEFONE": "CREATE SEQUENCE SQ_TELEFONE START WITH 1 INCREMENT BY 1"
            }
            return object_dict

    def process_script(self):
        dictionary_object = self.all_object()
        super().process_script(type_object=self.type, object_dict=dictionary_object)