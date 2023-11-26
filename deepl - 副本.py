import requests
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"
API_KEY = "api_key"  # Replace with your DeepL API key

def translate_text(text, target_lang):
    data = {
        'auth_key': API_KEY,
        'text': text,
        'target_lang': target_lang,
    }

    response = requests.post(DEEPL_API_URL, data=data)
    response_json = response.json()

    translations = response_json.get('translations', [{}])
    translated_text = translations[0].get('text', '')

    return translated_text

def translate():
    try:
        text_to_translate = text_to_translate_entry.get("1.0", "end-1c")  # read text from the start(1.0) to the end
        translated_text = translate_text(text_to_translate, 'ZH')  # Translate to ZH
        translated_text_box.delete("1.0", tk.END)  # Clear the text box
        translated_text_box.insert(tk.END, translated_text)  # Insert the translated text
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.geometry("800x600")  # Set the size of the window
root.title("Translator")

text_to_translate_label = tk.Label(root, text="Text to translate:")
text_to_translate_label.pack()

# Use scrolledtext widget which has a vertical scroll bar built in
text_to_translate_entry = scrolledtext.ScrolledText(root, width=90, height=16)
text_to_translate_entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

translated_text_label = tk.Label(root, text="Translated text:")
translated_text_label.pack()

translated_text_box = scrolledtext.ScrolledText(root, width=90, height=16)
translated_text_box.pack()

root.mainloop()
