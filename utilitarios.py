def aux():
    pass


def click_number(current_number, new_number):
    if current_number['text'] == '0':
        current_number.config(text='')
    current_number.config(text=current_number['text'] + new_number)

def backspace(current_number):
    if len(current_number['text']) > 1:
        current_number.config(text=current_number['text'][:-1])
    else:
        current_number.config(text='0')