class Token:
    def __init__(self, type,lexeme, line,column):
        self.type=type
        self.lexeme=lexeme
        self.line=line
        self.column=column

    def print_token(self):
        print("\n 1. Tipo:{}\n 2. Lexema:{}\n 3. Línea:{}\n 4. Columna:{}".format(self.type,self.lexeme,self.line,self.column))
    
    
    def get_type(self):
        return self.type

    def get_lexeme(self):
        return self.lexeme
    
    def get_line(self):
        return self.line
    
    def get_column(self):
        return self.column


class Error:
    def __init__(self, type,errorDescription, line,column):
        self.type = type
        self.errorDescription = errorDescription
        self.line = line
        self.column = column
    
    def get_type(self):
        return self.type

    def get_error_description(self):
        return self.errorDescription
    
    def get_line(self):
        return self.line
    
    def get_column(self):
        return self.column

    def print_error(self):
        print("\n 1. Tipo:{}\n 2. Descripción:{}\n 3. Línea:{}\n 4. Columna:{}".format(self.type,
        self.errorDescription,self.line,self.column))