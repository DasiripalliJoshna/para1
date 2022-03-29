def Check_Even(a):
    if a%2==0:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("enter number"))
    result=Check_Even(a)
    print(result)