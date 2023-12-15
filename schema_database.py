import oracledb  as cx_Oracle


def start_conection():
    """inicia a instancia oracle"""
    try:
        cx_Oracle.init_oracle_client(
            lib_dir=r"C:\instancia_oracle_cliente\instantclient_21_12")

    except Exception as error:
        if 'Oracle Client library has already been initialized' in str(error):
            return 'oracle já incializado'
    
    connection = cx_Oracle.connect( user="hr", password='hr', dsn="localhost/XEPDB1", encoding="UTF-8")
    return connection


def create_table():
    """criação das tabelas na base de dados"""
    connection = start_conection()
    cursor = connection.cursor()

    table_and_sequence = [
        """CREATE TABLE TB_ENDERECO(
                        ID_ENDERECO NUMBER ,
                        UF CHAR(2),
                        CIDADE VARCHAR2(100),
                        BAIRRO VARCHAR2(100),
                        RUA VARCHAR2(500),
                        NUMERO VARCHAR2(5),
                        CONSTRAINT PK_ENDERECO PRIMARY KEY (ID_ENDERECO)
                    )""",

        """
            CREATE TABLE TB_TELEFONE(
                        ID_TELEFONE NUMBER,
                        TIPO CHAR(3) CHECK( TIPO IN ('CEL','COM')),
                        DDD CHAR(2),
                        TELEFONE VARCHAR2(9),
                        CONSTRAINT PK_TELEFONE PRIMARY KEY (ID_TELEFONE)

                    )""",

        """ CREATE TABLE TB_CLIENTE (
                        ID_CLIENTE NUMBER,
                        PRIMEIRO_NOME VARCHAR2(30),
                        SOBRENOME VARCHAR2(30),    
                        GENERO CHAR(1),
                        CPF VARCHAR2(14),
                        FK_ENDERECO NUMBER,
                        FK_TELEFONE NUMBER,
                        CONSTRAINT PK_CLIENTE PRIMARY KEY (ID_CLIENTE),
                        CONSTRAINT FK_CLIENTE_ENDERECO FOREIGN KEY(FK_ENDERECO) REFERENCES TB_ENDERECO(ID_ENDERECO),
                        CONSTRAINT FK_CLIENTE_TELEFONE FOREIGN KEY(FK_TELEFONE) REFERENCES TB_TELEFONE(ID_TELEFONE)
                    )""",
        "CREATE SEQUENCE SEQUENCE_CLIENTE START WITH 1 INCREMENT BY 1",
        "CREATE SEQUENCE SEQUENCE_ENDERECO START WITH 1 INCREMENT BY 1",
        "CREATE SEQUENCE SEQUENCE_TELEFONE START WITH 1 INCREMENT BY 1"
        ]

    trigger_key = [""" CREATE OR REPLACE TRIGGER TGG_CLIENTE_PK
                        BEFORE INSERT ON TB_CLIENTE FOR EACH ROW
                        BEGIN
                            IF :NEW.ID_CLIENTE IS NULL THEN
                                :NEW.ID_CLIENTE := SEQUENCE_CLIENTE.NEXTVAL;
                            END IF;
                        END;
                    """,
                    """
                        CREATE OR REPLACE TRIGGER TGG_ENDERECO_PK
                        BEFORE INSERT ON TB_ENDERECO FOR EACH ROW
                        BEGIN
                            IF :NEW.ID_ENDERECO IS NULL THEN
                                :NEW.ID_ENDERECO := SEQUENCE_ENDERECO.NEXTVAL;
                            END IF;
                        END;
                    """,
                    """
                        CREATE OR REPLACE TRIGGER TGG_TELEFONE_PK
                        BEFORE INSERT ON TB_TELEFONE FOR EACH ROW
                        BEGIN
                            IF :NEW.ID_TELEFONE IS NULL THEN
                                :NEW.ID_TELEFONE := SEQUENCE_TELEFONE.NEXTVAL;
                            END IF;
                        END;
                    """
                   ]

    with connection:
        # tables and sequences
        for script in table_and_sequence:
            try:
                cursor.execute(script)

            except cx_Oracle.DatabaseError as e:
                error, = e.args
                if error.code == 955:
                    pass
                else:
                    print(e)
                    
        # triggers
        for trigger in trigger_key:
            cursor.execute(trigger)
            
        connection.commit()

