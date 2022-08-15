import sys
import clipboard
import json


SAVED_DATA = 'C:\\Users\\SeanCarley\\Desktopclipboard.json'

# save item to clipboard
def save_items(key):
    cb_data = load_items()
    with open(SAVED_DATA, 'w') as f:
        cb_data[key] = clipboard.paste()
        json.dump(cb_data, f)

# copy item from clipboard
def copy_item(key):
    cb_data = load_items()
    with open(SAVED_DATA, 'r'):
        clipboard.copy(cb_data[key])

# delete item from clipboard
def delete_item(key):
    cb_data = load_items()
    with open(SAVED_DATA, 'w') as f:
        cb_data.pop(key)
        json.dump(cb_data, f)

# clear all items from clipboard
def clear_all():
    cb_data = load_items()
    with open(SAVED_DATA, 'w') as f:
        cb_data = {}
        json.dump(cb_data, f)
  

# populate list of saveditems
def load_items():
    try:
        with open(SAVED_DATA, 'r') as f:
            cb_data = json.load(f)
            return cb_data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    cb_data = load_items()

    if command == 'save':
        # print('save')
        key = input('Enter a key: ')
        cb_data[key] = clipboard.paste()
        save_items(SAVED_DATA, cb_data)
    elif command == 'load':
        # print('load')
        key = input('Enter a key: ')
        if key in cb_data:
            clipboard.copy(cb_data[key])
            print('Data copied to clipboard.')
        else:
            print('key does not exist!')
    elif command == 'list':
        for i in cb_data:
            print('{}: {}'.format(i, cb_data[i]))
    else:
        print('unknown command')
else:
    pass  # print('Please pass exactly 1 command')
