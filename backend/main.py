# -*- coding: utf-8 -*-
# DropchipAI Main Module
# Dieses Modul dient als Einstiegspunkt fuer die DropchipAI-Anwendung.

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.core import DropchipCore
from src.core.config_manager import ConfigManager
from src.utils.logger import Logger

def main():
    
    # Kommandozeilenargumente parsen
    parser = argparse.ArgumentParser(description='DropchipAi - KI-gestuetzte Dropshipping-Automatisierung')
    parser.add_argument('--config', type=str, help='Pfad zur Konfigurationsdatei')
    parser.add_argument('--log-level', type=str, default='INFO', 
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Log-Level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    parser.add_argument('--keywords', type=str, nargs='+', 
                        help='Schluesselwoerter fuer die Produktrecherche')
    
    args = parser.parse_args()
    
    # Logger initialisieren
    logger = Logger(log_level=args.log_level)
    logger.info("DropchipAi wird gestartet...")
    
    # Konfiguration laden
    config_manager = ConfigManager(args.config)
    
    # DropchipCore initialisieren
    core = DropchipCore()
    
    # Wenn Schluesselwoerter angegeben wurden, fuehre Automatisierung durch
    if args.keywords:
        logger.info(f"Starte Automatisierung mit Keywords: {args.keywords}")
        result = core.full_automation(args.keywords)
        logger.info(f"Automatisierung abgeschlossen: {result} Produkte verarbeitet")
    else:
        logger.info("Keine Keywords angegeben. Verwende --keywords, um die Automatisierung zu starten.")
        print("Verwendung: python main.py --keywords 'Smart Watch' 'Wireless Earbuds'")

if __name__ == "__main__":
    main()