.PHONY: format run build clean logs shell test

# Formatear código
format:
	@echo "🎨 Formatting code..."
	docker run --rm -v $(PWD):/app -w /app python:3.11-slim \
		sh -c "pip install black -q && black scraper.py"

# Ejecutar scraper
run:
	@echo "🚀 Running scraper..."
	docker-compose up

# Construir imagen
build:
	@echo "🔨 Building image..."
	docker-compose build

# Limpiar
clean:
	@echo "🧹 Cleaning up..."
	docker-compose down
	docker system prune -f

# Ver logs
logs:
	@echo "📋 Showing logs..."
	docker-compose logs -f

# Abrir shell en el contenedor
shell:
	@echo "🐚 Opening shell..."
	docker-compose run --rm scraper bash

# Ver resultados
results:
	@echo "📊 Results:"
	@cat data/output.json

# Ayuda
help:
	@echo "Available commands:"
	@echo "  make format   - Format Python code"
	@echo "  make run      - Run the scraper"
	@echo "  make build    - Build Docker image"
	@echo "  make clean    - Clean up Docker"
	@echo "  make logs     - Show logs"
	@echo "  make shell    - Open bash in container"
	@echo "  make results  - Show scraped data"