# lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    # start writing your code here
    count = 0
    result = ''
    for i in sentence.split():
        if count % 2 == 0:
            result += i[::-1]+' '
        else:
            vowels = ''
            consonants = ''
            for j in i:
                if j.lower() in ['a', 'e', 'i', 'o', 'u']:
                    vowels += j
                else:
                    consonants += j
            result += consonants+vowels+' '
        count += 1
    return result.strip()


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
