def main():
    try:
        a = int(input("Hey Enter a Number:"))
        print(a)
        return

    except Exception as e:
        print(e)  
        return

    finally:
        print("Hey, I am inside of finally")  #Executed regardless of error!


main()            