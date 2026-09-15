# DATE — site Django rose / noir

## 1. Installation

Dans PowerShell :

```powershell
cd date_django
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py runserver
```

Puis ouvre http://127.0.0.1:8000/

## 2. Recevoir les réponses par e-mail

Le site utilise SMTP Gmail.

### Windows PowerShell

Avant de lancer le serveur :

```powershell
$env:EMAIL_HOST_USER="TON_ADRESSE_GMAIL@gmail.com"
$env:EMAIL_HOST_PASSWORD="TON_MOT_DE_PASSE_APPLICATION"
$env:DATE_RECIPIENT_EMAIL="TON_ADRESSE_DESTINATAIRE@gmail.com"
py manage.py runserver
```

Pour Gmail, utilise un mot de passe d'application, pas ton mot de passe Gmail habituel.

### IMPORTANT

Dans ta demande, l'adresse a été écrite `sidfatou00gmail.com`, qui ressemble à une adresse à laquelle il manque le `@`.

Si l'adresse correcte est `sidfatou00@gmail.com`, mets :

```powershell
$env:DATE_RECIPIENT_EMAIL="sidfatou00@gmail.com"
```

## 3. Ce que le site contient

- Page d'accueil plein écran
- Ambiance rose / noir premium
- Cinéma
- Picnic
- Glace
- Hôtel
- Choix de date
- Petit message
- Animations d'apparition
- Effet de grain cinématographique
- Halo rose qui suit la souris
- Cartes interactives
- Page de confirmation
- Envoi des réponses par e-mail via Django

Pour une mise en ligne, pense à mettre `DEBUG=False`, une vraie `SECRET_KEY`, les domaines dans `ALLOWED_HOSTS`, et des variables d'environnement pour les identifiants SMTP.


## Correction de l'erreur 530 Authentication Required

L'erreur :

`530 5.7.0 Authentication Required`

signifie que Gmail n'accepte pas l'envoi parce que les identifiants SMTP ne sont pas correctement configurés.

Avec un compte Gmail, active la validation en deux étapes puis crée un **mot de passe d'application**. Utilise ce mot de passe de 16 caractères dans `EMAIL_HOST_PASSWORD`, pas le mot de passe normal du compte.

Exemple PowerShell :

```powershell
$env:EMAIL_HOST_USER="tonadresse@gmail.com"
$env:EMAIL_HOST_PASSWORD="xxxx xxxx xxxx xxxx"
$env:DATE_RECIPIENT_EMAIL="sidfatou00@gmail.com"
py manage.py runserver
```

Vérifie surtout que l'adresse destinataire est correcte. `sidfatou00gmail.com` n'est pas une adresse Gmail valide : il faut normalement un `@`.
