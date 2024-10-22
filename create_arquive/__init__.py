from phone import Phone
from address import Address
from client import Client

if __name__ == '__main__':
    phone   = Phone()
    address = Address()
    cliente = Client()
    rows = 10

    phone.create_arquive(rows=rows)
    address.create_arquive(rows=rows)
    cliente.create_arquive(rows=rows)