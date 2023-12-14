#   BIBLIOTECAS
from faker import Faker
from random import choice, randint
import csv
import pandas as pd
from schema_database import start_conection


def create_csv(quantidade):
    f = Faker('pt_BR')
    #   telefones

    with open('tb_telefone.csv', 'a+', encoding='utf-8', newline='') as telefones_csv:
        for cadastro in range(quantidade):
            tipo_telefone = choice(['CEL', 'COM'])
            ddd_telefone  = f.msisdn()[2:4]
            num_telefone  = f.msisdn()[4:]

            if ddd_telefone and num_telefone not in telefones_csv:
                fieldnames = ['tipo', 'telefone', 'ddd']
                writer     = csv.DictWriter(telefones_csv, fieldnames=fieldnames)

                if telefones_csv.tell() == 0:
                    writer.writeheader()

                writer.writerow(
                    {'tipo': tipo_telefone, 'telefone': num_telefone, 'ddd': ddd_telefone})
            else:
                cadastro -= 1


    #   endereços dos clientes
    with open('tb_endereco.csv', 'a+', encoding='utf-8', newline='') as enderecos_csv:
        for cadastro in range(quantidade):
            uf         = f.estado()[0]
            cidade     = f.city(),
            bairro     = f.bairro()
            rua        = f.street_name()
            num_casa   = f.building_number()
            fieldnames = ['sigla_uf', 'cidade', 'bairro', 'rua', 'num_casa']
            writer     = csv.DictWriter(enderecos_csv, fieldnames=fieldnames)

            if enderecos_csv.tell() == 0:
                writer.writeheader()

            writer.writerow(
                {'sigla_uf': uf, 'cidade': cidade[0], 'bairro': bairro, 'rua': rua, 'num_casa': num_casa})

    
    #   cliente
    connection = start_conection()
    cursor = connection.cursor()
    with connection:
        with open('tb_cliente.csv', 'a+', encoding='utf-8', newline='') as clientes_csv:
            for cadastro in range(quantidade):
                genero = choice(['M', 'F'])
                estado = f.estado_nome()
                cpf    = f.cpf()

                if genero == 'M':
                    primeiro_nome = f.first_name_male()
                    sobrenome     = f.last_name_male()

                elif genero == 'F':
                    primeiro_nome = f.first_name_female()
                    sobrenome     = f.last_name_female()

                if cpf not in clientes_csv:
                    fieldnames = ['nome', 'sobrenome', 'genero','cpf', 'fk_endereco', 'fk_telefone']
                    writer = csv.DictWriter(
                        clientes_csv, fieldnames=fieldnames)

                    if clientes_csv.tell() == 0:
                        writer.writeheader()

                    cursor.execute('SELECT NVL(MAX(ID_ENDERECO),0)  FROM TB_ENDERECO')
                    max_fk_endereco = cursor.fetchone()[0]
                    
                    if max_fk_endereco == 0:
                        fk_endereco = randint(1,quantidade)
                    else:
                        fk_endereco = randint(1,max_fk_endereco)
                        

                    cursor.execute('SELECT NVL(MAX(ID_TELEFONE),0) FROM TB_TELEFONE')
                    max_fk_telefone = cursor.fetchone()[0]
                    
                    if max_fk_telefone == 0:
                       fk_telefone = randint(1,quantidade)
                    else:
                       fk_telefone = randint(1,max_fk_telefone)

                    writer.writerow({'nome': primeiro_nome, 'sobrenome': sobrenome, 'genero': genero,
                                       'cpf': cpf, 'fk_endereco': fk_endereco, 'fk_telefone': fk_telefone})


create_csv(10)