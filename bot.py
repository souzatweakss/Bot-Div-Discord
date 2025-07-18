import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

    try:
        with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
            mensagem = arquivo.read().strip()
    except FileNotFoundError:
        print("❌ Arquivo 'mensagem.txt' não encontrado.")
        return

    for guild in bot.guilds:
        enviadas = 0
        falhas = 0

        print(f"\n📣 Enviando mensagens para: {guild.name} ({guild.id})")

        for member in guild.members:
            if member.bot:
                continue

            try:
                await member.send(mensagem)
                enviadas += 1
                print(f"[✅] Enviado para: {member} ({member.id})")
            except discord.Forbidden:
                falhas += 1
                print(f"[❌] Bloqueado: {member} ({member.id})")
            except Exception as e:
                falhas += 1
                print(f"[⚠️] Erro ao enviar para {member} ({member.id}): {e}")


        print(f"\nResumo - {guild.name}: ✅ {enviadas} | ❌ {falhas}")

bot.run('')
