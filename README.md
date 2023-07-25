Bienvenue dans le projet Django de gestion de produit avec une API REST utilisant MongoDB comme base de données !

# Nom du projet : Gestion de Produit API

Ce projet est une application Django développée avec Python 3.11 et Django 4.2.3 pour gérer des produits en utilisant une API REST. La base de données utilisée est MongoDB.

## Installation

1. Assurez-vous d'avoir Python 3.11 installé sur votre système.
2. Installez Django 4.2.3 en utilisant la commande suivante :

```bash
pip install django==4.2.3
```

3. Installez le pilote MongoDB pour Django en utilisant la commande suivante :

```bash
pip install djongo
```

4. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/votre-utilisateur/gestion-produit-api.git
```

5. Naviguez vers le répertoire du projet :

```bash
cd gestion-produit-api
```

6. Lancez le serveur de développement en exécutant :

```bash
python manage.py runserver
```

Le serveur sera accessible à l'adresse `http://localhost:8000/`.

## API Endpoints

L'API fournit les méthodes suivantes pour gérer les produits :

### 1. Récupérer un produit par ID

```
GET /api/products/{id}/
```

Retourne les détails du produit correspondant à l'ID spécifié.

### 2. Récupérer tous les produits

```
GET /api/products/
```

Retourne la liste de tous les produits présents dans la base de données.

### 3. Sauvegarder un nouveau produit

```
POST /api/products/
```

Permet de créer un nouveau produit en envoyant les détails du produit dans le corps de la requête au format JSON.

### 4. Mettre à jour un produit existant

```
PUT /api/products/{id}/
```

Permet de mettre à jour les détails d'un produit existant spécifié par l'ID. Les nouvelles informations du produit doivent être envoyées dans le corps de la requête au format JSON.

### 5. Supprimer un produit par ID

```
DELETE /api/products/{id}/
```

Supprime le produit correspondant à l'ID spécifié.

### 6. Supprimer tous les produits

```
DELETE /api/products/
```

Supprime tous les produits de la base de données.

## Modèles

Le modèle de produit est défini comme suit :

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs du produit (le cas échéant)
```

N'hésitez pas à ajouter des champs supplémentaires au modèle si nécessaire.

## Tests

Des tests unitaires sont disponibles pour assurer le bon fonctionnement de l'API. Pour exécuter les tests, utilisez la commande suivante :

```bash
python manage.py test
```

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, assurez-vous de soumettre une demande de pull avec vos modifications.

## Auteurs

Liste des contributeurs du projet :

- [Brody Gaudel](https://github.com/BrodyGaudel)

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

---

Nous vous remercions d'utiliser notre application de gestion de produit avec une API REST. N'hésitez pas à nous contacter en cas de questions ou de problèmes.

Bon codage !
