from objects import CreateObjetct

class Trigger(CreateObjetct):
    def __init__(self) -> None:
        self.type = 'TRIGGER'
        super().__init__()
    
    
    
    def all_object(self) -> dict: 
        object_dict = {
            "TGG_CLIENTE_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_CLIENTE_PK
                                    BEFORE INSERT ON TB_CLIENTE FOR EACH ROW
                                    BEGIN
                                        IF :NEW.ID IS NULL THEN
                                            :NEW.ID := SQ_CLIENTE.NEXTVAL;
                                        END IF;
                                    END;""",

            "TGG_ENDERECO_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_ENDERECO_PK
                                        BEFORE INSERT ON TB_ENDERECO FOR EACH ROW
                                        BEGIN
                                            IF :NEW.ID IS NULL THEN
                                                :NEW.ID := SQ_ENDERECO.NEXTVAL;
                                            END IF;
                                        END;""",
            "TGG_TELEFONE_PK": """ CREATE OR REPLACE TRIGGER DEMO.TGG_TELEFONE_PK
                                    BEFORE INSERT ON TB_TELEFONE FOR EACH ROW
                                    BEGIN
                                        IF :NEW.ID IS NULL THEN
                                            :NEW.ID := SQ_TELEFONE.NEXTVAL;
                                        END IF;
                                    END; """
        }

        return object_dict

    def process_script(self):
        dictionary_object = self.all_object()
        super().process_script(type_object=self.type, object_dict=dictionary_object)  
