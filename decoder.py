#Ephraim Nicolas COP3502C
def decode(new_password):
#Ephraim Nicolas COP3502C
    original_password = ""
    for element in new_password:
        nums = str(int(element) - 3)
        original_password += nums
    return original_password
