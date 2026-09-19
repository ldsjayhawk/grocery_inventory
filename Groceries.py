import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from authentication import check_login


# Fetch the service account key JSON file contents
cred = credentials.Certificate('to-do-list-fd040-firebase-adminsdk-fbsvc-a0628bc947.json')

# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred)

# As an admin, the app has access to read and write all data, regradless of Security Rules
db = firestore.client()


# display menu function
def display_menu(user_id):
    print()
    print("Grocery Inventory Menu")
    print("1. Add new item")
    print("2. Edit item")
    print("3. Delete item")
    print("4. View inventory")
    print("5. View grocery list")
    print("6. Exit")
    print()
    print("Please make a selection: ")

    menu_choice = input()

    # send user to correct function based on menu choice
    # 6 prints Thank you and exits program
    if menu_choice == "6":
        print("Thank you!")
        print()
        exit()

    elif menu_choice == "1":
        add_item(user_id)

    elif menu_choice == "2":
        edit_item(user_id)

    elif menu_choice == "3":
        delete_item(user_id)

    elif menu_choice == "4":
        display_inventory(user_id)

    elif menu_choice == "5":
        display_grocery_list(user_id)

    else: 
        display_menu(user_id)

# Add item function
# Takes user input item and stores in item list
def add_item(user_id):
    #get user inputs
    print('Enter UPC')
    upc = input()
    print('Enter new item name: ')
    name = input()

    quantity = ''
    while not quantity.isdigit():    
        qty = input('Enter quantity (Number Required): ')

        try:
            quantity = int(qty)
            break

        except:
            print('Please enter a number for quantity')

    
    print('Enter storage location: ')
    location = input()
    # print('Enter expiration date: ')
    # expiration = input()

    # save new item as dictionary and add to 
    new_item = {'upc': upc, 'name': name, 'quantity': quantity, "location": location}
    db.collection('users').document(user_id).collection('inventory').document(upc).set(new_item)

    display_inventory(user_id)
    # display_menu()

# Edit item function
def edit_item(user_id):
    # display todo list - pass no to prevent display of menu
    display_inventory(user_id, "no")
    # select item to edit
    print('Enter UPC for item to edit: ')
    selected_item = input()
    edit_choice = ''

    docs = db.collection("users").document(user_id).collection("inventory").stream()

    for doc in docs:
        data = doc.to_dict()
        if selected_item == data["upc"]:
            edit_choice = display_edit_menu(selected_item)

            if edit_choice == "1":
                print('Enter new UPC:')
                new_upc = input()
                db.collection("users").document(user_id).collection('inventory').document(selected_item).update({"upc":new_upc})

            elif edit_choice == "2":
                print('Enter new item name: ')
                new_name = input()
                db.collection("users").document(user_id).collection('inventory').document(selected_item).update({"name":new_name})

            elif edit_choice == "3":
                print('Enter new item quantity: ')
                qty = input()
                new_qty = int(qty)
                db.collection("users").document(user_id).collection('inventory').document(selected_item).update({"quantity":new_qty})

            elif edit_choice == "4":
                print('Enter storage location: ')
                new_location = input()
                db.collection("users").document(user_id).collection('inventory').document(selected_item).update({"location":new_location})

            # elif edit_choice == "5":
            #     print('Enter expiration date: ')
            #     new_expiration = input()
            #     x["expiration"] = new_expiration

            else: 
                print(f'{edit_choice} is not a valid option.  Please choose again.')
                display_edit_menu()

    display_inventory(user_id)
    display_menu(user_id)

def display_edit_menu(selected_item):
    # enter new item
    print()
    print(f'What info would you like to update for {selected_item}?')
    print("1. UPC")
    print("2. Name")
    print("3. Quantity")
    print("4. Location")
    # print("5. Expiration")
    print("Enter Selection")
    print()
    edit_choice = input()

    return edit_choice


# Delete item function
def delete_item(user_id):
    # display todo list - pass no to prevent display of menu
    display_inventory(user_id, "no")

    # select item to delete
    print('Enter UPC for item to delete: ')
    selected_item = input()

    # find and delete selected item
    docs = db.collection("users").document(user_id).collection("inventory").stream()

    for doc in docs:
        data = doc.to_dict()
        if selected_item == data["upc"]:
            db.collection("users").document(user_id).collection("inventory").document(data["upc"]).delete()

    display_inventory(user_id)
    display_menu(user_id)

# View item list function
# Displays all grocery_list in the item list by looping through grocery_list variable
def display_inventory(user_id, menu='yes'):
    print()
    print("Inventory:")
    # print(user_id)

    docs = db.collection("users").document(user_id).collection("inventory").stream()

    for doc in docs:
        data = doc.to_dict()
        print(f'{data["upc"]}')
        print(f'{data["name"]}')
        print(f'quantity: {data["quantity"]}')
        print(f'location: {data["location"]}')
        print()

    if menu == "yes":
        display_menu(user_id)

def display_grocery_list(user_id, menu="yes"):
    grocery_list = []
    print()
    print("Grocery List:")
    # print(user_id)

    docs = db.collection("users").document(user_id).collection("inventory").stream()
    

    for doc in docs:
        data = doc.to_dict()

        if data["quantity"] == 0:
            grocery_list.append(data["name"])

    for item in grocery_list:    
        # print(item['name'], x['quantity'])
        print(item)

    if menu == "yes":
        display_menu(user_id)


user_id = check_login()

# calls display menu function to begin the program
display_menu(user_id)
