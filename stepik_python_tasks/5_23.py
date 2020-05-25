def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            x = int(input())
            print(end_message)
            return x
        except ValueError:
            print(error_message)


x = get_int('Input int number: ', 'Wrong value. Input int number:', 'Thank you.')
print(x)
