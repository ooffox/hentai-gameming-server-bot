import os
import discord
import discord
import keep_alive
from discord.ext import commands
from discord.ext.commands import BucketType
import random
import json
import asyncio
import time
from discord.utils import get
from discord.errors import NotFound
from datetime import datetime
from discord.ext.commands import has_permissions
async def load(file):
	with open(file, 'r') as f:
		users = json.load(f)
	return users

prefixes = ['hg ', 'HG ', 'Hg ', 'hG ']
client = commands.Bot(command_prefix=prefixes, case_insensitive=True)
places = [
		{
				'name': "kirbek's drawer",
				"kirbek's drawer": {
						'earnings': [600, 1000],
						'chances of death':
						0.15,
						'death':
						"u tried to search for coins in kirbek, but gumanku caught you and banned you",
						'get coins':
						"u searched for coins in kirbek's drawer while he wasnt looking and got {} coins"
				}
		},
		{
				'name': "roni misclick group",
				"roni misclick group": {
						'earnings': [2000, 4000],
						'chances of death':
						0.30,
						'death':
						"while searching for coins in roni's misclick group, roni's alzheimers acted up and he misclicked. you died.",
						'get coins':
						"u searched for coins in roni's misclick group while making sure he didnt misclick call and got {} coins"
				}
		},
		{
				'name': "hundred games",
				"hundred games": {
						'earnings': [400, 500],
						'chances of death':
						0.5,
						'death':
						"instead of running away from the cornucopia, you went there for coins, but got killed by zychuu instead",
						'get coins':
						"u searched for coins in the cornucopia and found {} coins"
				}
		},
		{
				'name': "kuskus glasses",
				"kuskus glasses": {
						'earnings': [300, 350],
						'chances of death':
						0,
						'death':
						"",
						'get coins':
						"you scouted kuskus' glasses for coins and somehow found {} coins in the lens"
				}
		},
		{
				'name': "madrid scammer centre",
				"madrid scammer centre": {
						'earnings': [200, 550],
						'chances of death':
						0.06,
						'death':
						"u went to madrid scammer centre, but you got scammed by ofoz and you paid him with all your money",
						'get coins':
						"u went to madrid scammer centre and got {} coins while looking in one of the drawers of one of the desks"
				}
		},
		{
				'name': "konfident battle ring",
				"konfident battle ring": {
						'earnings': [1000, 2000],
						'chances of death':
						0.15,
						'death':
						"while slaying some konfidents, asandir suddenly comes in and hits you from behind, instantly killing u",
						'get coins':
						"u went to the konfident battle ring and won {} coins by slaughtering some konfidents"
				}
		},
		{
				'name': "tom scott's videos",
				"tom scott's videos": {
						'earnings': [200, 600],
						'chances of death':
						0,
						'death':
						"",
						'get coins':
						"u searched in tom scott's videos for coins and got {} of them"
				}
		},
		{
				'name': "north korea",
				"north korea": {
						'earnings': [300, 500],
						'chances of death':
						0.1,
						'death':
						"",
						'get coins':
						"you convinced kim jong un to give you {} coins after making a deal with him"
				}
		},
		{
				'name': 'besko sawmill',
				'besko sawmill': {
						'earnings': [230, 400],
						'chances of death':
						0.09,
						'death':
						'u were searching the besko windmill and despite this being statistically impossible, the sawmill just collapsed and u died.',
						'get coins':
						'u went to the besko windmill and got {} coins',
				}
		},
		{
				'name': 'wroclaw',
				'wroclaw': {
						'earnings': [150, 250],
						'chances of death':
						0,
						'death':
						'',
						'get coins':
						'u went to <:wroclove:711341810877988896> WROCLAW <:wroclove:711341810877988896> and got {} coins'
				}
		},
		{
				'name': 'psie pole',
				'psie pole': {
						'earnings': [160, 310],
						'chances of death':
						0.01,
						'death':
						'while having a stroll in psie pole, you were too deep in thought to realize you were about to drown in the oder river. youre dead.',
						'get coins':
						' while having a stroll around psie pole, you found {} coins lying on the ground (somehow)'
				}
		},
		{
				'name': 'besko',
				'besko': {
						'earnings': [50, 250],
						'chances of death': 0,
						'death': '',
						'get coins': 'u went to epic besko and got {} coins'
				}
		},
		{
				'name': 'spain',
				'spain': {
						'earnings': [100, 200],
						'chances of death': 0,
						'death': '',
						'get coins': 'you had fiesta in spain and got {} coins'
				}
		},
		{
				'name': 'pitus channel',
				'pitus channel': {
						'earnings': [3000, 4000],
						'chances of death':
						0.25,
						'death':
						'you, for some twisted stupid reason, decided to go to pitus channel and so you found so much cringe that you had a heart attack and fucking died',
						'get coins':
						'you, for some twisted stupid reason, decided to go to pitus channel but instead of finding cringe you found {} coins'
				}
		},
		{
				'name': 'nitro golden ball',
				'nitro golden ball': {
						'earnings':
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30000],
						'chances of death':
						0,
						'death':
						'',
						'get coins':
						"u went to roni's epic nitro giveaway and got AN ASTOUNDING TOTAL OF {} COINS!!!"
				}
		},
]

encounters = {
		'opponents': ['tom scott'],
		'tom scott': {
				'damage': [40, 80],
				'health': 800,
				'abilities': {
						'abilities': ['brain increase'],
						'brain increase': [100, 300]
				}
		}
}


@client.event
async def on_guild_join(guild: discord.Guild):
	user = client.get_user(392067878695993355)
	await user.send('hentai gameming bot has joined {}'.format(guild.name))

@client.command(aliases = ['link'], description = "send the bot's invite link. no arguments.")
async def invite(ctx):
	await ctx.send('https://discord.com/api/oauth2/authorize?client_id=754453718048702575&permissions=8&scope=bot')

@commands.cooldown(1, 2, BucketType.user)
@client.command(aliases = ['tom scott', 'tom'], description = 'fetches a random tom scott video. no arguments.')
async def tomscott(ctx):
	videos = await load('tomscott.json')
	await ctx.send(f'https://youtu.be/{random.choice(videos)}')



@client.command(aliases = ['ban suggest'], description = 'bans someone from suggesting. requires manage channels perm. format: {discord member}')
@has_permissions(manage_channels = True)
async def suggestban(ctx, *, user: discord.Member):
	suggestdata = await load('suggestdata.json')
	suggestdata['banned'].append(user)
	with open('suggestdata.json', 'w') as f:
		json.dump(suggestdata, f)
	await ctx.send(f'{user} banned from suggesting succesfully')



@commands.cooldown(1, 30, BucketType.user)
@client.command(aliases = ['suggestion'], description = 'suggests a prompt. format: {suggestion}')
async def suggest(ctx, *, suggestion):
	if ctx.guild.id != 640270238868439071:
		await ctx.send('bruh thats a hentai gameming exclusive command, smh')
		return
	data = await load('suggestdata.json')
	banned_list = data['banned']
	if ctx.author in banned_list:
		await ctx.send('sent for ofoz to check...')
		
		ofox = client.fetch_user(392067878695993355)
		
		msg = await ofox.send(suggestion)
		data['suggestions_on_hold'].append(msg.id)
		
		def check(message: discord.Message):
			return message.author == ofox and message.channel == channel.DMChannel and message.content.split(', ')[1].split('|')[0] == msg.id
			
		answer = await ofox.wait_for('message', check = check, timeout = 43200)
		answer = answer.content
		choice = answer.split(', ')[0]
		if choice.startswith('n'):
			try:
				reason = answer.split(', ')[1].split('|')[1]
			except IndexError:
				reason = None
			await ctx.author(f'your suggestion was denied. \nREASON: {reason}')
			return
	suggest_channel = await client.fetch_channel(782617738463674398)
	em = discord.Embed(title = ctx.author, description = suggestion)
	message = await suggest_channel.send(embed = em)
		
	await message.add_reaction('<:hardagree:679457361554964491>')
	await message.add_reaction('<:harddisagree:679457362049761321>')
	with open('suggestdata.json', 'w') as f:
	  json.dump(data, f)

@client.event
async def on_raw_reaction_add(payload):
  payload = payload.message
  szuflada = await client.fetch_channel(642862900129693707)
  suggest_channel = await client.fetch_channel(782617738463674398)
  if payload.channel.id != szuflada.id and payload.channel.id != suggest_channel.id:
    return
	
	if payload.channel == suggest_channel:
	  data = await load('suggestdata.json')
	  cleared = data['cleared_suggestions']
	  msg = payload.message
		
		hard_agrees = find(lambda m: m.name == 'hardagree', msg.reactions)
		
		hard_disagrees = find(lambda m: m.name == 'harddisagree', msg.reactions)
		
		if hard_agrees.count == 6 and hard_agrees.count > hard_disagrees.count and msg.id not in cleared:
			data['cleared_suggestions'].append(msg.id)
			await msg.edit(msg.content + '\n(ACCCEPTED)')
			asandir = client.fetch_user(181005010249842688)
			await asandir.send(msg.content)
			
	with open('suggestdata.json', 'w') as f:
	  json.dump(data, f)
			
	
	if payload.channel == szuflada:
	  msg = payload.message
			
		ufam = find(lambda m: m.name == 'ufam', msg.reactions)
			
		watpie = find(lambda m: m.name == 'watpie', msg.reactions)
		if ufam.count == 5 and ufam.count > watpie.count:
		  mikrofon = find(lambda m: m.name == 'mikrofon kirbka', ctx.guild.roles)
		  await msg.author.remove_roles(mikrofon)
			
@client.event
async def on_message(message: discord.Message):
	banned = [568804357793906707, 784931335508328519]
	if message.channel.id in banned:
		channel = client.get_channel(message.channel.id)
		history = await channel.history(limit = 2).flatten()
		id = history[1].id
		try:
			message1 = await channel.fetch_message(id)
			content1 = message1.content
			if ' ' in content1:
				content1 = message1.content.split(' ')[-1]
		except NotFound:
			await client.process_commands(message)
		try:
			if ' ' in message.content:
				msg = message.content.split(' ')
				for i in msg:
					num1 = int(i)
					num2 = int(content1)
					if num1 != num2 + 1:
						await message.delete()
					else:
						content1 = i
			else:
				content = message.content
				try:
					if int(content) != int(content1) + 1:
						await message.delete()
				except ValueError:
					await message.delete()
		except ValueError:
			await message.delete()
	channel = client.get_channel(642862900129693707)
	try:
		message = await channel.fetch_message(message.id)
		
		await message.add_reaction('<:watpie:643923871283806237>')
		await message.add_reaction('<:ufam:643923998224285739>')
		if '<@181005010249842688>' in message.content.lower():
			user = client.get_user(181005010249842688)
			await user.send(f'{message.author} just pinged you in {message.channel.name}: \n{message.content}')
	except NotFound:
		await client.process_commands(message)
		return
	await client.process_commands(message)
	return






client.remove_command('help')

@commands.cooldown(1, 120, BucketType.user)
@client.command(description = 'displays this command')
async def help(ctx):
	text = ''
	for command in client.commands:
		text += f'| {command}: {command.description} |\n'
	em = discord.Embed(title = 'HENTAI GAMEMING BOT HELP', description = text, color = discord.Color.red())
	await ctx.send(embed = em)




@commands.cooldown(1, 15, BucketType.user)
@client.command(description = 'quotes a person. format: {person}|{quote}')
async def quote(ctx, *, msg):
	msg = msg.split('|')
	message = '{}'.format(msg[1])
	em = discord.Embed(title = msg[0], description = message, color = discord.Color.red())
	await ctx.send(embed = em)





async def reset_bank(member):
	await get_bank_data()
	await open_account(member)
	bal = await update_bank(member)
	await update_bank(member, -bal[0])


async def reset_wallet(member):
	await get_bank_data()
	await open_account(member)
	bal = await update_bank(member)
	await update_bank(member, -bal[1], 'bank')


@client.command(description = 'chooses wisely between some options. format: {times you want it to choose}, {the options themselves}')
async def choose(ctx, times, *, options):
	options = options.split(', ')
	final = []
	while len(final) != int(times):
		answer = random.choice(options)
		if answer in final:
			continue
		final.append(answer)
	if len(final) == 1:
		reply = 'my gut tells me the right answer is {}.'
	else:
		reply = 'my gut tells me the right answers are '
		for i in range(len(final) - 2):
			reply += '{}, '
		reply += '{} '
		reply += 'and {}.'
	await ctx.send(reply.format(*final))


@client.event
async def on_ready():
	channel = client.get_channel(772933106768150540)
	print('Bot is ready.')
	await client.change_presence(
			activity=discord.Activity(
					type=discord.ActivityType.watching,
					name="jotaro steal the source code"))
	users = await get_bank_data()
	for user, contents in users.items():
		for key, value in contents.items():
			if ' variable' in key:
				users[user][key] = False
				channel = client.get_channel(772933106768150540)
	channel = client.get_channel(772933106768150540)
	while True:
		time = datetime.now()
		seconds = time.second + time.minute * 60 + time.hour * 3600
		seconds_left = 86400 - seconds
		await asyncio.sleep(seconds_left)
		await channel.send('https://tenor.com/view/happynewyear-2017-gif-7464363')
				



@client.command(description = '100% accurate hate meter between 2 people. format: {person1} {person2}')
async def hate(ctx, Member1, Member2):
	percent = str(random.randint(0, 100)) + '%'
	em = discord.Embed(title='hate meter')
	em.add_field(name=f'{Member1}, {Member2}', value=percent)
	await ctx.send(embed=em)


@hate.error
async def hate_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
		await ctx.send('wtf no')
	else:
		raise error


@client.command(description = '100% accurate dick length meter. format: {person: if empty, the user}')
async def dick(ctx, person):
	length = random.randint(1, 25)
	if 'jotaro' in person.lower():
		length = 0.1
	await ctx.send(f'{person} has a dick length of {length} cm')


@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(description = 'scouts a place. no arguments.')
async def search(ctx):
	def check(message: discord.Message):
		return message.channel == ctx.channel and message.author == ctx.author

	death = random.random()
	place = random.choice(places), random.choice(places), random.choice(places)
	while place[0] == place[1] or place[0] == place[2] or place[1] == place[2]:
		place = random.choice(places), random.choice(places), random.choice(
				places)

	await ctx.send(f'where do u want to search?')
	await ctx.send(
			f"{place[0]['name']}, {place[1]['name']} or {place[2]['name']}")
	place = place[0]['name'], place[1]['name'], place[2]['name']
	answer = await client.wait_for('message', check=check, timeout=15)
	answer = answer.content.lower()
	if answer in place:
		index = 0
		for i in places:
			if answer != places[index]['name']:
				index += 1
			elif answer == places[index]['name']:
				break

		if death <= places[index][answer]['chances of death']:
			await reset_wallet(ctx.author)
			await ctx.send(places[index][answer]['death'])
			return
		coins = random.randint(places[index][answer]['earnings'][0],
													 places[index][answer]['earnings'][1])
		if answer == 'nitro golden ball':
			coins = random.choice(places[index][answer]['earnings'])
		await ctx.send(places[index][answer]['get coins'].format(coins))
		await update_bank(ctx.author, coins)
	else:
		await ctx.send(
				'mate are u fucking gay?? why are u trying to search that')


@search.error
async def search_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
		em = discord.Embed(
				title=
				"mate, stop doing things so quickly. this command is on a cooldown, and **{:.2f} seconds** are left until u can use it again."
				.format(error.retry_after),
				color=discord.Color.purple())
		await ctx.send(embed=em)
	else:
		raise error


@client.command(description = 'deletes all your bank/wallet money. no arguments')
async def pis(ctx):
	def check(message: discord.Message):
		return message.channel == ctx.channel and message.author == ctx.author

	await ctx.send('bro are u sure? `Y/N`')
	answer = await client.wait_for('message', check=check, timeout=15)
	bal = await update_bank(ctx.author)
	if answer.content.lower() == 'y' or answer.content.lower() == 'yes':
		await update_bank(ctx.author, -bal[0])
		await update_bank(ctx.author, -bal[1], 'bank')
		await ctx.send('u have lost all ur money lol')
	else:
		await ctx.send('ight gotchu fam')


@client.command(description = 'makes it so that you can fight with another discord member. pretty shitty and buggy, but i honestly dont give a slight fuck. format: {member who you want to fight}')
async def fight(ctx, member: discord.Member):
	turn = ctx.author

	def check(message: discord.Message):
		return message.author == turn and message.channel == ctx.channel

	current_turn = 1
	people = {
			ctx.author: {
					'health': 100,
					'heals': 3,
					'damage': 1.0,
					'defend': 0,
					'buff': current_turn,
					'defend_turns': current_turn
			},
			member: {
					'health': 100,
					'heals': 3,
					'damage': 1.0,
					'buff': current_turn,
					'defend': 0,
					'defend_turns': current_turn
			}
	}
	target = member
	protection = 0
	buff = 1
	while people[turn]['health'] > 0 and people[target]['health'] > 0:
		damage = abs(round(
				random.randint(2, 45) * people[turn]['damage'] -
				people[turn]['defend']))
		await ctx.send(
				f"{member}'s health: {people[member]['health']} \n{ctx.author}'s health: {people[ctx.author]['health']} \n{turn}'s turn, options are: buff up, defend, punch and heal (turn number {current_turn})"
		)
		answer = await client.wait_for('message', check=check, timeout=15)
		answer = answer.content.lower()
		if answer.startswith('p'):
			people[target]['health'] -= damage
			await ctx.send(
					f'{turn} went full cunt mode and attacked {target}, dealing {damage} HP.'
			)
		elif answer.startswith('d'):
			if current_turn < people[turn]['defend_turns']:
				await ctx.send(
						f'nah mate defend is on a cooldown for u rn, {people[turn]["defend_turns"] - current_turn} turns are left until you can use it again'
				)
				continue
			people[turn]['defend_turns'] += 6
			protect_amt = random.randint(1, 20)
			people[turn]['defend'] += protect_amt
			await ctx.send(
					f'{turn} protects himself by {protect_amt} points lol, bit of a pussy move but ok'
			)
		elif answer.startswith('b'):
			if current_turn < people[turn]['buff']:
				await ctx.send(
						f'nah mate buff is on a cooldown for u rn, {people[turn]["buff"] - current_turn} turns are left until you can use it again'
				)
				continue
			people[turn]['buff'] += 6
			buff_amt = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
			buff += random.choice(buff_amt)
			await ctx.send(
					f'{turn} buffs up and his attacks now deal ×{buff} the original damage, the cunt strong now'
			)
		elif answer.startswith('h'):
			if people[turn]['heals'] == 0:
				await ctx.send('mate u got no heals left')
				continue
			people[turn]['heals'] -= 1
			heal = random.randint(1, 45)
			people[turn]['health'] += heal
			await ctx.send(
					f'{turn} used a heal and recovered {heal} health points. mega pussy move there but ok'
			)
		else:
			continue
		if turn == ctx.author:
			turn = member
			target = ctx.author
		elif turn == member:
			turn = ctx.author
			target = member
		current_turn += 1
	if people[member]['health'] <= 0:
		await ctx.send(
				f'yoooo {ctx.author} just won against {member} by {people[ctx.author]["health"]} points, pog'
		)
	if people[ctx.author]['health'] <= 0:
		await ctx.send(
				f'yoooo {member} just won against {ctx.author} by {people[member]["health"]} points, pog'
		)


@client.command(description = 'chooses a member for a prompt. format: {prompt}')
async def who(ctx, *, thing):
	people = [
			member.name for member in ctx.guild.members if member.bot == False
	]
	thing = ' '.join(thing[:])
	if 'is a code thief' in thing.lower():
		people = ['King K. Kool']
	elif 'chuj' in thing.lower() and 'not chuj' not in thing.lower():
		people = ['Zychuj']
	elif 'nerd' in thing.lower() and 'not nerd' not in thing.lower():
		people = ['KusKus']
	await ctx.send('{} {}'.format(random.choice(people), thing))






@client.event
async def on_ready():
	channel = client.get_channel(772933106768150540)
	print('Bot is ready.')
	await client.change_presence(
			activity=discord.Activity(
					type=discord.ActivityType.watching,
					name="jotaro steal the source code"))


#dont think this even works for some reason lol
@client.event
async def on_member_remove(ctx, member: discord.Member):
	await ctx.send(f':crab: {member} is gone :crab:')


#8ball



@client.command(aliases=['8ball', 'ball8'], description = 'eightball. no arguments.')	#"aliases" are basically just other names for the command.
async def eightball(ctx):
	things = [
		'yeah lol', 'no',
		'what a cunt',
		'yes', 'of course not'
]
	await ctx.send(random.choice(things))


@client.command(description = 'displays ping. no arguments')
async def ping(ctx):
	await ctx.send(
			f'ping is {round(client.latency * 1000)}ms'
	)	#explains itself. gets the ping, rounds it up and sends it


#this code is absolute spaghetti i wont bother explaining it
@client.command(description = 'flips a coin. format: {face}, {amount you want to bet (default is 0)}')
async def coin(ctx, face=None, amount=0):
	users = await get_bank_data()
	user = ctx.author
	bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']]
	await open_account(user)
	chance = random.randint(0, 101)
	final = ''
	faces = ['tails', 'heads']
	correctface = False
	face = face.lower()
	if face in faces:
		correctface = True
	if correctface == False:
		await ctx.send(
				'hey cunt, tell me whether ure picking heads or tails next time will u'
		)
		return
	if 'spanish bull sperm variable' not in users[str(ctx.author.id)]:
		await update_value(ctx.author, 'spanish bull sperm variable', False)
	if users[str(ctx.author.id)]['spanish bull sperm variable'] == True:
		faces += [face.lower()]
	amount = int(amount)
	if amount > 150:
		await ctx.send(
				"lol dont try to bet more than 150 coins if i allowed u to do that the command would be busted"
		)
		return
	if bal[0] < amount:
		await ctx.send(
				'aye cunt thats bullshit, u cant bet that much with the current coins in ur wallet'
		)
		return
	if amount <= 0:
		await ctx.send('my man over here trying to bet lower than 0 coins smh')
	final = random.choice(faces)
	em = discord.Embed(
			title=f"coin's face: **{final}**", color=discord.Color.green())
	if face == final:
		win = True
	elif face != final:
		win = False
	if win == True:
		em.add_field(name='u won! Amount gained:', value=amount)
		await update_bank(user, amount)
		await ctx.send(embed=em)
	if win == False:
		em.add_field(name='u lost! Amount lost:', value=amount)
		await update_bank(user, -amount)
		await ctx.send(embed=em)


#balance command
@client.command(aliases=['bal'], description = 'displays balance. no arguments.')
async def balance(ctx):
	await open_account(ctx.author)

	user = ctx.author

	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]
	bank_amt = users[str(user.id)]["bank"]

	em = discord.Embed(
			title=f"{ctx.author.name}'s balance", color=discord.Color.green())
	em.add_field(name="wallet balance", value=wallet_amt)
	em.add_field(name="bank balance", value=bank_amt)

	await ctx.send(embed=em)


#beg command


@commands.cooldown(
		1, 15, commands.BucketType.user
)	#the first parameter sets how much times the command can be used before cooldown, the second parameter the seconds the cooldown lasts and the third is some weird shit. dont worry though, the third parameter should always just be "commands.BucketType.user" so u can just copy and paste it when u want to set a cooldown
@client.command(description = 'begs for coins. no arguments.')
async def beg(ctx):
	await open_account(ctx.author)
	users = await get_bank_data()
	death = random.random()
	if death >= 0.995:
		await reset_wallet(ctx.author)
		await ctx.send(
				'while begging, roni came up, told you to stop whining like a bitch, whipped out a gun and killed you'
		)
		return
	user = ctx.author
	people = [
			member.name for member in ctx.guild.members if member.bot == False
	]
	if "kirbek's cp folder variable" not in users[str(user.id)]:
		await update_value(ctx.author, "kirbek's cp folder variable", False)
	if users[str(user.id)]["kirbek's cp folder variable"] == True:
		for i in range(len(people)):
			people += ['KingKirbek']
	person = random.choice(people)
	earnings = random.randint(1, 101)
	if person == 'KingKirbek':
		earnings = random.randint(100, 600)

	await ctx.send(f'lol, {person} gave u {earnings} coins')
	await update_bank(ctx.author, earnings, 'wallet')


#the following is an error handler i found on stack overflow for when someone tries to call a command when its on cooldown
@beg.error
async def beg_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
		em = discord.Embed(
				title=
				"mate, stop doing things so quickly. this command is on a cooldown, and **{:.2f} seconds** are left until u can use it again."
				.format(error.retry_after),
				color=discord.Color.purple())
		await ctx.send(embed=em)
	else:
		raise error


#withdraw command
@client.command(aliases=['with'], description = 'withdraws money from the bank. format: {amount, normally set to all}')
async def withdraw(ctx, amount='all'):
	await open_account(ctx.author)	#opens up the user's bank data
	bal = await update_bank(ctx.author)
	type = isinstance(amount, str)
	if amount == 'all' or amount == 'All':
		await ctx.send(f'lol u withdrew {bal[0]} coins')
		await update_bank(ctx.author, bal[0], 'bank')
		await update_bank(ctx.author, -bal[0])
		return
	try:
		amount = int(amount)
	except ValueError:
		await ctx.send('mate wtf? thats a word u cant withdraw that')
		return
	if amount > bal[
			1]:	#checks the bank to see if the amount that the user inputted makes sense
		await ctx.send(
				'u abolute spanner u dont have that many coins in ur bank yet mate'
		)
		return
	if amount < 0:	#checks to see if the amount is negative
		await ctx.send(
				'u cunt, are u really trying to withdraw negative amounts of money? '
		)
		return
	if amount == 0:
		await ctx.send('congratulations u have withdrawn absolutely nothing')
		return
	await update_bank(ctx.author, amount, 'wallet')
	await update_bank(ctx.author, -1 * amount, 'bank')
	await ctx.send(f'lol u withdrew {amount} coins')


#gamble lol
@commands.cooldown(1, 7, commands.BucketType.user)
@client.command(aliases=['gamble'], description = 'gambles some money. format: {amount}')
async def bet(ctx, amount=None):
	await open_account(ctx.author)
	users = await get_bank_data()
	if amount == None:
		await ctx.send(
				'aye mate put some amount to withdraw at the very least will u')
		return
	bal = await update_bank(ctx.author)
	amount = int(amount)
	if amount > int(
			bal[0]
	):	#btw u dont need to put int(bal[0]), u can just put bal[0] its the same thing i just wrote int(bal[0]) because for some reason i thought not formatting it into an int was the cause of an error i had gotten
		await ctx.send(
				'u abolute spanner u dont have that many coins in ur wallet yet mate'
		)
		return
	if amount < 0:
		await ctx.send(
				'u cunt, are u really trying to gamble negative amounts of money? '
		)
		return
	if amount == 0:
		await ctx.send('congratulations u have gambled absolutely nothing')
		return
	urdice = random.randint(1, 10)
	hgdice = random.randint(1, 10)
	if 'spanish bull sperm variable' not in users[str(ctx.author.id)]:
		await update_value(ctx.author, 'spanish bull sperm variable', False)
	if users[str(ctx.author.id)]['spanish bull sperm variable'] == True:
		hgdice = random.randint(1, 8)

	if urdice > hgdice:
		em = discord.Embed(
				title=f"u won! ({ctx.author})", color=discord.Color.blue())

		em.add_field(name="hentai gamemer's dice roll:", value=hgdice)
		em.add_field(name="ur dice roll:", value=urdice)

		await update_bank(ctx.author, amount, 'wallet')

		await ctx.send(embed=em)

	elif urdice == hgdice:
		em = discord.Embed(
				title=f"u tied! ({ctx.author})", color=discord.Color.green())

		em.add_field(name="hentai gamemer's dice roll", value=hgdice)

		em.add_field(name="ur dice roll", value=urdice)

		await ctx.send(embed=em)

	elif hgdice > urdice:
		em = discord.Embed(
				title=f"u lost! ({ctx.author})", color=discord.Color.red())

		em.add_field(name="hentai gamemer's dice roll:", value=hgdice)

		em.add_field(name="ur dice roll:", value=urdice)

		await update_bank(ctx.author, -amount, 'wallet')

		await ctx.send(embed=em)


@bet.error
async def bet_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
		em = discord.Embed(
				title=
				"mate, stop doing things so quickly. this command is on a cooldown, and **{:.2f} seconds** are left until u can use it again."
				.format(error.retry_after),
				color=discord.Color.purple())
		await ctx.send(embed=em)
	else:
		raise error


#slots
@commands.cooldown(1, 7, commands.BucketType.user)
@client.command(aliases=['slot'], description = 'slots. format: {amount}')
async def slots(ctx, amount=None):
	users = await get_bank_data()
	await open_account(ctx.author)
	if amount == None:
		await ctx.send(
				'aye mate put some amount to gamble at the very least will u')
		return
	bal = await update_bank(ctx.author)
	amount = int(amount)
	if amount > int(bal[0]):
		await ctx.send(
				'u abolute spanner u dont have that many coins in ur wallet yet mate'
		)
		return
	if amount < 0:
		await ctx.send(
				'u cunt, are u really trying to gamble negative amounts of money? '
		)
		return
	if amount == 0:
		await ctx.send('congratulations u have gambled absolutely nothing')
		return
	final = []
	if 'spanish bull sperm variable' not in users[str(ctx.author.id)]:
		await update_value(ctx.author, 'spanish bull sperm variable', False)
	slot = [
			'roni', 'roni', 'gumanku', 'gumanku', 'gumanku', 'kirbek', 'kirbek',
			'kirbek', 'asandir'
	]
	if users[str(ctx.author.id)]['spanish bull sperm variable'] == True:
		slot = [
				'roni', 'roni', 'roni', 'gumanku', 'kirbek', 'kirbek', 'roni',
				'gumanku'
		]
	for i in range(3):
		a = random.choice(slot)
		final.append(a)
	if final == ['roni', 'roni', 'roni']:
		reward = amount * 4
		em = discord.Embed(
				title=f"u won! {final} ({ctx.author})", color=discord.Color.blue())
		em.add_field(name="Amount won", value=reward)

		await update_bank(ctx.author, reward, 'wallet')

		await ctx.send(embed=em)
	if final == ['kirbek', 'kirbek', 'kirbek']:
		reward = amount * 3
		em = discord.Embed(
				title=f"u won! {final} ({ctx.author})", color=discord.Color.blue())
		em.add_field(name="Amount won", value=reward)
		await update_bank(ctx.author, reward, 'wallet')

		await ctx.send(embed=em)
	if final == ['gumanku', 'gumanku', 'gumanku']:
		reward = amount * 2
		em = discord.Embed(
				title=f"u won! {final} ({ctx.author})", color=discord.Color.blue())
		em.add_field(name="Amount won", value=reward)

		await update_bank(ctx.author, reward, 'wallet')
		await ctx.send(embed=em)

	if final == ['asandir', 'asandir', 'asandir']:
		reward = amount * 2
		em = discord.Embed(
				title=f"u lost! {final} ({ctx.author})", color=discord.Color.red())
		em.add_field(name="Amount lost", value=99999999999999999999999999999)
		await update_bank(ctx.author, -bal[1], 'bank')
		await update_bank(ctx.author, -int(bal[0]), 'wallet')

		await ctx.send(embed=em)

	else:
		punishment = amount
		em = discord.Embed(
				title=f"u lost! {final} ({ctx.author})", color=discord.Color.red())
		em.add_field(name="Amount lost", value=punishment)
		await update_bank(ctx.author, punishment, 'wallet')

		await ctx.send(embed=em)


@slots.error
async def slots_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
		em = discord.Embed(
				title=
				"mate, stop doing things so quickly. this command is on a cooldown, and **{:.2f} seconds** are left until u can use it again."
				.format(error.retry_after),
				color=discord.Color.purple())
		await ctx.send(embed=em)
	else:
		raise error


#give command
@client.command(aliases=['share'], description = 'gives a discord member some money. format: {discord member} {amount}')
async def give(ctx, member: discord.Member, amount=None):
	await open_account(ctx.author)
	await open_account(member)
	if amount == None:
		await ctx.send(
				'aye mate put some amount to withdraw at the very least will u')
		return
	bal = await update_bank(ctx.author)
	amount = int(amount)
	if amount > bal[1]:
		await ctx.send(
				'listen i know u want to help the poor out but u cant really do that if ure poor too'
		)
		return
	if amount < 0:
		await ctx.send(
				'is it even possible to give someone negative amounts of money')
		return
	if amount == 0:
		await ctx.send(
				'u gave them 0 coins!!!!! wow!!!!!!! how generous!!!!!!!!')
		return
	await update_bank(ctx.author, -1 * amount, 'bank')
	await update_bank(member, amount, 'bank')
	await ctx.send(f'u gave {member} {amount} coins')


#deposit command
@client.command(aliases=['dep'], description = 'deposits some money into your bank. format: {amount, default set to all}')
async def deposit(ctx, amount='all'):
	await open_account(ctx.author)
	bal = await update_bank(ctx.author)
	type = isinstance(amount, str)
	if amount == 'all' or amount == 'All':
		await ctx.send(f'lol u withdrew {bal[0]} coins')
		await update_bank(ctx.author, -bal[1], 'bank')
		await update_bank(ctx.author, bal[1])
		return
	if amount != 'all' or amount != 'All' and type:
		await ctx.send('u cunt are u retarded? u cant deposit words')
	amount = int(amount)
	if amount > int(bal[0]):

		await ctx.send(
				'u abolute spanner u dont have that many coins in ur wallet yet')
		return
	if amount < 0:
		await ctx.send(
				'u cunt, are u really trying to deposit negative amounts of money? '
		)
		return
	if amount == 0:
		await ctx.send('congratulations u have deposited absolutely nothing')
		return
	await update_bank(ctx.author, amount, 'bank')
	await update_bank(ctx.author, -amount, 'wallet')
	await ctx.send(f'lol u deposited {amount} coins')


#opens up the bank data of a specific user
async def open_account(user):
	users = await get_bank_data()

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0
		users[str(user.id)]["kirbek's_cp_folder variable"] = False

	with open("mainbank.json", "w") as f:
		json.dump(users, f)
	return True


#loads the bank data
async def get_bank_data():
	with open('mainbank.json', 'r') as f:
		users = json.load(f)

	return users


#updates the bank
async def update_bank(
				user, change=0, mode='wallet'
):	#the "user" parameter is for what user's balance u want to change, "change" is for how much and "mode" is for either "bank" or "wallet"
	users = await get_bank_data()

	users[str(user.id)][mode] += change

	with open("mainbank.json", "w") as f:
		json.dump(users, f)
	bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']]
	return bal






mainshop = [
		{
				'name':
				"kirbek's cp folder",
				'price':
				1500,
				'description':
				"kirbek's folder full of cp in which he masturbates off of every day. makes u more likely to receive coins from kirbek when u beg and the money u receive from kirbek is higher as u blackmail him to give u more coins. effect lasts for 6 hours.",
				'time':
				21600
		},
		{
				'name':
				'spanish bull sperm',
				'price':
				5000,
				'description':
				'fresh, nice spanish bull sperm from the finest bull sperm factories in madrid. when you drink it, you will have higher odds of winning anything related to a bet. lasts 2 hours.',
				'time':
				7200
		}
]


@client.command(description = 'displays shop. no arguments.')
async def shop(ctx):
	em = discord.Embed(title='shop')
	for item in mainshop:
		name = item['name']
		price = item['price']
		desc = item['description']
		em.add_field(name=name, value=f'**{price} coins** \n{desc}')

	await ctx.send(embed=em)


@client.command(description = '{amount of money} {item name}')
async def buy(ctx, amount=1, *, item):
	await open_account(ctx.author)

	res = await buy_this(ctx.author, item, amount)

	if not res[0]:
		if res[1] == 1:
			await ctx.send(
					'hey cunt why are u trying to buy an item that doesnt exist')
			return
		if res[1] == 2:
			await ctx.send(
					f'absolute retarded spanner, u dont have enough money in ur wallet to buy that'
			)
			return
	item = item.split(' ')
	message = 'uve bought {} of '
	for i in range(len(item)):
		message += '{} '
	await ctx.send(message.format(amount, *item))


@client.command(aliases=['bag', 'inv'], description = 'displays inventory. no arguments.')
async def inventory(ctx):
	await open_account(ctx.author)
	user = ctx.author
	users = await get_bank_data()

	try:
		inventory = users[str(user.id)]['inventory']
	except:
		inventory = []

	em = discord.Embed(title='Inventory')
	for item in inventory:
		name = item['item']
		amount = item['amount']

		em.add_field(name=name, value=amount)

	await ctx.send(embed=em)


async def buy_this(user, item_name, amount):
	item_name = item_name.lower()
	name_ = None
	for item in mainshop:
		name = item['name'].lower()
		if name == item_name:
			name_ = name
			price = item['price']
			break

	if name_ == None:
		return [False, 1]

	cost = price * amount

	users = await get_bank_data()

	bal = await update_bank(user)

	if bal[0] < cost:
		return [False, 2]

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]['inventory']:
			n = thing['item']
			if n == item_name:
				old_amt = thing['amount']
				new_amt = old_amt + amount
				users[str(user.id)]['inventory'][index]['amount'] = new_amt
				t = 1
				break
			index += 1
		if t == None:
			obj = {'item': item_name, 'amount': amount}
			users[str(user.id)]['inventory'].append(obj)
	except:
		obj = {'item': item_name, 'amount': amount}
		users[str(user.id)]['inventory'] = [obj]

	with open('mainbank.json', 'w') as f:
		json.dump(users, f)

	await update_bank(user, -cost, 'wallet')

	return [True, 'Worked']


@client.command(description = 'sells an item. format: {amount} {item name}')
async def sell(ctx, amount, *, item):
	await open_account(ctx.author)

	res = await sell_this(ctx.author, item, amount)

	if not res[0]:
		if res[1] == 1:
			await ctx.send('that object doesnt exist mate')
			return
		if res[1] == 2:
			await ctx.send(f'u dont have {amount} of that item mate')
			return
		if res[1] == 3:
			await ctx.send('u dont have that in ur inventory mate')
			return

	await ctx.send(f'u just sold {amount} of {item} lol')


async def sell_this(user, item_name, amount, price=None):
	item_name = item_name.lower()
	name_ = None
	for item in mainshop:
		name = item['name'].lower()
		if name == item_name:
			name_ = name
			if price == None:
				price = item['price']
			break

	if name_ == None:
		return [False, 1]

	cost = price * amount * 0.80

	users = await get_bank_data()

	bal = await update_bank(user)

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]['inventory']:
			n = thing['item']
			if n == item_name:
				old_amt = thing['amount']
				new_amt = old_amt - amount
				if new_amt < 0:
					return [False, 2]
				users[str(user.id)]['inventory'][index]['amount'] = new_amt
				t = 1
				break
			index += 1
		if t == None:
			return [False, 3]
	except:
		return [False, 3]

	with open('mainbank.json', 'w') as f:
		json.dump(users, f)

	await update_bank(user, cost, 'wallet')

	return [True, 'Worked']


async def update_value(user, item, value):
	users = await get_bank_data()
	await open_account(user)

	users[str(user.id)][item] = value

	with open("mainbank.json", "w") as f:
		json.dump(users, f)
	return users[str(user.id)][item]


@client.command(aliases=['rank'], description = '{prompt} {member}')
async def percentage(ctx, condition, *, member):
	em = discord.Embed(
			title=f'{member} is {random.randint(0, 100)}% {condition}',
			color=discord.Color.blue())
	await ctx.send(embed=em)


@client.command(description = 'uses an item. format: {item_name}')
async def use(ctx, *, item_name):
	await open_account(ctx.author)
	user = ctx.author
	users = await get_bank_data()
	place = users[str(user.id)]

	res = await sell_this(ctx.author, item_name, 1, 0)

	if not res[0]:
		if res[1] == 1:
			await ctx.send('that object doesnt exist mate')
			return
		if res[1] == 2:
			await ctx.send(f'u dont have that item in ur inventory mate')
			return
		if res[1] == 3:
			await ctx.send('u dont have that in ur inventory mate')
			return

	index = 0
	item_name = item_name.lower()
	name_ = None
	for item in mainshop:
		name = item['name'].lower()
		if name != item_name:
			index += 1
		elif name == item_name:
			name_ = name
			break
	if name_ == None:
		await ctx.send('ey cunt at least tell me wtf you using')
		return
	name = item_name + ' variable'
	if name not in place:
		await update_value(ctx.author, name, False)
	await update_value(ctx.author, name, True)
	await ctx.send(
			f"you have used {mainshop[index]['name']}. you will get a dm when the effect wears off if the item has a non-permanent effect"
	)
	await asyncio.sleep(mainshop[index]['time'])
	await update_value(ctx.author, name, False)
	await ctx.author.send(f"the item {mainshop[index]['name']} has worn off")

token = os.environ.get("DISCORD_BOT_SECRET")
keep_alive.keep_alive()

client.run(token)