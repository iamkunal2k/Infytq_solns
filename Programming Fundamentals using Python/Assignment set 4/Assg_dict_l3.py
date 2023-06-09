# lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    p = 0
    e = 0
    o = 0

    for i in range(1, len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P':
            p += 1
        elif patient_medical_speciality_list[i] == 'E':
            e += 1
        elif patient_medical_speciality_list[i] == 'O':
            o += 1

    if p > e and p > o:
        max = p
    elif o > p and o > e:
        max = o
    else:
        max = e

    if max == p:
        speciality = "Pediatrics"
    elif max == e:
        speciality = "ENT"
    else:
        speciality = "Orthopedics"
    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [
    301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
