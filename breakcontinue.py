#break statement

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

    #continue statement -skips a loop
    devices = ["laptop","phone","mouse","tablet"]
    for x in devices:
        if x == "phone":

            continue
        print(x)