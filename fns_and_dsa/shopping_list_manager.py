def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice.isdigit() and 1 <= int(choice) <= 4:
            choice = int(choice)
            
            if choice == 1:
                item = input("Enter the item to add: ")
                shopping_list.append(item)
            elif choice == 2:
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print(f"{item} not found in the list.")
            elif choice == 3:
                if shopping_list:
                    print("Shopping List:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("The shopping list is empty.")
            elif choice == 4:
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
