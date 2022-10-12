#Write a Python script to check if a given key already exists in a dictionary.

Dict={5: 100, 6: 200, 7: 300, 10: 1, 20: 3, 30: 7, 1: 'Apple', 2: 'Banana', 3: 'Manago', 4: 'Greps'}
Keys= Dict.keys()
def check_key():
    Serch_Key = int(input("Enter Key:"))
    try:
        for i in Keys:
            if i==Serch_Key:
                print("This Key is already exits in Dictionary")
                break
        else:
            raise Exception
    except Exception as e:
        print("Try Again")
        check_key()
check_key()
