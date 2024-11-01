from objects import CreateObjetct

class Tables(CreateObjetct):
    def __init__(self) -> None:
        self.type = 'TABLE'
        super().__init__()
    
    
    def all_object(self) -> dict: 
        object_dict = {
                "TB_ENDERECO": """CREATE TABLE DEMO.TB_ENDERECO(
                                        ID NUMBER ,
                                        UF VARCHAR2(2),
                                        CIDADE VARCHAR2(100),
                                        BAIRRO VARCHAR2(100),
                                        RUA VARCHAR2(500),
                                        NUMERO VARCHAR2(5),
                                        CONSTRAINT PK_ENDERECO PRIMARY KEY (ID)
                                )""",

                "TB_TELEFONE": """CREATE TABLE DEMO.TB_TELEFONE(
                                        ID NUMBER,
                                        TIPO VARCHAR2(3) CHECK( TIPO IN ('CEL','COM')),
                                        DDD VARCHAR2(2),
                                        TELEFONE VARCHAR2(9),
                                        CONSTRAINT PK_TELEFONE PRIMARY KEY (ID)
                                )""",

                "TB_CLIENTE":  """ CREATE TABLE DEMO.TB_CLIENTE (
                                        ID NUMBER,
                                        PRIMEIRO_NOME VARCHAR2(30),
                                        SOBRENOME VARCHAR2(30),    
                                        GENERO VARCHAR2(1),
                                        CPF VARCHAR2(14),
                                        FK_ENDERECO NUMBER,
                                        FK_TELEFONE NUMBER,
                                        CONSTRAINT PK_CLIENTE PRIMARY KEY (ID),
                                        CONSTRAINT FK_CLIENTE_ENDERECO FOREIGN KEY(FK_ENDERECO) REFERENCES DEMO.TB_ENDERECO(ID),
                                        CONSTRAINT FK_CLIENTE_TELEFONE FOREIGN KEY(FK_TELEFONE) REFERENCES DEMO.TB_TELEFONE(ID)
                                    )"""
            }
        return object_dict

    def process_script(self):
        dictionary_object = self.all_object()
        super().process_script(type_object=self.type, object_dict=dictionary_object)