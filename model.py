# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import openai
import param

########################################################################
openai.api_key = "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"
########################################################################

def request(text):
    model_active = "text-davinci-003"
    try:
        print("\nmodelQ=[" + text + "]")
        response = openai.Completion.create(
            model= model_active,
            prompt=text,
            temperature=param.params["temperature"],
            max_tokens=param.params["max_tokens"],
            top_p=1.0,
            frequency_penalty=param.params["frequency_penalty"],
            presence_penalty=param.params["presence_penalty"],
            stop=param.params["stop"]
        )
        print("\nmodelA=[" + (response["choices"][0]["text"]) + "]\n")
        return response["choices"][0]["text"]
    except:
        print("\nmodelError = [An exception occurred:")
        print(sys.exc_info())
        print("]\n")
        return (" ** Model Exception occurred")


#
def set_key(key):
    openai.api_key = key
    print("Key is changed")
