from sequence import Sequences
from tables import Tables
from trigger import Trigger

if __name__ == '__main__':
    tables = Tables()
    sequences = Sequences()
    trigger = Trigger()    
    
    
    sequences.process_script()
    tables.process_script()
    trigger.process_script()    
    