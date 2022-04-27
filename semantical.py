class semantical:

    def __init__(self):
        pass

    def reading(self, token_list):
        self.token_list = token_list

        for i in range(len(self.token_list)):
            if self.token_list[i].get_lexeme() == 'RESULTADO':
                return "Se mostrara el resultado"
            elif self.token_list[i].get_lexeme() == 'JORNADA':
                return "Se mostrara los resultados de una jornada"
            elif self.token_list[i].get_lexeme() == 'GOLES':
                return "Se mostrara la cantidad de goles en una temporada"
            elif self.token_list[i].get_lexeme() == 'TABLA':
                return "Se mostrara la tabla en una temporada"
            elif self.token_list[i].get_lexeme() == 'PARTIDOS':
                return "Se mostrara los resultados de un equipo en la temporada"
            elif self.token_list[i].get_lexeme() == 'TOP':
                return "Se mostrara el top"
            elif self.token_list[i].get_lexeme() == 'ADIOS':
                return "Se procedera a cerrar el programa"
        else:
                return 'No he logrado entender lo que me has dicho'

            