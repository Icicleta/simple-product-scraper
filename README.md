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