import connection_oracle


class CrateObjetct:
    def __init__(self):
        self.connection = connection_oracle.connection()

    def all_dicts(self, type: str) -> dict:
        "save dicts to create new objects"

        if type == "SEQUENCE":
            object_dict = {
                "SQ_CLIENTE": "CREATE SEQUENCE SQ_CLIENTE START WITH 1 INCREMENT BY 1",
                "SQ_ENDERECO": "CREATE SEQUENCE SQ_ENDERECO START WITH 1 INCREMENT BY 1",
                "SQ_TELEFONE": "CREATE SEQUENCE SQ_TELEFONE START WITH 1 INCREMENT BY 1"
            }

        elif type == "TRIGGER":
            object_dict = {
                "TGG_CLIENTE_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_CLIENTE_PK
                                        BEFORE INSERT ON TB_CLIENTE FOR EACH ROW
                                        BEGIN
                                            IF :NEW.ID IS NULL THEN
                                                :NEW.ID := SQ_CLIENTE.NEXTVAL;
                                            END IF;
                                        END;""",

                "TGG_ENDERECO_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_ENDERECO_PK
                                         BEFORE INSERT ON TB_ENDERECO FOR EACH ROW
                                         BEGIN
                                             IF :NEW.ID IS NULL THEN
                                                 :NEW.ID := SQ_ENDERECO.NEXTVAL;
                                             END IF;
                                         END;""",
                "TGG_TELEFONE_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_TELEFONE_PK
                                        BEFORE INSERT ON TB_TELEFONE FOR EACH ROW
                                        BEGIN
                                            IF :NEW.ID IS NULL THEN
                                                :NEW.ID := SQ_TELEFONE.NEXTVAL;
                                            END IF;
                                        END; """
            }

        elif type == "TABLE":
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

    def process_script(self, type: str):
        """
        process to create objects
        Args: type (str): [SEQUENCE, TRIGGER, TABLE]
        """

        type = type.upper()

        for key, value in self.all_dicts(type=type).items():
            if not self.check_object_exists(type=type, name=key):
                self.create_object(sql_create_object=value)

        print(f'Process completed for objects {type}.')

    def check_object_exists(self, type: str, name: str) -> bool:
        """
        Consult the object table and if the object does not yet exist, we try to create it
        Args: type (str): [SEQUENCE, TRIGGER, TABLE]
              name (str): object name
        """
        object_exists = """SELECT COUNT(*) IND_TABLE_EXIST 
                            FROM ALL_OBJECTS 
                           WHERE OBJECT_TYPE = :TYPE
                            AND OBJECT_NAME = :NAME"""

        with self.connection.cursor() as cursor:
            for row in cursor.execute(object_exists, TYPE=type, NAME=name):
                return False if row[0] == 0 else True

    def create_object(self, sql_create_object: str):
        """
        Create object using input sql
        Args:
            sql_create_object (str): sql for creating object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql_create_object)


