import discord
import os
import requests
import json
import random
import time
client = discord.Client()
# ALL CALLED FUNCTIONS ARE HERE

#----- TRIVIA API CALL

#def trivia(dif):
  #   if, create new open trivia with custom parameters and paste the link here.
  #   check for any parameters problems in json returned.

  #---- LINKS ----#

  #https://opentdb.com/api.php?amount=1&category=18&difficulty=medium

  #https://opentdb.com/api.php?amount=1&difficulty=medium
  
  
  #response = requests.get("https://opentdb.com/api.php?amount=1&difficulty="+dif)
  #json_data = json.loads(response.text)
  
  #quote = [i['question']for i in json_data['results']]
  #quote=str(quote)
  #quote="*Question:*"+"```\n"+quote[1:-1]+"\n ```"
  
  
  #ans1=[i['incorrect_answers']for i in json_data['results']]
  #ans1=str(ans1)
  #ans1=ans1[2:-2]
  #ans2= [i['correct_answer']for i in json_data['results']]
  #ans2=str(ans2)
  #ans2=ans2[1:-1]
  #ans="*Choices:*```\n"+str(ans1)+", "+str(ans2)+"```"
    #"```Category: " + + "\n" + str(json_data['results']['type']) + "\n" + str(json_data['results']['question'])+"\n"  + str(json_data['results']['correct_answer'])+"```"
  #try twopart
  #except:
  #quote = "```Category: " + json_data['results']['category']  + "\n" + str(json_data['results']['type']) +  " ```"
  #  return(quote+ans) 


#----- CVD STATE WISE API FUNC (DOESNT WORK)
def cvd_states():
  response = requests.get("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
  json_data = json.loads(response.text)
  #Region_read=[
  #    "region",
  #    "totalInfected",
  #    "newInfected",
  #    "recovered",
  #    "newRecovered",
  #    "deceased",
  #    "newDeceased"]
  #a= (json_data["regionData"])
  #length=len([d for d in a])
  #sent=" "
  #for i in range(length):
  #  for j in Region_read:
  #    line=(str(j) + "- " +dict(a[i][j]))
  #    sent=sent+str(line)

  quote = "```" + "Covid India Info" +"\n" +"Source: ```" + (json_data['sourceUrl'])  +"\n```" + "active Cases: " + "\t" +"\t" +str(json_data["activeCases"]) + "```"

  return (quote)   

#----- COVID INDIA STATS API FUNC
def cvd_india():
  response = requests.get("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
  #Region_read=[
  #    "region",
  #    "totalInfected",
  #    "newInfected",
  #    "recovered",
  #    "newRecovered",
  #    "deceased",
  #    "newDeceased"]

  json_data = json.loads(response.text)

  quote = "```" + "Covid India Info" +"\n" +"Source: ```" + (json_data['sourceUrl'])  +"\n```" + "active Cases: " + "\t" +"\t" +str(json_data["activeCases"]) +"\n" + "active Cases New: "  +"\t" + str(json_data["activeCasesNew"])  + "\n" + "total Cases: " +"\t" +"\t" + str(json_data['totalCases']) +"\n" + "recovered: " +"\t"+"\t"  + str(json_data['recovered']) +"\n" + "recovered New: " +"\t" + str(json_data['recoveredNew'])+"\n" + "deaths: " +"\t"+"\t"  +"\t" + str(json_data['deaths']) +"\n"+ "deaths New: " +"\t" +"\t" + str(json_data['deathsNew']) +"\n"+ "previous Day Tests: " +"\t" + str(json_data['previousDayTests'])+"\n"+ "last Updated: " +"\t" + str(json_data['lastUpdatedAtApify'][:10]) + " "+ str(json_data['lastUpdatedAtApify'][11:-5]) +" ```"

  #a= (json_data["regionData"])
  #length=len([d for d in a])
  #sent=" "
  #for i in range(length):
  #  for j in Region_read:
  #    line=(str(j) + "- " +dict(a[i][j]))
  #    sent=sent+str(line)

  return (quote)   

# def cvd_india_info():

#----- XKCD COMIC API FUNC

#----- PLEASE UPDATE COMIC RANDOM URL UPPER LIMIT NEXT TIME YOU SEE THIS.

def comic(nom):
  #comic int 1-> 2529 as of 18-10-2021
  url="https://xkcd.com/"+str(nom)+"/info.0.json"
  
  response = requests.get(url)
  json_data = json.loads(response.text)
  try:
    quote = str(json_data['img'])
  #try twopart
  except:
    quote="```Error: Could not fetch JSON data```"
  
  return (quote)   
  return(response.text)


#----- ANY JOKE

def anyjoke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw")
  json_data = json.loads(response.text)

  #try single
  try:
    quote = "```Category: " + json_data['category']  + "\n" + str(json_data["joke"]) +  " ```"
  #try twopart
  except:
    quote = "```Category: " + json_data['category'] + "\n" + str(json_data["setup"]) + "\n" + str(json_data["delivery"]) + " ```"

  return(quote)   

#-----RANDOM DICE ROLL FUNC

def rolldice():
  roll = random.randint(1,6)
  quote = " \n" + "```Dice shows: "  + str(roll) + "```"
  return(quote)

#-----JOKE API FUNC

def joke():
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(response.text)

  quote = "```" + json_data['setup']  +"\n" +json_data['punchline'] +" ```"

  return(quote)   




#-----BOT SERVER IP API FUNC removed due to security concerns



#-----BITCOIN API FUNC

def get_coin():
  
  response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  json_data = json.loads(response.text)

  quote =  "`DISCLAIMER: " + json_data['disclaimer'] +" `" +"\n" +"Bitcoin rate as of " + json_data['time']['updated']  +"\n" +"```" +json_data['bpi']["USD"]['code'] + " : $"  +json_data['bpi']['USD']['rate'] +"\n" +json_data['bpi']["EUR"]['code'] + " : €"  +json_data['bpi']['EUR']['rate'] +"\n" +json_data['bpi']["GBP"]['code'] + " : £"  +json_data['bpi']['GBP']['rate'] +"```"
  return(quote)

def is_correct(m):
  return m.author == 'NAHOR IDEVRUTAHC'









#-----
#-----   main body 
#-----










@client.event
async def on_ready():
  print('Bot is online\nWe have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #-----sup reply
  if message.content.startswith('sup'):
    await message.channel.send('Wassup!')

  #elif message.content.startswith('bro joke'):
  #  quote = joke()
  #  await message.channel.send(quote)

  #-----IP comp bot running on (should not be public)
  #elif message.content.startswith('bot ip'):
  #  quote = get_ip()
  #hi  await message.channel.send(quote)

  #-----check if bot is online
  elif message.content.startswith('on?'):
    await message.channel.send(" ```BroBOT is online " + " ( ͡~ ͜ʖ ͡°)```  ")

  #-----Bitcoin stats 
  elif message.content.startswith('bro coin'):
    quote = get_coin()
    await message.channel.send(quote)
  

  #-----Invite link
  elif message.content.startswith('bot invite'):
    await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=821771855400665181&permissions=0&scope=bot")
  #
  
  #-----dice roll output
  elif message.content.startswith('bro roll'):
    await message.channel.send(" ```Rolling dice...``` ")
    time.sleep(1)
    quote = rolldice()
    await message.channel.send(quote)

  #-----
  #-----
  #-----ALL COMMANDS MENU
  #-----
  #-----
  
  elif message.content.startswith('bro help'):
  
    await message.channel.send(" ```Currently replies to:```")
    await message.channel.send("on?"+" \n"+"bot ip"+" \n"+"bro help"+" \n"+"bro roll"+" \n"+"bro comic"+" \n"+"bro joke"+" \n"+"bro trivia"+" \n"+"bro coin"+" \n"+"covid"+" \n"+"github")
    
    #await message.channel.send(" ```Currently replies to:" + " \n"+"-on?" + " \n"+"-sup"+ " \n" + "-bro help" + " \n"+"-bro roll" + " \n" + "-bro joke"+ "\n" + "-bro coin (bitcoin stats)"+ "\n" + "-cvd"+"\n" +"-state cvd"+  "[in progress]"+"\n" + "-bot ip```")



  #-----any joke 
  elif message.content.startswith('bro joke'):
    quote = anyjoke()
    await message.channel.send(quote)

  

  #elif message.content.startswith('covid info'):
  #  quote = cvd_india_info() 
  #  await message.channel.send(quote)

  #-----covid stat call
  elif message.content.startswith('covid'):
    quote = cvd_india()
    await message.channel.send(quote)

  #elif message.content.startswith('state cvd'):
  #  quote = cvd_states()
  #  await message.channel.send(quote)

  #-----reply sup
  elif message.content.startswith('Sup'):
    quote = "Wassup"
    await message.channel.send(quote)

  #-----GITHUB LINK
  elif message.content.startswith('github'):
    quote = "```https://github.com/Rohanc28/bro-bot-s```"
    await message.channel.send(quote)

  #-----Comic XKCD 
  elif message.content.startswith('bro comic'):
    nom=random.randint(1,2529)
    s="XKCD Comics\nN: "+str(nom)+"\n\n"
    await message.channel.send(s)
    quote = comic(nom)
    await message.channel.send(quote)

  #elif message.content.startswith('bro'):
      #if message.content
  elif message.content.startswith('bro trivia'):
    s= ['easy', 'medium', 'hard', '', 'medium', '']
    dif=""
    a=""
    dif=str(random.choice(s))
    a=a+"Difficulty: "+ dif +"\n"

    #quote = trivia(dif)
    response = requests.get("https://opentdb.com/api.php?amount=1&difficulty="+dif)
    json_data = json.loads(response.text)
  
    quote = [i['question']for i in json_data['results']]
    quote=str(quote)
    quote="**[Q]**"+"```\n"+quote[1:-1]+"\n ```"
  
  
    ans1=[i['incorrect_answers']for i in json_data['results']]
    ans1=str(ans1)
    ans1=ans1[2:-2]
    ans2= [i['correct_answer']for i in json_data['results']]
    ans2=str(ans2)
    ans2=ans2[1:-1]
    ans="**[Choices]**```\n"+str(ans1)+", "+str(ans2)+"```"
    #"```Category: " + + "\n" + str(json_data['results']['type']) + "\n" + str(json_data['results']['question'])+"\n"  + str(json_data['results']['correct_answer'])+"```"
  #try twopart
  #except:
  #quote = "```Category: " + json_data['results']['category']  + "\n" + str(json_data['results']['type']) +  " ```"

    await message.channel.send(quote+ans) 
    time.sleep(8)
    s="\n :white_check_mark: "+" Correct Answer is "+ ans2+""
    await message.channel.send(s)


    #answer after 5 seconds. for test mode remove delay

  #elif message.content.startswith('test arg'):
  #  await message.channel.send("Input:")
  #  guess = await on_ready.wait_for('message', check=is_correct, timeout=5.0)
  #  if int(guess.content) == "NAHOR IDEVRUATHC":
  #      await message.channel.send('You are right!')
  
'''
  elif message.content.startswith('bro guess'):
    await message.channel.send('```Guess a number between 1 and 10.```')
    def is_correct(m):
        return m.author == message.author and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        guess = await wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await message.channel.send('Sorry, you took too longwas {}.'.format(answer))

    if int(guess.content) == answer:
        await message.channel.send('*CORRECT!*')
    elif int(guess.content) is not answer:
        if guess.content>answer:
          await message.channel.send("Wrong, It's lower")
        else:
          await message.channel.send("Wrong, It's Higher")
  '''
  
  #-----TRIVIA 
  #elif message.content('bro trivia'):
  #  await message.channel.send("Enter difficulty too\n```bro trivia ez/med/hard```")
