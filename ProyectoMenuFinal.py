import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ply import lex, yacc

code = '''
if (isRaining()) {
    youbringRainCoat();
} else {
    youwearJacket();
}

IF LPAREN ID LPAREN RPAREN RPAREN LBRACE
    ID LPAREN RPAREN DOTCOM
RBRACE ELSE LBRACE
    ID LPAREN RPAREN DOTCOM
    LBRACE

'''

class Lexer:
    def __init__(self):
        # Definición de palabras reservadas, símbolos y otros patrones
        self.reserved_keywords = ['if', 'else']
        self.symbols = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=', '(', ')', '{', '}', ';']
        self.token_patterns = [
            ('VARIABLE', r'\$\w+'),
            ('Numero', r'^\-?[0-9]+(\.[0-9]+)?$|[0-9]+|-?[0-9]+'),
            ('reservada', r'\b(?:' + '|'.join(map(re.escape, self.reserved_keywords)) + r')\b'),
            ('Identificador', r'[A-Za-z_][A-Za-z0-9_]*'),
            ('Simbolos', '|'.join(map(re.escape, self.symbols))),
        ]
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_patterns)
        self.token_pattern = re.compile(self.token_regex)

    def tokenize(self, text):
        tokens = []
        position = 0
        while position < len(text):
            match = self.token_pattern.match(text, position)
            if match:
                token_type = match.lastgroup
                if token_type != 'SPACE':
                    token_value = match.group(token_type)
                    tokens.append((token_type, token_value))
                position = match.end()
            else:
                position += 1
        return tokens

tokens = (
    'IF',
    'ELSE',
    'ID',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'DOTCOM',
)

t_DOTCOM = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    return t

t_ignore = ' \t\n'

def t_error(t):
    error_message(f"Token desconocido '{t.value[0]}'", t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()

def p_if_loop(p):
    '''
    if_loop : IF LPAREN ID LPAREN RPAREN RPAREN LBRACE ID LPAREN RPAREN DOTCOM RBRACE ELSE LPAREN ID LPAREN RPAREN RPAREN LBRACE ID LPAREN RPAREN DOTCOM RBRACE
    '''

def p_error(p):
    if p:
        error_message(f"Error de sintaxis en '{p.value}'", p.lineno)
    else:
        error_message("Error de sintaxis: final inesperado del código", len(code_text.get("1.0", "end-1c").split('\n')))

parser = yacc.yacc()

def lex_analyzer(code):
    lexer.input(code)
    tokens = []
    
    line_number = 1
    
    for line in code.split('\n'):
        for token in lexer:
            token_type = token.type
            token_value = token.value
            tokens.append((line_number, token_type, token_value))
        
        line_number += 1
    
    return tokens

def parse_code(code):
    parser.parse(code, lexer=lexer)

def error_message(message, line_number):
    messagebox.showerror("Error de sintaxis", f"{message}\nEn la línea {line_number}")

def process_code():
    code = code_text.get("1.0", "end-1c")
    tokens = lex_analyzer(code)
    result_text.delete("1.0", "end")
    for token in tokens:
        line_number, token_type, token_value = token
        result_text.insert("end", f"Tokens ->: {token_type} -> {token_value}\n")
    try:
        parse_code(code)
    except Exception as e:
        show_error_message(str(e))

def show_success_message():
    messagebox.showinfo("Éxito", "Ejecución exitosa")

def show_error_message(error_message):
    messagebox.showerror("Error", f"Error durante la ejecución: {error_message}")



class NavegacionVentanasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Sintáctico y Léxico IF")
        
        self.text_label = tk.Label(text="ANALIZADOR LÉXICO Y SINTÁCTICO", height=1, width=50)
        self.text_label.pack(pady=1)
        self.text_label = tk.Label(text="Diego Gonzalez Carpio 5M", height=1, width=50)
        self.text_label.pack(pady=1)
        
        self.bottom_label = tk.Label(self.root, text="################# IF | ELSE ################# ", height=1, width=50)
        self.bottom_label.pack(side="bottom", pady=10)
        
        self.button_style = ttk.Style()
        self.button_style.configure("EstiloBoton.TButton", font=("Helvetica", 14), padding=20)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.ventana_actual = None
        
        self.if_text = tk.Text(self.frame, height=5, width=18, font=("Helvetica", 13))
        self.if_text.insert("1.0", "if (isRaining()) { \n youbringRainCoat(); \n } else (isSnowing()) { \n youwearJacket(); \n }")
        self.if_text.pack(pady=1)

        self.crear_botones()

    def crear_botones(self):
        boton_ventana1 = ttk.Button(self.frame, text="Analizador Sintáctico", style="EstiloBoton.TButton", command=self.mostrar_ventana1)
        boton_ventana2 = ttk.Button(self.frame, text="Analizador Léxico", style="EstiloBoton.TButton", command=self.mostrar_ventana2)

        boton_ventana1.pack(fill="x", padx=10, pady=5)
        boton_ventana2.pack(fill="x", padx=10, pady=5)

    def mostrar_ventana1(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()

        self.ventana_actual = tk.Toplevel(self.root)
        self.ventana_actual.title("Analizador Sintáctico")
        self.crear_interfaz_analizador_sintactico(self.ventana_actual)
        self.crear_boton_regresar(self.ventana_actual) 

    def mostrar_ventana2(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()

        self.ventana_actual = tk.Toplevel(self.root)
        self.ventana_actual.title("Analizador Léxico")
        self.crear_interfaz_analizador_lexico(self.ventana_actual)
        self.crear_boton_regresar(self.ventana_actual) 

    def crear_interfaz_analizador_sintactico(self, ventana):
        frame = tk.Frame(ventana)
        frame.pack(padx=20, pady=20)

        global code_text
        code_text = tk.Text(frame, height=10, width=50, font=("Arial", 13))
        code_text.pack()

        process_button = tk.Button(frame, text="Analizar",padx=10, command=process_code)
        process_button.pack(pady=8)
        
        clean_button = tk.Button(frame, text="Limpiar",padx=10, command=self.clean_all)
        clean_button.pack(pady=5)
        
        result_label = tk.Label(frame, text="Tokens:")
        result_label.pack(pady=5)

        global result_text
        result_text = tk.Text(frame, height=10, width=50)
        result_text.pack()

        status_label = tk.Label(frame, text="")
        status_label.pack()
    
    def clean_all(self):  # Agregar self como primer argumento
        code_text.delete("1.0", "end")
        result_text.delete("1.0", "end")

    def crear_interfaz_analizador_lexico(self, ventana):
        frame = tk.Frame(ventana)
        frame.pack(padx=20, pady=20)

        self.code_text = tk.Text(frame, height=10, width=50, font=("Arial", 13))
        self.code_text.pack()

        self.button_frame = tk.Frame(frame)
        self.button_frame.pack()

        self.analyzeL_button = tk.Button(self.button_frame, text="Analizar", command=self.analyze_text )
        self.analyzeL_button.grid(row=0, column=0, padx=30, pady=10)

        self.clean_button = tk.Button(self.button_frame, text="Limpiar", command=self.clean_text)
        self.clean_button.grid(row=0, column=2, padx=30, pady=10)

        self.tree = ttk.Treeview(frame, columns=("Linea", "Token", "Funcion", "Reservada", "Identificador", "Símbolo"), show="headings")
        self.tree.heading("Linea", text="Linea")
        self.tree.heading("Token", text="Token")
        self.tree.heading("Funcion", text="Funcion")
        self.tree.heading("Reservada", text="Reservada")
        self.tree.heading("Identificador", text="Identificador")
        self.tree.heading("Símbolo", text="Símbolo")

        self.tree.pack()
        

    def analyze_text(self):
        lexer = Lexer()
        text = self.code_text.get("1.0", "end")
        lines = text.split('\n')
        tokens_by_line = [lexer.tokenize(line) for line in lines]

        self.tree.delete(*self.tree.get_children())

        for line_number, line_tokens in enumerate(tokens_by_line, start=1):
            for token_type, token_value in line_tokens:
                row_data = [line_number, token_type, token_value, "", "", ""]
                if token_type == 'Numero':
                    row_data[5] = "x"
                elif token_type == 'reservada':
                    row_data[3] = "x"
                elif token_type == 'Identificador':
                    row_data[4] = "x"
                elif token_type == 'Simbolos':
                    row_data[5] = "x"

                self.tree.insert("", "end", values=row_data)

    def clean_text(self):
        self.code_text.delete("1.0", "end")
        self.tree.delete(*self.tree.get_children())
        
    def crear_boton_regresar(self, ventana):
        regresar_button = tk.Button(ventana, text="Regresar al Menú", command=self.regresar_al_menu)
        regresar_button.pack(side="bottom", pady=10)

    def regresar_al_menu(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()
            self.ventana_actual = None

if __name__ == "__main__":
    root = tk.Tk()
    app = NavegacionVentanasApp(root)
    root.mainloop()

