a=int(input("enter a no"))
b=int(input("enter another no"))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
ch=int(input("enter ur choice"))
match(ch):
    case 1:print("Result is",a+b)
    case 2:print("Result is",a-b)
    case 3:print("Result is",a*b)

    case 4:print("Result is",a/b)
    case default:print("invalid")

