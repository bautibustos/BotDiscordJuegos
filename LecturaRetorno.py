import json, os, sys

def retornojuego(id):
	with open("SafeFiles\\generado.json", "r") as File:
		diccio = json.load(File)#leo la lista
	devo=diccio[''][id]
	return devo
