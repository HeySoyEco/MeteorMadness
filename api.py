import requests
import time  # para hacer una pequeña pausa entre peticiones


def obtener_neos(paginas=5):
    """
    Obtiene NEOs de la API de la NASA, recorriendo varias páginas.
    Parámetro 'paginas' controla cuántas páginas descargar.
    """
    lneos = []
    api_key = "Fh37Ayni8aK9FXjwlpPm06ym4UPLeMOcwaMAjZkA"

    try:
        for page in range(paginas):
            url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?page={page}&api_key={api_key}"
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()

            neos = datos.get("near_earth_objects", [])
            print(f"✅ Página {page + 1}: {len(neos)} asteroides obtenidos")

            for asteroid in neos:
                name = asteroid["name"]
                diameter = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
                hazardous = asteroid["is_potentially_hazardous_asteroid"]

                neo = {
                    "Nombre": name,
                    "Diametro (m)": diameter,
                    "Peligroso": hazardous
                }
                lneos.append(neo)

            # pequeña pausa para evitar saturar la API
            time.sleep(0.5)

        print(f"\nTotal de asteroides obtenidos: {len(lneos)}\n")
        return lneos

    except requests.exceptions.HTTPError:
        print(f"Error al obtener datos: {respuesta.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API. Verifica tu conexión.")
    except requests.exceptions.Timeout:
        print("Error: La solicitud tardó demasiado en responder.")
    except ValueError:
        print("Error: No se pudieron procesar los datos recibidos.")


def main():
    lista = obtener_neos(10)  # cambia este número para más páginas
    for i, neo in enumerate(lista, start=1):
        print(f"\nAsteroide {i}\n")
        for clave, valor in neo.items():
            print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
