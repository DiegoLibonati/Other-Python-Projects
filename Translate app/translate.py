from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

class TranslateProgram:

    def __init__(self,master):
        master.title('Die Translator')
        master.geometry('1080x350')
        master.config(bg='#031927')
        master.resizable('False', 'False')

        #General
        self.ico = PhotoImage(file='./ico.png')
        self.font_family = 'Roboto'
        master.iconphoto(False, self.ico)

        #ComboBoxs
        self.languages = LANGUAGES
        self.languages_values = self.languages.values()
        self.lang_main = StringVar()
        self.lang_to_translate = StringVar()

        #Labels
        self.lang_main_text = StringVar()
        self.lang_to_translate_text = StringVar()
        
        # Lang MAIN
        ttk.Combobox(values=self.lang_values_uppercase(), font='Roboto 14', state='r', textvariable=self.lang_main).place(x=110, y=20)
        self.lang_main.set('ENGLISH')

        Label(font=(self.font_family, 20), textvariable=self.lang_main_text, bg="#031927", fg="#C8E0F4", border=1).place(x=165,y=55)
        self.lang_main_text.set('ENGLISH')

        self.main_text = Text(font='Roboto 18', bg='white', wrap=WORD, background='#031927', foreground='#C8E0F4', borderwidth=2)
        self.main_text.place(x=52, y=100, width=350, height=200)

        # Lang to TRANSLATE
        ttk.Combobox(values=self.lang_values_uppercase(), font='Roboto 14', state='r', textvariable=self.lang_to_translate).place(x=730, y=20)
        self.lang_to_translate.set('SPANISH')

        Label(font=(self.font_family, 20), textvariable=self.lang_to_translate_text, bg="#031927", fg="#C8E0F4", border=1).place(x=790,y=55)
        self.lang_to_translate_text.set('SPANISH')

        self.to_translate_text = Text(font='Roboto 18', bg='white', wrap=WORD, background='#031927', foreground='#C8E0F4', borderwidth=2)
        self.to_translate_text.place(x=675, y=100, width=350, height=200)

        #Button
        Button(width=10, text='Reverse', font=('Roboto 15'), cursor='hand2',command=lambda:self.reverse(), bg='#C8E0F4', fg='#031927').place(x=485, y=150)
        Button(width=10, text='Translate', font=('Roboto 15'), cursor='hand2',command=lambda:self.translate(), bg='#C8E0F4', fg='#031927').place(x=485, y=200)

    def lang_values_uppercase(self):

        new_lang_values = []

        for lang in self.languages_values:
            new_lang_values.append(lang.upper())

        return new_lang_values

    def label_lang_change(self):
        lang_main = self.lang_main.get()
        lang_to_translate = self.lang_to_translate.get()

        self.lang_main_text.set(lang_main)
        self.lang_to_translate_text.set(lang_to_translate)
        root.after(100,self.label_lang_change)
        
    def translate(self):
        try:
            text_main = self.main_text.get('1.0', 'end-1c')
            lang_main = self.lang_main.get().lower()
            lang_to_translate = self.lang_to_translate.get().lower()
            pseudonimo_main = []
            pseudonimo_to_translate = []

            for pseudonimo, country in self.languages.items():
                if lang_main == country:
                    pseudonimo_main.append(pseudonimo)
                    

                if lang_to_translate == country:
                    pseudonimo_to_translate.append(pseudonimo)

            translate_object = Translator()
            text_translate = translate_object.translate(text_main, src=pseudonimo_main[0], dest=pseudonimo_to_translate[0])

            self.to_translate_text.delete(1.0,END)
            self.to_translate_text.insert(END, text_translate.text)   
        except:
            messagebox.showerror(title='Error', message='Try again.')

    def reverse(self):
        text_main = self.main_text.get('1.0', 'end-1c')
        text_to_translate = self.to_translate_text.get('1.0', 'end-1c')
        lang_main = self.lang_main.get()
        lang_to_translate = self.lang_to_translate.get()

        self.lang_to_translate.set(lang_main)
        self.lang_to_translate_text.set(lang_main)

        self.lang_main.set(lang_to_translate)
        self.lang_main_text.set(lang_to_translate)

        self.main_text.delete(1.0, END)
        self.main_text.insert(END, text_to_translate)

        self.to_translate_text.delete(1.0, END)
        self.to_translate_text.insert(END, text_main)

        
root = Tk()

translate_program = TranslateProgram(root)
translate_program.label_lang_change()

root.mainloop()