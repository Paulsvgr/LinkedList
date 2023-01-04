from StackLinkedList import *

def go():
    still_going = True
    product_list = Stack()

    print('Enter a produkt, end by entering "exit" \n')
    while still_going:
        product = input("Enter product:  ")
        if "exit" in product.lower():
            break
        elif product:
            parts = product.split("-")
            if len(parts) == 2:
                if parts[1].isdigit():
                    if 200 <= int(parts[1]) <= 500:
                        only_letters = True
                        for char in parts[0]:
                            if not char.isalpha():
                                only_letters = False
                        if only_letters:
                            product_list.push(product)
                        else: 
                            print('Wrong format on the left side of "-"')
                    else:
                        print("The numberpart should be between 200 and 500")
                else:
                    print('Wrong format on the right side of "-"')
            else:
                print('Should be one "-" symbol')
        else:
            print("You can't enter empty value")
    print("Here are all the entered product:  \n")
    product_list.stack.sort_list()
    product_list.print_stack()

if __name__ == "__main__":
    go()
