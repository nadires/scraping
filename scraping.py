import re 
import requests
from bs4 import BeautifulSoup

website = "https://www.bna.com.ar/home/informacionalusuariofinanciero"
resultado = requests.get(website)
html_content = resultado.text


# Parsear el contenido HTML
soup = BeautifulSoup(html_content, "html.parser")

# Buscar el contenido dentro de las etiquetas <li> que contiene la tasa
li_tags = soup.find_all("li")
#print(li_tags)
# Buscar el <li> que comience con "Tasa Efectiva Mensual Vencida"
valor=0
for li in li_tags:
    if li.text.startswith("Tasa Efectiva Mensual Vencida"):
        # Imprimir todo el contenido del <li>
        print(f"Contenido del <li>: {li.text}")

         # Expresión regular para extraer el valor después del último igual
        pattern = r"=\s*([\d,.]+)%"
        match = re.search(pattern, li.text)
        
        if match:
            valor = match.group()
            print("El valor específico es:"+valor)
        break

print("aqui la variable"+valor)





# Expresión regular para encontrar la T.E.M. (30 días)
#pattern = r"T\.E\.M\.\s*\(30\s*días\)\s*=\s*([\d,]+\.\d+)%"
#pattern = r"Tasa Efectiva Mensual Vencida"
#print(pattern)
#lis= re.findall(pattern,str(li_tags))
#print(lis)


#for li in li_tags:
    
 #   match = re.findall(pattern, str(li.text))
  #  print(match)
    #if match:
     #   final= match.group()
      #  print(final)


# Recorrer las etiquetas <li> y aplicar la expresión regular
#for li in li_tags:
#    match = re.search(pattern, li.text)
#    if match:
#        tem_value = match.group(1)
#        print(f"Tasa Efectiva Mensual Vencida (30 días): {tem_value}%")
#        break
