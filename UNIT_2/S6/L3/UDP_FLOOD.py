#!/usr/bin/env python3
"""
Esercizio: Inviare pacchetti UDP di 1 KB verso un IP e una porta target.
Utilizzo didattico – non utilizzare su reti senza autorizzazione.
"""

import socket
import random
import sys

def main():
    # 1. Input dell'IP target
    target_ip = input("Inserisci l'IP del target: ").strip()
    if not target_ip:
        print("IP non valido. Uscita.")
        sys.exit(1)

    # 2. Input della porta UDP target
    try:
        target_port = int(input("Inserisci la porta UDP del target: ").strip())
        if not (1 <= target_port <= 65535):
            raise ValueError
    except ValueError:
        print("Porta non valida. Deve essere un numero tra 1 e 65535.")
        sys.exit(1)

    # 3. Numero di pacchetti da inviare
    try:
        num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? ").strip())
        if num_packets <= 0:
            raise ValueError
    except ValueError:
        print("Numero di pacchetti non valido. Deve essere un intero positivo.")
        sys.exit(1)

    # 4. Creazione del socket UDP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f"Errore nella creazione del socket: {e}")
        sys.exit(1)

    # 5. Costruzione del payload di 1 KB (1024 byte) con byte casuali
    # Usiamo random.randbytes() disponibile da Python 3.9
    payload = random.randbytes(1024)

    print(f"\nInvio di {num_packets} pacchetti UDP da 1 KB a {target_ip}:{target_port}...")
    print("Premi CTRL+C per interrompere.\n")

    # 6. Invio dei pacchetti
    sent = 0
    try:
        for i in range(num_packets):
            sock.sendto(payload, (target_ip, target_port))
            sent += 1
            # Piccola stampa di avanzamento ogni 100 pacchetti
            if sent % 100 == 0:
                print(f"Inviati {sent} pacchetti...")
    except KeyboardInterrupt:
        print(f"\nInterrotto dall'utente. Inviati {sent} pacchetti.")
    except socket.error as e:
        print(f"Errore di rete: {e}")
    finally:
        sock.close()
        print(f"\nProgramma terminato. Inviati {sent} pacchetti su {num_packets} richiesti.")

if __name__ == "__main__":
    main()