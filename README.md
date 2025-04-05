# DropchipAi

DropchipAi ist eine KI-gestützte Dropshipping-Automatisierungslösung, die E-Commerce-Prozesse über Plattformen wie Shopify und eBay optimiert.

## Überblick

DropchipAi kombiniert künstliche Intelligenz mit E-Commerce-Automatisierung, um den zeitaufwändigen Prozess des Produktfindens, Listens und Verkaufens über verschiedene Plattformen hinweg zu vereinfachen und zu optimieren.

### Hauptfunktionen

- **Automatisierte Produktrecherche**: Identifizierung von rentablen Produkten durch Marktanalyse und Google Trends
- **Lieferantenauswahl**: Bewertung und Auswahl der besten Lieferanten für diese Produkte
- **Content-Erstellung**: Automatische Generierung von Produktbeschreibungen und Listings
- **Multi-Channel-Vertrieb**: Gleichzeitiges Listing auf verschiedenen Plattformen (Shopify, eBay)
- **Preisoptimierung**: Vergleich und Optimierung der Preise für maximalen Gewinn
- **Prozessautomatisierung**: Reduzierung des manuellen Aufwands im Dropshipping-Prozess

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python-Paketmanager)
- Shopify-Konto (für Shopify-Integration)
- eBay-Entwicklerkonto (für eBay-Integration)

### Installationsschritte

1. Repository klonen:
   ```bash
   git clone https://github.com/yourusername/DropchipAi.git
   cd DropchipAi
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. Konfigurationsdatei erstellen:
   Erstellen Sie eine Datei `config/credentials.yaml` mit Ihren API-Schlüsseln:
   ```yaml
   shopify:
     shop_url: "your-store.myshopify.com"
     api_key: "your_api_key"
     password: "your_password"

   ebay:
     app_id: "your_app_id"
     dev_id: "your_dev_id"
     cert_id: "your_cert_id"
     auth_token: "your_auth_token"
     sandbox_mode: true  # Auf false setzen für Produktionsumgebung
   ```

## Verwendung

### Grundlegende Verwendung

```python
from src.core import DropchipCore

# DropchipCore initialisieren
core = DropchipCore()

# Vollständige Automatisierung durchführen
results = core.full_automation(["Smart Watch", "Wireless Earbuds"])
print(f"{len(results)} Produkte wurden verarbeitet")
```

### Nur Produktrecherche

```python
from src.ai.product_research import ProductResearch

# ProductResearch initialisieren
research = ProductResearch()

# Trendige Produkte finden
trending_products = research.find_trending_products(["Smart Watch", "Wireless Earbuds"])

# Profitable Produkte finden
profitable_products = research.find_profitable_products(trending_products)

# Vollständige Produktrecherche durchführen
results = research.full_product_research(["Smart Watch", "Wireless Earbuds"])
```

### Lieferantenbewertung

```python
from src.ai.supplier_scorer import SupplierScorer

# SupplierScorer initialisieren
scorer = SupplierScorer()

# Lieferanten für ein Produkt bewerten
product = {
    'product_name': 'Smart Watch - Premium Qualität',
    'suppliers': [
        {'name': 'Supplier-A', 'price': 22.99, 'rating': 4.2, 'delivery_days': 7},
        {'name': 'Supplier-B', 'price': 24.99, 'rating': 4.7, 'delivery_days': 5},
        {'name': 'Supplier-C', 'price': 19.99, 'rating': 3.8, 'delivery_days': 12}
    ]
}

scored_suppliers = scorer.score_suppliers(product)
best_supplier = scorer.find_best_supplier(product)
```

### Listing-Generierung

```python
from src.ai.listing_generator import ListingGenerator

# ListingGenerator initialisieren
generator = ListingGenerator()

# Listing für ein Produkt generieren
product = {
    'product_name': 'Smart Watch - Premium Qualität',
    'keyword': 'Smart Watch',
    'trend_score': 85,
    'profit_margin': 0.45,
    'supplier_price': 25.99,
    'market_price': 49.99,
    'suppliers': [
        {'name': 'Supplier-B', 'price': 24.99, 'rating': 4.7, 'delivery_days': 5, 'total_score': 92}
    ],
    'details': {
        'description': 'Diese hochwertige Smart Watch bietet zahlreiche Funktionen für Fitness und Alltag.',
        'features': [
            'Fitness-Tracking mit Herzfrequenzmessung',
            'Wasserdicht bis 50m',
            'Benachrichtigungen für Anrufe und Nachrichten',
            'Lange Akkulaufzeit von bis zu 7 Tagen'
        ],
        'specifications': {
            'material': 'Aluminium & Silikon',
            'weight': '45g',
            'dimensions': '44 x 38 x 10.7 mm',
            'battery': '300mAh'
        },
        'images': [
            'https://example.com/images/smart_watch_1.jpg',
            'https://example.com/images/smart_watch_2.jpg'
        ]
    }
}

shopify_listing = generator.generate_listing(product, platform='shopify')
ebay_listing = generator.generate_listing(product, platform='ebay')
```

### Shopify-Integration

```python
from src.api.shopify.connector import ShopifyManager

# ShopifyManager initialisieren
shopify = ShopifyManager()

# Produkt erstellen
product_data = {
    'title': 'Smart Watch - Premium Qualität',
    'description': '<h1>Smart Watch - Premium Qualität</h1><p>Diese hochwertige Smart Watch bietet zahlreiche Funktionen für Fitness und Alltag.</p>',
    'price': 49.99,
    'images': ['https://example.com/images/smart_watch_1.jpg']
}

product = shopify.create_product(product_data)
```

### eBay-Integration

```python
from src.api.ebay.connector import EbayManager

# EbayManager initialisieren
ebay = EbayManager()

# Artikel listen
item_data = {
    'title': 'Smart Watch - Premium Qualität',
    'description': '<h1>Smart Watch - Premium Qualität</h1><p>Diese hochwertige Smart Watch bietet zahlreiche Funktionen für Fitness und Alltag.</p>',
    'price': 49.99,
    'quantity': 10,
    'images': ['https://example.com/images/smart_watch_1.jpg']
}

listing = ebay.list_item(item_data)
```

## Projektstruktur

```
DropchipAi/
├── config/                # Konfigurationsdateien
│   ├── credentials.yaml   # API-Schlüssel (nicht im Git)
│   └── settings.yaml      # Allgemeine Einstellungen
├── src/                   # Quellcode
│   ├── ai/                # KI-Module
│   │   ├── product_research.py    # Produktrecherche
│   │   ├── supplier_scorer.py     # Lieferantenbewertung
│   │   └── listing_generator.py   # Listing-Generator
│   ├── api/               # API-Integrationen
│   │   ├── shopify/       # Shopify-Integration
│   │   │   └── connector.py
│   │   └── ebay/          # eBay-Integration
│   │       └── connector.py
│   ├── core/              # Kernkomponenten
│   │   ├── automation.py  # Automatisierungsmanager
│   │   └── config_manager.py  # Konfigurationsmanager
│   ├── data/              # Datenverarbeitung
│   │   ├── price_comparison.py    # Preisvergleich
│   │   └── google_trends.py       # Google Trends Analyse
│   ├── utils/             # Hilfsfunktionen
│   │   ├── logger.py      # Logging
│   │   └── data_loader.py # Datenlader
│   └── core.py            # Hauptklasse
├── tests/                 # Tests
│   ├── test_ai/           # Tests für KI-Module
│   ├── test_api/          # Tests für API-Integrationen
│   └── test_core/         # Tests für Kernkomponenten
├── main.py                # Hauptskript
├── requirements.txt       # Abhängigkeiten
└── README.md              # Diese Datei
```

## Tests ausführen

```bash
# Alle Tests ausführen
python -m unittest discover

# Spezifische Tests ausführen
python -m unittest tests.test_ai.test_product_research
python -m unittest tests.test_api.test_shopify_connector
python -m unittest tests.test_core.test_core
```

## Abhängigkeiten

- pandas: Datenverarbeitung und -analyse
- numpy: Numerische Berechnungen
- shopifyapi: Shopify API-Integration
- ebaysdk: eBay API-Integration
- pytrends: Google Trends API-Integration
- jinja2: Template-Engine für Listing-Generierung
- pyyaml: YAML-Dateiverarbeitung
- requests: HTTP-Anfragen

## Beitragen

Beiträge sind willkommen! Bitte erstellen Sie einen Fork des Repositories und reichen Sie einen Pull Request ein.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.