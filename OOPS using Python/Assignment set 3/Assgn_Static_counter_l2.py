# Problem Link
# https://infytq.onwingspan.com/web/en/viewer/hands-on/lex_auth_012751870201536512237_shared?collectionId=lex_auth_0125409722749255681063_shared&collectionType=Course&pathId=lex_auth_0127475769196216322339_shared

#lex_auth_012751870201536512237
#Start writing your code here

class Ticket:
    counter=0
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = None

    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_destination(self):
        return self.__destination
    
    def validate_source_destination(self):
        if self.__source.lower()=="delhi" and self.__destination.lower() in ["mumbai", "chennai", "pune","kolkata"]:
            return True
        else:
            return False
    
    def generate_ticket(self):
        if self.validate_source_destination():
            id="D"
            Ticket.counter+=1
            id+=self.__destination[0]
            if Ticket.counter<=9:
                id+="0"+str(Ticket.counter)
            else:
                id+=str(Ticket.counter)
            self.__ticket_id=id
        return self.__ticket_id
        