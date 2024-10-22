from arquive import CheckArquive
from random import choice
from csv import DictWriter


class Phone(CheckArquive):
    def __init__(self):
        self.file_name = 'TB_TELEFONE.CSV'
        super().__init__()

    
    def current_path(self):
        super().current_path()
    
    
    def remove_arquive(self):
        super().remove_arquive(file_name = self.file_name)

        
    def create_arquive(self, rows:int):
        self.remove_arquive()
        
        with open(self.file_name, 'a+', encoding='utf-8', newline='') as phone:
            for row in range(rows):
                type   = choice(['CEL', 'COM'])
                ddd    = self.faker.msisdn()[2:4]
                number = self.faker.msisdn()[4:]

                if ddd and number not in phone:
                    fieldnames = ['tipo', 'numero', 'ddd']
                    writer     = DictWriter(phone, fieldnames=fieldnames)

                    if phone.tell() == 0:
                        writer.writeheader()

                    writer.writerow({'tipo': type, 'numero': number, 'ddd': ddd})
                else:
                    cadastro -= 1
                    
        super().end_message(self.file_name)