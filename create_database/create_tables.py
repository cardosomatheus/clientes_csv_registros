import connection_oracle 

class CreateTables:
    
    def __init__(self):
        self.connection = connection_oracle.connection()

    def process_script(self):
        print('Starting Process...')

        list_table_name = ["TB_ENDERECO","TB_TELEFONE","TB_CLIENTE"]
        for table in list_table_name:
            table = table.upper()
            
            if not self.check_table_exists(table_name = table):
                self.create_table(table_name = table)        

        print('Process completed.')


    def check_table_exists(self,table_name:str) -> bool:
        table_exists = "SELECT COUNT(*) IND_TABLE_EXIST FROM ALL_TABLES WHERE TABLE_NAME = :TABLE_NAME"
        
        with self.connection.cursor() as cursor:
            for row in cursor.execute(table_exists, TABLE_NAME= table_name):
                return False if row[0] == 0 else True

    def create_table(self,table_name:str) -> str:
        dir_tables = {"TB_ENDERECO" : """CREATE TABLE DEMO.TB_ENDERECO(
                                            ID NUMBER ,
                                            UF VARCHAR2(2),
                                            CIDADE VARCHAR2(100),
                                            BAIRRO VARCHAR2(100),
                                            RUA VARCHAR2(500),
                                            NUMERO VARCHAR2(5),
                                            CONSTRAINT PK_ENDERECO PRIMARY KEY (ID)
                                       )""",

                      "TB_TELEFONE" : """CREATE TABLE DEMO.TB_TELEFONE(
                                            ID NUMBER,
                                            TIPO VARCHAR2(3) CHECK( TIPO IN ('CEL','COM')),
                                            DDD VARCHAR2(2),
                                            TELEFONE VARCHAR2(9),
                                            CONSTRAINT PK_TELEFONE PRIMARY KEY (ID)
                                       )""",

                      "TB_CLIENTE" :  """ CREATE TABLE DEMO.TB_CLIENTE (
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
        print()
        print('\*************************************************************************************/')
        
        with self.connection.cursor() as cursor:
            cursor.execute(dir_tables.get(table_name))
            
            
            


