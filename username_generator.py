import random

def main():

    if __name__ == "__main__":
        name_of_user = "Zeyad Mohamad"
        for i in range(5):
            generate_username(name_of_user)

def generate_username(name_of_user):
    
    # Constraints
    min_capital = 2
    min_special = 2
    min_digits = 2
    min_len = 8
    special_char = ["@", "#", "$", "&"]

    # variable to store generated username
    username = ""

    # remove space from name of user and making it in lower case
    name_of_user = "".join(name_of_user.split())
    name_of_user = name_of_user.lower()

    # calculate minimum characters that we need to take from name of user
    min_char_from_user = min_len - min_digits - min_special
    
    # take required part from name
    count = 0
    for i in range(random.randint(min_char_from_user,len(name_of_user))):
        if count < min_capital:
            username += name_of_user[i].upper()
            count += 1
        else:
            username += name_of_user[i]

    # temp_list to store digits and special_chars so that they can be shuffled before adding to username
    temp_list = []

    # add required digits
    for i in range(min_digits):
        temp_list.append(str(random.randint(0,9)))
    
    # append special characters
    for i in range(min_special):
        temp_list.append(special_char[random.randint(0,len(special_char)-1)])
    
    # shuffle the list
    random.shuffle(temp_list)
    username += "".join(temp_list)
    print(username)

main()




