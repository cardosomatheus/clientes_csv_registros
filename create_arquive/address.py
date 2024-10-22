from arquive import CheckArquive
from csv import DictWriter

class Address(CheckArquive):
    def __init__(self):
        self.file_name = 'TB_ENDERECO.CSV'
        super().__init__()

    
    def current_path(self):
        super().current_path()
    
    
    def remove_arquive(self):
        super().remove_arquive(file_name = self.file_name)
        


    def create_arquive(self, rows:int):
        self.remove_arquive()

        with open(self.file_name, 'a+', encoding='utf-8', newline='') as address:
            for row in range(rows):
                uf         = self.faker.estado()[0]
                cidade     = self.faker.city(),
                bairro     = self.faker.bairro()
                rua        = self.faker.street_name()
                num_casa   = self.faker.building_number()
                fieldnames = ['uf', 'cidade', 'bairro', 'rua', 'num_casa']
                writer     = DictWriter(address, fieldnames=fieldnames)

                if address.tell() == 0:
                    writer.writeheader()

                writer.writerow({'uf': uf, 'cidade': cidade[0], 'bairro': bairro, 'rua': rua, 'num_casa': num_casa})
        super().end_message(self.file_name)