def submit_addr():
    submit = input("Enter IP Address (Type x to End):  ")
    return submit

def make_octets(submit):
    octets = [""]
    index = 0
    for char in submit:
        if char == ".":
            octets.append("")
            index += 1
        else:
            octets[index]+= char
    return octets

def num_of_octets(octets):
    number_of_octets = len(octets)
    return number_of_octets

def check_ip_addr():
    valid = True # innocent until proven guilty...
    submit = submit_addr()
    octets = make_octets(submit)
    octet_count = num_of_octets(octets)
    if submit.upper() == "X":
        return
    elif octet_count != 4:
        print(submit + " does not have 4 octets, so it is not a valid IPv4 address") 
        return check_ip_addr()
    for octet in octets:
        try:
            octet = int(octet)
            assert(octet >= 0 and octet <=255)
        except:
            print(submit +  " is not a valid IPv4 Address. Only numbers between 0 and 255 are allowed in IPv4.")
            return check_ip_addr()
    print(submit + " is a valid IPv4 address.")
    return check_ip_addr()

check_ip_addr()
