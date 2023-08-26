import re
import json

# global variables #
customer_list = []
customer={}

# Main User Interface #

def main():
    user_choice()

def display_menu():
    print(
        """
        Welcome to ACME Travels System!
        Please choose an option. For example, if you want to list all customers, input '1'

        Menu:
        1. List all customers
        2. Search for customers
        3. Add new customer
        4. Update existing customer
        5. Delete customer
        6. Save and Export
        7. Exit
        """
)

def return_choice(function):
    return_choice = input('return to main? y/n:' )
    while return_choice != 'y' and return_choice !='n':
        return_choice = input('return to main? y/n:' )
    if return_choice == 'y':
        return main()
    else:
        return function()

# Utiilty #
def customer_search_initiate_validation(customer_name1):                 #Return Object Datatype
    customer_name = customer_name1
    input_without_spaces = customer_name.replace(" ", "")
    customer_name_validation = input_without_spaces.isalpha()
    while customer_name_validation != True:
        print('Please enter alphabetic letters only')
        customer_name = input('Enter customer\'s name: ')
        input_without_spaces= customer_name.replace(" ", "")
        customer_name_validation = input_without_spaces.isalpha()

    if customer_name_validation == True:
        for customer in customer_list:
            if customer['name'] == customer_name:
                print('Existing customer found')
                return customer
        print('customer not found')
        return False

def email_validator(email_address):                                     #Return validated email address
    email_to_validate = email_address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'       #r define raw string where \ does not escape
    validated_email = re.match(pattern, email_to_validate)
    while validated_email == None:
        print("Enter valid email Address")
        email_to_validate = input('Enter the customer\'s email address: ')
        validated_email = re.match(pattern, email_to_validate)
    return email_to_validate

def phone_number_validator(new_phone_number):                           #Return validated Phone number
    phone_number_to_validate = new_phone_number
    pattern = r'^[0-9]{0,15}$'
    validated_phone_number = re.match(pattern, phone_number_to_validate) 
    while validated_phone_number == None:
        print("Enter valid phone number")
        phone_number_to_validate = input('Enter the customer\'s phone number: ')
        validated_phone_number = re.match(pattern, phone_number_to_validate)
    return int(phone_number_to_validate)

def choice_validator(choice):                           #Return validated Phone number
    choice_to_validate = choice
    pattern = r'^[0-9]{0,2}$'
    validated_choice = re.match(pattern, choice_to_validate) 
    while validated_choice == None:
        print("Enter valid choice")
        choice_to_validate = input('Enter the choice between 1 to 7: ')
        validated_choice = re.match(pattern, choice_to_validate) 
    return int(choice_to_validate)



# User input carousell

def list_all_customers():
    if len(customer_list) > 0:
       for customer in customer_list:
            print(
                """
                'name:' %s
                'email:' %s
                'phone_number:' %d
                """
                % (customer['name'], customer['email'], customer['phone_number'])
            )
    else:
        print('No customers in record')
    return_choice(list_all_customers)

def search_for_customer():
    
    customer_name= input('search for customer: ')
    print('searched for customer name: ',customer_name)
    validated_customer = customer_search_initiate_validation(customer_name)
    
    if (validated_customer):
        print(
            """
            'name:' %s
            'email:' %s
            'phone_number:' %s            
            """
            % (validated_customer['name'], validated_customer['email'], validated_customer['phone_number'])
        )
    else:
        print("no customer found")
    return_choice(search_for_customer)

def add_new_customer():

    proceed = input('Proceed to enter new customer details? y/n: ')

    while proceed != 'y' and proceed !='n':
        proceed = input('Invalid response. Enter new customer details? y/n: ')

    if proceed == 'n':
        return_choice(add_new_customer)
    elif proceed == 'y':
        pass

    confirmation = "n"

    while confirmation == "n":
        new_customer_name = input('Enter the new customer\'s name: ')

        for customer in customer_list:
            while new_customer_name == customer['name']:
                print('name already exists')
                new_customer_name = input('Enter the new customer\'s name: ')

        validated_new_customer_name = new_customer_name.replace(" ","").isalpha()
        
        while validated_new_customer_name != True:
            new_customer_name = input('Enter the new customer\'s name (alphabets only): ')
            validated_new_customer_name = new_customer_name.replace(" ","").isalpha()
        
        new_email_address = input('Enter the customer\'s email address: ')
        validated_email_address = email_validator(new_email_address)

        new_phone_number = input('Enter the customer\'s phone number: ')
        validated_phone_number = phone_number_validator(new_phone_number)

        customer_entry = {
            'name': new_customer_name.strip(),
            'email': validated_email_address.strip(),
            'phone_number': validated_phone_number
        }

        print (
                """
                Entered particulars:
                name: %s
                email: %s
                phone_number: %d
                """
                %(new_customer_name, validated_email_address, validated_phone_number)
        )

        confirmation = input('Save customer details? y/n: ')
        while confirmation != 'y' and confirmation !='n':
            print('enter valid choice')
            confirmation = input('Save customer details? y/n: ')
        if confirmation == 'y':
            customer_list.append(customer_entry)
            print('customer details confirmed!')
            print(customer_list)
            main()
        elif confirmation == 'n':
            return_choice(add_new_customer)

def update_existing_customer():

        confirm = 'n'
        customer_to_search = input('search for customer by name: ')
        print('Customer searched: ', customer_to_search)

        found_customer = customer_search_initiate_validation(customer_to_search)  #return customer or print no customer found

        if found_customer:
            print (found_customer)
            confirm = input('Update this customer? y/n: ')

            while confirm != 'y' and confirm !='n':
                print('Enter valid confirmation y/n')
                confirm = input('Invalid response. Update this customer? y/n: ')
                
            if confirm == 'y':
                new_customer_name = input('Enter updated customer\'s name: ')
                validated_new_customer_name = new_customer_name.replace(" ","").isalpha()
                
                while validated_new_customer_name != True:
                    new_customer_name = input('Enter updated customer\'s name (alphabets only): ')
                    validated_new_customer_name = new_customer_name.replace(" ","").isalpha()
                    
                new_email_address = input('Enter updated customer\'s email address: ')
                validated_email_address = email_validator(new_email_address)

                new_phone_number = input('Enter updated customer\'s phone number: ')
                validated_phone_number = phone_number_validator(new_phone_number)

                customer_entry = {
                    'name': new_customer_name.strip(),
                    'email': validated_email_address.strip(),
                    'phone_number': validated_phone_number
                }

                found_customer_index = customer_list.index(found_customer)
                customer_list[found_customer_index] = customer_entry
                print('Customer updated:')
                print(customer_entry)

                return_choice(update_existing_customer)                
            else:
                return_choice(update_existing_customer)
        else:
            return_choice(update_existing_customer)


def delete_customer():

        confirm = 'n'
        customer_to_search = input('search for customer to delete by name: ')
        print('Customer searched: ', customer_to_search)

        found_customer = customer_search_initiate_validation(customer_to_search)  #return customer or print no customer found
        if found_customer:
            print (found_customer)
            confirm = input('delete this customer? y/n: ')

            while confirm != 'y' and confirm !='n':
                print('Enter valid confirmation y/n')
                confirm = input('Invalid response. Delete this customer? y/n: ')
                
            if confirm == 'y':
            
                found_customer_index = customer_list.index(found_customer)
                del customer_list[found_customer_index]
                print('Customer data deleted')

                return_choice(delete_customer)

            else:
                    return_choice(delete_customer)
        else:
            return_choice(delete_customer)

def save_and_export_data():

    if len(customer_list) > 0:
        file_path = "/Users/user/python02/output.json"
        with open(file_path, "w") as file:
            json.dump(customer_list, file)
        print('saved to folder user/python02 folder')
        return_choice(save_and_export_data)
    else:
        print('no customer exist')
        return_choice(save_and_export_data)

def user_choice():

    choice = 0
    while choice not in range(1,8):
        display_menu()
        choice = input("Please enter a choice 1-7: ")
        choice = choice_validator(choice)
           
        if choice == 1:
            print('Chosen: list customers')
            list_all_customers()
        
        elif choice == 2:
            print('Chosen: search for customer')
            search_for_customer()

        elif choice == 3:
            print('Chosen: Add new customer')
            add_new_customer()

        elif choice == 4:
            print('Chosen: Update exisitng customer')
            update_existing_customer()

        elif choice == 5:
            print('Chosen: Delete customer')
            delete_customer()

        elif choice == 6:
            print('Chosen: Save customer')
            save_and_export_data()

        elif choice == 7:
            print("Thank you for visiting. We hope to see you again")
            break

main()


