# AutoDiag Pro – Ultimate Edition

Offline-fähiges professionelles Diagnose-Tool für Kfz-Werkstätten, mobile Dienste und Hobby-Schrauber.

## Features

- OBD-II Diagnose (ELM327, CANable, Simulator)
- Live-Daten (RPM, Temperatur, Lambda, MAF, MAP, Batterie)
- Fehlercodes auslesen, decodieren, löschen
- Freeze Frame
- Fahrzeugprofile und Scan-Historie
- Professionelle PDF-Berichte
- Simulationsmodus für Demo und Schulungen
- 200+ DTCs aus SQLite-Datenbank

## Erweiterte Dokumentation

Siehe docs/reports für Review, Roadmap und Marktanalyse.

## Installation

```bash
pip install -r requirements.txt
python launcher.py
```

## Repository-Struktur

```
AutoDiag-Pro/
├── src/autodiag/
│   ├── adapters/        # ELM327, CANable, Simulator
│   ├── core/           # DiagnosticSession, DTCDecoder
│   ├── services/       # DiagnosticService, LiveService, ReportService
│   ├── gui/            # UI-Module
│   └── utils/          # Logger, Version
├── data/               # SQLite Datenbanken
├── docs/               # Dokumentation
├── scripts/            # Build-Scripts
├── tests/              # Unit Tests
└── config/             # Konfigurationen
```

## Lizenz

MIT License - Siehe LICENSE

## Status

✅ **Produktionsreife v1.0.0**
