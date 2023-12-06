import cx_Oracle

def start_instant_client():
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instancia_oracle_cliente\instantclient_21_12")
        
    except Exception as error:
        if 'Oracle Client library has already been initialized' in str(error):
            return 'oracle já incializado'
             
            


def create_table ():
    start_instant_client()
    connection = cx_Oracle.connect(user="hr", password='hr', dsn="localhost/XEPDB1",encoding="UTF-8")
    cursor = connection.cursor()
    
    sql_table = [
                """CREATE TABLE TB_ENDERECO(
                        ID_ENDERECO NUMBER ,
                        ESTADO VARCHAR2(30),
                        UF CHAR(2),
                        CIDADE VARCHAR2(30),
                        BAIRRO VARCHAR2(30),
                        RUA VARCHAR2(30),
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
                    )"""
            ]
    
    
    with connection:
        for table in sql_table:
            try:
                cursor.execute(table)
                
                print(f'table {table }')

            except cx_Oracle.DatabaseError as e:
                error, = e.args  
                if error.code == 955:
                    pass
                else:
                    print(e)
    
    print('ok')

    
create_table()  

list_values = []

        

        
    

#    list_values = [row for row in cursor.execute("SELECT * FROM EMPLOYEES")]
#
#    tamanho_sublista = 20
#    subregistros = [list_values[i: i+ tamanho_sublista] for i in range(0, len(list_values),tamanho_sublista)]
#    
#    for data in subregistros:
#        cursor.executemany("""INSERT INTO EMPLOYEES_V2 
#                                (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL,PHONE_NUMBER, HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID)
#                            VALUES (:1, :2, :3, :4,:5,:6,:7,:8,:9,:10,:11)""", data)
#        connection.commit()