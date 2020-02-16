year = int(input())+1
def cool_year(year):
    str_year = str(year)
    set_year = set(str_year)
    if len(set_year)==4:
        return True
    else:
        return False

while 1:
    if cool_year(year)==True:
        print(year)
        break
    elif cool_year(year)==False:
        year+=1
