from schema_database import create_table, start_conection
from client_data import create_csv
import pandas as pd
import os


def multi_insert(dataframe, tabela_destino):
    data = dataframe
    tabela = tabela_destino.upper()

    dict_inserts = {
        "TB_TELEFONE": """INSERT INTO TB_TELEFONE (TIPO, TELEFONE, DDD) VALUES (:1, :2, :3)""",
        "TB_ENDERECO": """INSERT INTO TB_ENDERECO (UF, CIDADE, BAIRRO, RUA, NUMERO) VALUES (:1, :2, :3, :4, :5)""",
        "TB_CLIENTE": """INSERT INTO TB_CLIENTE (PRIMEIRO_NOME, SOBRENOME, GENERO, CPF, FK_ENDERECO, FK_TELEFONE) VALUES (:1, :2, :3, :4, :5, :6)"""
    }

    if tabela in dict_inserts.keys():
        # converto os registros por linha em str e adiciono em tuplas
        list_tuple = [tuple(row[1]) for row in data.iterrows()]

        # 1000 tuplas se tornam 1 lista de tuplas  => [(),(),(),()]
        split_data = [list_tuple[i: i + 1000]
                      for i in range(0, len(list_tuple), 1000)]

        connection = start_conection()
        with connection:
            cursor = connection.cursor()
            insert_sql = dict_inserts.get(tabela)

            for data_100 in split_data:
                cursor.executemany(insert_sql, data_100, batcherrors=True)
                connection.commit()

                for error in cursor.getbatcherrors():
                    print("Error:  ", error.message,
                          "na linha:   ", error.offset)
    else:
        print(
            f'configuração feita para inserção em apenas 3 tabelas. {dict_inserts.keys}')


create_table()
create_csv(1000)
archive_path = os.getcwd()

# inserção de cada csv criado na oasta local
for archive_csv in sorted(os.listdir(archive_path), reverse=True):
    if archive_csv.endswith(".csv"):
        table_name = archive_csv.replace('.csv', '')
        full_path = os.path.join(archive_path, archive_csv)

        data = pd.read_csv(full_path, sep=',', encoding='UTF-8')
        multi_insert(dataframe=data, tabela_destino=table_name)
