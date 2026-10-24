# OMNI-SUPER-ENGINE – Info-Blatt

Repository: https://github.com/thejeffreyerlangen-netizen/OMNI-SUPER-ENGINE

## 1) Überblick

Das Repository ist ein Python-Projekt mit Fokus auf:

- Navier-Stokes / hyperviskose Glättung
- Ziolkowski-Raketen- und Stufenmodellierung
- symplektische Invarianz / Determinanten-Erhaltung
- Master-Engine-Architektur für einen „OMNI“-Kern

Die Projektbeschreibung lautet:

> Super Engine Omni (v4.6): M-DSL IR-Kernel für Navier-Stokes & Feld-PDEs. Max. Vektor-Performance mit H²-Sobolev-Dämpfung für 100% deterministische Plasma-Stabilität & Reaktor-Sicherheit.

Die aktuelle Projektdarstellung im Repository zeigt jedoch eine aktuelle Version mit dem Namen:

- Super Engine Omni v7.0 (Core 7)

## 2) Repository-Struktur

### Root-Verzeichnis

Wichtige Dateien im Root:

- README.md
- pyproject.toml
- requirements.txt
- pytest.ini
- install.sh
- run_v7_test_suite.py
- omni_engine.py
- omni_core7.py
- omni_super_engine_master_v7.py
- super_engine_omni_v460.py
- rigorous_master_test_suite_v460.py
- mutation_stresstest_hardened.py
- tests/
- omni_super_engine_v7_complete/

Zusätzlich gibt es mehrere ZIP-Archive und Snapshot-Versionen, darunter:

- omni-super-engine-v4.6.0-final.zip
- omni-super-engine-v4.6.0-production (1).zip
- omni-super-engine-v6.2.0-MASTER-UNIFIED.zip
- omni_core7_prototype-1.zip
- omni_super_engine_v7_complete.zip
- omni_super_engine_v7  2.zip

Diese Dateien sind überwiegend historische oder redundante Versionen / Archive und nicht der primäre laufende Kern.

### Wichtiger v7-Projektordner

Der echte Kern des laufenden Projekts befindet sich in:

- omni_super_engine_v7_complete/

Dort liegen unter anderem:

- README.md
- pyproject.toml
- requirements.txt
- pytest.ini
- install.sh
- run_v7_test_suite.py
- omni_super_engine_master_v7.py
- docs/
- tests/

## 3) Kern-Dateien

### README.md

Die Haupt-README beschreibt die Installation und den Start:

- Python venv erzeugen
- Requirements installieren
- run_v7_test_suite.py ausführen

### pyproject.toml

Wichtige Metadaten:

- Projektname: omni_super_engine
- Version: 7.0.0
- Beschreibung: Super Engine Omni v7.0 (Core 7)
- Python-Anforderung: >=3.8
- Abhängigkeiten:
  - numpy
  - pytest
  - matplotlib

### run_v7_test_suite.py

Ein kleiner Wrapper, der den Pytest-Lauf startet:

```python
import subprocess
import sys

if __name__ == "__main__":
    result = subprocess.run([sys.executable, "-m", "pytest", "-q"], check=False)
    raise SystemExit(result.returncode)
```

### omni_super_engine_v7_complete/omni_super_engine_master_v7.py

Dies ist die zentrale Logik-Datei. Sie enthält:

- OmniPhysicsBridge
  - enforce_symplectic_invariant(...)
  - translate_ziolkowski(...)
  - translate_navier_stokes(...)
- SuperEngineOmniCore7Master
  - initialize_state(...)
  - execute_evolution_cycle(...)

Die Funktionen betreiben:

1. Symplektische Invarianz
   - Matrixdeterminante wird auf 1 normiert.

2. Ziolkowski-Massen-/Stufen-Berechnung
   - Berechnet Massenverhältnisse, Startmasse, Treibstoffmasse, Strukturmasse.

3. Navier-Stokes-Hyperviskose Glättung
   - Fourier-basiertes H²-Sobolev-Filter mit Hyperviskosität.

4. Master-Engine-Zyklus
   - Ausführung eines vollständigen Simulations-/Evolutionszyklus.

## 4) Tests

Die zentrale Testdatei ist:

- tests/test_omni_physics_bridge.py

Diese prüft:

- symplektische Invarianz
- Ziolkowski-Stufenrechnung
- Navier-Stokes-Glättung
- Master-Engine-Evolutionszyklus

Beispielhafte Assertions:

- Determinante nahe 1.0
- mass_ratio > 2.5
- total_start_mass_m0 > 17000
- keine NaN-Werte im geglätteten Feld
- Status == VERIFIED_STABLE

## 5) Wichtiger Hinweis zu Testbench, Grafiken und Prüfberichten

Im Repository-Root liegen neben dem eigentlichen Code auch Testbench-Ausgaben, Diagramme, Prüfberichte und Visualisierungen, die für Validierung, Benchmarking und Nachweis der Ergebnisse relevant sind. Diese Dateien sind keine primären Laufzeitkomponenten, sondern ergänzende Artefakte für Tests, Analyse und Dokumentation.

Beispiele dafür sind:

- PNG-Graphen und Phase-Space-Visualisierungen
- Benchmark-/Prüfberichte
- Ergebnisdateien aus Testläufen
- Exportdaten für wissenschaftliche oder technische Auswertung

Diese Objekte dienen dazu, die Qualität, Stabilität und Ergebnisse der Simulationen nachvollziehbar zu dokumentieren, und sollten als ergänzende Prüf- bzw. Analyseausgaben verstanden werden – nicht als Hauptkernel des Projekts.

Der aktive Code liegt im Paketbereich `src/omni_engine/`, während Testbench-Ausgaben, Grafiken und Prüfberichte im Root-Bereich bzw. in `assets/`, `docs/` und ähnlichen Bereichen dokumentiert sind.

## 6) Was die Logik technisch macht

### OmniPhysicsBridge

#### enforce_symplectic_invariant

Stellt sicher, dass die Determinante einer Matrix exakt oder numerisch nahe 1 bleibt:

```python
det_val = np.linalg.det(j_matrix)
if np.abs(det_val) < 1e-12:
    return np.eye(j_matrix.shape[0], dtype=float)
scale = abs(det_val) ** (1.0 / n)
return j_matrix / scale
```

#### translate_ziolkowski

Berechnet die Raketenstufe mit:

- m_payload
- isp
- delta_v
- structural_ratio

Rückgabe:

- mass_ratio
- total_start_mass_m0
- propellant_mass_mp
- structural_mass_ms
- status

#### translate_navier_stokes

Nutzt FFT und ein Hyperviskositätsfilter:

```python
field_fft = np.fft.fft(field)
smoothing_filter = np.exp(-hyper_coeff * (k ** 4))
smoothed_fft = field_fft * smoothing_filter
return np.real(np.fft.ifft(smoothed_fft))
```

Das entspricht einer H²-Sobolev-ähnlichen Glättung im Spektralbereich.

### SuperEngineOmniCore7Master

Ziel:

- initialer Zustand
- physikalischer Modus wählen (Ziolkowski oder Navier-Stokes)
- evolutive Berechnung / Zyklus
- Ergebnis mit Status, Residuum und Brückendaten zurückgeben

Die Standardstatusmeldung ist:

- VERIFIED_STABLE

## 7) Start / Ausführung

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_v7_test_suite.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_v7_test_suite.py
```

### Alternative

```bash
python -m pytest -q
```

## 8) Kurzfazit

Das Repository enthält eine funktionale Python-Implementierung für eine "Super Engine Omni Core 7" mit:

- physikalischer Brücke zwischen Raketen- und Strömungsmodellen
- symplektischer Stabilität
- Hyperviskose Glättung
- Teststruktur zur Validierung zentraler Funktionen

Das vollständige Projekt liegt primär im Ordner:

- omni_super_engine_v7_complete/

Die ZIP-Dateien und älteren Snapshot-Versionen sind eher Archiv-/Historienartefakte als Kernprojekt.

## 9) Empfehlungen

Wenn du das Projekt lokal weiterentwickeln willst:

1. Hauptarbeitsordner: omni_super_engine_v7_complete/
2. Startpunkt: run_v7_test_suite.py
3. Prüfungen: pytest
4. Fokus: omni_super_engine_master_v7.py
5. Tests: tests/test_omni_physics_bridge.py

## 10) Link

https://github.com/thejeffreyerlangen-netizen/OMNI-SUPER-ENGINE

---

Dokument erstellt für die interne Repo-Übersicht / Projektinformation.
