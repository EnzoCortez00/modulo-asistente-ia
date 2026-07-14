import os
import requests
from dotenv import load_dotenv

# 1. Cargar las variables de entorno desde el archivo .env
load_dotenv()

def obtener_clima_actual():
    """
    Se conecta a la API del clima y devuelve un mensaje para el profesor.
    Ideal para alertar sobre tormentas que afecten la asistencia.
    """
    # 2. Leer las credenciales de forma segura
    api_key = os.getenv("WEATHER_API_KEY")
    ciudad = os.getenv("CIUDAD_POR_DEFECTO", "Mendoza")
    
    # Validar que la API Key exista (Buena práctica de seguridad)
    if not api_key:
        return "Error: No se encontró la API Key en el archivo .env"

    # 3. URL de la API del clima (usamos OpenWeatherMap como ejemplo)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        # 4. Realizar la petición HTTP usando 'requests'
        respuesta = requests.get(url)
        
        # Simulamos la respuesta exitosa para el prototipo
        # En la vida real haríamos: datos = respuesta.json()
        temperatura_simulada = 18.5
        condicion_simulada = "cielo claro"
        
        mensaje = f"🌤️ Clima en {ciudad} para la clase de hoy: {temperatura_simulada}°C, {condicion_simulada}."
        return mensaje

    except Exception as e:
        return f"Error al conectar con la API del Clima: {e}"

# Bloque de prueba (solo se ejecuta si corremos este archivo directamente)
if __name__ == "__main__":
    print("Iniciando prueba del Módulo Asistente IA...")
    resultado = obtener_clima_actual()
    print(resultado)