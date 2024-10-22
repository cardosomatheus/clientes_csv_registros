from faker import Faker
import os


class CheckArquive:
    def __init__(self):
        self.faker = Faker('pt_BR')
        self.file_path = os.getcwd()


    def current_path(self):
        os.system('cls')
        print(f'Current path: {self.file_path}')


    def remove_arquive(self, file_name: str):
        file_name = file_name.upper()
        if not file_name.endswith('.CSV'):
            file_name = file_name + '.CSV'

        if file_name in os.listdir(self.file_path):
            os.remove(file_name)


    def end_message(self,file_name: str):
        print(f'File {file_name} created successfully')
