# ghae

## FRANÇAIS

Cette bibliothèque détecte l'échec des requêtes à l'API de GitHub et les
signale en levant une exception.

### Contenu

L'exception `GitHubApiError` indique qu'une requête à l'API de GitHub a échoué.
Ses propriétés sont les suivantes.

* `message`: le message d'erreur.
* `doc_url`: l'URL de la documentation de l'erreur.
* `status`: le code du statut de la réponse.
* `req_url`: l'URL de la requête erronée.

La fonction `detect_github_api_error` examine les données provenant de l'API de
GitHub et lève `GitHubApiError` si elles résultent d'une requête erronée. Les
données doivent être un objet produit par la lecture du contenu de la réponse,
qui est en JSON.

L'utilisateur ne devrait pas lever `GitHubApiError` lui-même et plutôt se fier
à `detect_github_api_error`.

Pour plus d'informations, consultez la documentation et la démo dans le dépôt
de code source.

### Dépendances

Cette commande installe les dépendances nécessaires au développement de `ghae`.
```
pip install -r requirements-dev.txt
```

### Démo

La démo montre comment déterminer qu'une requête à l'API de GitHub est erronée.
Elle constitue aussi un exemple de gestion de `GitHubApiError`.

Affichez l'aide pour plus d'informations.
```
python demo.py -h
```

Cet exemple envoie une requête valide.
```
python demo.py -r GRV96/ghae
```

Cet exemple envoie une requête erronée.
```
python demo.py -r GRV96/gha
```

## ENGLISH

This library detects failed requests to the GitHub API and signals them by
raising an exception.

### Content

Exception `GitHubApiError` indicates that a request to the GitHub API has
failed. Its properties are the following.

* `message`: the error message.
* `doc_url`: the URL to the error's documentation.
* `status`: the response's status code.
* `req_url`: the erroneous request's URL.

Function `detect_github_api_error` examines data from the GitHub API and raises
a `GitHubApiError` if it is the result of an erroneous request. The data must
be an object returned by the parsing of the response's content, which is in
JSON.

The user should not raise a `GitHubApiError` themself and instead rely on
`detect_github_api_error`.

For more information, consult the documentation and the demo in the source code
repository.

### Dependencies

This command installs the dependencies required for the development of `ghae`.
```
pip install -r requirements-dev.txt
```

### Demo

The demo shows how to find out whether a request to the GitHub API is
erroneous. It also constitutes an example of handling a `GitHubApiError`.

Display the help message for more information.
```
python demo.py -h
```

This example sends a valid request.
```
python demo.py -r GRV96/ghae
```

This example sends an erroneous request.
```
python demo.py -r GRV96/gha
```
