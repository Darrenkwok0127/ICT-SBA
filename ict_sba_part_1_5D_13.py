import calendar
import os
from datetime import datetime, date
import msvcrt
from colorama import Fore, Style
import maskpass
import time

class key:
    def ESC():
        return "\x1b"
    def ENTER():
        return "\x0D"
    def SPACE():
        return "\x20"
    def BACKSPACE():
        return "\x08"
    def UP():
        return "\x00\x48"
    def DOWN():
        return "\x00\x50"
    def LEFT():
        return "\x00\x4b"
    def RIGHT():
        return "\x00\x4d"
#---------------------------------------------------------------------------------
class get:
    def date(): # Getting current date from computer
        global current_date, current_month, current_year, next_year, current_day
        current = datetime.now() # Getting date and time
        current_date = str(current.date()) # To find the current date
        current_day = current.strftime("%d") # Day
        current_month = current.strftime("%m") # Month
        current_year = current.strftime("%Y") # Year
        next_year = int(current_year) + 1 # Find the number of next year
       
    def data(): # Getting data from text file and make them(username & encrypted_password) into lists
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
         
    def classlist(): # Getting class list e.g 1A
        global class_list
        f = open("class_list.txt", "r")
        class_list = f.readlines()
        f.close()
        for i in range(len(class_list)):
            class_list[i] = class_list[i].strip("\n")
        for j in range(len(class_list)):
            class_list[j] = class_list[j].split("\t")
        for x in range(len(class_list)):
            bubble_sort(class_list[x])
        update.classlist()

    def adminpw_data(): # Getting administrator password data from text file
        f = open("encrypted_admin_pw.txt", "r")
        ap = f.readlines()
        f.close()
        for i in range(len(ap)):
            ap[i] = ap[i].strip()
        return ap

    def request(): # Getting reset password request from text file
        global request
        f = open("forgetpw_request.txt", "r")
        request = f.readlines()
        f.close()
        for i in range(len(request)):
            request[i] = request[i].strip("\n")

    def defaultpw(): # Getting default password from text file
        global default_pw
        f = open("default_pw.txt", "r")
        default_pw = f.readlines()
        f.close()
        for i in range(len(default_pw)):
            default_pw[i] = default_pw[i].strip("\n")

    def assm(): # Getting all assessments from text file
        global assm
        f = open(path + "\\"+ form + "\\" + selected_class + "_assessments.txt", "r")
        assm = f.readlines()
        f.close()
        for i in range(len(assm)):   
            assm[i] = assm[i].strip("\n")
            assm[i] = assm[i].split("\t")
        bubble_sort(assm)
        while len(assm) > 0 and assm[0][0] < current_date: # remove and append the expired assessments to assessments log
            get.assm_log()
            assm_log.append(assm[0][0])
            del assm[0]
            update.assm_log()
        update.assm()

    def assm_log(): # Getting assessments log from text file
        global assm_log
        f = open(path + "\\" + form +"_hw_log" + "\\" + selected_class + "_assessments_hw_log.txt", "r")
        assm_log = f.readlines()
        f.close()
        for i in range(len(assm_log)):
            assm_log[i] = assm_log[i].strip("\n")

    def exist_date(m, md, start_num): # Getting the date data from text file
        f = open("exist_date.txt", "r")
        ed = f.readlines()
        f.close()
        for i in range(len(ed)):
            ed[i] = ed[i].strip("\n")
        for j in range(len(ed)):
            ed[j] = ed[j].split("\t")
        for k in range(len(md)):
            for l in range(len(md[k])):
                if md[k][l] != 0:
                    check_weekend = calendar.weekday(schedule_year,m,md[k][l])
                    if check_weekend == 5 or check_weekend == 6:
                        ed[m-1].append(str(md[k][l]))
        if len(md) != 0:
            update.exist_date(ed)
        return ed
#---------------------------------------------------------------------------------
class update: 
    def username(): # update the username in text file
        f = open("username.txt", "w")
        for i in range(len(login_name)): # write all username into text file
            if i < len(login_name)-1:
                f.write(login_name[i] + "\n")
            else:
                f.write(login_name[i] + "")
        f.close()

    def password(): # update the password in text file
        f = open("encrypted_pw.txt", "w")
        for i in range(len(password)): # write all account password into text file
            if i < len(password) - 1:
                f.write(password[i] + "\n")
            else:
                f.write(password[i] + "")
        f.close()

    def assm(): # update assessement in text file
        f = open(path + "\\"+ form + "\\" + selected_class + "_assessments.txt", "w")
        for i in range(len(assm)):
            if i < len(assm) - 1:
                f.write(assm[i][0] + "\t" + assm[i][1] + "\n")
            else:
                f.write(assm[i][0] + "\t" + assm[i][1] + "")
        f.close()

    def assm_log(): # update assessment log in text file
        f = open(path + "\\" + form + "_hw_log" + "\\" + selected_class + "_assessments_hw_log.txt", "w")
        for i in range(len(assm_log)):
            if i < len(assm_log) - 1:
                f.write(assm_log[i] + "\n")
            else:
                f.write(assm_log[i] + "")
        f.close()

    def classlist(): # update class list of teachers in text file
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

    def forgetpw_request(): # update the request of forget password in text file
        f = open("forgetpw_request.txt", "w")
        for i in range(len(request)):
            if i < len(request) - 1:
                f.write(str(request[i]) + "\n")
            else:
                f.write(str(request[i]) + "")
        f.close()

    def defaultpw(): # update the default password in text file
        f = open("default_pw.txt", "w")
        for i in range(len(default_pw)):
            if i < len(default_pw) - 1:
                f.write(default_pw[i] + "\n")
            else:
                f.write(default_pw[i] + "")
        f.close()

    def exist_date(ed): # update the dates (specific period) in text file
        f = open("exist_date.txt", "w")
        for i in range(len(ed)):
            for j in range(len(ed[i])):
                if j < len(ed[i]) - 1:
                    f.write(ed[i][j] + "\t")
                elif i != len(ed) - 1 and j != len(ed[i]):
                    f.write(ed[i][j] + "\n")
                else:
                    f.write(ed[i][j] + "")
#---------------------------------------------------------------------------------
def print_date(): # Output the date of today
    get.date()
    print("                                                                                                            ", end = "")
    print(current_date) # Output date
#-------------------------------------------------------------------------------------------------------   
def system_name(): # Output the title
    print(Fore.BLUE +
"""                     █████╗  ██████╗ ██████╗███████╗ ██████╗ ██████╗███╗   ███╗███████╗███╗  ██╗████████╗
                    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝████╗ ████║██╔════╝████╗ ██║╚══██╔══╝
                    ███████║╚█████╗ ╚█████╗ █████╗  ╚█████╗ ╚█████╗ ██╔████╔██║█████╗  ██╔██╗██║   ██║   
                    ██╔══██║ ╚═══██╗ ╚═══██╗██╔══╝   ╚═══██╗ ╚═══██╗██║╚██╔╝██║██╔══╝  ██║╚████║   ██║   
                    ██║  ██║██████╔╝██████╔╝███████╗██████╔╝██████╔╝██║ ╚═╝ ██║███████╗██║ ╚███║   ██║   
                    ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝   """)
    print("""
 ██████╗ █████╗ ██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗   ██████╗██╗   ██╗ ██████╗████████╗███████╗███╗   ███╗
██╔════╝██╔══██╗██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
╚█████╗ ██║  ╚═╝███████║█████╗  ██║  ██║██║   ██║██║     █████╗    ╚█████╗  ╚████╔╝ ╚█████╗    ██║   █████╗  ██╔████╔██║
 ╚═══██╗██║  ██╗██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝     ╚═══██╗  ╚██╔╝   ╚═══██╗   ██║   ██╔══╝  ██║╚██╔╝██║
██████╔╝╚█████╔╝██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗  ██████╔╝   ██║   ██████╔╝   ██║   ███████╗██║ ╚═╝ ██║
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝  ╚═════╝    ╚═╝   ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝""" + Fore.RESET)
#-------------------------------------------------------------------------------------------------------
def leave_msg(): # Leave message
    os.system("cls")
    print_date()
    system_name()
    for x in range(3):
        print()
    print(Fore.CYAN)
    print("                            ██████╗   █████╗   █████╗  ██████╗  ██████╗  ██╗   ██╗ ███████╗ ██╗")
    print("                           ██╔════╝  ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗ ╚██╗ ██╔╝ ██╔════╝ ██║")
    print("                           ██║  ██╗  ██║  ██║ ██║  ██║ ██║  ██║ ██████╦╝  ╚████╔╝  █████╗   ██║")
    print("                           ██║  ╚██╗ ██║  ██║ ██║  ██║ ██║  ██║ ██╔══██╗   ╚██╔╝   ██╔══╝   ╚═╝")
    print("                           ╚██████╔╝ ╚█████╔╝ ╚█████╔╝ ██████╔╝ ██████╦╝    ██║    ███████╗ ██╗")
    print("                            ╚═════╝   ╚════╝   ╚════╝  ╚═════╝  ╚═════╝     ╚═╝    ╚══════╝ ╚═╝")
    print(Fore.RESET)
#-------------------------------------------------------------------------------------------------------
def main_menu(): # main menu
    os.system("cls")
    print_date()
    system_name()
    print()
    print()
    print(Fore.CYAN)
    print("                                                  <1>  Login")
    print()
    print("                                                  <2>  Forget Password")
    print()
    print("                                                 <ESC> Exit")
    print(Fore.RESET)
    k = readkey() # reading keyboard input
    while k != "1" and k != "2" and k != key.ESC():
        k = readkey()
    if k == "1": # When "1" key is pressed, it goes into login system
        os.system("cls")
        print_date()
        system_name()
        get.data()
        print()
        print()
        return "1"
    elif k == "2": # When "2" key is pressed, it goes into forget password function
        os.system("cls")
        get.data()
        get.request()
        return "2"
    elif k == key.ESC(): # When ESC key is pressed, it exits the program
        return "3"
#---------------------------------------------------------------------------------
def linear_search(arr, target): # To search if the target exists(e.g. teachers account)
    found = False
    for i in range(len(arr)): # linear search
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
def login(): # Login Page
    global username_index, password_index
    while True:
        print("                                                     [<Empty> To Return]")
        print()
        input_username = input("                                                  Username: ")
        if input_username == "":
            return
        else:
            print()
            input_password = maskpass.askpass("                                                  Password: ")
            input_password = encrypted_pw(input_password) # Encrypting password(unencrypted) so it uses to find if it is correct in the text file
            admin1, username_index = search_admin(login_name, input_username) # Search for admin username
            if admin1: # Check if admin account is logging in
                admin2, password_index = search_admin(password, input_password) # Search for admin password
                if admin1 and admin2 and username_index == password_index: # Check if it is the correct username and password (admin)
                    os.system("cls")
                    get.classlist()
                    for x in range(12):
                        print()
                    print(Fore.GREEN + "LOGIN SUCCESSFUL".rjust(64))
                    print()
                    print("Press <ANY KEY> to continue.".rjust(69) + Fore.RESET)
                    readkey()
                    loading()
                    return admin_system()
            else: # Check if teachers account is logging in
                check1, username_index = linear_search(login_name, input_username) # Search for teacher's username
                if username_index != None and password[username_index] == input_password:
                    password_index = username_index
                    check2 = True
                else:
                    check2 = False
                if check1 and check2 and username_index == password_index: # Check if it is the correct username and password (teachers)
                    os.system("cls")
                    get.classlist()
                    for x in range(12):
                        print()
                    print(Fore.GREEN + "LOGIN SUCCESSFUL".rjust(64))
                    print()
                    print("Press <ANY KEY> to continue.".rjust(69) + Fore.RESET)
                    readkey()
                    loading()
                    return teachers_system() 
            os.system("cls")
            print_date()
            system_name()
            print(Fore.RED + "The username/password is incorrect.".rjust(77) + Fore.RESET)
            print()
#---------------------------------------------------------------------------------
def forget_pw(): # Forget Password
    global request
    get.defaultpw()
    print()
    print()
    print("                                                  Forget your password? ")
    print()
    inp_name = input("                                        Please Enter your Username: ")
    if inp_name == "": # Return to main menu when empty input
        return
    else:
        isadmin1, username_index = search_admin(login_name, inp_name)
        if isadmin1: # If admin username detected
            check = False
            found = False
        else: # Teachers username detected
            check, username_index = linear_search(login_name, inp_name) # Check if teacher username exists
            found, temp = linear_search(request, str(username_index)) # Check if it didn't send request before
        if check and password[username_index] == default_pw[username_index]:
            os.system("cls")
            print_date()
            system_name()
            print()
            print()
            print()
            print(Fore.RED + "                                                     Request Decline")
            print()
            print("                                                Default Password Detected" + Fore.RESET)
            print()
            print("                                                Press <ANY KEY> To Return")
            readkey()
        elif check and not found: # teacher username exists and request send for the first time
            os.system("cls")
            print_date()
            system_name()
            request = request + [username_index]
            update.forgetpw_request()
            print()
            print()
            print()
            print(Fore.GREEN + "                                               Reset Password Request Sent")
            print()
            print("                                 Administrator Will Reset Your Password To Default ASAP" + Fore.RESET)
            print()
            print("                                                Press <ANY KEY> To Return")
            readkey()
        elif found: # request exists
            os.system("cls")
            print_date()
            system_name()
            print()
            print()
            print()
            print(Fore.RED + "                                                  Reset Request Pending")
            print()
            print("                                          Please Wait For Administrator to Reset" + Fore.RESET)
            print()
            print("                                                Press <ANY KEY> To Return")
            readkey()
        else: # No username found
            os.system("cls")
            print_date()
            system_name()
            print(Fore.RED + "                                         Username Not Found. Please Enter Again." + Fore.RESET)
            return forget_pw()
#---------------------------------------------------------------------------------
def admin_system(): # Admin account
    get.request()
    get.defaultpw()
    os.system("cls")
    print_date()
    print("                                                    Welcome Back." , login_name[username_index])
    for x in range(8):
        print()
    print(Fore.CYAN + "                                        <1>  Teachers Class Information")
    print()
    print("                                        <2>  Settings (Administrator)")
    print()
    if len(request) == 0: # No request
        print("                                        <3>  Reset Password Request" + Fore.RESET)
    else: # Request received
        print(Fore.RED + "                                        <3>  Reset Password Request *"+ Fore.RESET)
    print()
    print(Fore.CYAN + "                                        <4>  Specific Period Arrangement")
    print()
    print("                                        <5>  Reset Assessments Log")
    print()
    print("                                        <6>  Reset Specific Period")
    print()
    print("                                       <ESC> Sign Out" + Fore.RESET)
    print()
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != "4" and k != "5" and k != "6" and k != key.ESC():
        k = readkey()
    if k == "1": # When "1" is pressed
        os.system("cls")
        print()
        return teachers_info()
    elif k == "2": # When "2" is pressed
        return admin_setting()
    elif k == "3": # When "3" is pressed
        return reset_request()
    elif k == "4": # When "4" is pressed
        return specific_period()
    elif k == "5": # When "5" is pressed
        return reset_assm_log()
    elif k == "6": # When "6" is pressed
        return reset_specific_period()
    elif k == key.ESC(): # When ESC is pressed
        return
#---------------------------------------------------------------------------------
def teachers_info(): # Change teachers' class information
    get.date()
    print_date()
    for x in range(9):
        print()
    print("                              Which Teachers' account information you want to change?")
    print()
    inp_username = input("                                    <Empty input> Exit : ")
    if inp_username == "": # When empty input detected, return to admin system
        return admin_system()
    else:
        found, teachers_acc_index = linear_search(login_name, inp_username)
        if found and teachers_acc_index != 0: # teacher username exists and username not equal to admin
            return show_assigned_class(teachers_acc_index)
        else: # No username found
            os.system("cls")
            print(Fore.RED + "                                          User Not Found / Wrong Input." + Fore.RESET)
            return teachers_info()
#---------------------------------------------------------------------------------
def show_assigned_class(index):
    get.classlist()
    os.system("cls")
    print_date()
    for i in range(10):
        print()
    if class_list[index][0] != "Not yet Assigned": # If the element(s) is equal to class
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
        while k != "1" and k != "2" and k != key.ESC():
            k = readkey()
    else: # If the first element is "Not yet Assigned"
        print("                                              There is no Class Assigned.")
        print()
        print("                                             <1> Add Class       <ESC> Back")
        k = readkey()
        while k != "1" and k != key.ESC():
            k = readkey()
    os.system("cls")
    if k == "1": # When "1" key is pressed
        return add_class(index)
    elif k == "2": # When "2" key is pressed
        return del_class(index)
    elif k == key.ESC(): # When ESC key is pressed
        return teachers_info()
#---------------------------------------------------------------------------------
def add_class(index): # Assign Class to teachers
    selected = [] # stack
    while len(selected) <= 2:
        if len(selected) == 0:
            selected_form = choose_form(index)
            if selected_form == None: # When ESC key is pressed, it returns
                return show_assigned_class(index)
            else:
                selected.append(selected_form)
        if len(selected) == 1:
            selected_form_char = choose_form_char(index)
            if selected_form_char == None: # When ESC key is pressed, it returns to previous page
                selected.pop()
            else:
                selected.append(selected_form_char)
        if len(selected) == 2:
            selected_class = str(selected[0]) + selected[1]
            check, temp = linear_search(class_list[index], selected_class)
            if not check: # If the target does not exist
                if class_list[index][0] == "Not yet Assigned": # If the first element is equal to "Not yet Assigned"
                        class_list[index][0] = selected_class
                else: # Elements equal to classes
                    class_list[index] = class_list[index] + [selected_class]
                update.classlist()
                print_date()
                for i in range(10):
                    print()
                print("                                        "+ selected_class +" Assigned. Do you want to Assign More? ")
                print()
                print("                                         <ENTER> Continue       <ESC> Back")
                k = readkey()
                while k != key.ENTER() and k != key.ESC():
                    k = readkey()
                os.system("cls")
                if k == key.ENTER(): # When ENTER key is pressed
                    selected.pop()
                elif k == key.ESC(): # When ESC key is pressed
                    return show_assigned_class(index)
            else:
                print_date()
                for i in range(10):
                    print()
                print(Fore.RED + "                                        This Class Has Already Been Assigned." + Fore.RESET)
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
        print_date()
        print("                                          Select and Confirm Which Form")
        print()
        print("%35s" % "", end = "")
        for x in range(len(form_list)):
            if x+1 != form_num:
                print(form_list[x], end = "      ")
            else:
                print(Fore.GREEN + form_list[x] + Fore.RESET, end = "      ") # Show the selecting item using green colour text
        print()
        for i in range(22):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave")
        k = readkey()
        while k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.LEFT(): # When LEFT arrow key is pressed
            if form_num-1 < 1:
                form_num = len(form_list)
            else:
                form_num -= 1
        elif k == key.RIGHT(): # When RIGHT arrow key is pressed
            if form_num+1 > len(form_list):
                form_num = 1
            else:
                form_num += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            return form_num
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
#---------------------------------------------------------------------------------
def choose_form_char(index):
    leave = False
    form_char_list = ["A", "B", "C", "D"]
    form_char_num = 1
    while not leave:
        print_date()
        print("                                          Select and Confirm Which Form")
        print()
        print("%45s" % "", end = "")
        for x in range(len(form_char_list)):
            if x+1 != form_char_num:
                print(form_char_list[x], end = "      ")
            else:
                print(Fore.GREEN + form_char_list[x] + Fore.RESET, end = "      ") # Show the selecting item using green colour text
        print()
        for i in range(22):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave") 
        k = readkey()
        while k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.LEFT(): # When LEFT arrow key is pressed
            if form_char_num-1 < 1:
                form_char_num = len(form_char_list)
            else:
                form_char_num -= 1
        elif k == key.RIGHT(): # When RIGHT arrow key is pressed
            if form_char_num+1 > len(form_char_list):
                form_char_num = 1
            else:
                form_char_num += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            return form_char_list[form_char_num-1]
        elif k == key.ESC(): # When ESC key is pressed
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
        print_date()
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
                    print(Fore.GREEN + class_list[index][i] + Fore.RESET, end = "      ") # Show the selecting item using green colour text
            else:
                if i+1 != class_num:
                    print(class_list[index][i], end = "\n")
                else:
                    print(Fore.GREEN + class_list[index][i] + Fore.RESET, end = "\n") # Show the selecting item using green colour text
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
        while k != key.ESC() and k != key.ENTER() and k != key.LEFT() and k != key.RIGHT() and k != key.UP() and k != key.DOWN():
            k = readkey()
        if k == key.LEFT() and col > 1: # When LEFT arrow key is pressed
            col -= 1
            class_num -= 1
        elif k == key.RIGHT() and col < 4 and class_num < len(class_list[index]): # When RIGHT arrow key is pressed
            col += 1
            class_num += 1
        elif k == key.UP() and row > 1: # When UP arrow key is pressed
            row -= 1
            class_num -= 4
        elif k == key.DOWN() and class_num+4 <= len(class_list[index]): # When DOWN arrown key is pressed
            row += 1
            class_num += 4
        elif k == key.ENTER(): # When ENTER key is pressed
            os.system("cls")
            print_date()
            for z in range(10):
                print()
            print("                                                You Want To Delete " + class_list[index][class_num-1] + "?")
            print()
            print("                                             <ENTER> Confirm      <ESC> Back")
            k = readkey()
            while k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.ENTER(): # When ENTER key is pressed (Confirm)
                leave = True
            elif k == key.ESC(): # When ESC key is pressed (Return)
                return del_class(index)
            if leave:
                if len(class_list[index]) == 1: # If the list has only one element left, change the first element to "Not yet Assigned"
                    class_list[index][0] = "Not yet Assigned"
                else: # the list has more than one element
                    del class_list[index][class_num-1]
                update.classlist()
                if class_list[index][0] == "Not yet Assigned": # Check the first element if it is "Not yet Assigned"
                    return show_assigned_class(index)
                else:
                    return del_class(index)
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
            return show_assigned_class(index)
#---------------------------------------------------------------------------------
def admin_setting(): # Admin Setting
    os.system("cls")
    print_date()
    print("\t\t\t\t\t\t   Administrator Setting")
    for x in range(7):
        print()
    print(Fore.CYAN)
    print("\t\t\t\t         <1>  Reset Password")
    print()
    print("\t\t\t\t         <2>  Create Account")
    print()
    print("\t\t\t\t         <3>  Delete Account")
    print()
    print("\t\t\t\t        <ESC> Back" + Fore.RESET)
    print()
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != key.ESC():
        k = readkey()
    os.system("cls")
    if k == "1": # When "1" is pressed
        print()
        return resetpw()
    elif k == "2": # When "2" is pressed
        print()
        return create_acc()
    elif k == "3": # When "3" is pressed
        print()
        return delete_acc()
    elif k == key.ESC(): # When ESC key is pressed
        return admin_system()
#---------------------------------------------------------------------------------
def create_acc(): # To create a new teacher account
    global login_name, password, default_pw, class_list
    print_date()
    admin_pw = get.adminpw_data()
    for line in range(10):
        print()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(64))
    print()
    if input_admin_pw == "": # Return to previous page when empty input detected
        return admin_setting()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]: # Check if the admin password is correct
            os.system("cls")
            print(Fore.RED + "Administrator Password Incorrect.".rjust(75) + Fore.RESET)
            return create_acc()
        else:
            os.system("cls")
            print()
            while True:
                print_date()
                for y in range(10):
                    print()
                print("<Empty input> Exit".rjust(65))
                print()
                add_username = input("\t\t\t         Enter New Teacher Account Username: ")
                check, temp = linear_search(login_name, add_username)
                if add_username == "": # Return to previous page when empty input detected
                    return admin_setting()
                elif check: # Same username found
                    os.system("cls")
                    print(Fore.RED + "Username Has Been Used. Please Try Again".rjust(77) + Fore.RESET) 
                else:
                    display_password = add_password = add_username + "12345"
                    add_password = encrypted_pw(add_password)
                    login_name = login_name + [add_username]
                    password = password + [add_password]
                    default_pw = default_pw + [add_password]
                    class_list = class_list + [["Not yet Assigned"]]
                    append_item(add_username, add_password, "Not yet Assigned")
                    os.system("cls")
                    for x in range(9):
                        print()
                    print(Fore.GREEN + "                                    Username: " + add_username + "     Default Password: " + display_password)
                    print()
                    print("                                                   SIGN UP SUCCESSFUL")
                    print()
                    print("                                                       Continue ?" + Fore.RESET)
                    print()
                    print("                                         <ENTER> Continue        <ESC> Return")
                    k = readkey()
                    while k != key.ENTER() and k != key.ESC():
                        k = readkey()
                    if k == key.ENTER():
                        os.system("cls")
                        print()
                    elif k == key.ESC():
                        return admin_setting()
#---------------------------------------------------------------------------------
def delete_acc(): # To delete teachers' account
    print_date()
    if len(login_name) == 1:
        for line in range(10):
            print()
        print(Fore.RED + "                                            There are no Teacher(s) Account")
        print()
        print("                                                Press <ANY KEY> To Return" + Fore.RESET)
        readkey()
        os.system("cls")
        return admin_setting()
    else:
        temp = 0
        admin_pw = get.adminpw_data()
        for line in range(10):
            print()
        print("<Empty input> Exit".rjust(65))
        print()
        input_admin_pw = input("Enter the Administrator Password: ".rjust(61))
        print()
        if input_admin_pw == "": # Return to previous page when empty input detected
            return admin_setting()
        else:
            input_admin_pw = encrypted_pw(input_admin_pw)
            if input_admin_pw != admin_pw[0]: # Check if the admin password is correct
                os.system("cls")
                print(Fore.RED + "Administrator Password Incorrect.".rjust(75) + Fore.RESET)
                return delete_acc()
            else:
                while True:
                    os.system("cls")
                    index_user = choose_teachers_acc()
                    if index_user == None:
                        break
                    else:
                        for i in range(12):
                            print()
                        print(Fore.GREEN + "                                       User's ["+ login_name[index_user] +"] Account Will Be Deleted")
                        print()
                        print("                                                         Confirm?" + Fore.RESET)
                        print()
                        print("                                       <ENTER> Confirm               <ESC> Back")
                        k = readkey()
                        while k != key.ENTER() and k != key.ESC():
                            k = readkey()
                        if k == key.ENTER(): # When ENTER key is pressed
                            os.system("cls")
                            del login_name[index_user]
                            del password[index_user]
                            del default_pw[index_user]
                            del class_list[index_user]
                            update.username()
                            update.password()
                            update.defaultpw()
                            update.classlist()
                            os.system("cls")
                            for i in range(12):
                                print()
                            print(Fore.GREEN + "                                                 ACCOUNT DELETE SUCCESSFUL")
                            print()
                            print("                                                          Continue?" + Fore.RESET)
                            print()
                            print("                                       <ENTER> Continue               <ESC> Return")
                            k = readkey()
                            while k != key.ESC() and k != key.ENTER():
                                k = readkey()
                            if k == key.ENTER(): # When ENTER key is pressed
                                pass
                            elif k == key.ESC(): # When ESC key is pressed
                                return admin_setting()
                        elif k == key.ESC(): # When ESC key is pressed
                            pass
#---------------------------------------------------------------------------------
def choose_teachers_acc(): # Select the assessment you want to remove
    teachers_acc_num = len(login_name) - 1 # Exclude admin account
    total_page_num = -(-teachers_acc_num//10)
    start_num = 1
    page_num = 1
    select_index = 1
    while True:
        if teachers_acc_num == 0:
            print()
            print_date()
            for line in range(10):
                print()
            print(Fore.RED + "                                            There are no Teacher(s) Account")
            print()
            print("                                                Press <ANY KEY> To Return" + Fore.RESET)
            readkey()
            os.system("cls")
            return admin_setting()
        else:
            print_date()
            print("        Page "+ str(page_num) +"                   Select And Confirm the Teachers Account You want to Delete: ")
            print()
            if total_page_num < 2: # Case for only one page in total
                blank_line = 0
                for i in range(1, len(login_name)):
                    if i != select_index:
                        print("\t\t\t\t\t\t\t"+ login_name[i])
                    else:
                        print("\t\t\t\t\t\t\t"+ Fore.GREEN + login_name[i] + Fore.RESET) # Show the selecting item using green colour text
                    print()
                    blank_line += 2
                for j in range(21-blank_line):
                    print()
                print("                                                  <UP>     <DOWN>")
                print()
                print("                                        <ENTER> Confirm     <ESC> Leave")
                k = readkey()
                while k != key.ESC() and k != key.ENTER() and k != key.UP() and k != key.DOWN():
                    k = readkey()
                os.system("cls")
                if k == key.ESC(): # When ESC key is pressed
                    return admin_setting()
                elif k == key.ENTER(): # When ENTER key is pressed
                    return select_index
                elif k == key.UP() and select_index > 1: # When UP arrow key is pressed
                    select_index -= 1
                elif k == key.DOWN() and select_index < teachers_acc_num: # When DOWN arrow key is pressed
                    select_index += 1
            elif page_num > 1 and page_num < total_page_num: # Case for more than one pages but not in the last page
                for x in range(start_num, page_num*10+1):
                    if x != select_index:
                        print("\t\t\t\t\t\t\t"+ login_name[x])
                    else:
                        print("\t\t\t\t\t\t\t"+ Fore.GREEN + login_name[x] + Fore.RESET) # Show the selecting item using green colour text
                    print()
                print()
                print("                              <UP>     <DOWN>     <LEFT> Previous Page     <RIGHT> Next Page")
                print()
                print("                                        <ENTER> Confirm     <ESC> Leave")
                k = readkey()
                while k != key.LEFT() and k != key.RIGHT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                    k = readkey()
                os.system("cls")
                if k == key.LEFT(): # When LEFT arrow key is pressed
                    page_num -= 1
                    start_num -= 10
                    select_index = start_num
                elif k == key.RIGHT(): # When RIGHT arrow key is pressed
                    page_num += 1
                    start_num += 10
                    select_index = start_num
                elif k == key.UP() and select_index > start_num: # When UP arrow key is pressed
                    select_index -= 1
                elif k == key.DOWN() and select_index < page_num*10: # When DOWN arrow key is pressed
                    select_index += 1
                elif k == key.ESC(): # When ESC key is pressed
                    return admin_setting()
                elif k == key.ENTER(): # When ENTER key is pressed
                    return select_index
            elif page_num == total_page_num: # Case for the last page
                blank_line = 0
                for y in range(start_num, len(login_name)):
                    if y != select_index:
                        print("\t\t\t\t\t\t\t"+ login_name[y])
                    else:
                        print("\t\t\t\t\t\t\t"+ Fore.GREEN + login_name[y] + Fore.RESET) # Show the selecting item using green colour text
                    print()
                    blank_line += 2
                for j in range(21-blank_line):
                    print()
                print("                                       <UP>     <DOWN>     <LEFT> Previous Page")
                print()
                print("                                        <ENTER> Confirm     <ESC> Leave")
                k = readkey()
                while k != key.LEFT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                    k = readkey()
                os.system("cls")
                if k == key.LEFT(): # When LEFT arrow key is pressed
                    page_num -= 1
                    start_num -= 10
                    select_index = start_num
                elif k == key.UP() and select_index > start_num: # When UP arrow key is pressed
                    select_index -= 1
                elif k == key.DOWN() and select_index < teachers_acc_num: # When DOWN arrow key is pressed
                    select_index += 1
                elif k == key.ESC(): # When ESC key is pressed
                    leave = True
                    return schedule()
                elif k == key.ENTER(): # When ENTER key is pressed
                    return select_index
            else: # Case for the first page
                for z in range(start_num, page_num*10+1):
                    if z != select_index:
                        print("\t\t\t\t\t\t\t"+ login_name[z])
                    else:
                        print("\t\t\t\t\t\t\t"+ Fore.GREEN + login_name[z] + Fore.RESET) # Show the selecting item using green colour text
                    print()
                print()
                print("                                       <UP>     <DOWN>     <RIGHT> Next Page")
                print()
                print("                                        <ENTER> Confirm     <ESC> Leave")
                k = readkey()
                while k != key.RIGHT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                    k = readkey()
                os.system("cls")
                if k == key.RIGHT(): # When RIGHT arrow key is pressed
                    page_num += 1
                    start_num += 10
                    select_index = start_num
                elif k == key.UP() and select_index > 1: # When UP arrow key is pressed
                    select_index -= 1
                elif k == key.DOWN() and select_index < page_num*10: # When DOWN arrow key is pressed
                    select_index += 1
                elif k == key.ESC(): # When ESC key is pressed 
                    return admin_setting()
                elif k == key.ENTER(): # When ENTER key is pressed
                    return select_index
#---------------------------------------------------------------------------------
def reset_request(): # To approve the request from the teachers
    leave = False
    select_index = 1
    while not leave:
        os.system("cls")
        print_date()
        if len(request) == 0: # No request
            leave = True
            for i in range(11):
                print()
            print(Fore.RED + "                                     There is no reset password request from teachers")
            print()
            print("                                               Press <ANY KEY> To Return" + Fore.RESET)
            readkey()
            return admin_system()
        else: # Request exists
            row_num = 0
            if len(request) < 5: # When the number of request less than 5
                current_req = [''] * len(request)
                for i in range(len(request)):
                    current_req[i] = request[i]
            else: # When the number of request more than or equal to 5
                current_req = [''] * 5 # Limit the number of element be five
                for i in range(5):
                    current_req[i] = request[i]
            print("                                                  Reset Request From:")
            for x in range(6):
                print()
            for i in range(len(current_req)):
                if i+1 != select_index:
                    print("                                                       "+ login_name[int(current_req[i])])
                else:
                    print("                                                       "+ Fore.GREEN + login_name[int(current_req[i])] + Fore.RESET) # Show the selecting item using green colour text
                print()
                row_num += 2
            for j in range(18-row_num):
                print()
            print("                                   <UP>      <DOWN>      <ENTER> Confirm      <ESC> Back")
            k = readkey()
            while k != key.UP() and k != key.DOWN() and k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.UP() and select_index >= 1: # When UP arrow key is pressed
                select_index -= 1
                if select_index == 0:
                    select_index = len(current_req)
            elif k == key.DOWN() and select_index <= len(current_req): # When DOWN arrow key is pressed
                select_index += 1
                if select_index > len(current_req):
                    select_index = 1
            elif k == key.ENTER(): # When ENTER key is pressed
                os.system("cls")
                print_date()
                for i in range(12):
                    print()
                print(Fore.GREEN + "                                        Reset User's [" + login_name[int(current_req[select_index-1])] + "] Password to Default?" + Fore.RESET)
                print()
                print("                                 <ENTER> Accept      <BACKSPACE> Decline      <ESC> Back")
                k = readkey()
                while k != key.ENTER() and k != key.BACKSPACE() and k != key.ESC():
                    k = readkey()
                if k == key.ENTER(): # When ENTER key is pressed
                    os.system("cls")
                    get.defaultpw()
                    password[int(current_req[select_index-1])] = default_pw[int(current_req[select_index-1])]
                    del request[select_index-1]
                    update.password()
                    update.forgetpw_request()
                    print_date()
                    for i in range(10):
                        print()
                    print(Fore.GREEN + "                                               Password Reset Successful.")
                    print()
                    print("                                               Press <ANY KEY> To Return" + Fore.RESET)
                    readkey()
                    select_index = 1
                elif k == key.BACKSPACE(): # When BACKSPACE key is pressed
                    os.system("cls")
                    del request[select_index-1]
                    update.forgetpw_request()
                    print_date()
                    print(Fore.RED + "                                                   Request Declined")
                    print()
                    print("                                               Press <ANY KEY> To Return" + Fore.RESET)
                elif k == key.ESC(): # When ESC key is pressed
                    None
            elif k == key.ESC(): # When ESC key is pressed, return to admin system
                return admin_system()
#---------------------------------------------------------------------------------
def specific_period(): # Updating the specific period by admin
    os.system("cls")
    temp = [] # stack
    while len(temp) < 2:
        if len(temp) == 0:
            item = choose_month()
            if item == None:
                return admin_system()
            else:
                temp.append(item)
        if len(temp) == 1:
            item = choose_specific_period(temp[0])
            if item == None:
                temp.pop()
            else:
                print_date()
                for i in range(10):
                    print()
                print(Fore.GREEN + "                                            Specific Period Update SUCCESSFUL")
                print()
                print("                                                         Continue ?" + Fore.RESET)
                print()
                print("                                       <ENTER> Continue               <ESC> Return")
                k = readkey()
                while k != key.ENTER() and k != key.ESC():
                    k = readkey()
                if k == key.ENTER(): # When ENTER key is pressed
                    return specific_period()
                elif k == key.ESC(): # When ESC key is pressed
                    return admin_system()
#---------------------------------------------------------------------------------
def reset_assm_log(): # Clear All Assessment Logs data
    os.system("cls")
    admin_pw = get.adminpw_data()
    print_date()
    for temp in range(10):
        print()
    print("<Empty input> Exit".rjust(65))
    print()
    input_admin_pw = input("Enter the Administrator Password: ".rjust(64))
    print()
    if input_admin_pw == "": # Return to previous page when empty input detected
        return admin_system()
    else:
        input_admin_pw = encrypted_pw(input_admin_pw)
        if input_admin_pw != admin_pw[0]: # Check if the admin password is correct
            os.system("cls")
            print(Fore.RED + "Administrator Password Incorrect.".rjust(75) + Fore.RESET)
            return reset_assm_log()
        else:
            os.system("cls")
            print_date()
            for temp in range(11):
                print()
            print(Fore.RED + "                                             Clear All Assessment Logs Data ?" + Fore.RESET)
            print()
            print("                                       <ENTER> Confirm               <ESC> Back")
            k = readkey()
            while k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.ENTER(): # When ENTER key is pressed
                clear_log()
                os.system("cls")
                print_date()
                for i in range(11):
                    print()
                print(Fore.GREEN + "                                          Assessment Log Clear Successful.")
                print()
                print("                                             Press <ANY KEY> To Return" + Fore.RESET)
                readkey()
            elif k == key.ESC(): # When ESC key is pressed
                None
            return admin_system()
#---------------------------------------------------------------------------------
def reset_specific_period():
    month_list = ["[January]","[February]","[March]","[April]","[May]","[June]","[July]","[August]","[September]","[October]","[November]","[December]"]
    while True:
        os.system("cls")
        item = choose_month()
        if item != None:
            temp = []
            s = get.exist_date(item, temp, 0)
            print_date()
            for temp in range(11):
                print()
            print(Fore.RED + "                                         Clear "+ month_list[item-1] +" Specific Period Data ?" + Fore.RESET)
            print()
            print("                                       <ENTER> Confirm               <ESC> Back")
            k = readkey()
            while k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.ENTER():
                s[item-1] = "0"
                update.exist_date(s)
                os.system("cls")
                for temp in range(11):
                    print()
                print(Fore.RED + "                                                       Reset Others ?" + Fore.RESET)
                print()
                print("                                       <ENTER> Confirm               <ESC> Back")
                k = readkey()
                while k != key.ENTER() and k != key.ESC():
                    k = readkey()
                if k == key.ENTER():
                    None
                elif k == key.ESC():
                    return admin_system()
            elif k == key.ESC():
                None
        else:
            return admin_system()
#---------------------------------------------------------------------------------
def teachers_system(): # Teachers accounts
    get.defaultpw()
    os.system("cls")
    if password[password_index] == default_pw[password_index]:
        print_date()
        for i in range(10):
            print()
        print(Fore.GREEN + "                                                  First Login Detected")
        print()
        print("                                Please Change your password. Press <ANY KEY> To Continue" + Fore.RESET)
        readkey()
        os.system("cls")
        print()
        change_pw()
    else:
        print_date()
        print("                                                    Welcome Back." , login_name[username_index])
        for x in range(7):
            print()
        print(Fore.CYAN)
        print("                                        <1>  Schedule Assessments System")
        print()
        print("                                        <2>  Settings")
        print()
        print("                                        <3>  Searching")
        print()
        print("                                       <ESC> Sign Out" + Fore.RESET)
        k = readkey()
        while k != "1" and k != "2" and k != "3" and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == "1": # When "1" is pressed
            return choose_class(k)
        elif k == "2": # When "2" is pressed
            return teacher_setting()
        elif k == "3": # When "3" is pressed
            return choose_class(k)
        elif k == key.ESC(): # When ESC key is pressed
            return
#---------------------------------------------------------------------------------
def choose_class(key_num): # Select classes adding into teachers' account
    total_page_num = -(-len(class_list[username_index])//8)
    page_num = 1
    start_num = 0
    if class_list[username_index][0] != "Not yet Assigned": # When the elements in the list are classes
        global selected_class, form
        class_group = [0] * len(class_list[username_index])
        while True:
            print_date()
            if total_page_num == 1: # Case for only one page in total
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
                    elif k != key.ESC():
                        pass
                    else:
                        break # it will break when key is ESC
                if k == key.ESC():
                    return teachers_system()
                else: # When the range of 1 - maxiumum number of class that can be selected is pressed (e.g 1 - 4)
                    selected_class = class_group[k-1]
                    if int(selected_class[:1]) <= 3: # Find the first charactor of string (selected_class) smaller than 4 (e.g 2D --> 2)
                        form = "Junior"
                    else: # The first charactor of string (selected_class) larger than or equal to 4
                        form = "Senior"
                    if key_num == "1":
                        return schedule()
                    else:
                        return searching()
            elif page_num > 1 and page_num < total_page_num: # Case for more than one pages but not in the last page
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
                    elif k == key.ESC(): # When ESC key is detected
                        break
                    elif k == key.LEFT(): # When LEFT arrow key is detected
                        break
                    elif k == key.RIGHT(): # When RIGHT arrow key is detected
                        break
                    else: # When other key is detected (e.g charactors)
                        pass
                if k == key.LEFT(): # When LEFT key is pressed
                    page_num -= 1
                    start_num -= 8
                    os.system("cls")
                elif k == key.RIGHT(): # When RIGHT key is pressed
                    page_num += 1
                    start_num += 8
                    os.system("cls")
                elif k == key.ESC(): # When ESC key is pressed
                    return teachers_system()
                else:  # When the range of 1 - maxiumum number of class that can be selected is pressed (e.g 1 - 4)
                    selected_class = class_group[(page_num-1)*8+k-1]
                    if int(selected_class[:1]) <= 3: # Find the first charactor of string (selected_class) smaller than 4 (e.g 2D --> 2)
                        form = "Junior"
                    else: # The first charactor of string (selected_class) larger than or equal to 4
                        form = "Senior"
                    if key_num == "1":
                        return schedule()
                    else:
                        return searching()
            elif page_num == total_page_num: # Case for the first page
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
                    elif k == key.ESC(): # When ESC key is detected
                        break
                    elif k == key.LEFT(): # When LEFT key is detected
                        break
                    else:
                        pass
                if k == key.LEFT(): # When LEFT arrow key is pressed
                    page_num -= 1
                    start_num -= 8
                    os.system("cls")
                elif k == key.ESC(): # When ESC key is pressed
                    return teachers_system()
                else: # When the range of 1 - maxiumum number of class that can be selected is pressed (e.g 1 - 4)
                    selected_class = class_group[(page_num-1)*8+k-1]
                    if int(selected_class[:1]) <= 3: # Find the first charactor of string (selected_class) smaller than 4 (e.g 2D --> 2)
                        form = "Junior"
                    else: # The first charactor of string (selected_class) larger than or equal to 4
                        form = "Senior"
                    if key_num == "1":
                        return schedule()
                    else:
                        return searching()
            else: # Case for the last page
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
                            break # it will break when k is between a range (e.g. 1-3)
                    elif k == key.ESC(): # When ESC key is pressed
                        break
                    elif k == key.RIGHT(): # When RIGHT arrow key is pressed
                        break
                    else:
                        pass
                if k == key.RIGHT(): # When RIGHT arrow key is pressed
                    page_num += 1
                    start_num += 8
                    os.system("cls")
                elif k == key.ESC(): # When ESC key is pressed
                    return teachers_system()
                else: # When the range of 1 - 8 is pressed
                    selected_class = class_group[k-1]
                    if int(selected_class[:1]) <= 3: # Find the first charactor of string (selected_class) smaller than 4 (e.g 2D --> 2)
                        form = "Junior"
                    else: # The first charactor of string (selected_class) larger than or equal to 4
                        form = "Senior"
                    if key_num == "1":
                        return schedule()
                    else:
                        return searching()
    else: # When the first element of the list is "Not yet Assigned"
        print_date()
        for i in range(10):
            print()
        print(Fore.RED + "                                               Class Not yet Assigned.")
        print()
        print("                                              Press <ANY KEY> To Return" + Fore.RESET)
        readkey()
        return teachers_system()
#---------------------------------------------------------------------------------
def schedule(): # To open schedule system function
    os.system("cls")
    print_date()
    print("       Class: " + selected_class)
    get.assm()
    display_assm()
    if len(assm) == 0:
        print("                                                  <1>  Schedule Assessments")
        print()
        print("                                                 <ESC> Back")
        k = readkey()
        while k != "1" and k != key.ESC():
            k = readkey()
    else:
        print("                             <1> Schedule Assessments                 <2>  Delete Assessments")
        print()
        print("                             <3> Show All Assessments                <ESC> Back")
        k = readkey()
        while k != "1" and k != "2" and k != "3" and k != key.ESC():
            k = readkey()
    os.system("cls")
    if k == "1": # When "1" is pressed
        return add_assms()
    elif k == "2": # When "2" is pressed
        return del_assms()
    elif k == "3": # When "3" is pressed
        return show_all_assms()
    elif k == key.ESC(): # When ESC key is pressed
        return choose_class("1")
#---------------------------------------------------------------------------------
def display_assm(): # Display Assessments
    if len(assm) == 0:
        print(Fore.RED + "                                          There is no asseessment assigned." + Fore.RESET)
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
                print("                         ", display[i], end = "\t")
            else:
                print("                         ", display[i], end = "\n\n")
                row_num += 1
            num += 1
        if k == len(display) and len(assm) > len(display):
            row_num += 1
            print("                      And More.....")
        for j in range(17-row_num):
            print()
#---------------------------------------------------------------------------------
def add_assms(): # Adding assessment
    selected = [] #stack
    while len(selected) <= 5:
        if len(selected) == 0:
            item = choose_subject()
            if item == None:
                return schedule()
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
                for i in range(8):
                    print()
                print(Fore.RED)
                print("                            WARNING!! There are too many Assessments on a particular day !!!")
                print()
                print("                              The Assessment will schedule on ["+ assm_deadline + "]")
                print()
                print("                                                        Confirm ?" + Fore.RESET)
                print()
                print("                                        <ENTER> Confirm               <ESC> Back")
            else:
                for i in range(10):
                    print()
                print(Fore.GREEN)
                print("                              The Assessment will schedule on ["+ assm_deadline + "]")
                print()
                print("                                                        Confirm ?" + Fore.RESET)
                print()
                print("                                        <ENTER> Confirm               <ESC> Back")
            k = readkey()
            while k != key.ENTER() and k != key.ESC():
                k = readkey()
            os.system("cls")
            if k == key.ENTER(): # When ENTER key is pressed
                global assm
                assm = assm + [[assm_deadline, selected[4]]]
                update.assm()
                return schedule()
            elif k == key.ESC(): # When ESC key is pressed
                selected.pop()
#---------------------------------------------------------------------------------
def count_time(d):
    total_time = 0
    for i in range(len(assm)):
        find = assm[i][0].find(d)
        if find == -1: # When 
            pass
        else:
            total_time += float(assm[i][1]) # Find the total amount of time of assessments spending on a day
    return total_time
#---------------------------------------------------------------------------------
def del_assms(): # Remove assessment and confirm / not
    if len(assm) != 0:
        selected_del_assm = choose_del_assm()
        if selected_del_assm != None:
            for i in range(11):
                print()
            print(Fore.GREEN + "\t\t\t\t   You want to Remove The Assessment ["+ assm[selected_del_assm-1][0] + "]")
            print()
            print("\t\t\t\t\t\t\tConfirm ?" + Fore.RESET)
            print()
            print("\t\t\t\t\t<ENTER> Confirm\t\t\t<ESC> Back")
            k = readkey()
            while k != key.ENTER() and k != key.ESC():
                 k = readkey()
            os.system("cls")
            if k == key.ENTER(): # When ENTER key is pressed
                del assm[selected_del_assm-1]
                update.assm()
                return del_assms()
            elif k == key.ESC(): # When ESC key is pressed
                return del_assms()
    else: # No assessment detected
        return schedule()
#---------------------------------------------------------------------------------
def choose_del_assm(): # Select the assessment you want to remove
    total_page_num = -(-len(assm)//10)
    leave = False
    start_num = 0
    page_num = 1
    select_index = 1
    while not leave:
        print_date()
        print("\tPage "+ str(page_num) +"\t\t\t    Select And Confirm the Assessment You want to Delete: ")
        print()
        if total_page_num < 2: # Case for only one page in total
            blank_line = 0
            for i in range(len(assm)):
                if i+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[i][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.GREEN + assm[i][0] + Fore.RESET) # Show the selecting item using green colour text
                print()
                blank_line += 2
            for j in range(21-blank_line):
                print()
            print("                                                  <UP>     <DOWN>")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.ESC() and k != key.ENTER() and k != key.UP() and k != key.DOWN():
                k = readkey()
            os.system("cls")
            if k == key.ESC(): # When ESC key is pressed
                leave = True
                return schedule()
            elif k == key.ENTER(): # When ENTER key is pressed
                return select_index
            elif k == key.UP() and select_index > 1: # When UP arrow key is pressed
                select_index -= 1
            elif k == key.DOWN() and select_index < len(assm): # When DOWN arrow key is pressed
                select_index += 1
        elif page_num > 1 and page_num < total_page_num: # Case for more than one pages but not in the last page
            for x in range(start_num, page_num*10):
                if x+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[x][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.GREEN + assm[x][0] + Fore.RESET) # Show the selecting item using green colour text
                print()
            print()
            print("                              <UP>     <DOWN>     <LEFT> Previous Page     <RIGHT> Next Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.LEFT() and k != key.RIGHT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                k = readkey()
            os.system("cls")
            if k == key.LEFT(): # When LEFT arrow key is pressed
                page_num -= 1
                start_num -= 10
                select_index = start_num + 1
            elif k == key.RIGHT(): # When RIGHT arrow key is pressed
                page_num += 1
                start_num += 10
                select_index = start_num + 1
            elif k == key.UP() and select_index > start_num + 1: # When UP arrow key is pressed
                select_index -= 1
            elif k == key.DOWN() and select_index < page_num*10: # When DOWN arrow key is pressed
                select_index += 1
            elif k == key.ESC(): # When ESC key is pressed
                leave = True
                return schedule()
            elif k == key.ENTER(): # When ENTER key is pressed
                return select_index
        elif page_num == total_page_num: # Case for the last page
            blank_line = 0
            for y in range(start_num, len(assm)):
                if y+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[y][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.GREEN + assm[y][0] + Fore.RESET) # Show the selecting item using green colour text
                print()
                blank_line += 2
            for j in range(21-blank_line):
                print()
            print("                                       <UP>     <DOWN>     <LEFT> Previous Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.LEFT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                k = readkey()
            os.system("cls")
            if k == key.LEFT(): # When LEFT arrow key is pressed
                page_num -= 1
                start_num -= 10
                select_index = start_num + 1
            elif k == key.UP() and select_index > start_num + 1: # When UP arrow key is pressed
                select_index -= 1
            elif k == key.DOWN() and select_index < len(assm): # When DOWN arrow key is pressed
                select_index += 1
            elif k == key.ESC(): # When ESC key is pressed
                leave = True
                return schedule()
            elif k == key.ENTER(): # When ENTER key is pressed
                return select_index
        else: # Case for the first page
            for z in range(start_num, page_num*10):
                if z+1 != select_index:
                    print("\t\t\t\t\t\t"+ assm[z][0])
                else:
                    print("\t\t\t\t\t\t"+ Fore.GREEN + assm[z][0] + Fore.RESET) # Show the selecting item using green colour text
                print()
            print()
            print("                                       <UP>     <DOWN>     <RIGHT> Next Page")
            print()
            print("                                        <ENTER> Confirm     <ESC> Leave")
            k = readkey()
            while k != key.RIGHT() and k != key.UP() and k != key.DOWN() and k != key.ESC() and k != key.ENTER():
                k = readkey()
            os.system("cls")
            if k == key.RIGHT(): # When RIGHT arrow key is pressed
                page_num += 1
                start_num += 10
                select_index = start_num + 1
            elif k == key.UP() and select_index > 1: # When UP arrow key is pressed
                select_index -= 1
            elif k == key.DOWN() and select_index < page_num*10: # When DOWN arrow key is pressed
                select_index += 1
            elif k == key.ESC(): # When ESC key is pressed 
                leave = True
                return schedule()
            elif k == key.ENTER(): # When ENTER key is pressed
                return select_index
#---------------------------------------------------------------------------------
def show_all_assms(): # Show all the assessments scheduled
    blank_line = 0
    total_page_num = -(-len(assm)//11)
    leave = False
    start_num = 0
    page_num = 1
    while not leave:
        print_date()
        print("\tPage "+ str(page_num) +"\t\t\t\t       Assessments Shown Below: ")
        print()
        if total_page_num < 2: # Case for only have one page in total
            for i in range(len(assm)):
                print("\t\t\t\t\t"+ assm[i][0] + "\t" + assm[i][1] + " hour(s)")
                print()
                blank_line += 2
            for j in range(23-blank_line):
                print()
            print("\t\t\t\t\t\t  <ESC> Leave")
            k = readkey()
            while k != key.ESC():
                k = readkey()
            leave = True
        elif page_num > 1 and page_num < total_page_num: # Case for more than one pages but not in the last page
            for x in range(start_num, page_num*10):
                print("\t\t\t\t\t"+ assm[x][0] + "\t" + assm[x][1] + " hour(s)")
                print()
            print()
            print()
            print()
            print("\t\t\t      <LEFT> Previous Page\t<RIGHT> Next Page\t<ESC> Leave")
            k = readkey()
            while k != key.LEFT() and k != key.RIGHT() and k != key.ESC():
                k = readkey()
            os.system("cls")
            if k == key.LEFT():
                page_num -= 1
                start_num -= 10
            elif k == key.RIGHT():
                page_num += 1
                start_num += 10
            elif k == key.ESC():
                leave = True
        elif page_num == total_page_num: # Case for the last page
            blank_line = 0
            for y in range(start_num, len(assm)):
                print("\t\t\t\t\t"+ assm[y][0] + "\t" + assm[y][1] + " hour(s)")
                print()
                blank_line += 2
            for j in range(23-blank_line):
                print()
            print("\t\t\t\t     <LEFT> Previous Page\t<ESC> Leave")
            k = readkey()
            while k != key.LEFT() and k != key.ESC():
                k = readkey()
            os.system("cls")
            if k == key.LEFT():
                page_num -= 1
                start_num -= 10
            elif k == key.ESC():
                leave = True
        else: # Case for the first page
            for z in range(start_num, page_num*10):
                print("\t\t\t\t\t"+ assm[z][0] + "\t" + assm[z][1] + " hour(s)")
                print()
            print()
            print()
            print()
            print("\t\t\t\t\t<RIGHT> Next Page\t<ESC> Leave")
            k = readkey()
            while k != key.RIGHT() and k != key.ESC():
                k = readkey()
            os.system("cls")
            if k == key.RIGHT(): # When RIGHT arrow key is pressed
                page_num += 1
                start_num += 10
            elif k == key.ESC(): # When ESC key is pressed
                leave = True
    return schedule()
#---------------------------------------------------------------------------------
def choose_subject(): # Select the subject of the assessment
    leave = False
    row = 0
    col = 0
    subject_list = ["CHIN","ENG","MATH","CSD","CHIS","CLIT","HIST","PHY","M1"],["BIO","GEOG","ICT","ECON","BAFS","VA","MUSIC","CHEM","M2"]
    while not leave:
        print_date()
        print("\t\t\t\t\t  Select and Confirm the Subject")
        print()
        for i in range(len(subject_list)):
            print("\t\t     ", end = "")
            for j in range(len(subject_list[i])):
                if subject_list[row][col] != subject_list[i][j]:
                    print(subject_list[i][j], end = "      ") # print rest of the item which are not selected
                else:
                    print(Fore.GREEN + str(subject_list[i][j]) + Fore.RESET, end = "      ") # Show the selecting item using green colour text
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
        while k != key.UP() and k != key.DOWN() and k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.UP() and row <= 1: # When UP arrow key is pressed
            if row-1 < 0:
                row = 1
            else:
                row = 0
        elif k == key.DOWN() and row >= 0: # When DOWN arrow key is pressed
            if row+1 > 1:
                row = 0
            else:
                row = 1
        elif k == key.LEFT() and col >= 0: # When LEFT arrow key is pressed
            if col-1 < 0:
                col = 8
            else:
                col -= 1
        elif k == key.RIGHT() and col <= 8: # When RIGHT arrow key is pressed
            if col+1 > 8:
                col = 0
            else:
                col += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            return subject_list[row][col]
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
#---------------------------------------------------------------------------------
def choose_assm_type(): # Select the assessment type
    leave = False
    type_num = 1
    type_list = ["HW", "QUIZ", "UT", "TEST", "DICT"]
    while not leave:
        print_date()
        print("                                          Select and Confirm the Assessment Type")
        print()
        print("%40s" % "", end = "")
        for x in range(len(type_list)):
            if x+1 != type_num:
                print(type_list[x], end = "      ") # print rest of the item which are not selected
            else:
                print(Fore.GREEN + type_list[x] + Fore.RESET, end = "      ") # Show the selecting item using green colour text
        print()
        for i in range(20):
            print()
        print("\t\t\t     <LEFT>       <RIGHT>        <ENTER> Confirm        <ESC> Leave")
        k = readkey()
        while k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.LEFT() and type_num >= 1: # When LEFT arrow key is pressed
            if type_num-1 < 1:
                type_num = len(type_list)
            else:
                type_num -= 1
        elif k == key.RIGHT() and type_num <= len(type_list): # When RIGHT arrow key is pressed
            if type_num+1 > len(type_list):
                type_num = 1
            else:
                type_num += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            return type_list[type_num-1]
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
#---------------------------------------------------------------------------------
def choose_month(): # Select the month you want to add your assessment
    leave = False
    row = 1
    col = 1
    month = 1
    month_list = ["[1] January","[2] February","[3] March","[4] April","[5] May","\t[6] June\n\n","\t[7] July","[8] August","[9] September","[10] October","[11] November","[12] December"]
    while not leave:
        print_date()
        print("                                                Select And Confirm The Month")
        print()
        print("\t\t", end = "")
        for x in range(len(month_list)):
            if x+1 != month:
                print(month_list[x], end = "\t") # print rest of the month which are not selected
            else:
                print(Fore.GREEN + month_list[x] + Fore.RESET, end = "\t") # Show the selecting item using green colour text
        for x in range(17):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.UP() and k != key.DOWN() and k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.UP() and row >= 1: # When UP arrow key is pressed
            if row-1 < 1:
                row = 2
                month += 6
            else:
                row = 1
                month -= 6
        elif k == key.DOWN() and row <= 2: # When DOWN arrow key is pressed
            if row+1 > 2:
                row = 1
                month -= 6
            else:
                row = 2
                month += 6
        elif k == key.LEFT() and col >= 1: # When LEFT arrow key is pressed
            if col-1 < 1:
                col = 6
                month += 5
            else:
                col -= 1
                month -= 1
        elif k == key.RIGHT() and col <= 6: # When RIGHT arrow key is pressed
            if col+1 > 6:
                col = 1
                month -= 5
            else:
                col += 1
                month += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            return month
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
#---------------------------------------------------------------------------------
def choose_deadline(month): # Select the date which students should submit/have their assessment
    global schedule_year
    row = 0
    col = 0
    day_num = 1
    leave = False
    day_abbr = calendar.day_abbr # Get the abbreviate days of the week (e.g Monday, Tuesday)
    month_name = calendar.month_name # Get the month name (e.g January, February)
    if int(current_month) > month:
        schedule_year = next_year
    else:
        schedule_year = int(current_year)
    month_day = calendar.monthcalendar(schedule_year, month)
    for y in range(len(month_day[0])):
        if month_day[0][y] == 1: # Find the position of 1st date
            col = y
    s = get.exist_date(month, month_day, col)
    while not leave:
        print_date()
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
                if date_exist(s[month-1], month_day[i][j]) and month_day[row][col] == month_day[i][j]: # When overlap with the red highlighted date number using yellow colour text
                    print(Fore.YELLOW + str(month_day[i][j]) + Fore.RESET, end = "\t ")
                elif date_exist(s[month-1], month_day[i][j]): # Show the unavailable date using red colour text
                    print(Fore.RED + str(month_day[i][j]) + Fore.RESET, end = "\t ")
                elif month_day[row][col] != month_day[i][j]: # print rest of the date numbers
                    print(month_day[i][j], end = "\t ")
                else:
                    print(Fore.GREEN + str(month_day[i][j]) + Fore.RESET, end = "\t ") # Show the selecting number using green colour text
            print()
        for i in range(11):
            print()
        print("                                           <UP>")
        print()
        print("                                    <LEFT>      <RIGHT>      <ENTER> Confirm      <ESC> Back")
        print()
        print("                                          <DOWN>")
        k = readkey()
        while k != key.UP() and k != key.DOWN() and k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.UP() and row > 0 and month_day[row-1][col] != " ": # When UP arrow key is pressed
            day_num -= 7
            row -= 1
        elif k == key.DOWN() and row < len(month_day)-1 and month_day[row+1][col] != " ": # When DOWN arrow key is pressed
            day_num += 7
            row += 1
        elif k == key.LEFT() and col > 0 and month_day[row][col-1] != " ": # When LEFT arrow key is pressed
            day_num -= 1
            col -= 1
        elif k == key.RIGHT() and col < 6 and month_day[row][col+1] != " ": # When RIGHT arrow key is pressed
            day_num += 1
            col += 1
        elif k == key.ENTER(): # When ENTER key is pressed
            if (month == int(current_month) and day_num <= int(current_day)) or date_exist(s[month-1], month_day[row][col]):
                pass # the date expired or highlight in red ---> no respond
            else:
                return day_num
        elif k == key.ESC(): # When ESC key is pressed
            leave = True
#---------------------------------------------------------------------------------
def assm_time():
    os.system("cls")
    print_date()
    print()
    while True:
        for i in range(10):
            print()
        print("                                                       <Empty> To Return")
        print()
        inp = input("                   How much time does your assessment spend (0.1 - 5hrs): ")
        os.system("cls")
        if inp == "": # Return to previous page with empty input
            return None
        try:
            inp = float(inp)
            if inp <= 0 or inp > 5:
                print_date()
                print(Fore.RED + "                                                 Wrong Input! Enter Again." + Fore.RESET)
            else:
                return str(inp)
        except ValueError: # When input invaild data (string)
            print_date()
            print(Fore.RED + "                                                 Wrong Input! Enter Again." + Fore.RESET)
#---------------------------------------------------------------------------------
def choose_specific_period(month):
    global schedule_year
    row = 0
    col = 0
    day_num = 1
    leave = False
    day_abbr = calendar.day_abbr # Get the abbreviate days of the week (e.g Monday, Tuesday)
    month_name = calendar.month_name # Get the month name (e.g January, February)
    if int(current_month) > month:
        schedule_year = next_year
    else:
        schedule_year = int(current_year)
    month_day = calendar.monthcalendar(schedule_year, month)
    for y in range(len(month_day[0])):
        if month_day[0][y] == 1: # Find the position of 1st date
            col = y
    s = get.exist_date(month, month_day, col)
    while not leave:
        print_date()
        print("\t\t\t\t     Select and Confirm the Specific Period Arragement")
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
                if date_exist(s[month-1], month_day[i][j]) and month_day[row][col] == month_day[i][j]: # When overlap with the red highlighted date number using yellow colour text
                    print(Fore.YELLOW + str(month_day[i][j]) + Fore.RESET, end = "\t ")
                elif date_exist(s[month-1], month_day[i][j]): # Show the unavailable date using red colour text
                    print(Fore.RED + str(month_day[i][j]) + Fore.RESET, end = "\t ")
                elif month_day[row][col] != month_day[i][j]: # print rest of the date numbers
                    print(month_day[i][j], end = "\t ")
                else:
                    print(Fore.GREEN + str(month_day[i][j]) + Fore.RESET, end = "\t ") # Show the selecting number using green colour text
            print()
        for i in range(11):
            print()
        print("                               <UP>")
        print()
        print("                        <LEFT>       <RIGHT>      <SPACE> Select      <ENTER> Confirm      <ESC> Back")
        print()
        print("                              <DOWN>")
        k = readkey()
        while k != key.UP() and k != key.DOWN() and k != key.LEFT() and k != key.RIGHT() and k != key.SPACE() and k != key.ENTER() and k != key.ESC():
            k = readkey()
        os.system("cls")
        if k == key.UP() and row > 0 and month_day[row-1][col] != " ":
            day_num -= 7
            row -= 1
        elif k == key.DOWN() and row < len(month_day)-1 and month_day[row+1][col] != " ":
            day_num += 7
            row += 1
        elif k == key.LEFT() and col > 0 and month_day[row][col-1] != " ":
            day_num -= 1
            col -= 1
        elif k == key.RIGHT() and col < 6 and month_day[row][col+1] != " ":
            day_num += 1
            col += 1
        elif k == key.SPACE():
            if not date_exist(s[month-1], month_day[row][col]): # When the number does not highlight in red, append into list
                s[month-1].append(str(day_num))
            else:
                for j in range(len(s[month-1])): # When the number highligh in red, remove the number from list
                    if s[month-1][j] == str(day_num):
                        del s[month-1][j]
                        break
        elif k == key.ENTER():
            update.exist_date(s)
            return 0
        elif k == key.ESC():
            leave = True
#---------------------------------------------------------------------------------
def date_exist(s, d): # linear search for target d
    exist = False
    i = 0
    while not exist and i < len(s): # Search for target d if it is exist in list s
        if s[i] == str(d):
            exist = True
        i += 1
    return exist
#---------------------------------------------------------------------------------
def teacher_setting(): # To open setting function
    os.system("cls")
    print_date()
    print("\t\t\t\t\t\t      Settings")
    for x in range(7):
        print()
    print(Fore.CYAN)
    print("\t\t\t\t          <1>  Reset Password")
    print()
    print("\t\t\t\t         <ESC> Back" + Fore.RESET)
    k = readkey()
    while k != "1" and k != key.ESC():
        k = readkey()
    if k == "1":
        os.system("cls")
        print()
        return resetpw()
    elif k == key.ESC():
        return teachers_system()
#---------------------------------------------------------------------------------
def resetpw(): # To reset password
    while True:
        print_date()
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
                print(Fore.RED + "The Old Password is incorrect".rjust(70) + Fore.RESET)
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
                    print(Fore.RED + "                                            The Password Should Not Be Same." + Fore.RESET)
                elif new_pw == default_pw[password_index] and password_index != 0: # Check if the new password equal to the original / default password
                    os.system("cls")
                    print(Fore.RED + "                                   The Password Should Not Be Same As Default Password." + Fore.RESET)
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
                            print(Fore.RED + "                                            Two New Password are not the same " + Fore.RESET)
                        else:
                            pw_ok = pw_check(new_pw)
                            if pw_ok:
                                password[password_index] = new_pw
                                update.password()
                                for x in range(10):
                                    print()
                                print(Fore.GREEN + "                                               RESET PASSWORD SUCCESSFUL")
                                print()
                                print("                                                  Please Login Again")
                                print()
                                print("                                             Press <ANY KEY> to continue." + Fore.RESET)
                                readkey()
                                return
                            else:
                                print(Fore.RED + "                                       The New Password Does Not Meet Requirements" + Fore.RESET)
#---------------------------------------------------------------------------------
def change_pw(): # Change password for first login
    while True:
        print_date()
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
            print(Fore.RED + "                                            The Password Should Not Be Same." + Fore.RESET)
        else:
            re_enter_pw = input("                                        Enter the New Password again: ")
            if re_enter_pw == "": # Return when empty input
                return None
            else:
                re_enter_pw = encrypted_pw(re_enter_pw)
                os.system("cls")
                if new_pw != re_enter_pw: # Input data twice and check if they are the same
                    print(Fore.RED + "                                            Two New Password are not the same " + Fore.RESET)
                else:
                    pw_ok = pw_check(new_pw)
                    if pw_ok:
                        password[password_index] = new_pw
                        update.password()
                        for x in range(12):
                            print()
                        print(Fore.GREEN + "RESET PASSWORD SUCCESSFUL".rjust(68))
                        print()
                        print("Press <ANY KEY> to continue.".rjust(69) + Fore.RESET)
                        readkey()
                        return teachers_system()
                    else:
                        print(Fore.RED + "                                       The New Password Does Not Meet Requirements" + Fore.RESET)
#---------------------------------------------------------------------------------
def pw_check(pw): # Check if password meet the requirements of password rules
    pw = decrypted_pw(pw) # Decrypted password
    word_length, capital, small_letter, num, blank_space = pw_range_check(pw)
    if word_length and capital and small_letter and num and not blank_space:
        return True
    else:
        return False
#---------------------------------------------------------------------------------
def pw_range_check(pw2): # Check if the password consists of 8 characters (at least 1 number, 1 capital letter and 1 small letter) with no space
    wl = cl = sl = number = space = False
    for i in range(len(pw2)):
        if len(pw2) >= 8: # Check if the password has more than or equal to 8 characters
            wl = True
        if pw2[i] < "]" and pw2[i] > "?": # Check if the password has at least one capital letter
            cl = True
        if pw2[i] >= "/" and pw2[i] < ":": # Check if the password has at least one number
            number = True
        if pw2[i] > "`" and pw2[i] < "|": # Check if the password has at least one small letter
            sl = True
        if pw2[i] == " ": # Check if the password has spaces
            space = True
    return wl, cl, sl, number, space
#---------------------------------------------------------------------------------
def searching(): # Searching
    get.assm()
    get.assm_log()
    os.system("cls")
    print_date()
    print("                                                        Searching")
    for i in range(10):
        print()
    if len(assm_log) != 0: # Case when assessment log has item(s)
        print("                                   Please enter any words to search for assessments")
        print()
        inp_search = input("                                                      : ").upper()
        if inp_search == "":
            os.system("cls")
            return choose_class("3")
        else:
            return search_assm(inp_search)
    else: # Case when assessment log does not have items
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
        if find == -1: # When it can't find the input, find = -1
            pass
        else:
            result.append(assm_log[i]) # When it found, append into result
    total_page_num = -(-len(result)//20) 
    page_num = 1
    while True:
        os.system("cls")
        if total_page_num < 2: # Case for only one page in total
            print_date()
            print("                                                        Searching")
            print()
            if len(result) == 0: # Case for no result
                print("                                         The search result for \"" + inp + "\" is as follow.")
                print()
                print(Fore.RED + "                                                    No assessment Found." + Fore.RESET)
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
            while k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.ENTER(): # When ENTER key is pressed
                return searching()
            elif k == key.ESC(): # When ESC key is pressed
                os.system("cls")
                return choose_class(3)
        elif page_num > 1 and page_num < total_page_num: # Case for more than one pages but not the last page
            print_date()
            print("                                                        Searching")
            print()  
            print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
            print()
            for j in range((page_num-1)*20, page_num*20):
                print("                                                 "+ "%3s" % str(j+1) + ". " + result[j])
            print()
            print("                  <LEFT> Previous Page     <RIGHT> Next Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.LEFT() and k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.LEFT(): # When LEFT arrow key is pressed
                page_num -= 1
            elif k == key.RIGHT(): # When RIGHT arrow key is pressed
                page_num += 1
            elif k == key.ENTER(): # When ENTER key is pressed
                return searching()
            elif k == key.ESC(): # When ESC key is pressed
                os.system("cls")
                return choose_class(3)
        elif page_num == total_page_num: # Case for the last page
            print_date()
            print("                                                        Searching")
            print()   
            print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
            print()
            for j in range((page_num-1)*20, len(result)):
                print("                                                 " + "%3s" % str(j+1) + ". " + result[j])
            print()
            for x in range(20-len(result)+(page_num-1)*20):
                print()
            print("                               <LEFT> Previous Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.LEFT() and k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.LEFT(): # When LEFT arrow key is pressed
                page_num -= 1
            elif k == key.ENTER(): # When ENTER key is pressed
                return searching()
            elif k == key.ESC(): # When ESC key is pressed
                os.system("cls")
                return choose_class(3)
        else: # Case for the first page
            print_date()
            print("                                                        Searching")
            print()  
            print("                          The search result for \"" + inp + "\" is as follow. There are " + str(len(result)) + " result(s) found.")
            print()
            for j in range(page_num*20):
                print("                                                 " + "%3s" % str(j+1) + ". " + result[j])
            print()
            print("                               <RIGHT> Next Page     <ENTER> Search Again     <ESC> Return")
            k = readkey()
            while k != key.RIGHT() and k != key.ENTER() and k != key.ESC():
                k = readkey()
            if k == key.RIGHT(): # When RIGHT arrow key is pressed
                page_num += 1
            elif k == key.ENTER(): # When ENTER key is pressed
                return searching()
            elif k == key.ESC(): # When ESC key is pressed
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
def append_item(u, p, na):
    f1 = open("username.txt", "a")
    f2 = open("encrypted_pw.txt", "a")
    f3 = open("default_pw.txt", "a")
    f4 = open("class_list.txt", "a")
    f1.write("\n" + u) # write new username
    f2.write("\n" + p) # write new password
    f3.write("\n" + p)
    f4.write("\n" + na)# write "Not yet Assigned"
    f1.close()
    f2.close()
    f3.close()
    f4.close()
#---------------------------------------------------------------------------------
def clear_log(): # Clear all the log become empty text file
    for i in range(1, 4): # 2D-list for 12 files in each hw log folders
        for j in range(4):
            if j == 0:
                form_char = "A"
            elif j == 1:
                form_char = "B"
            elif j == 2:
                form_char = "C"
            else:
                form_char = "D"
            f1 = open(path + "\\" + "Junior_hw_log" + "\\" + str(i) + form_char + "_assessments_hw_log.txt", "w")
            f2 = open(path + "\\" + "Senior_hw_log" + "\\" + str(i+3) + form_char + "_assessments_hw_log.txt", "w")
            f1.write("")
            f2.write("")
            f1.close()
            f2.close()
#---------------------------------------------------------------------------------
def loading():
    print()
    item = "Loading.........."
    print(Fore.GREEN + "                                              ", end = "")
    for i in range(len(item)):
        print(item[i], end = "", flush = True)
        time.sleep(0.1)
    time.sleep(0.4)
    print(Fore.RESET)
#---------------------------------------------------------------------------------
def readkey():
    ch = msvcrt.getwch()
    if ch in "\x00\xe0":
        ch = "\x00" + msvcrt.getwch()
    return ch
#---------------------------------------------------------------------------------
while True:	# main program
    login_selection = main_menu()
    path = os.getcwd() # Getting the path of this python file
    if login_selection == "1":
        login()
    elif login_selection == "2":
        print_date()
        system_name()
        print("")
        forget_pw()
    elif login_selection == "3": # Leave Program
        leave_msg()
        break