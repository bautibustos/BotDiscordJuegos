#! python3

import discord, time, logging, ApiRequest, os, sys, LecturaRetorno
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-',intents=intents)
"""
@bot.event
async def on_message(message):
	if message.content == 'sex':
		await message.add_reaction('\U0001F346')#berenjena
		await message.add_reaction('\U0001F351')#durazno
"""
def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)#metodo para reiniciar el bot

@bot.command(name ="reiniciar")
async def reiniciar(ctx):
    id = int(ctx.author.id)#guarda la id del que escribio el mensaje
    if id == 848254286437023805: #id mia 
        await ctx.send("Reiniciando el bot...")#el bot manda el mensaje si tenemos los permisos
        restart_bot()#se llama el metodo
    else:
    	await ctx.send("No tienes los permisos suficientes!")#manda este mensaje si no tenemos permiso

@bot.event
async def on_ready():
        print('\nBot iniciado!') # mira el comentario abajo >
        await bot.change_presence (activity=discord.Activity(type=discord.ActivityType.watching,
        name='Cómo NO jugar al CSGO #69 - || NICE')) # Esto es para poner el estado del bot

@bot.command(name="ping")
async def ping(ctx):
	print("ping")
	antes = time.monotonic()
	m=await ctx.send('Pong!')
	p1=(time.monotonic()-antes)*1000 #variable de tiempo
	p2=(str(p1).split('.'))[0]#para escribir nomas
	await m.edit(content=f'Pong! (ms={p2})')

@bot.command(name="juegos")
async def juegos(ctx):
	print(ctx.channel.id)
	if ctx.channel.id == 933035820657553510:
		embed = discord.Embed(title="Juegos Disponibles", description="Los juegos que estan aqui pueden ser obtenidos en paginas de 3eros para pagainas como steam o epic, queda bajo tu responsabilidad.", color=0xFF5733)
		await ctx.send(embed=embed)
		em =discord.Embed(title="Listado", description=ApiRequest.mandojuego(), color=0x3498db)
		await ctx.send(embed=em)
		em =discord.Embed(description="Con el comando **-id** + el numero de ID obtenés mas información del juego *(Ej: -id 8)*", color=0xe91e63)
		await ctx.send(embed=em)
	else:
		await ctx.send("Este no es el canal no es para mandar jueguitos, el corecto es **#lojueguito**.")#

@bot.command(name="id")
async def juegos(ctx, id):
	if ctx.channel.id == 933035820657553510:
		try:
			safe= LecturaRetorno.retornojuego(int(id))
			em = discord.Embed(
				title=f"{safe['title']}", 
				color=discord.Colour.fuchsia()
				)
			em.set_thumbnail(url=f"{safe['photo']}")
			em.add_field(
				name="Descripcion",
				value=f"{safe['description']}",
				inline=True
				)
			em.add_field(
				name="Plataforma",
				value=f"{safe['platform']}",
				inline=True
				)
			em.add_field(
				name="Link",
				value=f"{safe['link']}",
				inline=False
				)
			await ctx.send(embed=em)
		except:
			em =discord.Embed(title="**ErrorType:** Anda pa' alla' bobo.",description="Esa ID no está o la escribiste mal, tanto te va a costar???", color=0xe74c3c)
			em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1060940895349919836/1064701789716353117/messi-bobo.png")
			await ctx.send(embed=em)
	else:
		await ctx.send("Este no es el canal no es para mandar jueguitos, el corecto es **#lojueguito**.")#

my_file=open("SafeFiles\\token.txt", "r")
token=str(my_file.read())
bot.run(f"{token}")