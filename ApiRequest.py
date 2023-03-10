import requests, json, os

#https://www.gamerpower.com/api-read pagina de documentacion

URL = "https://www.gamerpower.com/api/"
def mandojuego():
	data = requests.get(f"{URL}/giveaways?sort-by=value")#
	print(data)
	if data.status_code == 200:
		data_json= data.json()
		titulo=[]
		tipo=[]
		link=[]
		plat = []
		imagen=[]
		idgame=[]
		desc=[]
		cont=0
		for i in data_json:
			titulo.append(i['title'])
			tipo.append(i['type'])
			link.append(i['open_giveaway'])
			plat.append(i['platforms'])
			imagen.append(i['image'])
			desc.append(i['description'])
############ aca se guarda todo en archivo #############
		SaveFile={}
		SaveFile['']=[]
		for i in range(len(titulo)):
			if tipo[i]!='DLC':#		Filtro para que no muestre los que son dlc
				#idgame.append(cont)
				SaveFile[''].append({
					#"id":(f"ID {idgame[cont]}"),
					"title": titulo[i],
					"platform": plat[i],
					"photo": imagen[i],
					"link": f"{link[i]} ",
					"description":desc[i]
					})
			#cont=cont+1# 		contador para generar la id                     #(juego[''][2])
		with open("SafeFiles\\generado.json", "w") as archivo:
			json.dump(SaveFile,archivo)

############ Aca se genera todo el texto que se muestra ###############
		juego={}
		juego['']=[]
		for i in range(len(titulo)):
			if tipo[i]!='DLC':#		Filtro para que no muestre los que son dlc
				idgame.append(cont)
				juego[''].append({
					"id°":(f"**ID {idgame[cont]}°°**"),
					"": titulo[i],
					})
				cont=cont+1#contador para generar la id

		#lo siguiente genera toda la cadena de escritura 
		string = str(juego['']); string = string.replace("{", ""); string = string.replace("}", ""); string = string.replace("[", ""); string = string.replace("]", ""); string = string.replace("id°", "\n"); string = string.replace("'", ""); string = string.replace(":", ""); string = string.replace(",", ""); string = string.replace("°°", ":"); string = string.replace("Giveaway", "")
		#
	return string