import csv
import sys
from token_list import Error
class semantical:

    def __init__(self):
        pass

    def reading(self, token_list: list, error_list: list):
        self.token_list = token_list
        self.error_list = error_list
        if self.error_list == None:
            self.error_list = []
        state = 0
        team_list = []
        team_list.clear()
        reserved_lexeme = ''

        for i in range(len(self.token_list)):
            lexeme = self.token_list[i].get_lexeme()
            if state == 0:
                if lexeme == 'RESULTADO':
                    reserved_lexeme = 'RESULTADO'
                    state = 1
                elif lexeme == 'JORNADA':
                    reserved_lexeme = 'JORNADA'
                    state = 8
                elif lexeme == 'GOLES':
                    reserved_lexeme = 'GOLES'
                    state = 11
                elif lexeme == 'TABLA':
                    reserved_lexeme = 'TABLA'
                    state = 4
                elif lexeme == 'PARTIDOS':
                    state = 3
                    reserved_lexeme = 'PARTIDOS'
                
                elif lexeme == 'TOP':
                    state = 12
                    reserved_lexeme = 'TOP'
                elif lexeme == 'ADIOS':
                    sys.exit()

            elif state == 1:
                if self.token_list[i].get_type() == 'Cadena':
                    team_list.append(lexeme)
                    state = 2
                else:
                        error=Error('Error Semantico', "Se esperaba una cadena", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

            elif state == 2:
                if lexeme == 'VS':
                    state = 3
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (VS)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

            elif state == 3:
                if self.token_list[i].get_type() == 'Cadena':
                    team_list.append(lexeme)
                    state = 4
                else:
                        error=Error('Error Semantico', "Se esperaba una cadena", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

            elif state == 4:
                if lexeme == 'TEMPORADA':
                    state = 5
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (TEMPORADA)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0
            
            elif state == 5:
                if self.token_list[i].get_type() == 'Apertura':
                    state = 6
                    print("Saaan2")
                else:
                        error=Error('Error Semantico', "Se esperaba una apertura (<)", 1, i + 1)
                        error_list.append(error)
                        state = 0

            elif state == 6:
                if self.token_list[i].get_type() == 'Cadena':
                    counter = 0
                    print("Saaan 3")
                    for i in lexeme:
                        counter += 1
                        if counter == 9:
                            try:
                                new_var = lexeme[0] + lexeme[1] + lexeme[2] + lexeme[3]
                                second_var = lexeme[5] + lexeme[6] + lexeme[7] +lexeme[8]
                                check_var = int(new_var)
                                print(new_var)
                                check_var = int(second_var)
                                print(new_var)
                                team_list.append(lexeme)
                                print("JIija")
                                state = 7
                            except:
                                error=Error('Error Semantico', "Se esperaba dos números de 4 digitos", 1, i)
                                error_list.append(error)
                                state = 0
                                print("JIija2")
                else:
                        error=Error('Error Semantico', "Se esperaba un parametro", 1, i + 1)
                        self.error_list.append(error)
                        state = 0
            
            elif state == 7:
                print("Llegue hasta aca")
                print(lexeme)
                if lexeme == '>' and reserved_lexeme == 'RESULTADO':
                    state = 0
                    return self.csv_function(1, team_list)
                elif lexeme == '>' and reserved_lexeme == 'JORNADA':
                    state = 9
                elif lexeme == '>' and reserved_lexeme == 'GOLES':
                    return self.csv_function(3, team_list)
                elif lexeme == '>' and reserved_lexeme == 'TABLA':
                    return self.csv_function(4, team_list)
                elif lexeme == '>' and reserved_lexeme == 'PARTIDOS':
                    return self.csv_function(5, team_list)
                elif lexeme == '>' and reserved_lexeme == 'TOP':
                    return self.csv_function(6, team_list)
                else:
                        error=Error('Error Semantico', "Se esperaba un cierre (>)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0
            
            elif state == 8:
                if self.token_list[i].get_type() == 'Numero':
                    team_list.append(lexeme)
                elif lexeme == 'TEMPORADA':
                    print("Saaan")
                    state = 5
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (TEMPORADA)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

            elif state == 9:
                print("Noooo")
                if lexeme == '-f':
                    state = 10
                else:
                    error=Error('Error Semantico', "Se esperaba la palabra reservada (-f)", 1, i + 1)
                    self.error_list.append(error)
                    state = 0  

            elif state == 10:
                if  self.token_list[i].get_type() == 'Cadena':
                    team_list.append(lexeme)
                    state = 0
                    return self.csv_function(2, team_list)  
                else:
                    error=Error('Error Semantico', "Se esperaba la palabra reservada (-f)", 1, i + 1)
                    self.error_list.append(error)
                    state = 0 

            elif state == 11:
                if lexeme == 'LOCAL':
                    team_list.append(lexeme)
                    state = 3
                elif lexeme == 'VISITANTE':
                    team_list.append(lexeme)
                    state = 3
                elif lexeme == 'TOTAL':
                    team_list.append(lexeme)
                    state = 3
                else:
                    error=Error('Error Semantico', "Se esperaba la palabra reservada (-f)", 1, i + 1)
                    self.error_list.append(error)
                    state = 0 

            elif state == 12:
                if lexeme == 'SUPERIOR':
                    team_list.append(lexeme)
                    state = 4
                elif lexeme == 'INFERIOR':
                    team_list.append(lexeme)
                    state = 4
                elif lexeme == 'TOTAL':
                    team_list.append(lexeme)
                    state = 4
                else:
                    error=Error('Error Semantico', "Se esperaba la palabra reservada (-f)", 1, i + 1)
                    self.error_list.append(error)
                    state = 0 

        

        if state == 9:
            print("Oseeaaaaaa")
            state = 0
            return self.csv_function(2, team_list)            
                    

        else:
                return 'No he logrado entender lo que me has dicho'

    def csv_function(self, case, list):

        if case == 1:
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if list[2] == line['Temporada'] and list[0] == line['Equipo1'] and list[1] == line['Equipo2'] :
                        return 'El resultado de este partido en la temporada {} fue: {} {} - {} {}'.format(list[2], list[0], line['Goles1'],list[1],line['Goles2'])
                csv_file.close()

        elif case == 2:
            var = str(list[0])
            season = str(list[1])
            if len(list) == 3:
                var += str(list[1])
                season = str(list[2])
                
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:

                    if season == line['Temporada'] and var == line['Jornada']:
                        print(line['Temporada'], line['Jornada'], line['Equipo1'], line['Equipo2'])
                csv_file.close()

            return "Se procedera a escribir un html con todos los partidos de la jornada"
        
        elif case == 3:
            return "Se procedera a mostrar la cantidad de goles anotados por un equipo"

        elif case == 4:
            return 'Se procedera a mostrar la tabla de la temporada'

        elif case == 5:
            return 'Se procedera a mostrar los partidos de un equipo de la temporada'
        
        elif case == 6:
            return 'Se procedera a mostrar el top'
        


        

            