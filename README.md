# Simulatore di Processo Produttivo

Un simulatore modulare per processi produttivi del settore secondario, implementato in Python con paradigma Object-Oriented e design pattern.

## 📋 Descrizione

Questo progetto implementa una simulazione di un ambiente produttivo industriale, comprendente:
- **Macchinari** con capacità produttive e stati operativi
- **Magazzini** per la gestione delle materie prime e prodotti finiti
- **Sistema di monitoraggio** in tempo reale degli eventi di produzione
- **Gestione centralizzata** degli ordini e delle risorse

Il sistema è progettato seguendo i principi dell'Industria 4.0, utilizzando pattern architetturali come Observer e Strategy per una struttura estensibile e modulare.

## 🏗️ Architettura del Sistema

### Diagramma delle Classi (Semplificato)

### Componenti Principali

- **`Observer`**: Interfaccia astratta per gli osservatori
- **`ProcessoProduttivo`**: Classe base astratta per tutti i processi
- **`Macchina`**: Implementa il processo di produzione
- **`Magazzino`**: Gestisce l'inventario e i materiali
- **`GestioneProduzione`**: Coordina le risorse produttive
- **`LoggerProduzione`**: Registra tutti gli eventi del sistema

## 🚀 Installazione e Utilizzo

### Prerequisiti
- Python 3.10 o superiore
- Nessuna dipendenza esterna richiesta

### Esecuzione
```bash
# Clona o scarica il progetto
git clone <repository-url>
cd simulatore-processo-produttivo

# Esegui il simulatore
python simulatore_processo_produttivo.py

# Inizializzazione del sistema
gestione = GestioneProduzione()
logger = LoggerProduzione()

# Aggiunta macchinari
pressa = Macchina("Pressa CNC", capacita=50)
tornio = Macchina("Tornio Multiasse", capacita=30)

# Aggiunta magazzini
magazzino_pt = Magazzino("Magazzino Prodotti Finiti", capacita_massima=500)

# Configurazione sistema
gestione.aggiungi_macchina(pressa)
gestione.aggiungi_macchina(tornio)

# Collegamento osservatori
pressa.registra_observer(logger)
tornio.registra_observer(logger)
