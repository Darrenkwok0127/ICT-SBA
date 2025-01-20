import calendar
import os
from datetime import datetime, date
from readchar import readkey, key
from colorama import Fore, Style
import maskpass

def date(): # Output the date of today
    get_date()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t    ", end = "")
    print(current_date) # Output date
def get_date(): # Getting current date from computer
    global current_date, current_month, current_year, next_year, current_day
    current = datetime.now() # To find the current date
    current_date = str(current.date())
    current_day = current.strftime("%d")
    current_month = current.strftime("%m")
    current_year = current.strftime("%Y")
    next_year = int(current_year) + 1
#-------------------------------------------------------------------------------------------------------
def system_name(): # Output the title
    print(
"""                     █████╗  ██████╗ ██████╗███████╗ ██████╗ ██████╗███╗   ███╗███████╗███╗  ██╗████████╗
                    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝████╗ ████║██╔════╝████╗ ██║╚══██╔══╝
                    ███████║╚█████╗ ╚█████╗ █████╗  ╚█████╗ ╚█████╗ ██╔████╔██║█████╗  ██╔██╗██║   ██║   
                    ██╔══██║ ╚═══██╗ ╚═══██╗██╔══╝   ╚═══██╗ ╚═══██╗██║╚██╔╝██║██╔══╝  ██║╚████║   ██║   
                    ██║  ██║██████╔╝██████╔╝███████╗██████╔╝██████╔╝██║ ╚═╝ ██║███████╗██║ ╚███║   ██║   
                    ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   """)
    print("""
 ██████╗ █████╗ ██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗   ██████╗██╗   ██╗ ██████╗████████╗███████╗███╗   ███╗
██╔════╝██╔══██╗██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
╚█████╗ ██║  ╚═╝███████║█████╗  ██║  ██║██║   ██║██║     █████╗    ╚█████╗  ╚████╔╝ ╚█████╗    ██║   █████╗  ██╔████╔██║
 ╚═══██╗██║  ██╗██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝     ╚═══██╗  ╚██╔╝   ╚═══██╗   ██║   ██╔══╝  ██║╚██╔╝██║
██████╔╝╚█████╔╝██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗  ██████╔╝   ██║   ██████╔╝   ██║   ███████╗██║ ╚═╝ ██║
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝  ╚═════╝    ╚═╝   ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝""")
#-------------------------------------------------------------------------------------------------------
def main_menu(): # main menu
    os.system("cls")
    date()
    system_name()
    print()
    print()
    print()
    print("                                                  <1>  Login")
    print()
    print("                                                  <2>  Forget Password")
    print()
    print("                                                 <ESC> Exit")
    k = readkey() # reading keyboard input
    while k != "1" and k != "2" and k != key.ESC:
        k = readkey()
    if k == "1": # When user press "1", it goes into login system
        os.system("cls")
        date()
        system_name()
        get_data()
        print()
        print()
        return k
    elif k == "2": # When user press "2", it goes into forget password function
        os.system("cls")
        get_data()
        get_request()
        return k
    elif k == key.ESC: # When user press "ESC", it exits the program
        return "3"
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
def bubble_sort(unsorted_list): # bubble sort with ascending order
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                swap(j, j+1, unsorted_list)
#---------------------------------------------------------------------------------
def swap(a, b, ul): #swap items
    temp = ul[a]
    ul[a] = ul[b]
    ul[b] = temp
#---------------------------------------------------------------------------------
def get_data(): # Getting data from text file and make them(username & encrypted_password) into lists
    global login_name, password
    f1 = open("username.txt", "r")
    f2 = open("encrypted_pw.txt", "r")
    login_name = f1.readlines()
    password = f2.readlines()
    f1.close()
    f2.close()
    for i in range(len(login_name)):
        login_name[i] = login_name[i].strip("\n")
    for j in range(len(password)):
        password[j] = password[j].strip("\n")
#---------------------------------------------------------------------------------
def get_class(): # Getting class list e.g 1A
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
    global admin_pw
    f = open("encrypted_admin_pw.txt", "r")
    admin_pw = f.readlines()
    f.close()
    for i in range(len(admin_pw)):
        admin_pw[i] = admin_pw[i].strip()
#---------------------------------------------------------------------------------
def get_request(): # Getting reset password request from text file
    global request
    f = open("forgetpw_request.txt", "r")
    request = f.readlines()
    f.close()
    for i in range(len(request)):
        request[i] = request[i].strip("\n")
#---------------------------------------------------------------------------------
def get_defaultpw(): # Getting default password from text file
    global default_pw
    f = open("default_password.txt", "r")
    default_pw = f.readlines()
    f.close()
    for i in range(len(default_pw)):
        default_pw[i] = default_pw[i].strip("\n")
#---------------------------------------------------------------------------------
def get_assm(): # Getting all assessments from text file
    global assm
    f = open(path + "\\"+ form + "\\" + selected_class + "_assessments.txt", "r")
    assm = f.readlines()
    f.close()
    for i in range(len(assm)):   
        assm[i] = assm[i].strip("\n")
        assm[i] = assm[i].split("\t")
    bubble_sort(assm)
    while len(assm) > 0 and assm[0][0] < current_date:
        get_assm_log()
        assm_log.append(assm[0][0])
        del assm[0]
        update_assm_log()
    update_assm()
#---------------------------------------------------------------------------------
def get_assm_log(): # Getting assessments log from text file
    global assm_log
    f = open(path + "\\" + form +"_hw_log" + "\\" + selected_class + "_assessments_hw_log.txt", "r")
    assm_log = f.readlines()
    f.close()
    for i in range(len(assm_log)):
        assm_log[i] = assm_log[i].strip("\n")
#---------------------------------------------------------------------------------
def login(): # Login Page
    global username_index, password_index
    while True:
        print("                                                     ⬇ [<Empty> To Return]")
        print()
        input_username = input("                                                  Username: ")
        if input_username == "":
            return
        else:
            print()
            input_password = maskpass.askpass("                                                  Password: ")
            input_password = encrypted_pw(input_password) # Encrypting password(unencrypted) so it uses to find if it is correct in the text file
            admin1, username_index = search_admin(login_name, input_username) # Search for admin username
            if admin1: # When admin username found, check if admin password is correct
                admin2, password_index = search_admin(password, input_password) # Search for admin password
                check1 = False
                check2 = False
            else:
                check1, username_index = linear_search(login_name, input_username)
                if username_index != None and password[username_index] == input_password:
                    password_index = username_index
                    check2 = True
                else:
                    check2 = False
            if admin1 and admin2 and username_index == password_index: #Check if it is the correct username and password (admin)
                os.system("cls")
                get_class()
                for x in range(12):
                    print()
                print("LOGIN SUCCESSFUL".rjust(64))
                print()
                print("Press <ANY KEY> to continue.".rjust(69))
                readkey()
                return admin_system()
            else:
                if check1 and check2 and username_index == password_index: #Check if it is the correct username and password (teachers)
                    os.system("cls")
                    get_class()
                    for x in range(12):
                        print()
                    print("LOGIN SUCCESSFUL".rjust(64))
                    print()
                    print("Press <ANY KEY> to continue.".rjust(69))
                    readkey()
                    return teachers_system() 
            os.system("cls")
            date()
            system_name()
            print("The username/password is incorrect.".rjust(77))
            print()
#---------------------------------------------------------------------------------
def forget_pw(): # Forget Password
    global request
    print()
    print()
    print("                                                  Forget your password? ")
    print()
    inp_name = input("                                        Please Enter your Username: ")
    if inp_name == "":
        return
    else:
        isadmin1, username_index = search_admin(login_name, inp_name)
        if isadmin1:
            check = False
        else:
            check, username_index = linear_search(login_name, inp_name)
            found, temp = linear_search(request, str(username_index))
        if check and not found:
            os.system("cls")
            date()
            system_name()
            request = request + [username_index]
            update_forgetpw_request()
            print()
            print()
            print()
            print("                                               Reset Password Request Sent")
            print()
            print("                                 Administrator Will Reset Your Password To Default ASAP")
            print()
            print("                                               Press <ANY KEY> To Continue")
            readkey()
        elif found:
            os.system("cls")
            date()
            system_name()
            print()
            print()
            print()
            print("                                                  Reset Request Pending")
            print()
            print("                                          Please Wait For Administrator to Reset")
            print()
            print("                                                Press <ANY KEY> To Return")
            readkey()
        else:
            os.system("cls")
            date()
            system_name()
            print("                                         Username Not Found. Please Enter Again.")
            return forget_pw()
#---------------------------------------------------------------------------------
def admin_system(): # Admin account
    get_request()
    get_defaultpw()
    os.system("cls")
    date()
    print("                                                    Welcome Back." , login_name[username_index])
    for x in range(8):
        print()
    print("                                        <1>  Teachers Class Information")
    print()
    print("                                        <2>  Settings (Administrator)")
    print()
    if len(request) == 0:
        print("                                        <3>  Reset Password Request")
    else:
        print("                                        <3>" + Fore.RED + "  Reset Password Request *", Style.RESET_ALL)
    print()
    print("\t\t\t\t       <ESC> Sign Out")
    print()
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != key.ESC:
        k = readkey()
    if k == "1":
        os.system("cls")
        print()
        return teachers_info_function()
    elif k == "2":
        return admin_setting()
    elif k == "3":
        return reset_request()
    elif k == key.ESC:
        return
#---------------------------------------------------------------------------------
def teachers_info_function(): # Change teachers' class information
    get_data()
    date()
    for x in range(9):
        print()
    print("                                    Which Teachers' account info you want to change?")
    print()
    inp_username = input("                                    <Empty input> Exit : ")
    if inp_username == "":
        return admin_system()
    else:
        found, teachers_acc_index = linear_search(login_name, inp_username)
        if found and teachers_acc_index != 0:
            return show_assigned_class(teachers_acc_index)
        else:
            os.system("cls")
            print("                                          User Not Found / Wrong Input.")
            return teachers_info_function()
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
        return add_class(index)
    elif k == "2":
        return del_class(index)
    elif k == key.ESC:
        return teachers_info_function()
#---------------------------------------------------------------------------------
def add_class(index): # Assign Class to teachers
    selected = []
    while len(selected) <= 2:
        if len(selected) == 0:
            selected_form = choose_form(index)
            if selected_form == None:
                return show_assigned_class(index)
            else:
                selected.append(selected_form)
        if len(selected) == 1:
            selected_form_char = choose_form_char(index)
            if selected_form_char == None:
                selected.pop()
            else:
                selected.append(selected_form_char)
        if len(selected) == 2:
            selected_class = str(selected[0]) + selected[1]
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
                os.system("cls")
                if k == key.ENTER:
                    selected.pop()
                elif k == key.ESC:
                    return show_assigned_class(index)
            else:
                date()
                for i in range(10):
                    print()
                print("                                           This Class Had Already Assigned.")
                print()
                print("                                              Press <ANY KEY> To Return")
                readkey()
                os.system("cls")
                selected.pop()
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
def del_class(index): # Select the class you want to remove
    col = 1
    row = 1
    class_num = 1
    leave = False
    while not leave:
        row_num = 0
        os.system("cls")
        date()
        print()
        print("                                           Select the Class You Want to Delete")
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
        for x in range(13-row_num):
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
                return del_class(index)
            if leave:
                if len(class_list[index]) == 1:
                    class_list[index][0] = "Not yet Assigned"
                else:
                    del class_list[index][class_num-1]
                update_class()
                if class_list[index][0] == "Not yet Assigned":
                    return show_assigned_class(index)
                else:
                    return del_class(index)
        elif k == key.ESC:
            leave = True
            return show_assigned_class(index)
#---------------------------------------------------------------------------------
def admin_setting(): # Admin Setting
    os.system("cls")
    date()
    print("\t\t\t\t\t\t   Administrator Setting")
    for x in range(8):
        print()
    print("\t\t\t\t         <1>  Reset Password")
    print()
    print("\t\t\t\t         <2>  Create Account")
    print()
    print("\t\t\t\t         <3>  Delete Account")
    print()
    print("\t\t\t\t        <ESC> Back")
    print()
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != key.ESC:
        k = readkey()
    os.system("cls")
    if k == "1":
        print()
        return resetpw_function()
    elif k == "2":
        print()
        return create_acc_function()
    elif k == "3":
        print()
        return delete_acc_function()
    elif k == key.ESC:
        return admin_system()
#---------------------------------------------------------------------------------
def create_acc_function(): # To create a new teacher account
    global login_name, password, default_pw, class_list
    pw_ok = False
    found = False
    date()
    get_adminpw_data()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(64))
    print()
    if input_admin_pw == "":
        return admin_setting()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]:
            os.system("cls")
            print("Administrator Password Incorrect.".rjust(75))
            return create_acc_function()
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
                    return admin_setting()
                elif check:
                    os.system("cls")
                    print("Username Has Been Used. Please Try Again".rjust(77)) 
                else:
                    print()
                    add_password = input("\t\t\t         Enter New Teacher Account Password: ")
                    if add_password == "":
                        return admin_setting()
                    else:
                        pw_ok = pw_check(add_password)
                        if pw_ok:
                            found = True
                            add_password = encrypted_pw(add_password)
                            login_name = login_name + [add_username]
                            password = password + [add_password]
                            default_pw = default_pw + [add_password]
                            class_list = class_list + [["Not yet Assigned"]]
                            update_username()
                            update_password()
                            update_defaultpw()
                            update_class()
                            os.system("cls")
                            for x in range(12):
                                print()
                            print("\t\t\t\t\t         SIGN UP SUCCESSFUL")
                            print()
                            print("\t\t\t\t\t       Press <ANY KEY> To Exit")
                            readkey()
                            return admin_setting()
                        else:
                            os.system("cls")
                            print("The New Password Does Not Meet Requirements".rjust(77))
#---------------------------------------------------------------------------------
def delete_acc_function(): # To delete teachers' account
    temp = 0
    date()
    get_adminpw_data()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(61))
    print()
    if input_admin_pw == "":
        return admin_setting()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]:
            os.system("cls")
            print("Administrator Password Incorrect.".rjust(75))
            return delete_acc_function()
        else:
            found = False
            while not(found):
                if temp > 0:
                    print("<Empty input> Exit".rjust(65))
                    print()
                input_accname = input("\t\t\t   Enter the Account Username you want to delete: ")
                if input_accname == "":
                    return admin_setting()
                    break
                else:
                    check, index_user = linear_search(login_name, input_accname)
                    if check and index_user != 0:
                        found = True
                        del login_name[index_user]
                        del password[index_user]
                        del default_pw[index_user]
                        del class_list[index_user]
                        update_username()
                        update_password()
                        update_defaultpw()
                        update_class()
                        os.system("cls")
                        for i in range(12):
                            print()
                        print("\t\t\t\t\t      ACCOUNT DELETE SUCCESSFUL")
                        print()
                        print("\t\t\t\t\t       Press <ANY KEY> To Exit")
                        readkey()
                        return admin_setting()
                    else:
                        temp = 1
                        os.system("cls")
                        print("                                    Username not found / Invalid. Please try it again")
                        date()
#---------------------------------------------------------------------------------
def reset_request():
    leave = False
    select_index = 1
    while not leave:
        os.system("cls")
        date()
        if len(request) == 0:
            leave = True
            for i in range(11):
                print()
            print("                                     There is no reset password request from teachers")
            print()
            print("                                               Press <ANY KEY> To Return")
            readkey()
            return admin_system()
        else:
            row_num = 0
            if len(request) < 5:
                current_req = [''] * len(request)
                for i in range(len(request)):
                    current_req[i] = request[i]
            else:
                current_req = [''] * 5
                for i in range(5):
                    current_req[i] = request[i]
            print("                                                  Reset Request From:")
            for x in range(6):
                print()
            for i in range(len(current_req)):
                if i+1 != select_index:
                    print("                                                       "+ login_name[int(current_req[i])])
                else:
                    print("                                                       "+ Fore.RED + login_name[int(current_req[i])] + Style.RESET_ALL)
                print()
                row_num += 2
            for j in range(18-row_num):
                print()
            print("                                   <UP>      <DOWN>      <ENTER> Confirm      <ESC> Back")
            k = readkey()
            while k != key.UP and k != key.DOWN and k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.UP and select_index >= 1:
                select_index -= 1
                if select_index == 0:
                    select_index = len(current_req)
            elif k == key.DOWN and select_index <= len(current_req):
                select_index += 1
                if select_index > len(current_req):
                    select_index = 1
            elif k == key.ENTER:
                os.system("cls")
                date()
                for i in range(12):
                    print()
                print("                                        Reset User's [" + login_name[int(current_req[select_index-1])] + "] Password to Default?")
                print()
                print("                                 <ENTER> Accept      <BACKSPACE> Decline      <ESC> Back")
                k = readkey()
                while k != key.ENTER and k != key.BACKSPACE and k != key.ESC:
                    k = readkey()
                if k == key.ENTER:
                    os.system("cls")
                    get_defaultpw()
                    password[int(current_req[select_index-1])] = default_pw[int(current_req[select_index-1])]
                    del request[select_index-1]
                    update_password()
                    update_forgetpw_request()
                    date()
                    for i in range(10):
                        print()
                    print("                                               Password Reset Successful.")
                    print()
                    print("                                               Press <ANY KEY> To Return")
                    readkey()
                    select_index = 1
                elif k == key.BACKSPACE:
                    os.system("cls")
                    del request[select_index-1]
                    update_forgetpw_request()
                    date()
                    print("                                                   Request Declined")
                    print()
                    print("                                               Press <ANY KEY> To Return")
                elif k == key.ESC:
                    None
            elif k == key.ESC:
                return admin_system()
#---------------------------------------------------------------------------------
def teachers_system(): # Teachers accounts
    get_defaultpw()
    os.system("cls")
    if password[password_index] == default_pw[password_index]:
        date()
        for i in range(10):
            print()
        print("                                                  First Login Detected")
        print()
        print("                                Please Change your password. Press <ANY KEY> To Continue")
        readkey()
        os.system("cls")
        print()
        change_pw()
    else:
        date()
        print("                                                    Welcome Back." , login_name[username_index])
        for x in range(8):
            print()
        print("                                        <1>  Schedule Assessments System")
        print()
        print("                                        <2>  Settings")
        print()
        print("                                        <3>  Searching")
        print()
        print("                                       <ESC> Sign Out")
        k = readkey()
        while k != "1" and k != "2" and k != "3" and k != key.ESC:
            k = readkey()
        os.system("cls")
        if k == "1":
            return choose_class(k)
        elif k == "2":
            return teacher_setting()
        elif k == "3":
            return choose_class(k)
        elif k == key.ESC:
            return
#---------------------------------------------------------------------------------
def choose_class(key_num): # Select classes adding into teachers' account
    total_page_num = -(-len(class_list[username_index])//8)
    page_num = 1
    start_num = 0
    if class_list[username_index][0] != "Not yet Assigned":
        global selected_class, form
        class_group = [0] * len(class_list[username_index])
        while True:
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
                    return teachers_system()
                else:
                    selected_class = class_group[k-1]
                    if int(selected_class[:1]) <= 3:
                        form = "Junior"
                    else:
                        form = "Senior"
                    if key_num == "1":
                        return schedule_function()
                    else:
                        return searching()
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
                print("                               <LEFT> Previous Page      <RIGHT> Next Page      <ESC> Leave")
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
                    return teachers_system()
                else:
                    selected_class = class_group[(page_num-1)*8+k-1]
                    if int(selected_class[:1]) <= 3:
                        form = "Junior"
                    else:
                        form = "Senior"
                    if key_num == "1":
                        return schedule_function()
                    else:
                        return searching()
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
                    return teachers_system()
                else:
                    selected_class = class_group[(page_num-1)*8+k-1]
                    if int(selected_class[:1]) <= 3:
                        form = "Junior"
                    else:
                        form = "Senior"
                    if key_num == "1":
                        return schedule_function()
                    else:
                        return searching()
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
                    return teachers_system()
                else:
                    selected_class = class_group[k-1]
                    if int(selected_class[:1]) <= 3:
                        form = "Junior"
                    else:
                        form = "Senior"
                    if key_num == "1":
                        return schedule_function()
                    else:
                        return searching()
    else:
        date()
        for i in range(10):
            print()
        print("                                               Class Not yet Assigned.")
        print()
        print("                                              Press <ANY KEY> To Return")
        readkey()
        return teachers_system()
#---------------------------------------------------------------------------------
def schedule_function(): # To open schedule system function
    os.system("cls")
    date()
    print("       Class: " + selected_class)
    get_assm()
    display_assm()
    if len(assm) == 0:
        print("                                                  <1>  Schedule Assessments")
        print()
        print("                                                 <ESC> Back")
        k = readkey()
        while k != "1" and k != key.ESC:
            k = readkey()
    else:
        print("                             <1> Schedule Assessments                 <2>  Delete Assessments")
        print()
        print("                             <3> Show All Assessments                <ESC> Back")
        k = readkey()
        while k != "1" and k != "2" and k != "3" and k != key.ESC:
            k = readkey()
    os.system("cls")
    if k == "1":
        return add_assms()
    elif k == "2":
        return del_assms()
    elif k == "3":
        return show_all_assms()
    elif k == key.ESC:
        return choose_class("1")
#---------------------------------------------------------------------------------
def display_assm(): # Display Assessments
    if len(assm) == 0:
        print("                                          There is no asseessment assigned.")
        for x in range(21):
            print()
    else: # Displaying recent 6 assessments
        display = [''] * 6
        num = 1
        row_num = 0
        k = 0
        while k < len(assm) and k < len(display):
            display[k] = assm[k][0]
            k += 1
        print("                                     The Most Recent Assessments Scheduled Shown Below")
        print()
        for i in range(len(display)):
            if num % 2 != 0:
                print("\t\t\t    ", display[i], end = "")
            else:
                print("\t\t\t    ", display[i], end = "\n\n")
                row_num += 1
            num += 1
        if k == len(display) and len(assm) > len(display):
            row_num += 1
            print("\t\t\t And More.....")
        for j in range(17-row_num):
            print()
#---------------------------------------------------------------------------------
def add_assms(): # Adding assessment
    selected = [] #stack
    while len(selected) <= 5:
        if len(selected) == 0:
            item = choose_subject()
            if item == None:
                return schedule_function()
            else:
                selected.append(item)
        if len(selected) == 1:
            item = choose_assm_type()
            if item == None:
                selected.pop()
            else:
                selected.append(item)
        if len(selected) == 2:
            item = choose_month()
            if item == None:
                selected.pop()
            else:
                selected.append(item)
        if len(selected) == 3:
            item = choose_deadline(selected[2])
            if item == None:
                selected.pop()
            else:
                selected.append(item)
        if len(selected) == 4:
            inp_time = assm_time()
            if inp_time == None:
                selected.pop()
            else:
                selected.append(inp_time)
        if len(selected) == 5:
            assm_format1 = str(schedule_year) + "-" + "{:02d}".format(selected[2]) + "-" + "{:02d}".format(selected[3])
            assm_format2 = selected[0] + " " + selected[1]
            assm_deadline = assm_format1 + " " + assm_format2
            time = count_time(assm_format1)
            if time >= 5:
                for i in range(9):
                    print()
                print("                        ⚠  WARNING!! There are too many Assessments on a particular day ⚠ ⚠")
                print()
                print("                              The Assessment will schedule on ["+ assm_deadline + "]")
                print()
                print("                                                        Confirm ?")
                print()
                print("                                        <ENTER> Confirm               <ESC> Back")
            else:
                for i in range(11):
                    print()
                print("                              The Assessment will schedule on ["+ assm_deadline + "]")
                print()
                print("                                                        Confirm ?")
                print()
                print("                                        <ENTER> Confirm               <ESC> Back")
            k = readkey()
            while k != key.ENTER and k != key.ESC:
                k = readkey()
            os.system("cls")
            if k == key.ENTER:
                global assm
                assm = assm + [[assm_deadline, selected[4]]]
                update_assm()
                return schedule_function()
            elif k == key.ESC:
                selected.pop()
#---------------------------------------------------------------------------------
def count_time(d):
    total_time = 0
    for i in range(len(assm)):
        find = assm[i][0].find(d)
        if find == -1:
            pass
        else:
            total_time += float(assm[i][1])
    return total_time
#---------------------------------------------------------------------------------
def del_assms(): # Remove assessment and confirm / not
    if len(assm) != 0:
        selected_del_assm = choose_del_assm()
        if selected_del_assm != None:
            for i in range(11):
                print()
            print("\t\t\t\t   You want to Remove The Assessment ["+ assm[selected_del_assm-1][0] + "]")
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
                update_assm()
                return del_assms()
            elif k == key.ESC:
                return del_assms()
    else:
        return schedule_function()
#---------------------------------------------------------------------------------
def choose_del_assm(): # Select the assessment you want to remove
    total_page_num = -(-len(assm)//10)
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
                    print("\t\t\t\t\t\t"+ assm[i][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[i][0] + Style.RESET_ALL)
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
                return schedule_function()
            elif k == key.ENTER:
                return select_index
            elif k == key.UP and select_index > 1:
                select_index -= 1
            elif k == key.DOWN and select_index < len(assm):
                select_index += 1
        elif page_num > 1 and page_num < total_page_num:
            for x in range(start_num, page_num*10):
                if x+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[x][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[x][0] + Style.RESET_ALL)
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
                return schedule_function()
            elif k == key.ENTER:
                return select_index
        elif page_num == total_page_num:
            blank_line = 0
            for y in range(start_num, len(assm)):
                if y+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[y][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[y][0] + Style.RESET_ALL)
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
                return schedule_function()
            elif k == key.ENTER:
                return select_index
        else:
            for z in range(start_num, page_num*10):
                if z+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[z][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.RED + assm[z][0] + Style.RESET_ALL)
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
                return schedule_function()
            elif k == key.ENTER:
                return select_index
#---------------------------------------------------------------------------------
def show_all_assms(): # Show all the assessments scheduled
    blank_line = 0
    total_page_num = -(-len(assm)//11)
    leave = False
    start_num = 0
    page_num = 1
    while not leave:
        date()
        print("\tPage "+ str(page_num) +"\t\t\t\t       Assessments Shown Below: ")
        print()
        if total_page_num < 2:
            for i in range(len(assm)):
                print("\t\t\t\t\t\t"+ assm[i][0])
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
                print("\t\t\t\t\t\t"+ assm[x][0])
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
                print("\t\t\t\t\t\t"+ assm[y][0])
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
                print("\t\t\t\t\t\t"+ assm[z][0])
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
    return schedule_function()
#---------------------------------------------------------------------------------
def choose_subject(): # Select the subject of the assessment
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
def choose_assm_type(): # Select the assessment type
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
def choose_month(): # Select the month you want to add your assessment
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
def choose_deadline(month): # Select the date which students should submit/have their assessment
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
def assm_time():
    os.system("cls")
    date()
    print()
    while True:
        for i in range(10):
            print()
        print("                                                       <Empty> To Return ⬇ ")
        print()
        inp = input("                   How much time does your assessment spend (0.1 - 5hrs): ")
        os.system("cls")
        if inp == "":
            return None
        try:
            inp = float(inp)
            if inp <= 0 or inp > 5:
                date()
                print("                                                 Wrong Input! Enter Again.")
            else:
                return str(inp)
        except ValueError:
            date()
            print("                                                 Wrong Input! Enter Again.")
#---------------------------------------------------------------------------------
def teacher_setting(): # To open setting function
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
        return resetpw_function()
    elif k == key.ESC:
        return teachers_system()
#---------------------------------------------------------------------------------
def resetpw_function(): # To reset password
    while True:
        date()
        print("")
        print("          Password must include at least 8 characters (at least 1 number, 1 capital letter and 1 small letter)")
        print("                                         Password must not contain any blank space")
        print()
        print("                                                    <Empty input> Exit")
        print()
        old_pw = input("                                        Enter the Old Password: ")
        if old_pw == "": # Return admin setting / teacher setting when empty input
            if password_index == 0:
                return admin_setting()
            else:
                return teacher_setting()
        else:
            old_pw = encrypted_pw(old_pw)
            if old_pw != password[password_index]: # Check if the old password is correct
                os.system("cls")
                print("The Old Password is incorrect".rjust(70))
            else:
                new_pw = input("                                        Enter the New Password: ")
                if new_pw == "": # Return admin setting / teacher setting when empty input
                    if password_index == 0:
                        return admin_setting()
                    else:
                        return teacher_setting()
                new_pw = encrypted_pw(new_pw)
                if new_pw == old_pw: # Check if the new password is equal to old password
                    os.system("cls")
                    print("                                            The Password Should Not Be Same.")
                elif new_pw == default_pw[password_index]:
                    os.system("cls")
                    print("                                   The Password Should Not Be Same As Default Password.")
                else:
                    re_enter_pw = input("                                        Enter the New Password again: ")
                    if re_enter_pw == "": # Return admin setting / teacher setting when empty input
                        if password_index == 0:
                            return admin_setting()
                        else:
                            return teacher_setting()
                    else:
                        re_enter_pw = encrypted_pw(re_enter_pw)
                        os.system("cls")
                        if new_pw != re_enter_pw: # Input data twice and check if they are the same
                            print("                                            Two New Password are not the same ")
                        else:
                            pw_ok = pw_check(new_pw)
                            if pw_ok:
                                password[password_index] = new_pw
                                update_password()
                                for x in range(10):
                                    print()
                                print("RESET PASSWORD SUCCESSFUL".rjust(68))
                                print()
                                print("Please Login Again".rjust(65))
                                print()
                                print("Press <ANY KEY> to continue.".rjust(69))
                                readkey()
                                return
                            else:
                                print("                                       The New Password Does Not Meet Requirements")
#---------------------------------------------------------------------------------
def change_pw():
    while True:
        date()
        print("")
        print("          Password must include at least 8 characters (at least 1 number, 1 capital letter and 1 small letter)")
        print("                                         Password must not contain any blank space")
        print()
        print("                                                    <Empty input> Exit")
        print()
        new_pw = input("                                        Enter the New Password: ")
        if new_pw == "": # Return when empty input
            return None
        new_pw = encrypted_pw(new_pw)
        if new_pw == default_pw[password_index]: # Check if the new password is equal to old password
            os.system("cls")
            print("                                            The Password Should Not Be Same.")
        else:
            re_enter_pw = input("                                        Enter the New Password again: ")
            if re_enter_pw == "": # Return when empty input
                return None
            else:
                re_enter_pw = encrypted_pw(re_enter_pw)
                os.system("cls")
                if new_pw != re_enter_pw: # Input data twice and check if they are the same
                    print("                                            Two New Password are not the same ")
                else:
                    pw_ok = pw_check(new_pw)
                    if pw_ok:
                        password[password_index] = new_pw
                        update_password()
                        for x in range(12):
                            print()
                        print("RESET PASSWORD SUCCESSFUL".rjust(68))
                        print()
                        print("Press <ANY KEY> to continue.".rjust(69))
                        readkey()
                        return teachers_system()
                    else:
                        print("                                       The New Password Does Not Meet Requirements")
#---------------------------------------------------------------------------------
def pw_check(pw): # Check if password meet the requirements of password rules
    word_length, capital, small_letter, num, blank_space = pw_range_check(pw)
    if word_length == True and capital == True and small_letter == True and num == True and blank_space == True:
        return True
    else:
        return False
#---------------------------------------------------------------------------------
def pw_range_check(pw2): # Check if the password consists of 8 characters (at least 1 number, 1 capital letter and 1 small letter) with no space
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
def searching(): # Searching
    get_assm_log()
    os.system("cls")
    date()
    print("                                                        Searching")
    for i in range(10):
        print()
    if len(assm_log) != 0:
        print("                                   Please enter any words to search for assessments")
        print()
        inp_search = input("                                                      : ").upper()
        if inp_search == "":
            os.system("cls")
            return choose_class("3")
        else:
            return search_assm(inp_search)
    else:
        print("                                             There are no assessments record")
        print()
        print("                                                Press <ANY KEY> To Return")
        readkey()
        os.system("cls")
        return choose_class("3")
#---------------------------------------------------------------------------------
def search_assm(inp): # To search assessments and show the result
    result = []
    for i in range(len(assm_log)):
        find = assm_log[i].find(inp)
        if find == -1:
            pass
        else:
            result.append(assm_log[i])
    total_page_num = -(-len(result)//20)
    page_num = 1
    while True:
        os.system("cls")
        if total_page_num == 1:
            date()
            print("                                                        Searching")
            print()
            if len(result) == 0:
                print("                                         The search result for \"" + inp + "\" is as follow.")
                print()
                print("                                                    No assessment Found.")
            else:    
                print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
                print()
                for j in range(len(result)):
                    print("                                                 " + "%3s" % str(j+1) + ". " + result[j])
            print()
            for x in range(20-len(result)):
                print()
            print("                                         <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.ENTER:
                return searching()
            elif k == key.ESC:
                os.system("cls")
                return choose_class(3)
        elif page_num > 1 and page_num < total_page_num:
            date()
            print("                                                        Searching")
            print()
            if len(result) == 0:
                print("                                         The search result for \"" + inp + "\" is as follow.")
                print()
                print("                                                    No assessment Found.")
            else:    
                print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
                print()
                for j in range((page_num-1)*20, page_num*20):
                    print("                                                 "+ "%3s" % str(j+1) + ". " + result[j])
            print()
            print("                  <LEFT> Previous Page     <RIGHT> Next Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.LEFT and k != key.RIGHT and k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.LEFT:
                page_num -= 1
            elif k == key.RIGHT:
                page_num += 1
            elif k == key.ENTER:
                return searching()
            elif k == key.ESC:
                os.system("cls")
                return choose_class(3)
        elif page_num == total_page_num:
            date()
            print("                                                        Searching")
            print()
            if len(result) == 0:
                print("                                         The search result for \"" + inp + "\" is as follow.")
                print()
                print("                                                    No assessment Found.")
            else:    
                print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
                print()
                for j in range((page_num-1)*20, len(result)):
                    print("                                                 " + "%3s" % str(j+1) + ". " + result[j])
            print()
            for x in range(20-len(result)+(page_num-1)*20):
                print()
            print("                               <LEFT> Previous Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.LEFT and k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.LEFT:
                page_num -= 1
            elif k == key.ENTER:
                return searching()
            elif k == key.ESC:
                os.system("cls")
                return choose_class(3)
        else:
            date()
            print("                                                        Searching")
            print()
            if len(result) == 0:
                print("                                         The search result for \"" + inp + "\" is as follow.")
                print()
                print("                                                    No assessment Found.")
            else:    
                print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
                print()
                for j in range(page_num*20):
                    print("                                                 " + "%3s" % str(j+1) + ". " + result[j])
            print()
            print("                               <RIGHT> Next Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.RIGHT and k != key.ENTER and k != key.ESC:
                k = readkey()
            if k == key.RIGHT:
                page_num += 1
            elif k == key.ENTER:
                return searching()
            elif k == key.ESC:
                os.system("cls")
                return choose_class(3)
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
def update_assm(): # update assessement in text file
    f = open(path + "\\"+ form + "\\" + selected_class + "_assessments.txt", "w")
    for i in range(len(assm)):
        if i < len(assm) - 1:
            f.write(assm[i][0] + "\t" + assm[i][1] + "\n")
        else:
            f.write(assm[i][0] + "\t" + assm[i][1] + "")
    f.close()
#---------------------------------------------------------------------------------
def update_assm_log(): # update assessment log in text file
    f = open(path + "\\" + form + "_hw_log" + "\\" + selected_class + "_assessments_hw_log.txt", "w")
    for i in range(len(assm_log)):
        if i < len(assm_log) - 1:
            f.write(assm_log[i] + "\n")
        else:
            f.write(assm_log[i] + "")
    f.close()
#---------------------------------------------------------------------------------
def update_class(): # update class list of teachers in text file
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
def update_forgetpw_request(): # update the request of forget password in text file
    f = open("forgetpw_request.txt", "w")
    for i in range(len(request)):
        if i < len(request) - 1:
            f.write(str(request[i]) + "\n")
        else:
            f.write(str(request[i]) + "")
    f.close()
#---------------------------------------------------------------------------------
def update_defaultpw(): # update the default password in text file
    f = open("default_password.txt", "w")
    for i in range(len(default_pw)):
        if i < len(default_pw) - 1:
            f.write(default_pw[i] + "\n")
        else:
            f.write(default_pw[i] + "")
    f.close()
#---------------------------------------------------------------------------------
while True:	# main program
    login_selection = main_menu()
    path = os.getcwd() # Getting the path of this python file
    if login_selection == "1":
        login()
    elif login_selection == "2":
        date()
        system_name()
        print("")
        forget_pw()
    elif login_selection == "3": # Leave Program
        break

#85%