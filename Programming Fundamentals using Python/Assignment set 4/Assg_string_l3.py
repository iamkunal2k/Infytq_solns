#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    string =""
    sentence = data.split()
    vowels = "aeiouAEIOU"
    
    for i in sentence:
        if(len(i) == 1) :
            string += i
        else:
            for j in i:
                 if j not in set(vowels):
                     string += j
        string = string+ " "
    return string[0:-1]

data="I love Python"
print(sms_encoding(data))