import requests
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

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
        target_lang = lang_selector.get()
        translated_text = translate_text(text_to_translate, target_lang)  # Translate to selected language
        translated_text_box.delete("1.0", tk.END)  # Clear the text box
        translated_text_box.insert(tk.END, translated_text)  # Insert the translated text
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.geometry("800x600")  # Set the size of the window
root.title("Translator")

# Create a dropdown list for language selection
lang_selector = ttk.Combobox(root, values=['EN', 'ZH', 'DE', 'FR', 'ES', 'IT', 'NL', 'PL'], state="readonly")
lang_selector.set('EN')
lang_selector.grid(row=0, column=1, padx=(0,10))

text_to_translate_label = tk.Label(root, text="Text to translate:")
text_to_translate_label.grid(row=0, column=0, sticky='W')

# Use scrolledtext widget which has a vertical scroll bar built in
text_to_translate_entry = scrolledtext.ScrolledText(root, font=("Microsoft YaHei", 10))
text_to_translate_entry.grid(row=1, column=0, sticky='nsew')

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.grid(row=1, column=1, sticky='nsew')

translated_text_label = tk.Label(root, text="Translated text:")
translated_text_label.grid(row=0, column=2, sticky='W')

translated_text_box = scrolledtext.ScrolledText(root, font=("Microsoft YaHei", 10))
translated_text_box.grid(row=1, column=2, sticky='nsew')

# Configure the grid to expand as window size changes
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
