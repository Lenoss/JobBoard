La base de données est une base MySQL 8.0 hébergée sur une machine Azure.
Elle n'est accessible uniquement de l'école ainsi que du domicile de chacun des développeurs pour des raisons de sécurité.

api/advertisement :
	GET: Permet de récupérer tous les éléments advertisements
		Retourne les éléments en JSON
	POST: Permet d'envoyer le formulaire d'ajout
		Retourne un message de validation ou d'erreur en JSON
	PATCH: Permet d'envoyer le formulaire de modification
		Retourne un message de validation ou d'erreur en JSON
	DELETE: Permet d'envoyer le formulaire de suppression
		Retourne un message de validation ou d'erreur en JSON
api/advertisement/id :
	GET: Permet de récupérer 1 seul élément de la table advertisements
		Retourne l'élément en JSON


api/auth/login :
	POST: Permet d'envoyer les informations de connexion
		Retourne un message de validation ou d'erreur en JSON 


api/company :
	GET: Permet de récupérer tous les éléments companies
		Retourne les éléments en JSON
	POST: Permet d'envoyer le formulaire d'ajout
		Retourne un message de validation ou d'erreur en JSON
	PATCH: Permet d'envoyer le formulaire de modification
		Retourne un message de validation ou d'erreur en JSON
	DELETE: Permet d'envoyer le formulaire de suppression
		Retourne un message de validation ou d'erreur en JSON
api/company/id :
	GET: Permet de récupérer 1 seul élément de la table companies
		Retourne l'élément en JSON



api/user/id :
	GET: Permet de récupérer tous les informations concernant l'utilisateur par rapport à l'id
		Retourne les éléments en JSON


api/city :
	GET: Permet de récupérer tous les éléments cities
		Retourne les éléments en JSON
	POST: Permet d'envoyer le formulaire d'ajout
		Retourne un message de validation ou d'erreur en JSON
	PATCH: Permet d'envoyer le formulaire de modification
		Retourne un message de validation ou d'erreur en JSON
	DELETE: Permet d'envoyer le formulaire de suppression
		Retourne un message de validation ou d'erreur en JSON
city/id :
	GET: Permet de récupérer 1 seul élément de la table companies
		Retourne l'élément en JSON