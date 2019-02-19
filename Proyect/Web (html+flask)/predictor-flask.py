# coding=utf-8
from flask import Flask, redirect, url_for, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model/Venta_casas_model.sav', 'rb'))

#............................................................

@app.route('/', methods=['GET','POST'])
def Search(model=model):
    if request.method == 'GET':
        return render_template('index.html')
    else:
        var = [

        {'Duplex':0,
  	'Casa':1,
  	'Departamento':2},

 	{'Central': 8,
  	'Cerro-Argüello': 2,
 	'Este': 3,
  	'Guiñazú': 10,
  	'Nordeste': 9,
 	'Noroeste': 4,
  	'Norte': 6,
  	'Oeste': 7,
  	'Sudeste': 1,
  	'Sudoeste': 5,
  	'Sur': 0},

 	{'1 de Mayo': 251,
        '20 de Junio': 225,
        'Acosta': 160,
        'Alameda': 89,
        'Alberdi': 63,
        'Alberto': 212,
        'Alejandro Carbó': 255,
        'Alejandro Centeno': 116,
        'Alt. de San Martín': 24,
        'Alta Córdoba': 13,
        'Altamira': 121,
        'Alto Alberdi': 17,
        'Alto Palermo': 175,
        'Alto Verde': 21,
        'Altos de La Calera': 113,
        'Altos de Manantales': 58,
        'Altos de V. Sarsfield': 44,
        'Altos de Villa Cabrera': 95,
        'Altos del Chateau': 166,
        'Ameghino Sud': 185,
        'Amp. Pueyrredón': 238,
        'Amp. Res. America': 228,
        'Amp. las Palmas': 192,
        'Arguello': 5,
        'Arguello Norte': 180,
        'Avenida': 139,
        'Ayacucho': 31,
        'Bella Vista': 187,
        'Bialet Masse': 107,
        'Cabildo': 204,
        'Cabo Farina': 176,
        'Caseros': 236,
        'Cañitas': 57,
        'Cañuelas': 254,
        'Centenario': 152,
        'Centro': 105,
        'Centro America': 137,
        'Cerro Chico': 87,
        'Cerro Norte': 208,
        'Cerro de las Rosas': 55,
        'Cerveceros': 206,
        'Chacra del Norte': 12,
        'Chacra del Sur': 64,
        'Chacras de la Villa': 219,
        'Chateau Carreras': 110,
        'Cinco Lomas': 77,
        'Ciudadela': 217,
        'Claros del Bosque': 0,
        'Cofico': 20,
        'Colinas de V. Sarsfield': 36,
        'Colinas del Cerro': 132,
        'Colón': 134,
        'Comarca de Allende': 14,
        'Condor Alto': 199,
        'Condor Bajo': 241,
        'Crisol Norte': 127,
        'Crisol Sud': 47,
        'Cuatro Hojas': 145,
        'Cuesta Colorada': 98,
        'Dean Funes': 214,
        'Docta Urbanización Inteligente': 86,
        'Don Bosco': 104,
        'Ducasse': 243,
        'El Refugio': 99,
        'El Rodeo': 15,
        'El Trebol': 111,
        'Empalme': 96,
        'Escobar': 25,
        'Estancia Q2': 147,
        'Ferr. Mitre': 128,
        'Ferreyra': 191,
        'Fincas del Sur I': 146,
        'General Artigas': 258,
        'General Bustos': 61,
        'General Paz': 6,
        'General Pueyrredon': 103,
        'Golf': 74,
        'Granadero Pringles': 268,
        'Granja de Funes': 91,
        'Greenville': 174,
        'Greenville 2': 1,
        'Guemes': 68,
        'Hipolito Irigoyen': 201,
        'Hogar Propio': 271,
        'Horizonte': 32,
        'Inaudi': 133,
        'Industrial': 232,
        'Ipona': 126,
        'Irupe': 267,
        'Ituzaingo': 270,
        'Jardines del Jockey': 143,
        'Jardín': 33,
        'Jardín Claret': 67,
        'Jardín Espinosa': 29,
        'Jardín de los Boulevares': 164,
        'Jardín del Pilar': 130,
        'Jeronimo L. Cabrera': 227,
        'Jorge Newbery': 138,
        'José Hernandez': 222,
        'José Ignacio Díaz SE': 69,
        'Juan B. Justo': 260,
        'Juan XXIII': 71,
        'Juniors': 53,
        'Kennedy': 247,
        'La Carolina': 66,
        'La Catalina': 49,
        'La Cuesta': 23,
        'La Estanzuela': 118,
        'La France': 200,
        'La Herradura': 259,
        'La Morada': 136,
        'La Paloma': 73,
        'La Pankana': 161,
        'La Paya I': 81,
        'La Paya II': 39,
        'La Rufina': 173,
        'La Salle': 162,
        'Lamadrid': 210,
        'Las Dalias': 194,
        'Las Flores': 59,
        'Las Lilas': 211,
        'Las Magnolias': 168,
        'Las Margaritas': 196,
        'Las Palmas': 60,
        'Las Rosas': 92,
        'Liceo General Paz': 48,
        'Lomas Este': 34,
        'Lomas Oeste': 186,
        'Lomas de San Martín': 120,
        'Lomas de la Carolina': 248,
        'Lomas del Chateau ': 101,
        'Lomas del Suquía': 221,
        'Los Boulevares': 52,
        'Los Carolinos': 170,
        'Los Gigantes': 115,
        'Los Granados': 231,
        'Los Naranjos': 79,
        'Los Olmos': 195,
        'Los Olmos Sud': 215,
        'Los Paraisos': 189,
        'Los Platanos': 94,
        'Los Prados': 245,
        'Los Prados II': 216,
        'Los Robles': 183,
        'Maipu Sección 1': 90,
        'Maipu Sección 2': 2,
        'Manantiales': 4,
        'Marcos Sastre': 202,
        'Marechal': 252,
        'Mariano Balcarce': 262,
        'Mariano Fragueiro': 167,
        'Marq. de Sobremonte': 93,
        'Matienzo': 11,
        'Mirador': 224,
        'Miradores de Manantiales': 27,
        'Nueva Córdoba': 16,
        'Nueva Italia': 141,
        'Nuevo Poeta Lugones': 82,
        'Nuevo Urca': 106,
        'Observatorio': 124,
        'Olivos': 263,
        'Ona': 250,
        'Otro': 3,
        'Padre Claret': 144,
        'Palermo Bajo': 28,
        'Palmas de Claret': 18,
        'Panamericano': 119,
        'Parque Horizonte': 9,
        'Paso de los Andes': 78,
        'Patria': 239,
        'Patricios': 140,
        'Poeta Lugones': 42,
        'Pque. Atlantica': 142,
        'Pque. Capital': 148,
        'Pque. Capital Sud': 244,
        'Pque. Chacabuco': 72,
        'Pque. Corema': 108,
        'Pque. Don Bosco': 182,
        'Pque. Latino': 223,
        'Pque. Liceo I': 150,
        'Pque. Liceo II': 220,
        'Pque. Montecristo': 26,
        'Pque. República': 205,
        'Pque. San CARLOS': 193,
        'Pque. San Vicente': 197,
        'Pque. Velez Sarsfield': 41,
        'Pque. los Molinos': 114,
        'Prados de la Villa': 181,
        'Primera Junta': 203,
        'Providencia': 158,
        'Puente Blanco': 266,
        'Quebrada de las Rosas': 30,
        'Quinta Santa Ana': 178,
        'Quintas de Arguello': 50,
        'Ramón J. Carcano': 153,
        'Res. America': 171,
        'Res. Chateau Carreras': 70,
        'Res. San Carlos': 112,
        'Res. Santa Ana': 188,
        'Res. Santa Rosa': 97,
        'Res. Sud': 242,
        'Res. Velez Sarfield': 45,
        'Riberas de Manantiales': 83,
        'Rivadavia': 269,
        'Rivera Indarte': 149,
        'Rogelio Martinez': 62,
        'Rosedal': 122,
        'SMATA': 100,
        'SMATA II': 190,
        'San Alfonso': 40,
        'San Alfonso I': 237,
        'San Antonio': 249,
        'San Daniel': 159,
        'San Felipe': 265,
        'San Fernando': 84,
        'San Francisco': 117,
        'San Ignacio': 246,
        'San Isidro': 65,
        'San Javier': 234,
        'San José': 56,
        'San Lorenzo': 198,
        'San Martin': 75,
        'San Pablo': 154,
        'San Rafael': 169,
        'San Salvador': 54,
        'San Vicente': 135,
        'Santa Clara de Asis': 102,
        'Santa Isabel': 165,
        'Santa Rita': 129,
        'Santina Norte': 51,
        'Sargento Cabral': 218,
        'Sarmiento': 209,
        'Siete Soles': 80,
        'Solares de Santa María': 10,
        'Tablada Park': 46,
        'Talleres Este': 123,
        'Talleres Oeste': 151,
        'Talleres Sud': 240,
        'Tejas 3': 35,
        'Tejas del Sur I': 38,
        'Tejas del Sur II': 43,
        'Teniente Benj. Matienzo': 253,
        'Terranova': 156,
        'Terrazas de La Estanzuela': 131,
        'UOCRA': 157,
        'Urca': 7,
        'Urquiza': 257,
        'Valle Escondido': 37,
        'Valle del Sol': 179,
        'Villa Adela': 261,
        'Villa Alberdi': 235,
        'Villa Allende Parque': 155,
        'Villa Argentina': 88,
        'Villa Azalais': 229,
        'Villa Belgrano': 22,
        'Villa Cabrera': 85,
        'Villa Corina': 230,
        'Villa Coronel Olmedo': 177,
        'Villa Esquiu': 172,
        'Villa Gran Parque': 226,
        'Villa Marta': 76,
        'Villa Quizquizacate': 213,
        'Villa Revol': 256,
        'Villa Rivera Indarte': 109,
        'Villa Warcalde': 19,
        'Villa el Libertador': 184,
        'Villa los Angeles': 233,
        'Yapeyu': 163,
        'Yofre I': 264,
        'Yofre Norte': 207,
        'Yofre Sud': 125,
        'Zumaran': 8},
       	
	{'Abierto': 2, 
        'Cerrado': 0, 
        'Con Seguridad': 1, 
        'Country': 3},]

        propiedad = int(var[0][request.form['propiedad']])
        zona = int(var[1][request.form['zona']])
        barrio = int(var[2][request.form['barrio']])
        tipobarrio = int(var[3][request.form['tipobarrio']])
        dormitorios = int(request.form['dormitorios'])
        banios = int(request.form['banios'])
        mst2C = float(request.form['mst2C'])
        mst2T = float(request.form['mst2T'])
  
        col = ['Tipo de Propiedad', 'Zona', 'Barrio', 'Tipo de Barrio',
         'Cantidad de Dormitorios', 'Cantidad de Baños',
         'Superficie Cubierta m2', 'Superficie Total m2',
         'Superficie Cubierta m2_was_missing', 'Superficie Total m2_was_missing',
         'Cantidad de Dormitorios_was_missing', 'Cantidad de Baños_was_missing',
         'Zona_was_missing', 'Barrio_was_missing', 'Tipo de Barrio_was_missing']
  
        row =[[propiedad,zona,barrio,
              tipobarrio,dormitorios,
              banios,mst2C,mst2T,
              False,False,False,False,False,False,False]]
   
        inp = pd.DataFrame(row, columns=col)
        	
        predict = "U$S {:,.2f}".format( int(model.predict(inp)[0]) )
  
        return render_template('index.html', _anchor="search", result=predict)

#............................................................

if __name__ == '__main__':
    app.run(debug = True)