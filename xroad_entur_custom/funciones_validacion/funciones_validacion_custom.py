import re
from datetime import datetime

def validador_variables(cb):
    def wrapper(variable):
        regexp = '(-|\.|\+54)'
        
        if type(variable) != 'str':
            try:
                variable = str(variable)
            except:
                return TypeError

        if re.search(regexp,variable):
            variable = re.sub(regexp,'',variable)
            return cb(variable)

        return cb(variable)

    return wrapper


def validador_var(variable):
    regexp = '(-|\.|\+54)'
    
    variable = str(variable)

    if re.search(regexp,variable):
        variable = re.sub(regexp,'',variable)
        return variable

    return variable


def comprobando_uuid(variable):
    """
        Valida  Unique ID
    """    
    regexp = '.{36}'

    try:
        return True if re.search(regexp, variable) else False
    except:
        return False

def comprobando_lat_long(variable):
    
    reg_exp = '^-?[0-9]\d*(\.\d+)?$'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False


def comprobando_no_determinado(variable):
    reg_exp = '.+'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False
    

def comprobando_alfanumerico(variable):
    variable = variable.strip()
    reg_exp = '\w*\d+'   
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False
    

def comprobando_numeros_telefonicos(variable):
    if re.search('\.0+$',variable):
        variable = int(variable)

    reg_exp = "(^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$|\d{8,10})"
    try:
        if re.search(reg_exp,variable): return True
        else: return False
    except:
        return False


def comprobando_correo_valido(variable):
    variable = variable.strip()
    regexp = '^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$'
    try:
        return True if re.search(regexp,variable) else False
    except:
        return False

def comprobando_fecha_general(variable):
    
    variable = variable.strip()

    try:
        if datetime.strptime(variable, '%Y-%m-%d'):
            return True
    except:
        try:
            if datetime.strptime(variable, '%Y-%m-%d %H:%M:%S'): return True
        except:
            try:
                if datetime.strptime(variable, '%Y-%m-%d %H:%M:%S.%f'): return True
            except Exception as e:
                print(f'{e}\n{type(e)} : {type(e).__doc__}')
                return False


def comprobando_numeros(variable):
    """
    Valida numeros sin tener en cuenta la longitud de la misma
    """
    variable = variable.strip()
    reg_exp = "^[0-9]*$"
    if re.search(reg_exp, variable):
        return True
    else:
        return False


def comprobando_fechas_date(variable):
    """
    Valida fechas con el siguiente formato
    yyyy-mm-dd | dd-mm-yyyy | yy/mm/dd | dd/mm/yy
    
    1987/10/10  |   1987-10-10 
    19/10/1987  |   19-10-1987 
    
    """
    
    reg_exp = "(^((1[0-2]|0?[1-9]|.{2}))(\/|\-)(3[01]|[12][0-9]|0?[1-9])(\/|\-)(?:[0-9]{2})?[0-9]{2}$|^(?:[0-9]{2})?[0-9]{2}(\/|\-)(3[01]|[12][0-9]|0?[1-9])(\/|\-)((1[0-2]|0?[1-9])|.{2})$)"
    return True if re.search(reg_exp, variable) else False



def comprobando_strings(variable):
    """
    Valida palabra que empiecen
    con Letras del tipo Latin-1
    
    Ejemplo: Onómla
    
    No son válidos : [1hola , mateo!, @sarasa]
    """

    variable = variable.strip()
    reg_exp = "^[a-zA-ZÀ-ÿ\u00C0-\u017F]*$"

    return True if re.search(reg_exp, variable) else False


def comprobando_direcciones_completas(variable):    
    variable = variable.strip()
    reg_exp = "^[0-9a-zA-Z\u00C0-\u017F\s\.\,\-\d]*"
    return True if re.search(reg_exp, variable) else False
   

def comprobando_calles(variable):    
    variable = variable.strip()
    reg_exp = "^[a-zA-Z\u00C0-\u017F\s\.\d]*"
    
    return True if re.search(reg_exp, variable) else False


def comprobando_string_chars(variable):
    """
    Valida secuencia de palabras que empiecen
    con Letras del tipo Latin-1
    
    Ejemplo: [Marcela D'Marco , Śalim R++P ]
    
    No son válidos : [Śalim v+¿s¿' , mateo!, @sarasa .data]
    """

    variable = variable.strip()
    regexp = '^[a-zA-Z\u00C0-\u017F\s\/].*[a-zA-Z\u00C0-\u017F]$'
    
    return True if re.search(regexp,variable) else False

def comprobando_cp(variable):    
    variable = variable.strip()
    reg_exp = "^([a-zA-Z]{1}[0-9]{4}[a-zA-Z]{3}|[0-9]{4})$"
    
    return True if re.search(reg_exp, variable) else False

def comprobando_string_chars_especiales(variable):
    """
    Valida secuencia de palabras que empiecen
    con Letras del tipo Latin-1
    
    Ejemplo: [Marcela D'Marco 123 , 123-Valim ,sarasa123@asd qwerty]
    
    No son válidos : [Śalim v+¿s¿' , mateo! sd!]
    """
    
    variable = variable.strip()
    regexp = '^[0-9a-zA-Z\u00C0-\u017F\s\/\(\)].*[0-9a-zA-Z\u00C0-\u017F\(\)]$'
    
    return True if re.search(regexp,variable) else False

def comprobando_strings_numeros(variable):  
    variable = variable.strip()
    regexp = "^[0-9a-zA-Z\u00C0-\u017F\s\/].*[0-9a-zA-Z\u00C0-\u017F]$"
    return True if re.search(regexp,variable) else False


def comprobando_digitos_dni(variable):
    
    try:
        variable = int(variable.strip())
        variable = str(variable)

        reg_exp = "^[0-9]{7,8}$"
    
        return True if re.search(reg_exp, variable) else False
        
    except:
        return False

     
@validador_variables
def comprobando_telefonos(variable):
     
    try:
        variable = variable.strip()
        data = int(variable)
        data = str(data)
        reg_exp="^[0-9]{8,13}$"
        
        return True if re.search(reg_exp, data) else False
    except:
        return False


def comprobando_booleanos(variable):
    variable = variable.strip()
    if variable.isnumeric():
        variable = int(variable)
    boolean = [1,0,True,False]
    return variable in boolean 


def comprobando_genero(variable):
    variable = variable.strip()
    regexp = "(hombre|mujer|femenino|masculino|masc\.|fem\.|h|m|f)$"
    return True if re.search(regexp,variable,re.IGNORECASE) else False


def comprobando_carrera(variable):
    variable = variable.strip()
    regexp = "^[0-9a-zA-Z\u00C0-\u017F\s\/\(\)].*[0-9a-zA-Z\(\)]$"
    return True if re.search(regexp,variable,re.IGNORECASE) else False


def comprobando_nombres(variable):
    variable = variable.strip()
    regexp = '^([a-zñ\u00C0-\u017F]+ ?)*[a-zñ\u00C0-\u017F]+$'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_letras_3_o_menos(variable):
    regexp = '^[\w]{1,3}$'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_letras_y_numeros(variable):
    regexp = '[A-Z0-9]+'
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_tipos_bool_logicos(variable):
    regexp = "^(si|no|s|n|y)$"
    return True if re.search(regexp,variable,re.IGNORECASE) else False

def comprobando_decimales(variable):
    try:
        float(variable)
        return True
    except:
        return False
    
def cuit_cleaner(variable):
    """
    Limpieza de separadores si es que existan
    """
    
    SEP_CHARS = [".","-"," ","_"]
    
    for char_ in SEP_CHARS:
        if char_ in variable:
            return variable.replace(char_,"")
    
    return variable
    
    
def validador_cuit(cuit_cuil_validador):
    """
    validar que sea un tipo de dato cuit cuil
    para el territorio argentino
    """
    
    reg_exp = "^[2-3][0-9][0-9]{8}[a0-9]{1}$"
    return True if re.search(reg_exp, cuit_cuil_validador) else False


def verificador_modulo_ponderado(variable):
    """
    Fuente de construccion de CUIT
    https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Identificaci%C3%B3n_Tributaria
    
    Validador MODULO11
    https://es.wikipedia.org/wiki/C%C3%B3digo_de_control
    
    """
    BASE = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    ponderacion = [int(digito_cuit) * digito_ponderador for (digito_cuit, digito_ponderador) in zip(variable, BASE)]
    
    return  sum(ponderacion) % 11
    

def validador_digito(ponderacion):
    """
    Valida por el resultado de la ponderación
    """
   
    if ponderacion  == 10:  return  [9,4]
    if ponderacion  == 11:  return  [0]
    
    ponderacion = 11 - ponderacion
    
    return  [ponderacion]


def custom_comprobando_cuit_cuil(variable):
    
    
    if len(variable) == 0 or variable is None: return False
    
    variable_ = cuit_cleaner(variable)
    
    
    PERSONAS_FISICAS = [20, 23, 24, 25, 26 , 27 ]
    PERSONAS_JURIDICAS = [30, 33, 34 ]
    
    TIPO = variable_[:2]
    DNI = variable_[2:][:-1]
    DIGITO_VERIFICADOR = int(variable_[-1:])

    if not validador_cuit(variable_):
        return False
        
    ponderacion = verificador_modulo_ponderado(f"{TIPO}{DNI}")
    
    return DIGITO_VERIFICADOR in validador_digito(ponderacion)



def comprobando_numero_sade(variable):
    reg_exp = "\d-\d-\d-\d-\d"
    return True if re.search(reg_exp, variable) else False


def comprobando_piso_depto(variable):
    reg_exp = "^(\d|\w)+$"
    return True if re.search(reg_exp, variable) else False


def comprobando_celular(variable):
    reg_exp = "^(11|15)\d{8}$"
    return True if re.search(reg_exp, variable) else False


def comprobando_barrios(variable):
    BARRIOS_BUENOS_AIRES = ["Agronomía",
    "Almagro",
    "Balvanera",
    "Barracas",
    "Belgrano",
    "Boedo",
    "Caballito",
    "Chacarita",
    "Coghlan",
    "Colegiales",
    "Constitución",
    "Flores",
    "Floresta",
    "La Boca",
    "La Paternal",
    "Liniers",
    "Mataderos",
    "Monserrat",
    "Monte Castro",
    "Nueva Pompeya",
    "Núñez",
    "Palermo",
    "Parque Avellaneda",
    "Parque Chacabuco",
    "Parque Chas",
    "Parque Patricios",
    "Puerto Madero",
    "Recoleta",
    "Retiro",
    "Saavedra",
    "San Cristóbal",
    "San Nicolás",
    "San Telmo",
    "Vélez Sársfield",
    "Versalles",
    "Villa Crespo",
    "Villa del Parque",
    "Villa Devoto",
    "Villa General Mitre",
    "Villa Lugano",
    "Villa Luro",
    "Villa Ortúzar",
    "Villa Pueyrredón",
    "Villa Real",
    "Villa Riachuelo",
    "Villa Santa Rita",
    "Villa Soldati",
    "Villa Urquiza"]

    BARRIOS_POPULARES = ['Rodrigo Bueno', 'Saldías', 'Zavaleta', 'El Pueblito', 'Villa 26', 'El Campito', '19 de Octubre (Lamadrid)', 'Puente Barracas', 'Luján 2364', 'Lamadrid', 'Agustín de Vedia', 'Agustín Magaldi', 'Pedro de Mendoza', 'Villa 21-24', 'Villa 13 Bis', 'Padre Rodolfo Ricciardelli (Ex Villa 1-11-14)', 'Barrio Obrero', 'Barrio Inta', 'Calacita', 'Los Piletones', 'La Esperanza', 'Villa 15', 'Pirelli', 'Scapino', 'Barrio Fátima', 'Los Pinos', 'María Auxiliadora', 'Villa 20', 'Bermejo', 'Emáus','NHT del Trabajo', 'Ramón Carillo', 'Lacarra', 'Cildáñez', 'Nuestro Barrio', 'Playón de Chacarita', 'La Carbonilla', 'Jorge Newbery', 'La Rotonda', 'Santander', 'El Ombú', 'Pedro de Mendoza y Villarino', 'Matanza y Ferre', 'La Esquina', 'Playón de Caballito', 'Sin Nombre', 'La Veredita', 'Padre Mugica (Ex Villa 31 y 31 Bis)', 'Zanchetti', 'El Pescadito']
    
    BARRIOS_BUENOS_AIRES += BARRIOS_POPULARES
    
    BARRIOS_BUENOS_AIRES = [barrio.lower() for barrio in BARRIOS_BUENOS_AIRES]
    
    variable = variable.lower()
    
    return variable in BARRIOS_BUENOS_AIRES


def comprobando_comuna(variable):
    reg_exp = "comuna\s\d{1,2}$"
    return True if re.search(reg_exp, variable,re.IGNORECASE) else False