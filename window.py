from tkinter import *
from tkinter import ttk
from multicb import *

# functions
def add_item_to_clipboard():
    ''' add the currently copied item to the clipboard '''
    if len(ent1_text.get()) > 0:
        save_items(ent1_text.get())
        populate_list_of_clipboard_items()
    else:
        pass


def populate_list_of_clipboard_items():
    ''' populate the list of items on the clipboard '''
    lst_data = load_items()
    if lst_data == {}:
        lst_bx.delete(0, "end")
        txt_bx.delete("0.0", "end")
    else:
        lst_bx.delete(0, "end")
        txt_bx.delete("0.0", "end")
        lb_pos = 1
        key = ''
        for i in lst_data:
            if lb_pos == 1:
                key = str(i)
            lst_bx.insert(lb_pos, i)
            lb_pos += 1

        lst_bx.selection_set(0)
        if len(lst_data[key]) > 25:
            txt_bx.insert("0.0", lst_data[key][0:25] + "...")
        else:
            txt_bx.insert("0.0", lst_data[key])


def show_selected_key_content(event):
    ''' show the content of the selected item (up to 25 characters) '''
    lst_data = load_items()
    if lst_data == {}:
        pass
    else:
        selectedkeytext = lst_bx.get(lst_bx.curselection())
        data_to_be_copied = str(lst_data[selectedkeytext])
        txt_bx.delete("0.0", "end")
        if len(data_to_be_copied) > 25:
            txt_bx.insert("0.0", data_to_be_copied[0:25] + "...")
        else:
            txt_bx.insert("0.0", data_to_be_copied)

def copy_selected_key_content():
    ''' copy the content of the selected key for pasting'''
    key = lst_bx.get(lst_bx.curselection())
    copy_item(key)


def delete_selected_key():
    ''' delete the selected key '''
    key = lst_bx.get(lst_bx.curselection())
    delete_item(key)
    txt_bx.delete("0.0", "end")
    populate_list_of_clipboard_items()

def clear_all_items():
    clear_all()
    populate_list_of_clipboard_items()


root = Tk()
root.title('Multi-Clipboard')
root.iconbitmap("favicon.ico")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Copy', command=copy_selected_key_content)
editmenu.add_command(label='Delete', command=delete_selected_key)
editmenu.add_separator()
editmenu.add_command(label='Clear All', command=clear_all_items)
menubar.add_cascade(label='Edit', menu=editmenu)
# aboutmenu = Menu(menubar, tearoff=0)
# aboutmenu.add_command(label='How it Works')
# aboutmenu.add_command(label='Version')
# menubar.add_cascade(label='About', menu=aboutmenu)

mainframe = ttk.Frame(root, padding="3 3 12 12", relief=RIDGE)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# add or remove an entry to the clipboard
lbl1_text = StringVar()
lbl1 = Label(mainframe, textvariable=lbl1_text, width=15, padx=0.5, pady=0.5).grid(row=1, column=1)
lbl1_text.set('Enter a Key: ')

ent1_text = StringVar()
ent1 = Entry(
    mainframe, width=15, textvariable=ent1_text,
).grid(row=1, column=2)

btn_add = Button(
    mainframe, text='Add', 
    width=10, padx=0.5, pady=0.5,
    command=add_item_to_clipboard
).grid(row=1, column=3, columnspan=2)


# show existing keys and content of selected key
lbl2 = Label(
    mainframe, text="List of Existing Keys: ", 
    padx=0.5, pady=0.5
).grid(row=2, column=1, columnspan=2)
lst_bx = Listbox(
    mainframe, width=25, height=15, 
    selectmode=SINGLE
)

lst_bx.grid(row=3, column=1, columnspan=2)

lbl3 = Label(
    mainframe, text="Content of Selected Key: ", 
    padx=0.5, pady=0.5
).grid(row=2, column=3, columnspan=2)

txt_bx = Text(mainframe, width=35, height=15, exportselection=0)
txt_bx.grid(row=3, column=3, columnspan=2)

populate_list_of_clipboard_items()
lst_bx.bind('<<ListboxSelect>>', show_selected_key_content)

btn_lod = Button(
    mainframe, text='Copy', 
    width=10, padx=0.5, pady=0.5, 
    command=copy_selected_key_content
).grid(row=4, column=3)

btn_del = Button(
    mainframe, text='Delete', 
    width=10, padx=0.5, pady=0.5, 
    command=delete_selected_key
).grid(row=4, column=4)

root.config(menu=menubar)
root.mainloop()