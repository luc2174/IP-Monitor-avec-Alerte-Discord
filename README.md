Ce script vérifie régulièrement l’adresse IP publique de la machine et envoie une notification sur un webhook Discord dès qu’elle change.

🔧 Fonctionnalités
🔄 Vérifie l’adresse IP publique toutes les 60 secondes

📡 Envoie une alerte Discord uniquement si l’IP a changé

⚙️ Peut être exécuté au démarrage automatiquement (shell:startup)

🔒 Aucune donnée personnelle n’est stockée

🛠 Utilisation
Remplacez le lien du webhook Discord dans le script.

Installez la dépendance :

Modifier
pip install requests


(Optionnel) Compilez en .exe :
"pyinstaller --onefile --noconsole ip_monitor.py"

Placez le fichier .exe dans shell:startup pour un lancement automatique.
