from ftplib import B_CRLF
from re import S
from token_list import Token
from token_list import Error

class lexical_analyzer:
    
    def __init__(self):
        self.token_list = []
        self.error_list = []
        self.semantic_error_list = []
        self.entry_text = ""

    def analyzer(self, text: str):
        text += "#"
        state = 0
        line = 1
        column = 1
        new_word = ''

        print(text)

        #BEGIN: List of words:
        
        #Begin: RESULTADO
        r_resultado = False
        e_resultado = False
        s_resultado = False
        u_resultado = False
        l_resultado = False
        t_resultado = False
        a_resultado = False
        d_resultado = False
        #END: RESULTADO

        #Begin: VS
        v_vs = False
        #END: VS
        
        #Begin: TEMPORADA
        t_temporada = False
        e_temporada = False
        m_temporada = False
        p_temporada = False
        o_temporada = False
        r_temporada = False
        a_temporada = False
        d_temporada = False
        #END: TEMPORADA

        #Begin: JORNADA
        j_jornada = False
        o_jornada = False
        r_jornada = False
        n_jornada = False
        a_jornada = False
        d_jornada = False
        #END JORNADA

        #Begin: GOLES
        g_goles = False
        o_goles = False
        l_goles = False
        e_goles = False
        #END: GOLES

        #Begin: LOCAL
        l_local = False
        o_local = False
        c_local = False
        a_local = False
        #END: LOCAL

        #Begin: VISITANTE
        i_visitante = False
        s_visitante = False
        i_visitante2 = False
        t_visitante = False
        a_visitante = False
        n_visitante = False
        t_visitante2 = False
        #END VISITANTE

        #Begin: TOTAL
        t_total = False
        a_total = False
        #END: TOTAL

        #Begin: TABLA
        a_tabla = False
        b_tabla = False
        l_tabla = False
        #END: TABLA

        #Begin: PARTIDOS
        p_partidos = False
        a_partidos = False
        r_partidos = False
        t_partidos = False
        i_partidos = False
        d_partidos = False
        o_partidos = False
        #END: PARTIDOS

        #Begin: TOP
        t_top = False
        o_top = False
        #END: TOP

        #Begin: SUPERIOR
        s_superior = False
        u_superior = False
        p_superior = False
        e_superior = False
        r_superior = False
        i_superior = False
        o_superior = False
        #END:SUPERIOR

        #Begin: INFERIOR
        i_inferior = False
        n_inferior = False
        f_inferior = False
        e_inferior = False
        r_inferior = False
        i_inferior = False
        o_inferior = False
        #END: INFERIOR

        #Begin: ADIOS
        a_adios= False
        d_adios= False
        i_adios= False
        o_adios= False
        #END:ADIOS

        #END: List of words:

        for char in range(len(text)):
            letter = text[char]

            if letter ==  '#':
                print("Se ha terminado la lectura")
                break

            if letter==" ":
                column+=1
                continue
                
            if letter=="\n":
                line+=1
                column=0
                continue
            
            column+=1
            

            if state == 0:

                #R -> RESULTADO
                if letter == 'R':
                    r_resultado = True
                    state = 1
                    new_word += letter

                #V -> VS | VISITANTE
                elif letter == 'V':
                    v_vs = True
                    v_visitante = True
                    state = 1
                    new_word += letter

                #T -> TEMPORADA | TABLA | TOTAL | TOP
                elif letter == 'T':
                    t_temporada = True
                    t_tabla = True
                    t_total = True
                    t_top = True
                    state = 1
                    new_word += letter
                
                #J -> JORNADA
                elif letter == 'J':
                    j_jornada = True
                    state = 1
                    new_word += letter

                #G -> GOLES
                elif letter == 'G':
                    g_goles = True
                    state = 1
                    new_word += letter

                #L _> LOCAL
                elif letter == 'L':
                    l_local = True
                    state = 1
                    new_word += letter
                
                #P -> PARTIDOS
                elif letter == 'P':
                    p_partidos = True
                    state = 1
                    new_word += letter
                
                #S -> SUPERIOR
                elif letter == 'S':
                    s_superior = True
                    state = 1
                    new_word += letter

                #I -> INFERIOR
                elif letter == 'I':
                    i_inferior = True
                    state = 1
                    new_word += letter

                # A -> ADIOS
                elif letter == 'A':
                    a_adios = True
                    state = 1
                    new_word += letter
                else:
                    print("No se reconociokahkjhfadskhfdasjkhfsdjkahsadfjk")

            elif state == 1:
    
                #RE -> RESULTADO
                if r_resultado:
                    if letter == 'E':
                        e_resultado = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VS -> VS | VI -> VISITANTE
                elif v_vs:
                    if letter == 'S':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        v_vs = False
                        state=0
                    elif letter == 'I':
                        i_visitante= True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TE -> TEMPORADA |TA -> TABLA |TO -> TOTAL | TOP
                elif t_temporada:
                    if letter == 'E':
                        e_temporada = True
                        new_word += letter
                        state = 2
                    elif letter == 'A':
                        a_tabla = True
                        new_word += letter
                        state = 2
                    elif letter == 'O':
                        o_top == True
                        new_word += letter
                        state = 2
                    else: 
                        new_word = ""
                        t_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #JO -> JORNADA
                elif j_jornada:
                    if letter == 'O':
                        o_jornada = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        j_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #GO -> GOLES
                elif g_goles:
                    if letter == 'O':
                        o_goles = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        g_goles = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #LO _> LOCAL
                elif l_local:
                    if letter == 'O':
                        o_local = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        l_local = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PA -> PARTIDOS
                elif p_partidos:
                    if letter == 'A':
                        a_partidos = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SU -> SUPERIOR
                elif s_superior:
                    if letter == 'U':
                        u_superior = True
                        state = 2
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #I -> INFERIOR
                elif i_inferior:
                    if letter == 'N':
                        n_inferior = True
                        state = 2
                    else:
                        new_word = ""
                        i_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                # A -> ADIOS
                elif a_adios:
                    if letter == 'D':
                        d_adios = True
                        state = 2
                    else:
                        new_word = ""
                        a_adios = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 2:
        
                #RES -> RESULTADO
                if e_resultado:
                    if letter == 'S':
                        s_resultado = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VIS -> VISITANTE
                elif i_visitante:
                    if letter == 'S':
                        s_visitante= True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEM -> TEMPORADA |TAB -> TABLA |TOT -> TOTAL |TOP ->TOP
                elif e_temporada:
                    if letter == 'M':
                        m_temporada = True
                        new_word += letter
                        state = 3
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                elif a_tabla:
                    if letter == 'B':
                        b_tabla = True
                        new_word += letter
                        state = 3
                    else: 
                        new_word = ""
                        t_temporada = False
                        a_tabla = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                elif o_top:
                    if letter == 'P':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        state=0
                    if letter == 'T':
                        t_total = True
                        new_word += letter
                        state = 3
                    else: 
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                
                #JOR -> JORNADA
                elif o_jornada:
                    if letter == 'R':
                        r_jornada = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #GOL -> GOLES
                elif o_goles:
                    if letter == 'L':
                        l_goles = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        g_goles = False
                        o_goles = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #LOC _> LOCAL
                elif o_local:
                    if letter == 'O':
                        c_local = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        l_local = False
                        o_local = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PAR -> PARTIDOS
                elif a_partidos:
                    if letter == 'R':
                        r_partidos = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUP -> SUPERIOR
                elif u_superior:
                    if letter == 'P':
                        p_superior = True
                        state = 3
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INF -> INFERIOR
                elif n_inferior:
                    if letter == 'F':
                        f_inferior = True
                        state = 3
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                # ADI -> ADIOS
                elif d_adios:
                    if letter == 'I':
                        i_adios = True
                        state = 3
                    else:
                        new_word = ""
                        a_adios = False
                        d_adios = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 3:
            
                #RESU -> RESULTADO
                if s_resultado:
                    if letter == 'U':
                        u_resultado = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISI -> VISITANTE
                elif s_visitante:
                    if letter == 'I':
                        i_visitante2= True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEMP -> TEMPORADA |TABL -> TABLA |TOT -> TOTAL 
                elif m_temporada:
                    if letter == 'P':
                        p_temporada = True
                        new_word += letter
                        state = 4
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                elif b_tabla:
                    if letter == 'L':
                        l_tabla = True
                        new_word += letter
                        state = 4
                    else: 
                        new_word = ""
                        t_temporada = False
                        a_tabla = False
                        b_tabla = False
                        error = Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0   

                elif t_total:
                    if letter == 'A':
                        a_total= True
                        new_word += letter
                        state = 4
                    else: 
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        t_total = False
                        error = Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0  

                #JORN -> JORNADA
                elif r_jornada:
                    if letter == 'N':
                        n_jornada = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        r_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #GOLE -> GOLES
                elif l_goles:
                    if letter == 'E':
                        e_goles = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        g_goles = False
                        o_goles = False
                        l_goles = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #LOCA _> LOCAL
                elif c_local:
                    if letter == 'A':
                        a_local = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        l_local = False
                        o_local = False
                        c_local = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PART -> PARTIDOS
                elif r_partidos:
                    if letter == 'T':
                        t_partidos = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUPE -> SUPERIOR
                elif p_superior:
                    if letter == 'E':
                        e_superior = True
                        state = 4
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INFE -> INFERIOR
                elif f_inferior:
                    if letter == 'E':
                        f_inferior = True
                        state = 4
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                # ADIO -> ADIOS
                elif i_adios:
                    if letter == 'O':
                        o_adios = True
                        state = 4
                    else:
                        new_word = ""
                        a_adios = False
                        d_adios = False
                        i_adios = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 4:
                
                #RESUL -> RESULTADO
                if u_resultado:
                    if letter == 'L':
                        l_resultado = True
                        state = 5
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISITA -> VISITANTE
                elif i_visitante2:
                    if letter == 'T':
                        t_visitante= True
                        state = 5
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEMPO -> TEMPORADA |TABLA -> TABLA |TOTAL -> TOTAL 
                elif p_temporada:
                    if letter == 'O':
                        o_temporada = True
                        new_word += letter
                        state = 5
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        p_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                elif l_tabla:
                    if letter == 'A':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        b_tabla = False
                        l_tabla = False
                        state=0
                    else: 
                        new_word = ""
                        t_temporada = False
                        a_tabla = False
                        b_tabla = False
                        l_tabla = False
                        error = Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0   

                elif a_total:
                    if letter == 'L':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        t_total = False
                        a_total = False
                        state=0
                    else: 
                        new_word = ""
                        t_temporada = False
                        o_top = False
                        t_total = False
                        a_total = False
                        error = Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0  

                #JORNA -> JORNADA
                elif n_jornada:
                    if letter == 'A':
                        a_jornada = True
                        state = 5
                        new_word += letter
                    else:
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        r_jornada = False
                        n_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #GOLES -> GOLES
                elif e_goles:
                    if letter == 'S':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        g_goles = False
                        o_goles = False
                        l_goles = False
                        e_goles = False
                        state=0
                    else:
                        new_word = ""
                        g_goles = False
                        o_goles = False
                        l_goles = False
                        e_goles = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #LOCAL _> LOCAL
                elif a_local:
                    if letter == 'L':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        l_local = False
                        o_local = False
                        c_local = False
                        a_local = False
                        state=0
                    else:
                        new_word = ""
                        l_local = False
                        o_local = False
                        c_local = False
                        a_local = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PARTI -> PARTIDOS
                elif t_partidos:
                    if letter == 'I':
                        i_partidos = True
                        state = 5
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        t_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUPER -> SUPERIOR
                elif e_superior:
                    if letter == 'R':
                        r_superior = True
                        state = 5
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        e_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INFER -> INFERIOR
                elif e_inferior:
                    if letter == 'R':
                        r_inferior = True
                        state = 5
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        e_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                # ADIOS -> ADIOS
                elif o_adios:
                    if letter == 'S':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        a_adios = False
                        d_adios = False
                        i_adios = False
                        o_adios = False
                        state=0
                    else:
                        new_word = ""
                        a_adios = False
                        d_adios = False
                        i_adios = False
                        o_adios = False 
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 5:
                
                #RESULT -> RESULTADO
                if l_resultado:
                    if letter == 'T':
                        a_resultado = True
                        state = 6
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        l_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISITA -> VISITANTE
                elif t_visitante:
                    if letter == 'A':
                        a_visitante= True
                        state = 6
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        t_visitante = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEMPOR -> TEMPORADA 
                elif o_temporada:
                    if letter == 'R':
                        a_temporada = True
                        new_word += letter
                        state = 6
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        p_temporada = False
                        o_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #JORNAD -> JORNADA
                elif a_jornada:
                    if letter == 'D':
                        d_jornada = True
                        state = 6
                        new_word += letter
                    else:
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        r_jornada = False
                        n_jornada = False
                        a_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PARTID -> PARTIDOS
                elif i_partidos:
                    if letter == 'D':
                        d_partidos = True
                        state = 6
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        t_partidos = False
                        i_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUPERI -> SUPERIOR
                elif r_superior:
                    if letter == 'I':
                        i_superior = True
                        state = 6
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        e_superior = False
                        r_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INFERI -> INFERIOR
                elif r_inferior:
                    if letter == 'I':
                        r_inferior = True
                        state = 6
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        e_inferior = False
                        r_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 6:
                
                #RESULTA -> RESULTADO
                if t_resultado:
                    if letter == 'A':
                        a_resultado = True
                        state = 7
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        l_resultado = False
                        t_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISITA -> VISITANTE
                elif a_visitante:
                    if letter == 'N':
                        n_visitante= True
                        state = 7
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        t_visitante = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEMPORA -> TEMPORADA 
                elif r_temporada:
                    if letter == 'A':
                        a_temporada = True
                        new_word += letter
                        state = 7
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        p_temporada = False
                        o_temporada = False
                        r_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #JORNADA -> JORNADA
                elif d_jornada:
                    if letter == 'A':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        r_jornada = False
                        n_jornada = False
                        a_jornada = False
                        d_jornada = False
                        state=0
                    else:
                        new_word = ""
                        j_jornada = False
                        o_jornada = False
                        r_jornada = False
                        n_jornada = False
                        a_jornada = False
                        d_jornada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PARTIDO -> PARTIDOS
                elif d_partidos:
                    if letter == 'O':
                        o_partidos = True
                        state = 7
                        new_word += letter
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        t_partidos = False
                        i_partidos = False
                        d_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUPERIO -> SUPERIOR
                elif i_superior:
                    if letter == 'O':
                        o_superior = True
                        state = 7
                        new_word += letter
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        e_superior = False
                        r_superior = False
                        i_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INFERIO -> INFERIOR
                elif i_inferior:
                    if letter == 'O':
                        o_inferior = True
                        state = 7
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        e_inferior = False
                        r_inferior = False
                        i_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 7:
                
                #RESULTAD -> RESULTADO
                if a_resultado:
                    if letter == 'D':
                        d_resultado = True
                        state = 8
                        new_word += letter
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        l_resultado = False
                        t_resultado = False
                        a_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISITANT -> VISITANTE
                elif n_visitante:
                    if letter == 'T':
                        t_visitante2= True
                        state = 8
                        new_word += letter
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        t_visitante = False
                        a_visitante = False
                        n_visitante = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                        
                #TEMPORADA -> TEMPORADA 
                elif d_temporada:
                    if letter == 'A':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        p_temporada = False
                        o_temporada = False
                        r_temporada = False
                        d_temporada = False
                        state=0
                    else: 
                        new_word = ""
                        t_temporada = False
                        e_temporada = False
                        m_temporada = False
                        p_temporada = False
                        o_temporada = False
                        r_temporada = False
                        d_temporada = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #PARTIDOS -> PARTIDOS
                elif o_partidos:
                    if letter == 'S':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        t_partidos = False
                        i_partidos = False
                        d_partidos = False
                        o_partidos = False
                        state=0
                    else:
                        new_word = ""
                        p_partidos = False
                        a_partidos = False
                        r_partidos = False
                        t_partidos = False
                        i_partidos = False
                        d_partidos = False
                        o_partidos = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                
                #SUPERIOR -> SUPERIOR
                elif o_superior:
                    if letter == 'R':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        e_superior = False
                        r_superior = False
                        i_superior = False
                        o_superior = False
                        state=0
                    else:
                        new_word = ""
                        s_superior = False
                        u_superior = False
                        p_superior = False
                        e_superior = False
                        r_superior = False
                        i_superior = False
                        o_superior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

                #INFERIOR -> INFERIOR
                elif o_inferior:
                    if letter == 'R':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        e_inferior = False
                        r_inferior = False
                        i_inferior = False
                        o_inferior = False
                        state=0
                    else:
                        new_word = ""
                        i_inferior = False
                        n_inferior = False
                        f_inferior = False
                        e_inferior = False
                        r_inferior = False
                        i_inferior = False
                        o_inferior = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

            elif state == 8:
                
                #RESULTADO -> RESULTADO
                if d_resultado:
                    if letter == 'O':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        l_resultado = False
                        t_resultado = False
                        a_resultado = False
                        d_resultado = False
                        state = 0
                    else:
                        new_word = ""
                        r_resultado = False
                        e_resultado = False
                        s_resultado = False
                        u_resultado = False
                        l_resultado = False
                        t_resultado = False
                        a_resultado = False
                        d_resultado = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0
                        

                #VISITANTE -> VISITANTE
                elif t_visitante2:
                    if letter == 'E':
                        new_word += letter
                        token = Token("Palabra Reservada",new_word, line, column)
                        self.token_list.append(token)
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        t_visitante = False
                        a_visitante = False
                        n_visitante = False
                        t_visitante2 = False
                        state=0
                    else:
                        new_word = ""
                        v_vs = False
                        i_visitante = False
                        s_visitante = False
                        i_visitante2 = False
                        t_visitante = False
                        a_visitante = False
                        n_visitante = False
                        t_visitante2 = False
                        error=Error("Entrada incorrecta: {} -> {}".format(new_word, letter),"No se identifico la palabra reservada",line,column)
                        self.error_list.append(error)
                        state = 0

    def clean(self):
        self.token_list = []
        self.errror_list = []
        self.semantic_error_list = []
