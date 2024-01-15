def customer_num():
    phone_num = {
            "0": "zero",
            "1": "one",
            "2": "two"
    }

    phone = input("Enter phone number: ")
    output = ""

    for item in phone:
        output += phone_num.get(item, "!") + " "
    print(output)
customer_num()
