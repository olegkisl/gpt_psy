#####
from datetime import datetime
import model
import param

history_text = ""
history_visible_text = ""


def request(txt):
    res = model.request(txt)
    # return "\nJohn:"+res+"\nPatient:"
    return res


def request_summary(txt):
    res = model.request(txt)
    return res


def save(file, txt):
    open(file, "w", encoding="utf-8", errors='ignore').write(txt)


def save_append(file, txt):
    open(file, "a", encoding="utf-8", errors='ignore').write(txt)


def start():
    print("\n****START****\n")
    global history_text
    global history_visible_text
    history_text = ""
    history_visible_text = ""
    f1 = open(param.prefix(), encoding="utf-8", errors='ignore').read()
    f2 = open(param.last_summary(), encoding="utf-8", errors='ignore').read()
    f3 = param.params["consultant_name"] + ":"
    if len(f2) < 25:
        f2 = " "
    else:
        f2 = param.params["summary_name"] + f2
    f1 = f1.replace('(@)', f2)
    answer = request(f1 + "\n" + f3)
    answer = answer.strip() + "\n" + param.params["client_name"] + ":"
    history_text = f1 + answer
    history_visible_text = f3 + answer
    return history_visible_text


def request_answer(txt):
    global history_text
    global history_visible_text
    txt = txt.strip()
    txt = txt + "\n" + param.params["consultant_name"] + ":"
    history_text += txt
    history_visible_text += txt
    answer = request(history_text)
    answer = answer.strip() + "\n" + param.params["client_name"] + ":"
    history_text += answer
    history_visible_text += answer
    return history_visible_text


def stop():
    print("\n****STOP****\n")
    global history_text
    global history_visible_text
    txt = param.params["summary_generating_phrase"]
    txt = txt + "\n" + param.params["consultant_name"] + ":"
    history_text += txt
    answer = request_summary(history_text)
    history_text += answer
    summ = answer
    summary_filter = param.params["summary_filter"]
    for x in summary_filter:
        summ = summ.replace(x, " ", 1)
    save(param.last_summary(), summ)
    ct = datetime.now()
    save_append(param.history(), "\n\n----------------- NEXT SESSION ------------------\nTime:-" + str(ct) + "\n")
    save_append(param.history(), history_text)
    history_text = ""
    history_visible_text = ""
    return param.params["end_session_message"]
