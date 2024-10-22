from arquive import CheckArquive
from random import choice
from csv import DictWriter

class Client(CheckArquive):
    def __init__(self):
        self.file_name = 'TB_CLIENTE.CSV'
        super().__init__()

    
    def current_path(self):
        super().current_path()
    
    
    def remove_arquive(self):
        super().remove_arquive(file_name = self.file_name)

        
    def gender_name (self, gender:str) -> list:   
        if gender == 'M':
            first_name  = self.faker.first_name_male()
            second_name = self.faker.last_name_male()
        elif gender == 'F':
            first_name  = self.faker.first_name_female()
            second_name = self.faker.last_name_female()        

        return first_name,second_name


    def create_arquive(self, rows:int):
        self.remove_arquive()

        with open(self.file_name, 'a+', encoding='utf-8', newline='') as client:
            for row in range(rows):
                genero = choice(['M', 'F'])
                estado = self.faker.estado_nome()
                cpf    = self.faker.cpf()
                first_name, second_name = self.gender_name(gender=genero)

                if cpf not in client:
                    fieldnames = ['nome', 'sobrenome', 'genero','cpf']
                    writer = DictWriter(client, fieldnames=fieldnames)

                    if client.tell() == 0:
                        writer.writeheader()                        

                    writer.writerow({'nome': first_name, 'sobrenome': second_name, 'genero': genero,'cpf': cpf})
        
        super().end_message(self.file_name)