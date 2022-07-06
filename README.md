# Night Data Elaboration - Azure Function
## Finalità
La finalità della Azure Function è quella di creare delle elaborazioni notturne atte a mostrare agli amministratori di SerenApp alcuni dati recuperati dai braccialetti dei clienti. L'elaborazione viene effettuata alla mezzanotte di ogni giorno.
## Tecnologie
- Azure Functions for Python
- Pandas
- Matplotlib (da verificare ancora in base alla libreria che verrà usata)
## Funzionamento
Il progetto è stato diviso in due parti: una cartella *modules* che contiene i moduli per la connessione e l'elaborazione dei dati e la cartella *nightelab* che contiene i file necessari per il corretto funzionamento della Azure Function.
La Function richiama il modulo di elaborazione che conterrà tutta la logica per recuperare i dati ed effettuare le elaborazioni. A quel punto verranno restituiti alla Function i grafici elaborati e quest'ultima si occuperà di rendere disponibili questi ultimi alla dashboard.
## Istruzioni
Il progetot è stato realizzato in un ambiente virtuale creato mediante *virtualenv*. Per il funzionamento è necessario installare le dipendenze tramite il comando `pip install -r requirments.txt`. Verificare quindi di avviare correttamente l'ambiente virtuale ed avviare la Function 