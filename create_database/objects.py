import connection_oracle

class CreateObjetct:
    def __init__(self):
        self.connection = connection_oracle.connection()


    def process_script(self, type_object :str, object_dict :dict):
        """
        process to create objects
        Args: type_object (str): [SEQUENCE, TRIGGER, TABLE]
        """
        
    
        type_object = type_object.upper()

        for key, value in object_dict.items():
            if not self.check_object_exists(type_object,key):
                self.create_object(sql_create_object=value)

        print(f'Process completed for objects {type_object}.')


    def check_object_exists(self, object_name :str, name :str) -> bool:
        """
        Consult the object table and if the object does not yet exist, we try to create it
        Args: OBJECT_TYPE (str): [SEQUENCE, TRIGGER, TABLE]
              name (str): object name
        """
        object_exists = """SELECT COUNT(*) IND_TABLE_EXIST 
                            FROM ALL_OBJECTS 
                           WHERE OBJECT_TYPE = :TYPE
                            AND OBJECT_NAME = :NAME"""

        with self.connection.cursor() as cursor:
            for row in cursor.execute(object_exists, TYPE=object_name, NAME=name):
                return False if row[0] == 0 else True

    
    def create_object(self, sql_create_object: str):
        """
        Create object using input sql
        Args:
            sql_create_object (str): sql for creating object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql_create_object)


