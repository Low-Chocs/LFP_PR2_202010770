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

class match:
    
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
            <h1>Jornada</h1>
            <form>
        </header>
        <div>"""
    
    def table(self, list, second_list):
        if len(list) >= 1:
            self.writer+='''
            
            <table class="table table">
        <thead>
        <tr>
        <th scope="col">Jornada</th>
        <th scope="col">Temporada</th>
        <th scope="col">Local</th>
        <th scope="col">Goles del local</th>
        <th scope="col">Visitante</th>
        <th scope="col">Goles del visitante</th>
        </tr>
        </thead>
        <tbody>
        '''
            counter=0
            
            for i in range(len(list)):
                element = list[i]
                if i > 1:
                    counter += 1
                if counter == 1 and i > 1:
                    self.writer+='''   
                    <tr>
                    <th scope="row">{}</th>
                    <td>{}</td>
                    <td>{}</td>'''.format(list[0], list[1], list[i])
                elif counter == 2 and i > 1:
                    self.writer+='''   
                    <td>{}</td>'''.format(list[i])
                elif counter == 3 and i > 1:
                    self.writer+='''   
                    <td>{}</td>'''.format(list[i])
                elif counter == 4 and i > 1:
                    self.writer+='''   
                    <td>{}</td>'''.format(list[i])
                    counter = 0

            self.writer += '''   
            </tr>
            '''

            self.writer+='''</tbody>
            </table> 
            '''
        else: self.writer += '''
        <h2>No se han detectado partidos</h2> 
            </div>
        <footer>
       <h2>Luis Mariano Moreira García 202010770</h2> 
        </footer>
        </body>
        </html>'''
        file_name = second_list[3]
        with open("{}.html".format(file_name),"w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("{}.html".format(file_name))

class general_table:

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
            <h1>Tabla   </h1>
            <form>
        </header>
        <div>"""
    
    def table(self, list, second_list):
        if len(list) >= 1:
            self.writer+='''
            
            <table class="table table">
        <thead>
        <tr>
        
        <th scope="col">Equipo</th>
        <th scope="col">Jornadas</th>
        <th scope="col">G</th>
        <th scope="col">E</th>
        <th scope="col">P</th>
        <th scope="col">G+</th>
        <th scope="col">G-</th>
        <th scope="col">Pts</th>
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
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            '''.format(i[7],i[0], i[1], i[2], i[3], i[4], i[5], i[6])

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
        file_name = second_list[1]
        with open("{}.html".format(file_name),"w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("{}.html".format(file_name))

class only_match:
    
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
            <h1>Tabla   </h1>
            <form>
        </header>
        <div>"""
    
    def table(self, list, file, posInicial):
        if len(list) >= 1:
            self.writer+='''
            
            <table class="table table">
        <thead>
        <tr>
        
        <th scope="col">Partido</th>
        <th scope="col">Equipo local</th>
        <th scope="col">Goles Local</th>
        <th scope="col">Equipo Visitante</th>
        <th scope="col">Goles Visitante</th>
        </tr>
        </thead>
        <tbody>
        '''
            counter=posInicial
            
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
            '''.format(counter,i[0], i[1], i[2], i[3])

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
        file_name = file
        with open("{}.html".format(file_name),"w") as writer:
            writer.write(self.writer)
            writer.close()
        os.startfile("{}.html".format(file_name))
