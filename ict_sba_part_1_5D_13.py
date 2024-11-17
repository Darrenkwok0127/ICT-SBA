import calendar
import os
from datetime import datetime, date
from readchar import readkey, key
from colorama import Fore, Style

def date(): # Output the date of today
    get_date()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t    ", end = "")
    print(current_date) # Output date
def get_date():
    global current_date, current_month, current_year, next_year, current_day
    current = datetime.now() # To find the current date
    current_date = str(current.date())
    current_day = current.strftime("%d")
    current_month = current.strftime("%m")
    current_year = current.strftime("%Y")
    next_year = int(current_year) + 1
    
#-------------------------------------------------------------------------------------------------------
def system_name(): # Output the title 
    print(" █████╗  ██████╗ ██████╗███████╗ ██████╗ ██████╗███╗   ███╗███████╗███╗  ██╗████████╗".rjust(105))
    print("██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝████╗ ████║██╔════╝████╗ ██║╚══██╔══╝".rjust(105))
    print("███████║╚█████╗ ╚█████╗ █████╗  ╚█████╗ ╚█████╗ ██╔████╔██║█████╗  ██╔██╗██║   ██║   ".rjust(105))
    print("██╔══██║ ╚═══██╗ ╚═══██╗██╔══╝   ╚═══██╗ ╚═══██╗██║╚██╔╝██║██╔══╝  ██║╚████║   ██║   ".rjust(105))
    print("██║  ██║██████╔╝██████╔╝███████╗██████╔╝██████╔╝██║ ╚═╝ ██║███████╗██║ ╚███║   ██║   ".rjust(105))
    print("╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   ".rjust(105))
    print(" ██████╗ █████╗ ██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗   ██████╗██╗   ██╗ ██████╗████████╗███████╗███╗   ███╗".rjust(100))
    print("██╔════╝██╔══██╗██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║".rjust(100))
    print("╚█████╗ ██║  ╚═╝███████║█████╗  ██║  ██║██║   ██║██║     █████╗    ╚█████╗  ╚████╔╝ ╚█████╗    ██║   █████╗  ██╔████╔██║".rjust(100))
    print(" ╚═══██╗██║  ██╗██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝     ╚═══██╗  ╚██╔╝   ╚═══██╗   ██║   ██╔══╝  ██║╚██╔╝██║".rjust(100))
    print("██████╔╝╚█████╔╝██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗  ██████╔╝   ██║   ██████╔╝   ██║   ███████╗██║ ╚═╝ ██║".rjust(100))
    print("╚═════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝  ╚═════╝    ╚═╝   ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝".rjust(100))
#-------------------------------------------------------------------------------------------------------
def main_menu(): 
    global login_name, password
    os.system("cls")
    date()
    system_name()
    for i in range(4):
        print()
    print("<ENTER> Login ".rjust(64))
    print()
    print("<ESC>  Exit ".rjust(63))
    k = readkey() # reading keyboard input
    while k != key.ENTER and k != key.ESC:
        k = readkey()
    if k == key.ENTER: # When user press "ENTER", it goes into login system
        os.system("cls")
        date()
        system_name()
        login_name, password = get_data()
        print()
        print()
        return True
    elif k == key.ESC: # When user press "2", it exits the program
        return False
#---------------------------------------------------------------------------------
def linear_search(arr, target): # To search if the target exists(e.g. teachers account)
    found = False
    for i in range(len(arr)):
        if arr[i] == target:
            found = True
            break
    if found:
        return found, i
    else:
        return found, None
#---------------------------------------------------------------------------------
def search_admin(arr, target): # To search if the target exists(e.g. teachers account)
    found = False
    if arr[0] == target:
        found = True
        return found, 0
    else:
        return found, None
#---------------------------------------------------------------------------------
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                swap(j, j+1, unsorted_list)
#---------------------------------------------------------------------------------
def swap(a, b, ul):
    temp = ul[a]
    ul[a] = ul[b]
    ul[b] = temp
#---------------------------------------------------------------------------------
def get_data(): # Getting data from text file and make them(username & encrypted_password) into lists
    f1 = open("username.txt", "r")
    f2 = open("encrypted_pw.txt", "r")
    l_name = f1.readlines()
    pw = f2.readlines()
    f1.close()
    f2.close()
    for i in range(len(l_name)):
        l_name[i] = l_name[i].strip("\n")
    for j in range(len(pw)):
        pw[j] = pw[j].strip("\n")
    return l_name, pw
#---------------------------------------------------------------------------------
def get_class():
    global class_list
    f = open("class_list.txt", "r")
    class_list = f.readlines()
    f.close()
    for i in range(len(class_list)):
        class_list[i] = class_list[i].strip("\n")
    for j in range(len(class_list)):
        class_list[j] = class_list[j].split("\t")
    for x in range(len(class_list)):
        for y in range(len(class_list[x])):
            bubble_sort(class_list[x])
    update_class()
#---------------------------------------------------------------------------------
def get_adminpw_data(): # Getting administrator password data from text file
    f = open("encrypted_admin_pw.txt", "r")
    a_pw = f.readlines()
    f.close()
    for i in range(len(a_pw)):
        a_pw[i] = a_pw[i].strip()
    return a_pw
#---------------------------------------------------------------------------------
def login(counting):
    global username_index, password_index
    counting += 1
    print()
    print()
    input_username = input("Username: ".rjust(60))
    print()
    input_password = input("Password: ".rjust(60))
    input_password = encrypted_pw(input_password) # Encrypting password(unencrypted) so that it uses to find if it is correct
    isadmin1, username_index = search_admin(login_name, input_username)
    if isadmin1:
        check1 = False
        check2 = False
        isadmin2, password_index = search_admin(password, input_password)
    else:
        check1, username_index = linear_search(login_name, input_username)
        if username_index != None and password[username_index] == input_password:
            password_index = username_index
            check2 = True
        else:
            check2 = False
    if check1 and check2 and username_index == password_index:
        os.system("cls")
        get_class()
        for x in range(12):
            print()
        print("LOGIN SUCCESSFUL".rjust(64))
        print()
        print("Press <ANY KEY> to continue.".rjust(69))
        readkey()
        teachers_system() 
    elif isadmin1 and isadmin2:
        os.system("cls")
        get_class()
        for x in range(12):
            print()
        print("LOGIN SUCCESSFUL".rjust(64))
        print()
        print("Press <ANY KEY> to continue.".rjust(69))
        readkey()
        admin_system() 
    else:
        if counting % 3 == 0:
            while True:
                os.system("cls")
                date()
                system_name()
                for x in range(5):
                    print()
                print("\t\t\t\t\t\t\tContinue?")
                print()
                print("\t\t\t\t\t<ENTER> Continue\t<ESC> Back To Menu ")
                k = readkey()
                while k != key.ENTER and k != key.ESC:
                    k = readkey()
                if k == key.ENTER:
                    break
                elif k == key.ESC:
                    return
        os.system("cls")
        date()
        system_name()
        print("The username/password is incorrect.".rjust(77))
        print()
        login(counting)
#---------------------------------------------------------------------------------
def admin_system(): # admin account
    os.system("cls")
    date()
    print("\t\t\t\t\t\t    Welcome Back." , login_name[username_index])
    for x in range(8):
        print()
    print("\t\t\t\t        <1>  Teachers Class Information")
    print()
    print("\t\t\t\t        <2>  Settings (Administrator)")
    print()
    print("\t\t\t\t       <ESC> Sign Out")
    print()
    k = readkey()
    while k != "1" and k != "2" and k != key.ESC:
        k = readkey()
    if k == "1":
        os.system("cls")
        print()
        teachers_info_function()
    elif k == "2":
        admin_function()
    elif k == key.ESC:
        return
#---------------------------------------------------------------------------------
def teachers_info_function():
    global login_name, password
    login_name, password = get_data()
    date()
    for x in range(9):
        print()
    print("                                    Which Teachers' account info you want to change?")
    print()
    inp_username = input("                                    <Empty input> Exit : ")
    if inp_username == "":
        admin_system()
    else:
        found, teachers_acc_index = linear_search(login_name, inp_username)
        if found and teachers_acc_index != 0:
            show_assigned_class(teachers_acc_index)
        else:
            os.system("cls")
            print("                                          User Not Found / Wrong Input.")
            teachers_info_function()
#---------------------------------------------------------------------------------
def show_assigned_class(index):
    get_class()
    os.system("cls")
    date()
    for i in range(10):
        print()
    if class_list[index][0] != "Not yet Assigned":
        print("                                           Current Class Assigned:", end = " ")
        for i in range(len(class_list[index])):
            if (i+1) % 4 != 0:
                print(class_list[index][i], end = " ")
            else:
                print(class_list[index][i], end = "\n")
                print("                                                                   ", end = "")
        print()
        print()
        print("                                   <1> Add Class       <2> Delete Class       <ESC> Back")
        k = readkey()
        while k != "1" and k != "2" and k != key.ESC:
            k = readkey()
    else:
        print("                                              There is no Class Assigned.")
        print()
        print("                                             <1> Add Class       <ESC> Back")
        k = readkey()
        while k != "1" and k != key.ESC:
            k = readkey()
    os.system("cls")
    if k == "1":
        add_class(index)
    elif k == "2":
        del_class(index)
    elif k == key.ESC:
        teachers_info_function()
#---------------------------------------------------------------------------------
def add_class(index):
    stop = False
    while not stop:
        selected_form = choose_form(index)
        if selected_form == None:
            break
        else:
            selected_form_char = choose_form_char(index)
            if selected_form_char == None:
                pass
            else:
                selected_class = str(selected_form) + selected_form_char
                check, temp = linear_search(class_list[index], selected_class)
                if not check:
                    if class_list[index][0] == "Not yet Assigned":
                        class_list[index][0] = selected_class
                    else:
                        class_list[index] = class_list[index] + [selected_class]
                    update_class()
                    date()
                    for i in range(10):
                        print()
                    print("                                        "+ selected_class +" Assigned. Do you want to Assign More? ")
                    print()
                    print("                                         <ENTER> Continue       <ESC> Back")
                    k = readkey()
                    while k != key.ENTER and k != key.ESC:
                        k = readkey()
                    if k == key.ENTER:
                        os.system("cls")
                        pass
                    elif k == key.ESC:
                        stop = True
                        show_assigned_class(index)
                else:
                    date()
                    for i in range(10):
                        print()
                    print("                                           This Class Had Already Assigned.")
                    print()
                    print("                                              Press <ANY KEY> To Return")
                    readkey()
                    os.system("cls")
#---------------------------------------------------------------------------------
def choose_form(index):
    leave = False
    form_list = ["F1", "F2", "F3", "F4", "F5", "F6"]
    form_num = 1
    while not leave:
        date()
        print("                                          Select and Confirm Which Form")
        print()
        print("%35s" % "", end = "")
        for x in range(len(form_list)):
            if x+1 != form_num:
                print(form_list[x], end = "      ")
            else:
                print(Fore.RED + form_list[x] + Style.RESET_ALL, end = "      ")
        print()
        for i in range(22):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave")
        print(form_num)
        k = readkey()
        while k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.LEFT and form_num >= 1:
            if form_num-1 < 1:
                form_num = len(form_list)
            else:
                form_num -= 1
        elif k == key.RIGHT and form_num <= len(form_list):
            if form_num+1 > len(form_list):
                form_num = 1
            else:
                form_num += 1
        elif k == key.ENTER:
            return form_num
        elif k == key.ESC:
            leave = True
            show_assigned_class(index)
#---------------------------------------------------------------------------------
def choose_form_char(index):
    leave = False
    form_char_list = ["A", "B", "C", "D"]
    form_char_num = 1
    while not leave:
        date()
        print("                                          Select and Confirm Which Form")
        print()
        print("%45s" % "", end = "")
        for x in range(len(form_char_list)):
            if x+1 != form_char_num:
                print(form_char_list[x], end = "      ")
            else:
                print(Fore.RED + form_char_list[x] + Style.RESET_ALL, end = "      ")
        print()
        for i in range(22):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave")
        print(form_char_num)
        k = readkey()
        while k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.LEFT and form_char_num >= 1:
            if form_char_num-1 < 1:
                form_char_num = len(form_char_list)
            else:
                form_char_num -= 1
        elif k == key.RIGHT and form_char_num <= len(form_char_list):
            if form_char_num+1 > len(form_char_list):
                form_char_num = 1
            else:
                form_char_num += 1
        elif k == key.ENTER:
            return form_char_list[form_char_num-1]
        elif k == key.ESC:
            leave = True
#---------------------------------------------------------------------------------
def del_class(index):
    col = 1
    row = 1
    class_num = 1
    leave = False
    while not leave:
        row_num = 0
        os.system("cls")
        date()
        for x in range(5):
            print()
        print("                                                ", end = "")
        for i in range(len(class_list[index])):
            if (i+1) % 4 != 0:
                if i+1 != class_num:
                    print(class_list[index][i], end = "      ")
                else:
                    print(Fore.RED + class_list[index][i] + Style.RESET_ALL, end = "      ")
            else:
                if i+1 != class_num:
                    print(class_list[index][i], end = "\n")
                else:
                    print(Fore.RED + class_list[index][i] + Style.RESET_ALL, end = "\n")
                row_num += 2
                print()
                print("                                                ", end = "")
        print()
        for x in range(15-row_num):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.ESC and k != key.ENTER and k != key.LEFT and k != key.RIGHT and k != key.UP and k != key.DOWN:
            k = readkey()
        if k == key.LEFT and col > 1:
            col -= 1
            class_num -= 1
        elif k == key.RIGHT and col < 4 and class_num < len(class_list[index]):
            col += 1
            class_num += 1
        elif k == key.UP and row > 1:
            row -= 1
            class_num -= 4
        elif k == key.DOWN and class_num+4 <= len(class_list[index]):
            row += 1
            class_num += 4
        elif k == key.ENTER:
            os.system("cls")
            date()
            for z in range(10):
                print()
            print("                                                You Want To Delete " + class_list[index][class_num-1] + "?")
            print()
            print("                                             <ENTER> Confirm      <ESC> Back")
            k = readkey()
            while k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.ENTER:
                leave = True
            elif k == key.ESC:
                del_class(index)
            if leave:
                if len(class_list[index]) == 1:
                    class_list[index][0] = "Not yet Assigned"
                else:
                    del class_list[index][class_num-1]
                update_class()
                
                if class_list[index][0] == "Not yet Assigned":
                    show_assigned_class(index)
                else:
                    del_class(index)
        elif k == key.ESC:
            leave = True
            show_assigned_class(index)
#---------------------------------------------------------------------------------
def admin_function():
    os.system("cls")
    date()
    print("\t\t\t\t\t\t   Administrator Setting")
    for x in range(8):
        print()
    print("\t\t\t\t         <1>  Reset Password")
    print()
    print("\t\t\t\t         <2>  Find Password")
    print()
    print("\t\t\t\t         <3>  Create Account")
    print()
    print("\t\t\t\t         <4>  Delete Account")
    print()
    print("\t\t\t\t        <ESC> Back")
    print()
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != "4" and k != key.ESC:
        k = readkey()
    os.system("cls")
    if k == "1":
        print()
        admin_resetpw_function()
    elif k == "2":
        print()
        find_pw_function()
    elif k == "3":
        print()
        create_acc_function()
    elif k == "4":
        print()
        delete_acc_function()
    elif k == key.ESC:
        admin_system()
#---------------------------------------------------------------------------------
def find_pw_function():
    global login_name, password
    temp = 0
    date()
    login_name, password = get_data()
    admin_pw = get_adminpw_data()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(64))
    print()
    if input_admin_pw == "":
        admin_function()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]:
            os.system("cls")
            print("Administrator Password Incorrect.".rjust(75))
            find_pw_function()
        else:
            found = False
            while not(found):
                if temp > 0:
                    print("<Empty input> Exit".rjust(65))
                    print()
                input_accname = input("Enter the Account Username: ".rjust(58))
                if input_accname == "":
                    admin_function()
                    break
                else:
                    check, index_user = linear_search(login_name, input_accname)
                    if check:
                        found = True
                        target_pw = decrypted_pw(password[index_user])
                        for i in range(8):
                            print()
                        print("\t\t\t\t\t", login_name[index_user], "'s password is \"" + target_pw + "\"")
                        input("Press <ENTER> To Exit".rjust(65))
                        admin_function()
                    else:
                        os.system("cls")
                        print("                                         Username not found. Please try it again")
                        date()
                        temp += 1
#---------------------------------------------------------------------------------
def create_acc_function(): # To create a new teacher account
    global login_name, password, class_list
    pw_ok = False
    found = False
    date()
    admin_pw = get_adminpw_data()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(64))
    print()
    if input_admin_pw == "":
        admin_function()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]:
            os.system("cls")
            print("Administrator Password Incorrect.".rjust(75))
            create_acc_function()
        else:
            os.system("cls")
            print()
            while not found:
                date()
                print("                Password must include at least 8 characters (at least 1 number, 1 capital letter and 1 small letter)")
                print("                                       Password must not contain any blank space")
                print()
                print("<Empty input> Exit".rjust(65))
                for y in range(3):
                    print()
                add_username = input("\t\t\t         Enter New Teacher Account Username: ")
                check, temp = linear_search(login_name, add_username)
                if add_username == "":
                    admin_function()
                    break
                elif check:
                    os.system("cls")
                    print("Username Has Been Used. Please Try Again".rjust(77)) 
                else:
                    print()
                    add_password = input("\t\t\t         Enter New Teacher Account Password: ")
                    if add_password == "":
                        admin_function()
                        break
                    else:
                        pw_ok = pw_check(add_password)
                        if pw_ok:
                            found = True
                            login_name = login_name + [0]
                            password = password + [0]
                            class_list = class_list + [["Not yet Assigned"]]
                            add_password = encrypted_pw(add_password)
                            login_name[len(login_name)-1] = add_username
                            password[len(password)-1] = add_password
                            update_username()
                            update_password()
                            update_class()
                            os.system("cls")
                            for x in range(12):
                                print()
                            print("\t\t\t\t\t         SIGN UP SUCCESSFUL")
                            print()
                            input("\t\t\t\t\t       Press <ENTER> To Exit")
                            admin_function()
                        else:
                            os.system("cls")
                            print("The New Password Does Not Meet Requirements".rjust(77))                            
#---------------------------------------------------------------------------------
def delete_acc_function(): # To delete teachers' account
    temp = 0
    date()
    admin_pw = get_adminpw_data()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(61))
    print()
    if input_admin_pw == "":
        admin_function()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]:
            os.system("cls")
            print("Administrator Password Incorrect.".rjust(75))
            delete_acc_function()
        else:
            found = False
            while not(found):
                if temp > 0:
                    print("<Empty input> Exit".rjust(65))
                    print()
                input_accname = input("\t\t\t   Enter the Account Username you want to delete: ")
                if input_accname == "":
                    admin_function()
                    break
                else:
                    check, index_user = linear_search(login_name, input_accname)
                    if check and index_user != 0:
                        found = True
                        del login_name[index_user]
                        del password[index_user]
                        del class_list[index_user]
                        update_username()
                        update_password()
                        update_class()
                        os.system("cls")
                        for i in range(12):
                            print()
                        print("\t\t\t\t\t      ACCOUNT DELETE SUCCESSFUL")
                        print()
                        print("\t\t\t\t\t       Press <ANY KEY> To Exit")
                        readkey()
                        admin_function()
                    else:
                        temp = 1
                        os.system("cls")
                        print("                                    Username not found / Invalid. Please try it again")
                        date()
#---------------------------------------------------------------------------------
def teachers_system(): # teachers accounts
    os.system("cls")
    date()
    print("\t\t\t\t\t\t    Welcome Back." , login_name[username_index])
    for x in range(8):
        print()
    print("\t\t\t\t        <1>  Schedule Assessments System")
    print()
    print("\t\t\t\t        <2>  Settings")
    print()
    print("\t\t\t\t       <ESC> Sign Out")
    k = readkey()
    while k != "1" and k != "2" and k != key.ESC:
        k = readkey()
    os.system("cls")
    if k == "1":
        choose_class()
    elif k == "2":
        setting_function()
    elif k == key.ESC:
        return
#---------------------------------------------------------------------------------
def choose_class():
    total_page_num = (len(class_list[username_index])//8)+1
    page_num = 1
    start_num = 0
    if class_list[username_index][0] != "Not yet Assigned":
        leave = False
        global selected_class
        class_group = [0] * len(class_list[username_index])
        while not leave:
            date()
            if total_page_num == 1:
                print("                                                Please Select the Class")
                for y in range(10-len(class_group)):
                    print()
                for x in range(len(class_list[username_index])):
                    class_group[x] = class_list[username_index][x]
                    print("                                                       <" + str(x + 1) + "> " + class_group[x])
                    print()
                print("                                                      <ESC> Leave")
                while True:
                    k = readkey()
                    if k.isnumeric(): # check if k is integers
                        k = int(k)
                        if k < 1 or k > len(class_group):
                            pass
                        else:
                            break # it will break when k is between a range(e.g. 1-3)
                    elif k != key.ESC:
                        pass
                    else:
                        break # it will break when key is ESC
                if k == key.ESC:
                    leave = True
                    teachers_system()
                else:
                    leave = True
                    selected_class = class_group[k-1]
                    schedule_function()
            elif page_num > 1 and page_num < total_page_num:
                num = 0
                print("                                                Please Select the Class")
                for y in range(2):
                    print()
                for x in range(start_num, page_num*8):
                    num += 1
                    class_group[x] = class_list[username_index][x]
                    print("                                                       <" + str(num) + "> " + class_group[x])
                    print()
                print("                                         <LEFT> Previous Page      <ESC> Leave")
                while True:
                    k = readkey()
                    if k.isnumeric(): # check if k is integers
                        k = int(k)
                        if k < 1 or k > num:
                            pass
                        else:
                            break # it will break when k is between a range(e.g. 1-3)
                    elif k == key.ESC:
                        break
                    elif k == key.LEFT:
                        break
                    elif k == key.RIGHT:
                        break
                    else:
                        pass
                if k == key.LEFT:
                    page_num -= 1
                    start_num -= 8
                    os.system("cls")
                elif k == key.RIGHT:
                    page_num += 1
                    start_num += 8
                    os.system("cls")
                elif k == key.ESC:
                    leave = True
                    teachers_system()
                else:
                    leave = True
                    selected_class = class_group[(page_num-1)*8+k-1]
                    schedule_function()
            elif page_num == total_page_num:
                num = 0
                row_num = 0
                print("                                                Please Select the Class")
                for y in range(2):
                    print()
                for x in range(start_num, len(class_group)):
                    num += 1
                    class_group[x] = class_list[username_index][x]
                    print("                                                       <" + str(num) + "> " + class_group[x])
                    print()
                    row_num += 2
                for y in range(16-row_num):
                    print()
                print("                                         <LEFT> Previous Page      <ESC> Leave")
                while True:
                    k = readkey()
                    if k.isnumeric(): # check if k is integers
                        k = int(k)
                        if k < 1 or k > num:
                            pass
                        else:
                            break # it will break when k is between a range(e.g. 1-3)
                    elif k == key.ESC:
                        break
                    elif k == key.LEFT:
                        break
                    else:
                        pass
                if k == key.LEFT:
                    page_num -= 1
                    start_num -= 8
                    os.system("cls")
                elif k == key.ESC:
                    leave = True
                    teachers_system()
                else:
                    leave = True
                    selected_class = class_group[(page_num-1)*8+k-1]
                    schedule_function()
            else:
                print("                                                Please Select the Class")
                for y in range(2):
                    print()
                for x in range(8):
                    class_group[x] = class_list[username_index][x]
                    print("                                                       <" + str(x + 1) + "> " + class_group[x])
                    print()
                print("                                          <RIGHT> Next Page      <ESC> Leave")
                while True:
                    k = readkey()
                    if k.isnumeric(): # check if k is integers
                        k = int(k)
                        if k < 1 or k > 8:
                            pass
                        else:
                            break # it will break when k is between a range(e.g. 1-3)
                    elif k == key.ESC:
                        break
                    elif k == key.RIGHT:
                        break
                    else:
                        pass
                if k == key.RIGHT:
                    page_num += 1
                    start_num += 8
                    os.system("cls")
                elif k == key.ESC:
                    leave = True
                    teachers_system()
                else:
                    leave = True
                    selected_class = class_group[k-1]
                    schedule_function()
    else:
        date()
        for i in range(10):
            print()
        print("                                               Class Not yet Assigned.")
        print()
        print("                                              Press <ANY KEY> To Return")
        readkey()
        teachers_system()
#---------------------------------------------------------------------------------
def schedule_function(): # To open schedule system function
    global assm
    os.system("cls")
    date()
    print(selected_class)
    assm = get_assm()
    display_assm()
    if len(assm) == 0:
        print("                                              <1> Schedule Assessments")
        print()
        print("                                              <ESC> Back")
        k = readkey()
        while k != "1" and k != key.ESC:
            k = readkey()
    else:
        print("                        <1> Schedule Assessments                 <2>  Delete Assessments")
        print()
        print("                        <3> Show All Assessments                <ESC> Back")
        k = readkey()
        while k != "1" and k != "2" and k != "3" and k != key.ESC:
            k = readkey()
    os.system("cls")
    if k == "1":
        add_assms()
    elif k == "2":
        del_assms()
    elif k == "3":
        show_all_assms()
    elif k == key.ESC:
        choose_class()
#---------------------------------------------------------------------------------
def display_assm():
    if len(assm) == 0:
        print("\t\t\t\t\tThere are no asseessments assigned.")
        for x in range(22):
            print()
    else:
        display = [''] * 6
        num = 1
        row_num = 0
        k = 0
        while k < len(assm) and k < len(display):
            display[k] = assm[k]
            k += 1
        print("\t\t\t\tThe Most Recent Assessments Scheduled Shown Below")
        print()
        for i in range(len(display)):
            if num % 2 != 0:
                print("\t\t\t", display[i], end = "")
            else:
                print("\t\t\t", display[i], end = "\n\n")
                row_num += 1
            num += 1
        if k == len(display) and len(assm) > len(display):
            row_num += 1
            print("\t\t\t And More.....")
        for j in range(17-row_num):
            print()
#---------------------------------------------------------------------------------
def get_assm():
    f = open(selected_class + "_assessments.txt", "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].strip("\n")
    if len(a) > 0:
        bubble_sort(a)
        while a[0] < current_date and len(a) > 0:
            del a[0]
        update_assm(a)
    return a
#---------------------------------------------------------------------------------
def add_assms():
    back1 = False
    while not back1:
        selected_subject = choose_subject()
        if selected_subject == None:
            back1 = True
            schedule_function()
        else:
            back2 = False
            while not back2:
                selected_type = choose_assm_type()
                if selected_type == None:
                    back2 = True
                else:
                    back3 = False
                    while not back3:
                        selected_month = choose_month()
                        if selected_month == None:
                            back3 = True
                        else:
                            back4 = False
                            while not back4:
                                selected_month = int(selected_month)
                                selected_day = choose_deadline(selected_month)
                                if selected_day == None:
                                    back4 = True
                                else:
                                    selected_month = "{:02d}".format(selected_month)
                                    selected_day = "{:02d}".format(selected_day)
                                    for i in range(11):
                                        print()
                                    assm_deadline = str(schedule_year) + "-" + selected_month + "-" + selected_day + " " + selected_subject + " " + selected_type
                                    print("\t\t\t\t     The Assessment schedule on ["+ assm_deadline + "]")
                                    print()
                                    print("\t\t\t\t\t\t\tConfirm ?")
                                    print()
                                    print("\t\t\t\t\t<ENTER> Confirm\t\t\t<ESC> Back")
                                    k = readkey()
                                    while k != key.ENTER and k != key.ESC:
                                        k = readkey()
                                    os.system("cls")
                                    if k == key.ENTER:
                                        global assm
                                        assm = assm + [0]
                                        assm[len(assm) - 1] = assm_deadline
                                        update_assm(assm)
                                        schedule_function()
                                        back1 = True
                                        back2 = True
                                        back3 = True
                                        back4 = True
                                    elif k == key.ESC:
                                        pass
#---------------------------------------------------------------------------------
def del_assms():
    selected_del_assm = choose_del_assm()
    if selected_del_assm != None:
        for i in range(11):
            print()
        print("\t\t\t\t   You want to Remove The Assessment ["+ assm[selected_del_assm-1] + "]")
        print()
        print("\t\t\t\t\t\t\tConfirm ?")
        print()
        print("\t\t\t\t\t<ENTER> Confirm\t\t\t<ESC> Back")
        k = readkey()
        while k != key.ENTER and k != key.ESC:
             k = readkey()
        os.system("cls")
        if k == key.ENTER:
            del assm[selected_del_assm-1]
            update_assm(assm)
            schedule_function()
        elif k == key.ESC:
            del_assms()
#---------------------------------------------------------------------------------
def choose_del_assm():
    total_page_num = (len(assm)//10)+1
    leave = False
    start_num = 0
    page_num = 1
    select_index = 1
    while not leave:
        date()
        print("\tPage "+ str(page_num) +"\t\t\t    Select And Confirm the Assessment You want to Delete: ")
        print()
        if total_page_num < 2:
            blank_line = 0
            for i in range(len(assm)):
                if i+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[i])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[i] + Style.RESET_ALL)
                print()
                blank_line += 2
            for j in range(21-blank_line):
                print()
            print("                                                   <UP>     <DOWN>")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.ESC and k != key.ENTER and k != key.UP and k != key.DOWN:
                k = readkey()
            os.system("cls")
            if k == key.ESC:
                leave = True
                schedule_function()
            elif k == key.ENTER:
                return select_index
            elif k == key.UP and select_index > 1:
                select_index -= 1
            elif k == key.DOWN and select_index < len(assm):
                select_index += 1
        elif page_num > 1 and page_num < total_page_num:
            for x in range(start_num, page_num*10):
                if x+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[x])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[x] + Style.RESET_ALL)
                print()
            print()
            print("                              <UP>     <DOWN>     <LEFT> Previous Page     <RIGHT> Next Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.LEFT and k != key.RIGHT and k != key.UP and k != key.DOWN and k != key.ESC and k != key.ENTER:
                k = readkey()
            os.system("cls")
            if k == key.LEFT:
                page_num -= 1
                start_num -= 10
                select_index = start_num + 1
            elif k == key.RIGHT:
                page_num += 1
                start_num += 10
                select_index = start_num + 1
            elif k == key.UP and select_index > start_num + 1:
                select_index -= 1
            elif k == key.DOWN and select_index < page_num*10:
                select_index += 1
            elif k == key.ESC:
                leave = True
                schedule_function()
            elif k == key.ENTER:
                return select_index
        elif page_num == total_page_num:
            blank_line = 0
            for y in range(start_num, len(assm)):
                if y+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[y])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[y] + Style.RESET_ALL)
                print()
                blank_line += 2
            for j in range(21-blank_line):
                print()
            print("                                        <UP>     <DOWN>     <LEFT> Previous Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.LEFT and k != key.UP and k != key.DOWN and k != key.ESC and k != key.ENTER:
                k = readkey()
            os.system("cls")
            if k == key.LEFT:
                page_num -= 1
                start_num -= 10
                select_index = start_num + 1
            elif k == key.UP and select_index > start_num + 1:
                select_index -= 1
            elif k == key.DOWN and select_index < len(assm):
                select_index += 1
            elif k == key.ESC:
                leave = True
                schedule_function()
            elif k == key.ENTER:
                return select_index
        else:
            for z in range(start_num, page_num*10):
                if z+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[z])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[z] + Style.RESET_ALL)
                print()
            print()
            print("                                        <UP>     <DOWN>     <RIGHT> Next Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.RIGHT and k != key.UP and k != key.DOWN and k != key.ESC and k != key.ENTER:
                k = readkey()
            os.system("cls")
            if k == key.RIGHT:
                page_num += 1
                start_num += 10
                select_index = start_num + 1
            elif k == key.UP and select_index > 1:
                select_index -= 1
            elif k == key.DOWN and select_index < page_num*10:
                select_index += 1
            elif k == key.ESC:
                leave = True
                schedule_function()
            elif k == key.ENTER:
                return select_index
#---------------------------------------------------------------------------------
def show_all_assms():
    blank_line = 0
    total_page_num = (len(assm)//11)+1
    leave = False
    start_num = 0
    page_num = 1
    while not leave:
        date()
        print("\tPage "+ str(page_num) +"\t\t\t\t       Assessments Shown Below: ")
        print()
        if total_page_num < 2:
            for i in range(len(assm)):
                print("\t\t\t\t\t\t"+ assm[i])
                print()
                blank_line += 2
            for j in range(23-blank_line):
                print()
            print("\t\t\t\t\t\t  <ESC> Leave")
            k = readkey()
            while k != key.ESC:
                k = readkey()
            leave = True
        elif page_num > 1 and page_num < total_page_num:
            for x in range(start_num, page_num*10):
                print("\t\t\t\t\t\t"+ assm[x])
                print()
            print()
            print()
            print()
            print("\t\t\t      <LEFT> Previous Page\t<RIGHT> Next Page\t<ESC> Leave")
            k = readkey()
            while k != key.LEFT and k != key.RIGHT and k != key.ESC:
                k = readkey()
            os.system("cls")
            if k == key.LEFT:
                page_num -= 1
                start_num -= 10
            elif k == key.RIGHT:
                page_num += 1
                start_num += 10
            elif k == key.ESC:
                leave = True
        elif page_num == total_page_num:
            blank_line = 0
            for y in range(start_num, len(assm)):
                print("\t\t\t\t\t\t"+ assm[y])
                print()
                blank_line += 2
            for j in range(23-blank_line):
                print()
            print("\t\t\t\t     <LEFT> Previous Page\t<ESC> Leave")
            k = readkey()
            while k != key.LEFT and k != key.ESC:
                k = readkey()
            os.system("cls")
            if k == key.LEFT:
                page_num -= 1
                start_num -= 10
            elif k == key.ESC:
                leave = True
        else:
            for z in range(start_num, page_num*10):
                print("\t\t\t\t\t\t"+ assm[z])
                print()
            print()
            print()
            print()
            print("\t\t\t\t\t<RIGHT> Next Page\t<ESC> Leave")
            k = readkey()
            while k != key.RIGHT and k != key.ESC:
                k = readkey()
            os.system("cls")
            if k == key.RIGHT:
                page_num += 1
                start_num += 10
            elif k == key.ESC:
                leave = True
    schedule_function()
#---------------------------------------------------------------------------------
def choose_subject():
    leave = False
    row = 0
    col = 0
    subject_list = ["CHIN","ENG","MATH","CSD","CHIS","CLIT","HIST","PHY","M1"],["BIO","GEOG","ICT","ECON","BAFS","VA","MUSIC","CHEM","M2"]
    while not leave:
        date()
        print("\t\t\t\t\t  Select and Confirm the Subject")
        print()
        for i in range(len(subject_list)):
            print("\t\t     ", end = "")
            for j in range(len(subject_list[i])):
                if subject_list[row][col] != subject_list[i][j]:
                    print(subject_list[i][j], end = "      ")
                else:
                    print(Fore.RED + str(subject_list[i][j]) + Style.RESET_ALL, end = "      ")
            print()
            print()
        for i in range(15):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.UP and k != key.DOWN and k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.UP and row <= 1:
            if row-1 < 0:
                row = 1
            else:
                row = 0
        elif k == key.DOWN and row >= 0:
            if row+1 > 1:
                row = 0
            else:
                row = 1
        elif k == key.LEFT and col >= 0:
            if col-1 < 0:
                col = 8
            else:
                col -= 1
        elif k == key.RIGHT and col <= 8:
            if col+1 > 8:
                col = 0
            else:
                col += 1
        elif k == key.ENTER:
            return subject_list[row][col]
        elif k == key.ESC:
            leave = True
#---------------------------------------------------------------------------------
def choose_assm_type():
    leave = False
    type_num = 1
    type_list = ["HW", "QUIZ", "UT", "TEST", "DICT", "SBA"]
    while not leave:
        date()
        print("                                          Select and Confirm the Assessment Type")
        print()
        print("%35s" % "", end = "")
        for x in range(len(type_list)):
            if x+1 != type_num:
                print(type_list[x], end = "      ")
            else:
                print(Fore.RED + type_list[x] + Style.RESET_ALL, end = "      ")
        print()
        for i in range(20):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave")
        k = readkey()
        while k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.LEFT and type_num >= 1:
            if type_num-1 < 1:
                type_num = len(type_list)
            else:
                type_num -= 1
        elif k == key.RIGHT and type_num <= len(type_list):
            if type_num+1 > len(type_list):
                type_num = 1
            else:
                type_num += 1
        elif k == key.ENTER:
            return type_list[type_num-1]
        elif k == key.ESC:
            leave = True
#---------------------------------------------------------------------------------
def choose_month():
    leave = False
    row = 1
    col = 1
    month = 1
    month_list = ["[1] January","[2] Feburary","[3] March","[4] April","[5] May","\t[6] June\n\n","\t[7] July","[8] August","[9] September","[10] October","[11] November","[12] December"]
    while not leave:
        date()
        print("\t\t\t\tSelect And Confirm The Month You Want To Schedule The Assessment")
        print()
        print("\t\t", end = "")
        for x in range(len(month_list)):
            if x+1 != month:
                print(month_list[x], end = "\t")
            else:
                print(Fore.RED + month_list[x] + Style.RESET_ALL, end = "\t")
        for x in range(17):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.UP and k != key.DOWN and k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.UP and row >= 1:
            if row-1 < 1:
                row = 2
                month += 6
            else:
                row = 1
                month -= 6
        elif k == key.DOWN and row <= 2:
            if row+1 > 2:
                row = 1
                month -= 6
            else:
                row = 2
                month += 6
        elif k == key.LEFT and col >= 1:
            if col-1 < 1:
                col = 6
                month += 5
            else:
                col -= 1
                month -= 1
        elif k == key.RIGHT and col <= 6:
            if col+1 > 6:
                col = 1
                month -= 5
            else:
                col += 1
                month += 1
        elif k == key.ENTER:
            return month
        elif k == key.ESC:
            leave = True
#---------------------------------------------------------------------------------
def choose_deadline(month):
    global schedule_year
    row = 0
    col = 0
    day_num = 1
    leave = False
    day_abbr = calendar.day_abbr
    month_name = calendar.month_name
    if int(current_month) > month:
        schedule_year = next_year
    else:
        schedule_year = int(current_year)
    month_day = calendar.monthcalendar(schedule_year, month)
    for y in range(len(month_day[0])):
        if month_day[0][y] == 1:
            col = y
    while not leave:
        date()
        print("\t\t\t\t     Select and Confirm the Deadline of Assessment")
        print()
        print("%60s" % month_name[month], schedule_year)
        print()
        print("\t\t\t\t", end = "")
        for x in range(len(day_abbr)):
            print(day_abbr[x], end = "\t")
        print()
        for i in range(len(month_day)):
            print("\t\t\t\t ", end = "")
            for j in range(len(month_day[i])):
                if month_day[i][j] == 0:
                    month_day[i][j] = " " 
                if month_day[row][col] != month_day[i][j]:
                    print(month_day[i][j], end = "\t ")
                else:
                    print(Fore.RED + str(month_day[i][j]) + Style.RESET_ALL, end = "\t ")
            print()
        for i in range(11):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.UP and k != key.DOWN and k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == key.UP and row > 0 and month_day[row-1][col] != " ":
            day_num -= 7
            row -= 1
        elif k == key.DOWN and row < len(month_day)-1 and month_day[row+1][col] != " ":
            day_num += 7
            row += 1
        elif k == key.LEFT and col > 0 and month_day[row][col-1] != " ":
            day_num -= 1
            col -= 1
        elif k == key.RIGHT and col < 6 and month_day[row][col+1] != " ":
            day_num += 1
            col += 1
        elif k == key.ENTER:
            if month == int(current_month) and day_num <= int(current_day):
                pass
            else:
                return day_num
        elif k == key.ESC:
            leave = True
#---------------------------------------------------------------------------------
def setting_function(): # To open setting function
    os.system("cls")
    date()
    print("\t\t\t\t\t\t      Settings")
    for x in range(8):
        print()
    print("\t\t\t\t          <1>  Reset Password")
    print()
    print("\t\t\t\t         <ESC> Back")
    k = readkey()
    while k != "1" and k != key.ESC:
        k = readkey()
    if k == "1":
        os.system("cls")
        print()
        resetpw_function()
    elif k == key.ESC:
        teachers_system()
#--------------------------------------------------------------------------------- 
def resetpw_function(): # To reset password
    global login_name, password
    pw_ok = False
    date()
    print("")
    print("\t\tPassword must include at least 8 characters (at least 1 number, 1 capital letter and 1 small letter)")
    print("\t\t\t\t         Password must not contain any blank space")
    print()
    print("<Empty input> Exit".rjust(65))
    print()
    old_pw = input("Enter the Old Password: ".rjust(64))
    if old_pw == "":
        setting_function()
    else:
        old_pw = encrypted_pw(old_pw)
        if old_pw != password[password_index]:
            os.system("cls")
            print("The Old Password is incorrect".rjust(70))
            resetpw_function()
        else:
            new_pw = input("Enter the New Password: ".rjust(64))
            new_pw = encrypted_pw(new_pw)
            if new_pw == "":
                setting_function()
            elif new_pw == old_pw:
                os.system("cls")
                print("The Password Should Not Be Same.".rjust(70))
                resetpw_function()
            else:
                re_enter_pw = input("Enter the New Password again: ".rjust(70))
                re_enter_pw = encrypted_pw(re_enter_pw)
                if re_enter_pw == "":
                    setting_function()
                else:
                    os.system("cls")
                    if new_pw != re_enter_pw:
                        print("Two New Password are not the same ".rjust(76))
                        resetpw_function()
                    else:
                        pw_ok = pw_check(new_pw)
                        if pw_ok == True:
                            password[password_index] = new_pw
                            update_password()
                            login_name, password = get_data()
                            for x in range(10):
                                print()
                            print("RESET PASSWORD SUCCESSFUL".rjust(68))
                            print()
                            print("Please Login Again".rjust(65))
                            print()
                            input("Press <ENTER> to continue.".rjust(69))
                            
                        else:
                            print("The New Password Does Not Meet Requirements".rjust(77))
                            resetpw_function()
#--------------------------------------------------------------------------------- 
def admin_resetpw_function(): # To reset password
    pw_ok = False
    date()
    print("")
    print("\t\tPassword must include at least 8 characters (at least 1 number, 1 capital letter and 1 small letter)")
    print("\t\t\t\t         Password must not contain any blank space")
    print()
    print("<Empty input> Exit".rjust(65))
    print()
    old_pw = input("Enter the Old Password: ".rjust(64))
    if old_pw == "":
        admin_function()
    else:
        old_pw = encrypted_pw(old_pw)
        if old_pw != password[password_index]:
            os.system("cls")
            print("The Old Password is incorrect".rjust(70))
            admin_resetpw_function()
        else:
            new_pw = input("Enter the New Password: ".rjust(64))
            new_pw = encrypted_pw(new_pw)
            if new_pw == "":
                admin_function()
            elif new_pw == old_pw:
                os.system("cls")
                print("The Password Should Not Be Same.".rjust(70))
                resetpw_function()
            else:
                re_enter_pw = input("Enter the New Password again: ".rjust(70))
                re_enter_pw = encrypted_pw(re_enter_pw)
                if re_enter_pw == "":
                    admin_function()
                else:
                    os.system("cls")
                    if new_pw != re_enter_pw:
                        print("Two New Password are not the same ".rjust(76))
                        admin_resetpw_function()
                    else:
                        pw_ok = pw_check(new_pw)
                        if pw_ok == True:
                            password[password_index] = new_pw
                            update_password()
                            for x in range(10):
                                print()
                            print("RESET PASSWORD SUCCESSFUL".rjust(68))
                            print()
                            print("Please Login Again".rjust(65))
                            print()
                            input("Press <ENTER> to continue.".rjust(69))
                            
                        else:
                            print("The New Password Does Not Meet Requirements".rjust(77))
                            admin_resetpw_function()
#---------------------------------------------------------------------------------
def pw_check(pw):
    word_length, capital, small_letter, num, blank_space = pw_range_check(pw)
    if word_length == True and capital == True and small_letter == True and num == True and blank_space == True:
        return True
    else:
        return
#---------------------------------------------------------------------------------
def pw_range_check(pw2):
    wl = cl = sl = number = space = False
    for i in range(len(pw2)):
        if len(pw2) >= 8:
            wl = True
        if pw2[i] < "]" and pw2[i] > "?":
            cl = True
        if pw2[i] >= "/" and pw2[i] < ":":
            number = True
        if pw2[i] > "`" and pw2[i] < "|":
            sl = True
        if pw2[i] != " ":
            space = True
    return wl, cl, sl, number, space
#---------------------------------------------------------------------------------
def encrypted_pw(pw): # To encrypted password(unencrypted)
    word = []
    temp = ""
    word.extend(pw) # To separate password(string) into list(word)
    for j in range(len(word)):
        word[j] = chr(ord(word[j]) + 5)
        temp += word[j] # To combine charactors into a string(result)
    return temp
#---------------------------------------------------------------------------------
def decrypted_pw(ip_pw): # To decrypted password(encrypted)
    word = []
    temp = ""
    word.extend(ip_pw)
    for i in range(len(word)):
        word[i] = chr(ord(word[i]) - 5)
        temp += word[i] # combine char in list to a string
    return temp
#---------------------------------------------------------------------------------
def update_username():
    f = open("username.txt", "w")
    for i in range(len(login_name)): # write all username into text file
        if i < len(login_name)-1:
            f.write(login_name[i] + "\n")
        else:
            f.write(login_name[i] + "")
    f.close()
#---------------------------------------------------------------------------------
def update_password(): # update the password in text file
    f = open("encrypted_pw.txt", "w")
    for i in range(len(password)): # write all account password into text file
        if i < len(password) - 1:
            f.write(password[i] + "\n")
        else:
            f.write(password[i] + "")
    f.close()
#---------------------------------------------------------------------------------
def update_assm(assm_list):
    f = open(selected_class + "_assessments.txt", "w")
    for i in range(len(assm_list)):
        if i < len(assm_list) - 1:
            f.write(assm_list[i] + "\n")
        else:
            f.write(assm_list[i] + "")
    f.close()
#---------------------------------------------------------------------------------
def update_class():
    f = open("class_list.txt", "w")
    for i in range(len(class_list)):
        for j in range(len(class_list[i])):
            if j < len(class_list[i]) - 1:
                f.write(class_list[i][j] + "\t")
            elif i != len(class_list) - 1 and j != len(class_list[i]):
                f.write(class_list[i][j] + "\n")
            else:
                f.write(class_list[i][j] + "")
    f.close()
#---------------------------------------------------------------------------------
while True:	# main program
    login_or_not = main_menu()
    if login_or_not:
        count = 0
        login(count)
    else:
        break

#56%