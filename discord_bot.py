import discord
from discord.ext import commands,tasks
import random
from itertools import cycle
user_imp=0
bot=commands.Bot(command_prefix='.')
bot.remove_command("help")


@bot.event
async def on_ready():
    
    print("Bot Ready")
   
@bot.group(invoke_without_command="True")
async def help(ctx):
    em=discord.Embed(title="help",description="use .help <command> for more info ",color=ctx.author.color)
    em.add_field(name="Questions",value="answer,choose")
    em.add_field(name="Games",value="playsps,handcricket,blackjack")
    em.add_field(name="Greetings",value="greet")
    await ctx.send(embed=em)

@help.command()
async def answer(ctx):
    em=discord.Embed(title="answer",
    description="Answer your question",color=ctx.author.color)
    em.add_field(name="syntax",value=".answer <question>")
    await ctx.send(embed=em)

@help.command()
async def choose(ctx):
    em=discord.Embed(title="choose",
    description="chooses between multiple options separated by a comma(,)",color=ctx.author.color)
    em.add_field(name="syntax",value=".choose <choices>")
    await ctx.send(embed=em)


@help.command()
async def playsps(ctx):
    em=discord.Embed(title="playsps",
    description="plays stone paper scissor",color=ctx.author.color)
    em.add_field(name="syntax",value="playsps <ur move>")
    await ctx.send(embed=em)

@help.command()
async def handcricket(ctx):
    em=discord.Embed(title="handcricket",
    description="plays hand cricket",color=ctx.author.color)
    em.add_field(name="syntax",value=".handcricket")
    await ctx.send(embed=em)

@help.command()
async def blackjack(ctx):
    em=discord.Embed(title="blackjack",
    description="plays blackjack",color=ctx.author.color)
    em.add_field(name="syntax",value=".blackjack")
    await ctx.send(embed=em)

@help.command()
async def greet(ctx):
    em=discord.Embed(title="greet",
    description="greets based on time",color=ctx.author.color)
    em.add_field(name="syntax",value=".greet")
    await ctx.send(embed=em)


@bot.command()
async def answer(ctx,*,question):
    responses=['Sure','Maybe','No way','Busy!!!Ask later']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')
    # await ctx.send(file=discord.File('sasuke-naruto-uhdpaper.com-4K-48.jpg'))

@bot.command()
async def greet(ctx):
   
    import time
    t = time.localtime()
    current_time = time.strftime("%H", t)
    current_time=int(current_time)
    print(current_time)
    if current_time>=19 or current_time<=3:
        await ctx.send('GN Fellas')
    elif current_time>3 and current_time<=11:
        await ctx.send('GM Fellas')
    elif current_time>11 and current_time<=15:
        await ctx.send('GA Fellas')
    elif current_time>15 and current_time<19:
        await ctx.send('GE Fellas')

@bot.command()
async def choose(ctx,*,question):

    index=[]
    n=0
    i=0
    for i in range(len(question)):
        if(question[i]==','):
            index.append(i)
            n=n+1
        i=i+1
    options=[]
    # print(index[n-1])
    l=0
    h=index[0]
    c=question[l:h]
    options.append(c)
    for i in range(1,n,1):
        l=h+1
        h=index[i]
        c=question[l:h]
        options.append(c)
    l=h+1
    h=len(question)
    c=question[l:h]
    options.append(c)
    print(options)
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(options)}')

@bot.command()
async def playsps(ctx,*,question):
    sps=['stone','paper','scissor']
    question=question.lower();
    ans=random.choice(sps)
    await ctx.send(f'U:{question}\nBot:{ans}')
    if question==ans:
        await ctx.send('Tie')
    elif question=='stone' and ans=='paper':
        await ctx.send('Bot wins')
    elif question=='stone' and ans=='scissor':
        await ctx.send('You win')
    elif question=='paper' and ans=='scissor':
        await ctx.send('Bot wins')
    elif question=='paper' and ans=='stone':
        await ctx.send('You win')
    elif question=='scissor' and ans=='stone':
        await ctx.send('Bot wins')
    elif question=='scissor' and ans=='paper':
        await ctx.send('You win')

@bot.event
async def on_ready():
    
    print("Bot ready")

inp=7
@bot.event
async def on_message(message):
    if message.content.startswith('.handcricket'):
        channel = message.channel
        await channel.send('Lets play!')
        i=3
        user_sum=0
        B_sum=0
        global user_inp
        user_inp=7
        B_inp=['0','1','2','3','4','5','6']
        B_bowl_inp=['0','0','0','0','1','1','2','2','2','3','3','3','3','4','4','4','4','4'
        ,'5','5','5','5','5','5','6','6','6','6','6','6','6',]
        b_inp=0
        user_toss='even'
        user_no=1
        b_no=1
        def check(m):
            global user_inp
            # print(m.content)
            user_inp=m.content
            return m.content == 'bat' or m.content=='bowl' or m.content == 'Bat' or m.content=='Bowl' or m.content == 'Odd' or m.content=='Even' or m.content == 'odd' or m.content=='even' or m.content =='0' or m.content =='1' or m.content =='2' or m.content =='3' or m.content =='4' or m.content =='5' or m.content =='6' and m.channel == channel

        await channel.send('Toss Odd or Even')
        msg = await bot.wait_for('message', check=check)
        user_toss=user_inp
        await channel.send('Enter number')
        msg = await bot.wait_for('message', check=check)
        user_no=int(user_inp)
        b_no=random.choices(B_inp)
        b_no=''.join(b_no)
        b_no=int(b_no)
        rem=(user_no+b_no)%2
        await channel.send(f'U:{user_no}\tB:{b_no}')
        flag=0
        if rem==1 and user_toss.lower()=='odd':
            await channel.send('U win,Bat or Bowl?')
            msg = await bot.wait_for('message', check=check)
            user_toss=user_inp
        elif rem==0 and user_toss.lower()=='even':
            await channel.send('U win,Bat or Bowl?')
            msg = await bot.wait_for('message', check=check)
            user_toss=user_inp
        else:
            await channel.send('Bot wins,Bot wants to Bowl')
            flag=1

        user_inp=7
        print(user_inp,b_inp)
        #U bat first
        if user_toss.lower()=='bat' or flag==1:
            while(user_inp!=b_inp):
                await channel.send('Play')
                msg = await bot.wait_for('message', check=check)
                user_inp=int(user_inp)
                b_inp=random.choices(B_bowl_inp)
                b_inp=''.join(b_inp)
                b_inp=int(b_inp)
                print(user_inp,b_inp)
                if(user_inp!=b_inp):
                    # print(user_inp,b_inp)
                    if user_inp==0:
                        doke=b_inp
                        user_sum=user_sum+doke
                    else:
                        user_sum=user_sum+user_inp
                    await channel.send(f'U:{user_inp}\tBot:{b_inp}\tscore:{user_sum}')
            await channel.send(f'Ur final score:{user_sum}')

            b_inp=7
            await channel.send('Bot batting')
            while(user_inp!=b_inp and B_sum<=user_sum):
                await channel.send('Play')
                msg = await bot.wait_for('message', check=check)
                user_inp=int(user_inp)
                b_inp=random.choices(B_inp)
                b_inp=''.join(b_inp)
                b_inp=int(b_inp)
                print(user_inp,b_inp)
                if(user_inp!=b_inp):
                    # print(user_inp,b_inp)
                    if b_inp==0:
                        doke=user_inp
                        B_sum=B_sum+doke
                    else:
                        B_sum=B_sum+b_inp
                    await channel.send(f'U:{user_inp}\tBot:{b_inp}\tscore:{B_sum}')
            await channel.send(f'Bot final score:{B_sum}')
            print(B_sum,user_sum,'j')
        
        else:

            while(user_inp!=b_inp):
                await channel.send('Play')
                msg = await bot.wait_for('message', check=check)
                user_inp=int(user_inp)
                b_inp=random.choices(B_inp)
                b_inp=''.join(b_inp)
                b_inp=int(b_inp)
                print(user_inp,b_inp)
                if(user_inp!=b_inp):
                    # print(user_inp,b_inp)
                    if b_inp==0:
                        doke=user_inp
                        B_sum=B_sum+doke
                    else:
                        B_sum=B_sum+b_inp
                    await channel.send(f'U:{user_inp}\tBot:{b_inp}\tscore:{B_sum}')
            await channel.send(f'Bot final score:{B_sum}')

            b_inp=7
            await channel.send('U r batting')
            while(user_inp!=b_inp and user_sum<=B_sum):
                await channel.send('Play')
                msg = await bot.wait_for('message', check=check)
                user_inp=int(user_inp)
                b_inp=random.choices(B_bowl_inp)
                b_inp=''.join(b_inp)

                b_inp=int(b_inp)
                print(user_inp,b_inp)
                if(user_inp!=b_inp):
                    # print(user_inp,b_inp)
                    if user_inp==0:
                        doke=b_inp
                        user_sum=user_sum+doke
                    else:
                        user_sum=user_sum+user_inp
                    await channel.send(f'U:{user_inp}\tBot:{b_inp}\tscore:{user_sum}')
            await channel.send(f'Ur final score:{user_sum}')




        if B_sum>user_sum:
            await channel.send('B wins')


        elif B_sum<user_sum:
            await channel.send('U win')


        else:
            await channel.send('Tie')
            await channel.send('Tie:breaker Odd or Even')
            msg = await bot.wait_for('message', check=check)
            user_toss=user_inp
            await channel.send('Enter number')
            msg = await bot.wait_for('message', check=check)
            user_no=int(user_inp)
            b_no=random.choices(B_inp)
            b_no=''.join(b_no)
            b_no=int(b_no)
            rem=(user_no+b_no)%2
            await channel.send(f'U:{user_no}\tB:{b_no}')
            if rem==1 and user_toss.lower()=='odd':
                await channel.send('U win')
            elif rem==0 and user_toss.lower()=='even':
                await channel.send('U win')
            else:
                await channel.send('Bot wins')


    elif message.content.startswith('.blackjack'):

        #initialization
        channel = message.channel
        await channel.send('Lets play!')

        # global user_inp
        user_inp='a'
        cards=dict(ace_hearts=11,two_hearts=2,three_hearts=3,four_hearts=4,five_hearts=5
        ,six_hearts=6,seven_hearts=7,eight_hearts=8,nine_hearts=9,ten_hearts=10
        ,jack_hearts=10,king_hearts=10,queen_hearts=10,
        ace_diamond=11,two_diamond=2,three_diamond=3,four_diamond=4,five_diamond=5
        ,six_diamond=6,seven_diamond=7,eight_diamond=8,nine_diamond=9,ten_diamond=10
        ,jack_diamond=10,king_diamond=10,queen_diamond=10,
        ace_spade=11,two_spade=2,three_spade=3,four_spade=4,five_spade=5
        ,six_spade=6,seven_spade=7,eight_spade=8,nine_spade=9,ten_spade=10
        ,jack_spade=10,king_spade=10,queen_spade=10,
        ace_club=11,two_club=2,three_club=3,four_club=4,five_club=5
        ,six_club=6,seven_club=7,eight_club=8,nine_club=9,ten_club=10
        ,jack_club=10,king_club=10,queen_club=10)
        l = list(cards.items())
        random.shuffle(l)
        cards = dict(l)
        players_sum=[]
        players_ace_sum=[]
        players_ace_flag=[]
        players_flag=[]
        dealer_sum=0
        dealer_ace_flag=0
        dealer_ace_sum=0
        names=[]
        global bet
        def check(m):
            global user_inp
            # print(m.content)
            user_inp=m.content
            user_inp=user_inp.lower()
            return m.content =='0' or m.content =='1' or m.content =='2' or m.content =='3' or m.content =='4' or m.content == 'shok' or m.content=='Shok' or m.content == 'B' or m.content=='b' or m.content == 'Sama' or m.content=='Kettavan' or m.content == 'sama' or m.content=='kettavan' or m.content == 'Hit' or m.content=='Stand'or m.content == 'hit' or m.content=='stand' and m.channel == channel
        
        #getting input
        await channel.send('Enter no. of players')
        msg = await bot.wait_for('message', check=check)
        n=int(user_inp)
        for i in range(n):
            players_sum.append(0)
            players_flag.append(0)
            players_ace_sum.append(0)
            players_ace_flag.append(0)
        
        for i in range(n):

            initial_card1=cards.popitem()
            initial_card2=cards.popitem()
        # print(card)
            if  initial_card1[1]==11:
                players_ace_flag[i]=1
                players_ace_sum[i]=1+initial_card2[1]

            if  initial_card2[1]==11:
                players_ace_flag[i]=1
                players_ace_sum[i]=1+initial_card1[1]
            

            players_sum[i]=initial_card1[1]+initial_card2[1]
            if players_ace_flag[i]==1:
                await channel.send(f'player:{i+1}-card1={initial_card1[0]}\tcard2={initial_card2[0]}\tsum={players_sum[i]} or {players_ace_sum[i]}')
            else:
                await channel.send(f'player:{i+1}-card1={initial_card1[0]}\tcard2={initial_card2[0]}\tsum={players_sum[i]}')
            if players_sum[i]==21:
                await channel.send('Blackjack')
                players_flag[i]=3
        f=0
        for i in range(n):
            if  players_flag[i]!=3:
                f=1
        
        if f==1:
            dealer_card1=cards.popitem()
            dealer_card2=cards.popitem()
            dealer_sum=dealer_card1[1]
            if  dealer_card1[1]==11:
                dealer_ace_flag=1
                dealer_ace_sum=1+dealer_card2[1]
            dealer_sum=dealer_card1[1]
            if  dealer_card2[1]==11:
                dealer_ace_flag=1
                dealer_ace_sum=1+dealer_card2[1]

            await channel.send(f'Dealer sum={dealer_sum}+unknown card')
        # msg = await bot.wait_for('message', check=check)

        prod=1
        for i in range(n):
            prod=prod*players_flag[i]

        print(prod)

        #game players

        while(prod==0):
            prod=1
            for j in range(n):
                while players_flag[j]==0:
                    if players_ace_flag[j]==0:
                        await channel.send(f'player:{j+1}\tUr current sum={players_sum[j]}\tEnter ur choice:hit or stand')
                    else:
                        await channel.send(f'player:{j+1}\tUr current sum={players_sum[j]} or {players_ace_sum[j]}\tEnter ur choice:hit or stand')
                    msg = await bot.wait_for('message', check=check)
                    if  user_inp=='stand' or players_sum[j]==21  or players_ace_sum[j]==21 :
                        players_flag[j]=1
                    elif user_inp=='hit':
                        card=cards.popitem()
                        if players_ace_flag[j]==1 or card[1]==11:
                            
                            if players_ace_flag[j]==0:
                                players_ace_flag[j]=1
                                players_ace_sum[j]=players_sum[j]+1
                            else:
                                players_ace_sum[j]=card[1]+players_ace_sum[j]
                            players_sum[j]=card[1]+players_sum[j]
                            await channel.send(f'player:{j+1}\tcard={card[0]}\tsum={players_sum[j]} or {players_ace_sum[j]}')

                        else:
                            players_sum[j]=card[1]+players_sum[j]
                            await channel.send(f'player:{j+1}\tcard={card[0]}\tsum={players_sum[j]}')
                    if players_sum[j]>21:
                         if players_ace_flag[j]==0:
                            players_flag[j]=2
                            await channel.send(f'player:{j+1} loses')

                         else:
                             players_sum[j]=players_ace_sum[j]
                             players_ace_flag[j]=0

            for i in range(n):
                prod=prod*players_flag[i]   

        #game dealer

        print('l')
        f=0
        for i in range(n):
            if players_flag[i]!=2:
                f=1
        if(f):
            if dealer_ace_flag==0:
                temp_sum=dealer_sum
                dealer_sum=dealer_card2[1]+dealer_sum
                await channel.send(f'Dealer sum={temp_sum}+unknown card\nunknown card:{dealer_card2}\ndealersum={dealer_sum}')

            else:
                if dealer_sum==11:
                    dealer_sum=dealer_card2[1]+dealer_sum
                    dealer_ace_sum=1+dealer_card2[1]
                    await channel.send(f'Dealer sum=11 or 1 +unknown card\nunknown card:{dealer_card2}\ndealersum={dealer_sum} or {dealer_ace_sum}')
                else:
                    temp_sum=dealer_sum
                    dealer_sum=dealer_sum+dealer_card2[1]
                    dealer_ace_sum=temp_sum+1
                    await channel.send(f'Dealer sum={temp_sum}+unknown card\nunknown card:{dealer_card2}\ndealersum={dealer_sum} or {dealer_ace_sum}')

            while(True):
                if  dealer_sum>21:
                    if dealer_ace_flag==0:
                        await channel.send(f'Dealer sum={dealer_sum}\tdealer sum > 21')
                        for i in range(n):
                            if players_flag[i]==1:
                                await channel.send(f'player:{i+1} wins')


                        break
                    else:
                        await channel.send(f'Dealer sum={dealer_sum} or {dealer_ace_sum}')
                        dealer_sum=dealer_ace_sum
            
                elif dealer_sum>16:
                    await channel.send(f'Dealer sum={dealer_sum}\tdealer sum > 16')
                    for i in range(n):
                        if players_flag[i]==1 and players_sum[i]>dealer_sum:
                            await channel.send(f'player:{i+1} wins')

                        elif players_flag[i]==1 and players_sum[i]==dealer_sum:
                            await channel.send(f'player:{i+1} tie')
                        elif players_flag[i]==1 and players_sum[i]<dealer_sum:
                            await channel.send(f'player:{i+1} loses')

                    break
                else:
                    card=cards.popitem()
                    await channel.send(f'Dealer next card={card[0]}')
                    if dealer_ace_flag==0 and card[1]!=11:
                        dealer_sum=card[1]+dealer_sum
                        
                    else:
                        if dealer_ace_flag==0:
                            dealer_ace_sum=dealer_sum+1
                            dealer_sum=dealer_sum+card[1]
                            dealer_ace_flag=1
                        else:
                            dealer_ace_sum=dealer_ace_sum+card[1]
                            dealer_sum=dealer_sum+card[1]
    await bot.process_commands(message)
    
#enter your bot token
bot.run('<Enter your bot token here>')




