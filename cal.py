def days_to_months(days):
    months = days / 30 
    return months

days = int(input("Masukkan jumlah hari: "))
print(f"{days} hari sama dengan {days_to_months(days)} bulan.")

Loop = True
while Loop:
    days = int(input("Masukkan hari: "))
    if days == 0:
        Loop = False
    elif days < 0:
        print("Hari tidak valid.")
    else:
        print(f"{days} hari sama dengan {days_to_months(days)} bulan.")
        

