# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('Hello! this is python...')
# This is a sample Python graph script.

# =====================================================
# *****************************************************
# =====================================================

import tkinter as tk



def goWindow():

    #  встроенная функция завершения приложения ==========================
    def do_cloze():
        window.destroy()
    # ====================================================================

    window = tk.Tk()
    window.geometry('450x450')
    window.title('примеры построения графиков')

    btnCloze = tk.Button(window, text = 'Закрыть', font=('Helvetica', 10, 'bold'), command=do_cloze)
    btnCloze.place(x=330, y=400, width=90, height=30)

    window.mainloop()

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    goWindow()


if __name__ == '__main__':
    print_hi('PyCharm graph script')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
