from schema_database import create_table, start_conection
import pandas as pd



data = pd.read_csv(r"C:\git_matheus\Criacao-de-csv-\tb_telefone.csv", sep=',', encoding='UTF-8')

#list_tuple = [tuple(row[1]) for row in data.iterrows()]
#
#split_data = [list_tuple[i: i+ 100] for i in range(0, len(list_tuple),100)]
#
#    
#connection = start_conection()
#print(split_data[0])

#data.info()

#dtype_phone = {}


#with connection:
#    for data_100 in split_data:
#        insert_phone = """INSERT INTO TB_TB_TELEFONE (TIPO, TELEFONE, DDD) VALUES (:1, :2 :3)"""
#        
#        cursor = connection.cursor()        
#        cursor.executemany(insert_phone, data_100)
#        connection.commit()
        
        
        
        
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