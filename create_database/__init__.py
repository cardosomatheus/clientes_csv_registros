from create_objects import CreateObjetct

if __name__ == '__main__':
    object = CreateObjetct()
    
    object.process_script("SEQUENCE")
    object.process_script("TABLE")
    object.process_script("TRIGGER")    