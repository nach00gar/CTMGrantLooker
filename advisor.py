import requests
from bs4 import BeautifulSoup
from datetime import date

def consulta(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titulo = soup.find(class_='views-field views-field-titulo-formal block')
    estado = soup.find(class_='views-field views-field-estado-plazo block')
    fecha = soup.find(class_='views-field views-field-fecha-actualizacion block')
    return titulo.text + "  " + estado.text + " " + fecha.text

junta = ["https://www.juntadeandalucia.es/servicios/sede/tramites/procedimientos/detalle/8701.html", "https://www.juntadeandalucia.es/servicios/sede/tramites/procedimientos/detalle/22597.html", "https://www.juntadeandalucia.es/servicios/sede/tramites/procedimientos/detalle/13755.html"]

if __name__ == "__main__":
    resultados=[]
    resultados.append("Consultado a día de hoy : "+ str(date.today()))
    for enlace in junta:
        resultados.append(consulta(enlace))
    response = requests.get("https://www.dipgra.es/ayudas/")
    soup = BeautifulSoup(response.text, 'html.parser')
    resultado = soup.find(class_='resultados_otros_tipos_contenidos')
    resultados.append("Estas son las últimas convocatorias de la Diputación: ")
    for a in resultado.find_all(class_='tdTitulo'):
        resultados.append(a.text)
    print(resultados)
    with open("results.txt", "a") as f:
        f.write('<head> <meta charset="UTF-8"> </head>')
        for a in resultados:
            f.write("<p>")
            f.write(a.replace("\n", "<br>\n"))
            f.write("</p>")
    
