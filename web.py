import os

class token_report:
    
    def __init__(self):
        self.writer="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
    <title>Lexic Report</title>
    <link rel="stylesheet" href="html/Css/report.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
        <header>
            <h1>Lista de tokens</h1>
            <form>
        </header>
        <div>"""
    
    def table(self, list):
        if len(list) >= 1:
            self.writer+='''
            
            <table class="table table">
        <thead>
        <tr>
        
        <th scope="col">#</th>
        <th scope="col">Tipo</th>
        <th scope="col">Lexema</th>
        <th scope="col">Línea</th>
        <th scope="col">Columna</th>
        </tr>
        </thead>
        <tbody>
        '''
            counter=0
            
            for i in list:
                counter+=1
                self.writer+='''   
            <tr>
                <th scope="row">{}</th>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            '''.format(counter,i.get_type(),i.get_lexeme(),i.get_line(),i.get_column())

            self.writer+='''</tbody>
            </table> 
            '''
        else: self.writer += '''
        <h2>No hay tokens disponibles</h2> 
            </div>
        <footer>
       <h2>Luis Mariano Moreira García 202010770</h2> 
        </footer>
        </body>
        </html>'''
        with open("token_report.html","w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("token_report.html")

class error_report:
    
    def __init__(self):
        self.writer="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
    <title>Lexic Report</title>
    <link rel="stylesheet" href="html/Css/report.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
        <header>
            <h1>Lista de errores</h1>
            <form>
        </header>
        <div>"""
    
    def table(self, list):
        if len(list) >= 1:
            self.writer+='''
            
            <table class="table table">
        <thead>
        <tr>
        
        <th scope="col">#</th>
        <th scope="col">Tipo</th>
        <th scope="col">Error</th>
        <th scope="col">Línea</th>
        <th scope="col">Columna</th>
        </tr>
        </thead>
        <tbody>
        '''
            counter=0
            
            for i in list:
                counter+=1
                self.writer+='''   
            <tr>
                <th scope="row">{}</th>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            '''.format(counter,i.get_type(),i.get_error_description(),i.get_line(),i.get_column())

            self.writer+='''</tbody>
            </table> 
            '''
        else: self.writer += '''
        <h2>No se han detectado errores</h2> 
            </div>
        <footer>
       <h2>Luis Mariano Moreira García 202010770</h2> 
        </footer>
        </body>
        </html>'''
        with open("token_report.html","w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("token_report.html")