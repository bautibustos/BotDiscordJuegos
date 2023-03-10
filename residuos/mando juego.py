import requests, json, os

data = requests.get(str(URL)+str("giveaways"), params="platform=steam&type=loot&sort-by=popularity")#esto para steam
#print(data)
""""
if data.status_code == 200:
	data_json= data.json()
	for i in data_json:
		print("Nombre: ",i['title'],
			"Tipo: ",i['type'])
"""


def mandojuego():
	data = requests.get(str(URL)+str("filter"), params="platform=epic-games-store.steam&type=game.loot&sort-by=popularity")#esto para epic
	print(data)
	if data.status_code == 200:
		data_json= data.json()
		titulo=[]
		tipo=[]
		link=[]
		imagen=[]

		for i in data_json:
			titulo.append(i['title'])
			tipo.append(i['type'])
			link.append(i['open_giveaway'])
			imagen.append(i['image'])
		juego={}
		juego["Juegos"]=[]
		for i in range(len(titulo)):
			if tipo[i]!='DLC':
				juego["Juegos"].append({
					"Nombre": titulo[i],
					"Link": link[i],
					})

		string = str(juego)
		string = string.replace("{", "")
		string = string.replace("[", "")
		string = string.replace("]", "")
		string = string.replace("}", "")
		string = string.replace("'", "")
		string = string.replace("Nombre", "\nNombre")
	return string