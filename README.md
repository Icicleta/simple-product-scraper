# Web Scraper with Python and Docker 🕷️

Simple web scraper for learning Docker and BeautifulSoup.

## Features

- 🐳 Fully Dockerized
- 📦 Easy setup
- 💾 JSON output
- 🔄 Live code reload

## Quick Start
```bash
# Clone and run
git clone https://github.com/Icicleta/simple-product-scraper.git
cd simple-product-scraper
docker-compose up --build

# View results
cat data/output.json
```

## 🔧 Using Make Commands

This project includes a Makefile for common tasks:
```bash
# Format code with Black
make format

# Run the scraper
make run

# Build Docker image
make build

# Clean up Docker containers and images
make clean

# Show available commands
make help
```

### Available Commands

- `make format` - Format Python code using Black
- `make run` - Run the scraper with docker-compose
- `make build` - Build the Docker image
- `make clean` - Remove containers and clean Docker system
- `make help` - Display available commands

**Note:** `make format` requires Docker and will install Black temporarily in a container.

## Usage
```bash
# Custom URL
docker-compose run --rm -e TARGET_URL=https://example.com scraper

# Without Docker
pip install -r requirements.txt
python scraper.py
```

## Configuration

Change URL in `docker-compose.yml`:
```yaml
environment:
  - TARGET_URL=https://your-site.com
```

## Development

Edit `scraper.py` and run again (no rebuild needed):
```bash
docker-compose up
```

## Output Format
```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "headings": ["Example Domain"],
  "links_count": 1
}
```

## Cleanup
```bash
docker-compose down
docker system prune -f
```

## Legal

⚠️ Respect robots.txt and terms of service. Educational purposes only.

## License

MIT - see [LICENSE](LICENSE)
