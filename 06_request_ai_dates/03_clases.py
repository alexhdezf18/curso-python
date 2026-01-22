# 1. Introduccion a las clases de Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia
# de una clases 

# Nos permite agrupar datos (atributos o propiedades) y funciones (metodos)
#en un solo lugar


# Ejemplo basico de una clases
class Coche:
    # atributo de la clase(comparte todas las instancias)
    tipo = "Vehiculo de cuatro ruedas"
    ruedas = 4

    # metodo especial que es el que construye el objeto
    #se llama automaticamente en este metodo cuando creas la instancia
    def __init__(self, marca, modelo, color):
         # atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arranco")
    
mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()

coche_de_pheralb = Coche("Ford", "Fiesta", "azul")
coche_de_pheralb.arrancar()

# Encapsulacion:  es oculatar los detalles interno de una clase y exponer
# solo la interfaz publica

# Crear una clase para llamar a la AI de OpenAi, DeepSeek o LO QUE SEA
import requests

OPENAI_KEY = ""
DEEPSEEK_KEY = ""

class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self._url = url
        self.model = model
    
    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")
openai_api.call("Escibe un poema sobre la programacion")


print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")
deepseek_api.call("Escibe un poema sobre la programacion")