from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime
import random

class Observer(ABC):
    @abstractmethod
    def aggiorna(self, evento: str):
        pass

class ProcessoProduttivo(ABC):
    def __init__(self, nome: str, tempo_ciclo: float):
        self.nome = nome
        self.tempo_ciclo = tempo_ciclo
        self.stato = "fermo"
        self.observers: List[Observer] = []
    
    def registra_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def rimuovi_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notifica_observers(self, evento: str):
        for observer in self.observers:
            observer.aggiorna(evento)
    
    @abstractmethod
    def esegui(self):
        pass

# Creazione e avvio macchinario
class Macchina(ProcessoProduttivo):
    def __init__(self, nome: str, capacita: int):
        super().__init__(nome, tempo_ciclo=60.0)  # Ciclo di produzione di 60 secondi
        self.capacita = capacita
        self.produzione_attuale = 0 # Produzione attuale a 0
    
    def esegui(self):
        self.stato = "lavoro"
        self.notifica_observers(f"{self.nome}: Avvio produzione")
        
        try:
            self.produzione_attuale += self.capacita
            self.notifica_observers(f"{self.nome}: Produzione completata")
        except Exception as e:
            self.notifica_observers(f"{self.nome}: Errore durante la produzione - {str(e)}")
        
        self.stato = "fermo"

# Creazione e gestione magazzino
class Magazzino(ProcessoProduttivo):
    def __init__(self, nome: str, capacita_massima: int):
        super().__init__(nome, tempo_ciclo=30.0)
        self.capacita_massima = capacita_massima
        self.inventario: Dict[str, int] = {}
    
    def ricevi_materiale(self, tipo: str, quantita: int):
        if sum(self.inventario.values()) + quantita <= self.capacita_massima:
            self.inventario[tipo] = self.inventario.get(tipo, 0) + quantita
            self.notifica_observers(f"{self.nome}: Ricevuto materiale {tipo}")
            return True
        return False
    
    def esegui(self):
        self.stato = "controllo"
        self.notifica_observers(f"{self.nome}: Controllo inventario")
        
        for tipo, quantita in self.inventario.items():
            self.notifica_observers(f"{self.nome}: {tipo}: {quantita}")
        
        self.stato = "pronto"

class GestioneProduzione:
    def __init__(self):
        self.macchine: List[Macchina] = []
        self.magazzini: List[Magazzino] = []
    
    def aggiungi_macchina(self, macchina: Macchina):
        self.macchine.append(macchina)
    
    def aggiungi_magazzino(self, magazzino: Magazzino):
        self.magazzini.append(magazzino)
    
    def gestisci_ordine(self, ordine: Dict):
        macchina_disponibile = None
        for macchina in self.macchine:
            if macchina.stato == "fermo":
                macchina_disponibile = macchina
                break
        
        if macchina_disponibile:
            macchina_disponibile.esegui()
        else:
            print("Nessuna macchina disponibile per l'ordine")

# Registro degli eventi
class LoggerProduzione(Observer):
    def aggiorna(self, evento: str):
        print(f"[{datetime.now()}] {evento}")

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione del sistema di produzione
    gestione = GestioneProduzione()
    
    # Aggiunta delle macchine
    macchina1 = Macchina("Macchina 1", capacita=100)
    macchina2 = Macchina("Macchina 2", capacita=150)
    gestione.aggiungi_macchina(macchina1)
    gestione.aggiungi_macchina(macchina2)
    
    # Aggiunta dei magazzini
    magazzino1 = Magazzino("Magazzino Materie Prime", capacita_massima=1000)
    magazzino2 = Magazzino("Magazzino Prodotti Finiti", capacita_massima=1500)
    gestione.aggiungi_magazzino(magazzino1)
    gestione.aggiungi_magazzino(magazzino2)
    
    # Aggiunta dell'observer
    logger = LoggerProduzione()
    macchina1.registra_observer(logger)
    macchina2.registra_observer(logger)
    magazzino1.registra_observer(logger)
    magazzino2.registra_observer