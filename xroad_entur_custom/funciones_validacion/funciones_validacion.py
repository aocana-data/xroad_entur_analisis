
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

