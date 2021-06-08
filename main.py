import discord
import random
import os
from keep_alive import keep_alive


client = discord.Client()

Workouts = ["Pushups", "Sit-ups", "Squats", "Lunges"]
Pushups = ["Regular", "Diamond", "Wide"]
Sit_Ups = ["Crunches", "Leg Raises", "Roman Twists", "Bicycle Twists"]
Lunges = ["Front", "Back"]

def workout1():
  reps = random.randint(5,10)
  workout = random.choice(Workouts)
  sets = random.randint(1,3)
  return(f'Do {reps} reps of {workout} for {sets} sets')

def workout2():
  reps = random.randint(10,20)
  workout = random.choice(Workouts)
  sets = random.randint(1,3)
  return(f'Do {reps} reps of {workout} for {sets} sets')

def workout3():
  reps = random.randint(25,35)
  workout = random.choice(Workouts)
  sets = random.randint(1,3)
  return(f'Do {reps} reps of {workout} for {sets} sets')

def push_up():
  pushup = random.choice(Pushups)
  return(f'Try doing some {pushup} pushups today')

def sit_up():
  situp = random.choice(Sit_Ups)
  return(f'Try doing some {situp} for today')

def lunge():
  Lunge = random.choice(Lunges)
  return(f'Try doing some {Lunge} lunges today')

@client.event
async def on_ready():
  print('We have logged in as{0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!easy'):
    exercise = workout1()
    await message.channel.send(exercise)

  if msg.startswith('!med'):
    exercise = workout2()
    await message.channel.send(exercise)

  if msg.startswith('!hard'):
    exercise = workout3()
    await message.channel.send(exercise)

  if msg.startswith('!push'):
    push = push_up()
    await message.channel.send(push)

  if msg.startswith('!sit'):
    sit = sit_up()
    await message.channel.send(sit)

  if msg.startswith('!lunge'):
    lun = lunge()
    await message.channel.send(lun)

keep_alive()
client.run(os.getenv('TOKEN'))