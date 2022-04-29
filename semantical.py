import csv
from operator import pos
import sys
from token_list import Error
from web import match
from web import general_table
from web import only_match
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
                    state = 0
                    return self.csv_function(3, team_list)
                elif lexeme == '>' and reserved_lexeme == 'TABLA':
                    state = 9
                elif lexeme == '>' and reserved_lexeme == 'PARTIDOS':
                    state = 15
                elif lexeme == '>' and reserved_lexeme == 'TOP':
                    state = 13
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
                if  self.token_list[i].get_type() == 'Cadena' and reserved_lexeme == 'JORNADA':
                    team_list.append(lexeme)
                    state = 0
                    return self.csv_function(2, team_list)  
                elif  self.token_list[i].get_type() == 'Cadena' and reserved_lexeme == 'TABLA':
                    team_list.append(lexeme)
                    state = 0
                    return self.csv_function(4, team_list)
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
                else:
                    error=Error('Error Semantico', "Se esperaba la palabra reservada (-f)", 1, i + 1)
                    self.error_list.append(error)
                    state = 0 

            elif state == 13:
                if lexeme == '-n':
                    state = 14
            
            elif state == 14:
                if self.token_list[i].get_type() == 'Numero':
                    team_list.append(lexeme)
                    print("jfdkash")
                    print(len(self.token_list))
                    print(i)
                    if len(self.token_list) == i+1:
                        state = 0
                        return self.csv_function(6, team_list)
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (TEMPORADA)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

            elif state == 15:
                if lexeme == '-f':
                    team_list.append(lexeme)
                    state = 16
                elif lexeme == '-ji':
                    team_list.append(lexeme)
                    state = 17
                elif lexeme == '-jf':
                    team_list.append(lexeme)
                    state = 17
                else:
                    pass

            elif state == 16:
                if self.token_list[i].get_type() == 'Cadena':
                    team_list.append(lexeme)
                    print(len(self.token_list))
                    print(i)
                    if len(self.token_list) == i+1:
                        state = 0
                        return self.csv_function(5, team_list)
                    else:
                        print("jkshkjfdhjkdfkjsdhkjdfsh")
                        state = 15
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (TEMPORADA)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0


            elif state == 17:
                if self.token_list[i].get_type() == 'Numero':
                    team_list.append(lexeme)
                    print(len(self.token_list))
                    print(i)
                    if len(self.token_list) == i+1:
                        state = 0
                        print("dskjhkjdasf")
                        return self.csv_function(5, team_list)
                    else:
                        print("jkahfjkhdjfasjkdfh")
                        state = 15
                else:
                        error=Error('Error Semantico', "Se esperaba la palabra reservada (TEMPORADA)", 1, i + 1)
                        self.error_list.append(error)
                        state = 0

        

        if state == 9:
    
            if   reserved_lexeme == 'JORNADA':
                team_list.append('jornada')
                state = 0
                return self.csv_function(2, team_list)   
            elif  reserved_lexeme == 'TABLA':
                team_list.append('temporada')
                state = 0
                return self.csv_function(4, team_list)   

        elif state == 13:
        
            if   reserved_lexeme == 'TOP':
                state = 0
                return self.csv_function(6, team_list)         

        elif state == 15:
            
            if   reserved_lexeme == 'PARTIDOS':
                state = 0
                return self.csv_function(5, team_list)    
                    

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
            if len(list) == 4:
                var += str(list[1])
                season = str(list[2])
            new_list = []
            new_list.append(var)
            new_list.append(season)
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if season == line['Temporada'] and var == line['Jornada']:
                        new_list.append(line['Equipo1'])
                        new_list.append(line['Goles1'])
                        new_list.append(line['Equipo2'])
                        new_list.append(line['Goles2'])
                csv_file.close()
            new_match = match()
            lists = list
            new_match.table(new_list, lists)

            return "Se procedera a escribir un html con todos los partidos de la jornada"
        
        elif case == 3:
            goals = 0
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if list[0] == 'LOCAL':
                        if list[2] == line['Temporada'] and list[1] == line['Equipo1']:
                            goals += int(line['Goles1'])
                    elif list[0] == 'VISITANTE':
                        if list[2] == line['Temporada'] and list[1] == line['Equipo2']:
                            goals += int(line['Goles2'])
                    else:
                        if list[2] == line['Temporada'] and list[1] == line['Equipo1']:
                            goals += int(line['Goles1'])
                        if list[2] == line['Temporada'] and list[1] == line['Equipo2']:
                            goals += int(line['Goles2'])
                csv_file.close()

            if list[0] == 'LOCAL':
                return 'La cantidad de goles del {} como local fue de: {}'.format(list[1], goals)
            elif list[0] == 'VISITANTE':
                return 'La cantidad de goles del {} como visitante fue de: {}'.format(list[1], goals)
            elif list[0] == 'TOTAL':
                 return 'La cantidad de goles totales del {} fueron de: {}'.format(list[1], goals)

        elif case == 4:
            dict_table = {}
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if list[0] == line['Temporada']:
                        if not line['Equipo1'] in dict_table:
                            dict_table[line['Equipo1']] = [0,0,0,0,0,0,0,line['Equipo1']]
                        dict_table[line['Equipo1']][0] += 1
                        if line['Goles1'] > line['Goles2']:
                            dict_table[line['Equipo1']][1] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2]) )
                        elif line['Goles1'] == line['Goles2']:
                            dict_table[line['Equipo1']][2] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2] ))
                        else:
                            dict_table[line['Equipo1']][3] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2] ))

                        if not line['Equipo2'] in dict_table:
                            dict_table[line['Equipo2']] = [0,0,0,0,0,0,0, line['Equipo2']]
                        dict_table[line['Equipo2']][0] += 1
                        if line['Goles1'] < line['Goles2']:
                            dict_table[line['Equipo2']][1] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][5] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )
                        elif line['Goles1'] == line['Goles2']:
                            dict_table[line['Equipo2']][2] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][5] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )
                        else:
                            dict_table[line['Equipo2']][3] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][6] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )

                csv_file.close()

                sortedVal = {k: v for k, v in sorted(dict_table.items(), key = lambda v: v[1][6])}
                sorted_list = []
                aux_sorted_list = []
                for element in reversed(sortedVal):
                    sorted_list.append(sortedVal[element])
                
                new_table = general_table()
                new_table.table(sorted_list, list)
                
                
            return 'Se procedera a mostrar la tabla de la temporada'

        elif case == 5:
            match_list = []
            for i in range( len(list)):
                if list[i] == '-f':
                    name = list[i+1]
                if list[i] == '-ji':
                    pos_initial = int(list[i+1])
                if list[i] == '-jf':
                    final_pos = int(list[i+1])
                if not('-j' in list):
                    name = 'partidos'
                if not('-ji' in list):
                    pos_initial = 0
                if not('-jf' in list):
                    final_pos = 0
            print("Logre pasaaaaaaaaaar")

            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                if pos_initial == 0 and final_pos == 0:
                    for line in csv_reader:
                        if list[1] == line['Temporada'] and list[0] == line['Equipo1']:
                            match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                        if list[1] == line['Temporada'] and list[0] == line['Equipo2']:
                            match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                elif pos_initial != 0  and final_pos == 0:
                    counter = 0
                    for line in csv_reader:
                        
                        print(list[1])
                        print(list[0])
                        print(line['Temporada'])
                        print(pos_initial)

                        if list[1] == line['Temporada'] and list[0] == line['Equipo1']:
                            counter += 1
                            if counter >= pos_initial:
                                match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                        if list[1] == line['Temporada'] and list[0] == line['Equipo2']:
                            counter += 1
                            if counter >= pos_initial:
                                match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                elif pos_initial == 0  and final_pos != 0:
                    counter = 0
                    for line in csv_reader:
                        if counter >= final_pos:
                            break
                        if list[1] == line['Temporada'] and list[0] == line['Equipo1']:
                            counter += 1
                            match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                        if list[1] == line['Temporada'] and list[0] == line['Equipo2']:
                            counter += 1
                            match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                
                else:
                    counter = 0
                    for line in csv_reader:
                        
                        if list[1] == line['Temporada'] and list[0] == line['Equipo1']:
                            counter += 1
                            if counter >= pos_initial:
                                match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                        elif list[1] == line['Temporada'] and list[0] == line['Equipo2']:
                            counter += 1
                            if counter >= pos_initial:
                                match_list.append([line['Equipo1'], line['Goles1'], line['Equipo2'], line['Goles2']])
                        if counter >= final_pos:
                            print("Quebramos")
                            print(len(match_list))
                            break


                csv_file.close()

            all_match = only_match()
            all_match.table(match_list, name, pos_initial)
            return 'Se procedera a mostrar los partidos de un equipo de la temporada'
        
        elif case == 6:

            dict_table = {}
            with open('Csvfile/LaLigaBot-LFP.csv') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if list[1] == line['Temporada']:
                        if not line['Equipo1'] in dict_table:
                            dict_table[line['Equipo1']] = [0,0,0,0,0,0,0,line['Equipo1']]
                        dict_table[line['Equipo1']][0] += 1
                        if line['Goles1'] > line['Goles2']:
                            dict_table[line['Equipo1']][1] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2]) )
                        elif line['Goles1'] == line['Goles2']:
                            dict_table[line['Equipo1']][2] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2] ))
                        else:
                            dict_table[line['Equipo1']][3] += 1
                            dict_table[line['Equipo1']][4] += int(line['Goles1'])
                            dict_table[line['Equipo1']][5] += int(line['Goles2'])
                            dict_table[line['Equipo1']][6] = (3 *  int(dict_table[line['Equipo1']][1]) + int(dict_table[line['Equipo1']][2] ))

                        if not line['Equipo2'] in dict_table:
                            dict_table[line['Equipo2']] = [0,0,0,0,0,0,0, line['Equipo2']]
                        dict_table[line['Equipo2']][0] += 1
                        if line['Goles1'] < line['Goles2']:
                            dict_table[line['Equipo2']][1] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][5] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )
                        elif line['Goles1'] == line['Goles2']:
                            dict_table[line['Equipo2']][2] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][5] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )
                        else:
                            dict_table[line['Equipo2']][3] += 1
                            dict_table[line['Equipo2']][4] += int(line['Goles2'])
                            dict_table[line['Equipo2']][6] += int(line['Goles1'])
                            dict_table[line['Equipo2']][6] = (3 *  int(dict_table[line['Equipo2']][1]) + int(dict_table[line['Equipo2']][2]) )

                csv_file.close()

            sortedVal = {k: v for k, v in sorted(dict_table.items(), key = lambda v: v[1][6])}
            sorted_list = []
            aux_sorted_list = []
            for element in reversed(sortedVal):
                sorted_list.append(sortedVal[element])
            for element in sortedVal:
                aux_sorted_list.append(sortedVal[element])

            print(str(len(list)), 'this is the len')
            if len(list) == 4:
                print("PASEEEEEEEEE2")
                top_condition = str(list[3])+str(list[4])
                top_condition = int(top_condition)
            elif len(list) == 3:
                print("PASSSSSSSSSSSSSSSSSSS")
                top_condition = int(list[2])
            elif len(list) == 2:
                print("PASEEEEEEEEE3")
                top_condition = 5

            if list[0] == 'SUPERIOR':
                message = 'El top superior de la temporada {} fue:\n'.format(list[1])
                var = 0
                print("Holaaaaa mundo")
                for i in sorted_list:
                    print("Holaaaaa 22mundo")
                    var += 1
                    if var <= top_condition:
                        print("Por aca ando")
                        message +='{}. {}\n'.format(var, i[7])
                        if var == top_condition:
                            break
                return message
            else:
                message = 'El top inferior de la temporada {} fue:\n'.format(list[1])
                var = 0
                for i in aux_sorted_list:
                    var += 1
                    if var <= top_condition:
                        message +='{}. {}\n'.format(var, i[7])
                        if var == top_condition:
                            break
                return message



        
        