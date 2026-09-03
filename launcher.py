#!/usr/bin/env python3
"""Einstiegspunkt für AutoDiag Pro – Ultimate Edition."""
import sys
from pathlib import Path

# src zum Pfad hinzufügen
sys.path.insert(0, str(Path(__file__).parent / "src"))

from autodiag.main import main

if __name__ == "__main__":
    main()
