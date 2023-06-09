#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    result = [0,0,0]
    for x,y  in word_dict.items():
        if x == y:
            result[0] += 1
        elif len(x) == len(y):
            count = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    count += 1
            if count <= 2:
                result[1] += 1
            else :
                result[2] += 1
        else:
            result[2] += 1
            
    return result
                
        

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))