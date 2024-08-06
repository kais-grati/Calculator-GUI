import customtkinter as ctk


root = ctk.CTk()
root.geometry('400x600')
root.resizable(False, False)
root.title('Calc by Kais')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")
root.configure(bg='#1f1f1f')
root.wm_iconbitmap('icon.ico')

def mode_menu(choice):
    pass


mode_actuel= ctk.StringVar(value=" Standard")
mode = ctk.CTkOptionMenu(
    root,
    values=[' Standard', ' Scientifique', ' Graphique', ' Bases', ' Devise', ' Longueur',' Volume', ' Masse', ' Temperature', ' Vitesse'],
    command=mode_menu,
    text_font=('Arial', 20),
    dropdown_text_font=('Arial', 20),
    button_hover_color='#33363c',
    bg_color = '#1f1f1f',
    button_color='#1f1f1f',
    fg_color = '#1f1f1f',
    variable=mode_actuel
)
mode.grid(sticky='w',row = 0, column = 0,columnspan=3, pady=(10,20), padx=(30,0))

bars = ctk.CTkTextbox(
    root,
    text_font=('Arial', 20),
    bg_color = '#1f1f1f',
    fg_color = '#1f1f1f',
    width=50
)
bars.insert('0.0','☰')
bars.configure(state='disabled')
bars.place(x=0,y=0)

lcd_text=ctk.StringVar()
text = ['0']
lcd = ctk.CTkEntry(
    root,
    state='readonly', 
    readonlybackground="#1c1e25",
    border_color='white',
    height=100,
    textvariable= lcd_text,
    text_font=('Roboto', 24)
    )

lcd.grid(row = 1, column = 0,pady=0, columnspan=4, sticky='nesw', padx=(5,0))
lcd_text.set(''.join(text))

def click(key):
    global text
    if key in {'+/-', 'C', 'del', '='} and len(text) == 1:
        if text[-1] == '0':
            text = ['0']
    elif key in {'1','2','3','4','5','6','7','8','9','0'} and text[-1] == '²':
        text = [key]
    elif key in {'1','2','3','4','5','6','7','8','9','0'} and text[0]=='0':
        try:
            text[1] in {'+','x','/','-'}
            text.append(key)
        except:
            text.append(key)
            text.pop(0)
    elif key in {'+','x','/','-','²','^'} and text[-1] in {'+','x','/','-','²','^'}:
        text.append(key)
        text.pop(-2)
    elif key in {'1','2','3','4','5','6','7','8','9','0','+','x','/','-'}:
        if key in {'+','x','/','-'} and text[-1] == ',':
            text.pop(-1)
        text.append(key)
    elif key == ',' and text[-1] in {'+','x','/','-'}:
        text.append('0')
        text.append(',')
    elif key in {'²',',','^'} and text[-1] not in {'²',',','^'}:
        text.append(key)
    elif key == '²' and text[-1] == ',':
        text.pop(-1)
        text.append('²')
    elif key == '%':
        text.append('/100')
    elif key == '1/x':
        if text[-1] == '0':
            pass
        elif text[-1] in {'+','x','/','-'}:
            pass
        elif 'x' not in text and '+' not in text and '-' not in text and '/' not in text:
            text.insert(0, '1/')
        else:
            for i,b in enumerate(reversed(text), 1):
                if b in {'+','x','/','-'}:
                    text.insert(-(i-1), '1/')
                    break
    if key == '+/-':
        if text[0] == '0':
            pass
        elif text[-1] in {'+','x','/','-'}:
            pass
        elif 'x' not in text and '+' not in text and '-' not in text and '/' not in text and '^' not in text:
            text.insert(0, '(-')
            text.append(')')
        else:
            for i,b in enumerate(reversed(text), 1):
                if b in {'+','x','/','-','^'}:
                    text.insert(-(i-1), '(-')
                    text.append(')')
                    break
    if key == 'sqrt':
        if text[0] == '0':
            pass
        elif text[-1] in {'+','x','/','-','^'}:
            pass
        elif text[-1] == ',':
            text.pop(-1)
            if 'x' not in text and '+' not in text and '-' not in text and '/' not in text:
                text.insert(0, 'sqrt(')
                text.append(')')
            else:
                for i,b in enumerate(reversed(text), 1):
                    if b in {'+','x','/','-','^'}:
                        text.insert(-(i-1), 'sqrt(')
                        text.append(')')
                        break
        elif 'x' not in text and '+' not in text and '-' not in text and '/' not in text and '^' not in text:
            text.insert(0, 'sqrt(')
            text.append(')')
        else:
            for i,b in enumerate(reversed(text), 1):
                if b in {'+','x','/','-','^'}:
                    text.insert(-(i-1), 'sqrt(')
                    text.append(')')
                    break
    if key == 'C':
        text = ['0']
    if key == 'del':
        if len(text) == 1:
            text = ['0']
        else:
            text.pop(-1)
    lcd_text.set(''.join(text))
    if key == '=': 
        if text[-1] in {'+','-',',','x','/','^'}:
            text.pop(-1)  
            lcd_text.set(''.join(text))
        for i,b in enumerate(text):
            if b == 'x':
                text[i] = '*'
            elif b == '²':
                text[i] = '**2'
            elif b == ',':
                text[i] = '.'
            elif b == '^':
                text[i] = '**'
        try:    
            lcd_text.set(str(eval(''.join(text))))
            
        except ZeroDivisionError:
            lcd_text.set('Error, division by zero')
        except:
            lcd_text.set('Error')
        text = ['0']

button_sqrt = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='√x',
    height = 70,
    width = 96,
    command= lambda : click('sqrt')
)
button_sqrt.grid(column=0, row=2, pady=1, padx=(5,1))
button_percent = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='%',
    height = 70,
    width = 96,
    command= lambda : click('%')

)
button_percent.grid(column=1, row=2, pady=1, padx=1)
button_frac = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='1/x',
    height = 70,
    width = 96,
    command= lambda : click('1/x')

)
button_frac.grid(column=2, row=2, pady=1, padx=1)
button_expo = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='xʸ',
    height = 70,
    width = 96,
    command= lambda : click('^')

)
button_expo.grid(column=3, row=2, pady=1, padx=1)

button_sqr = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='x²',
    height = 70,
    width = 96,
    command= lambda : click('²')

)
button_sqr.grid(column=0, row=3, pady=1, padx=(5,1))

button_clear = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='C',
    height = 70,
    width = 96,
    command= lambda : click('C')

)
button_clear.grid(column=1, row=3, pady=1, padx=1)

button_del = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#2b2d39',
    text='del',
    height = 70,
    width = 96,
    command= lambda : click('del')

)
button_del.grid(column=2, row=3, pady=1, padx=1)

button_divide = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    fg_color= '#2b2d39',
    text='/',
    height = 70,
    width = 96,
    command= lambda : click('/')

)
button_divide.grid(column=3 , row=3 , pady=1, padx=1)

button7 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='7',
    height = 70,
    width = 96,
    command= lambda : click('7')

)
button7.grid(column=0, row=4, pady=1, padx=(5,1))
button8 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='8',
    height = 70,
    width = 96,
    command= lambda : click('8')

)
button8.grid(column=1 , row=4 , pady=1, padx=1)
button9 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='9',
    height = 70,
    width = 96,
    command= lambda : click('9')

)
button9.grid(column=2 , row=4 , pady=1, padx=1)

button_fois = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    fg_color= '#2b2d39',
    text='x',
    height = 70,
    width = 96,
    command= lambda : click('x')

)
button_fois.grid(column=3 , row=4, pady=1, padx=1)

button4 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='4',
    height = 70,
    width = 96,
    command= lambda : click('4')

)
button4.grid(column=0 , row=5, pady=1, padx=(5,1))
button5 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='5',
    height = 70,
    width = 96,
    command= lambda : click('5')

)
button5.grid(column=1 , row=5, pady=1, padx=1)

button6 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='6',
    height = 70,
    width = 96,
    command= lambda : click('6')

)
button6.grid(column=2 , row=5, pady=1, padx=1)

button_moins = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    fg_color= '#2b2d39',
    text='-',
    height = 70,
    width = 96,
    command= lambda : click('-')

)
button_moins.grid(column=3 , row=5, pady=1, padx=1)

button1 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='1',
    height = 70,
    width = 96,
    command= lambda : click('1')

)
button1.grid(column=0 , row=6, pady=1, padx=(5,1))

button2 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='2',
    height = 70,
    width = 96,
    command= lambda : click('2')

)
button2.grid(column=1 , row=6, pady=1, padx=1)

button3 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='3',
    height = 70,
    width = 96,
    command= lambda : click('3')

)
button3.grid(column=2 , row=6, pady=1, padx=1)

button_plus = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    fg_color= '#2b2d39',
    text='+',
    height = 70,
    width = 96,
    command= lambda : click('+')

)
button_plus.grid(column=3 , row=6, pady=1, padx=1)

button_signe = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='+/-',
    height = 70,
    width = 96,
    command= lambda : click('+/-')
)
button_signe.grid(column=0, row=7, pady=1, padx=(5,1))

button0 = ctk.CTkButton(
    root,
    text_font = ('Roboto', 15),
    fg_color= '#33363c',
    text='0',
    height = 70,
    width = 96,
    command= lambda : click('0')

)
button0.grid(column=1 , row=7, pady=1, padx=1)

button_virgule = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    fg_color= '#33363c',
    text=',',
    height = 70,
    width = 96,
    command= lambda : click(',')

)
button_virgule.grid(column=2 , row=7, pady=1, padx=1)

button_equal = ctk.CTkButton(
    root,
    text_font = ('Roboto', 20),
    hover_color= '#ad9fc3',
    fg_color= '#c0b0d8',
    text='=',
    text_color= '#6c6379',
    height = 70,
    width = 96,
    command= lambda : click('=')
)
button_equal.grid(column=3 , row=7, pady=1, padx=1)

root.mainloop()
