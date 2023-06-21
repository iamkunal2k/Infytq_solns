# Problem Link
# https://infytq.onwingspan.com/web/en/viewer/hands-on/lex_auth_012727139457941504148_shared?collectionId=lex_auth_0125409722749255681063_shared&collectionType=Course&pathId=lex_auth_012748294791266304132_shared


#lex_auth_012727139457941504148
#Start writing your code here       

class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = 0

    def get_bill_id(self) :
        return self.__bill_id
    
    def get_bill_amount(self) :
        return self.__bill_amount
    
    def get_patient_name(self) :
        return self.__patient_name
    
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        medicine = 0
        for i in range(len(quantity_list)):
            medicine = medicine+quantity_list[i]*price_list[i]

        self.__bill_amount = consultation_fees+medicine 

x=Bill(1010,"Kunal")
x.calculate_bill_amount(1900,[11,12,13],[2,3,4])
print(x.get_bill_amount())