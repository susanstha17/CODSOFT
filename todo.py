import os

def view_info(info):
    if not info:
        print("No info found:")
    else:
        for i, inf in enumerate(info, 1):
         print(f"{i}. {inf} ")
         
def add_info(info, new_info):
    info.append(new_info)
    print("Info Added Successfully.")
    
def update_info(info, index, updated_info):
    if 1 <= index <= len(info):
        info[index -1] =updated_info
        print("Info Update Successfully")
    else:
        print("Invalid Info index.")


def delete_info(info, index):
    if 1 <= index <= len(info):
       delete_info = info.pop(index-1)
       print(f"Task '{delete_info}' deleted Successfully")
    else:
        print("Invalid Info index.")



def save_info_to_file(file_path, info):
    with open(file_path, "w")as file:
        for inf in info:
            file.write(f"{inf}\n")
            
        


def load_info_from_file(file_path):
    info = []
    if os.path.exists(file_path):
        with open(file_path, "r")as file:
            info = file.read().splitlines()
    return info   


def main():
    file_path = "todo.txt"
    info = load_info_from_file(file_path)
    while True:
        print("\n--- Todo List ---")
        print("1. View Info")
        print("2. Add Info")
        print("3. Update Info")
        print("4. Delete Info")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5):")
        if choice == "1":
            view_info(info)
        elif choice == "2":
            new_info = input("Enter the info to add:")
            add_info(info, new_info)
        elif choice == "3":
            index = int(input("Enter the info index to update:"))
            updated_info = input("Enter the info to update:")
            update_info(info, index, updated_info)
        elif choice == "4":
            index = int(input("Enter the info index to delete:"))
            delete_info(info, index)
        elif choice == "5":
            save_info_to_file(file_path, info)
            print("Info saved. Exiting..")
            break
        else:
            print("Invalid choice.Re-enter the choice.")
        
        
if __name__ == "__main__":
    main()
    