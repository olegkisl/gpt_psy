import json
from os import path

param_file_1 = 'params.txt'
history_1 = "history.txt"
prefix_1 = "prefix.txt"
last_summary_1 = "summary.txt"

params = ""
current_folder = "default"


def param_file():
    return path.join(current_folder, param_file_1)


def history():
    return path.join(current_folder, history_1)


def prefix():
    return path.join(current_folder, prefix_1)


def last_summary():
    return path.join(current_folder, last_summary_1)


def load_param(folder):
    global params
    global current_folder
    if folder == "":
        folder = "default"
    try:
        current_folder = folder
        f1 = open(param_file(), encoding="utf-8", errors='ignore').read()
        params = json.loads(f1)
        print("params:")
        print(params)
        return "OK:"
    except:
        print("\nERROR: params load error: " + folder)
        return "Params load error:"