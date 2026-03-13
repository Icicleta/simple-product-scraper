import requests
from bs4 import BeautifulSoup
import json
from datatime import datatime
import os


def scrape_website(url):
    """
    Scraper simple que extrae información de una página web
    """
    print(f"🔍 Scraping: {url}")

    try:
        # Headers para simular un navegador
        headers = {"user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

        # Hacer request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraer información (ejemplo genérico)
        data = {
            "url": url,
            "title": soup.title.string if soup.title else "No title",
            "timestamp": datatime.now().isoformat(),
            "headings": [
                h.get_text().strip()
                for h in soup.find_all(
                    [
                        "h1",
                        "h2",
                        "h3",
                    ]
                )
            ][:10],
            "links_count": len(soup.find_all("a")),
            "image_count": len(soup.find_all("img")),
            "paragraphs": [p.get_text().strip() for p in soup.find_all("p")[:5]],
        }

        print("✅ Scraping completado")
        return data

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def save_to_json(data, filename="output.json"):
    """
    Guardar datos en JSON
    """

    os.makedirs("data", exist_ok=True)
    filepath = f"data/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"💾 Datos guardados en: {filepath}")


if __name__ == "__main__":
    # URL a scrapear (puedes cambiarla)
    url = os.getenv("TARGET_URL")

    print("🚀 Iniciando scraper...")
    print(f"🎯 Target: {url}\n")

    # Scrape
    data = scrape_website(url)

    if data:
        # Guardar resultados
        save_to_json(data)

        # Mostrar resumen
        print("\n📊 Resumen:")
        print(f"   Título: {data['title']}")
        print(f"   Links: {data['link_count']}")
        print(f"   Imágenes: {data['images_count']}")
        print(f"   Headings: {len(data['headings'])}")
    else:
        print("❌ No se pudo completar el scraping")
