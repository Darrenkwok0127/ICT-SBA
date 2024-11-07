from datetime import datetime, date
current = datetime.now()
current_date = current.date()
current_month = current.strftime("%m")
current_year = current.strftime("%Y")
next_year = int(current_year) + 1
inp_month = int(input("Input month: "))
inp_day = int(input("Input Day: "))
print(current_month)
print(current_date)
if int(current_month) > inp_month:
    assm_date = date(next_year, inp_month, inp_day)
else:
    assm_date = date(int(current_year), inp_month, inp_day)
print(assm_date)
if current_date == assm_date:
    print("Same")
else:
    print("Not the Same")