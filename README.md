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
a `GitHubApiError` if the data is the result of an erroneous request. The data
must be an object returned by the parsing of the response's content, which is
in JSON.

The user should not raise `GitHubApiError` by themself and instead rely on
`detect_github_api_error`.

For more information, consult the documentation and the demo in the source code
repository.
