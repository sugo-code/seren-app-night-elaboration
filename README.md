# Night Data Elaboration - Azure Function
## Finalità
La finalità della Azure Function è quella di creare delle elaborazioni notturne atte a mostrare agli amministratori di SerenApp alcuni dati recuperati dai braccialetti dei clienti. L'elaborazione viene effettuata alla mezzanotte di ogni giorno.
## Tecnologie
- Azure Functions for Python
- Pandas
- SQLAlchemy
## Funzionamento
Il progetto contiene i moduli per la connessione al database (data.py) e l'elaborazione dei dati (elaboration.py).
La Function richiama il modulo di elaborazione che contiene tutta la logica per recuperare i dati ed effettuare le elaborazioni. Questi dati verranno poi restituiti alla Function che si occupera del loro caricamento su database.
## Istruzioni
Il progetto è stato realizzato in un ambiente virtuale creato mediante *virtualenv*. Per il funzionamento in locale è necessario installare le dipendenze tramite il comando `pip install -r requirments.txt`. Verificare quindi il corretto avvio dell'ambiente virtuale e, a qual punto, avviare la Function.
