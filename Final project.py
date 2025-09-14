import pygame
import random
pygame.init()
pygame.mixer.init()
winx=500
winy=500
win=pygame.display.set_mode((winx, winy))
pygame.display.set_caption("Snake Game")
front=pygame.image.load("front.jpg")
bg2=pygame.image.load("bg2.png")
bg2=pygame.transform.scale(bg2,(winx,winy)).convert_alpha()
front=pygame.transform.scale(front,(winx,winy)).convert_alpha()
end=pygame.image.load("end.png")
end=pygame.transform.scale(end,(winx,winy)).convert_alpha()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
font=pygame.font.SysFont(None,32)
clock=pygame.time.Clock()

#fo=open("file1.txt","w")
#fo.write("0")
#fo.close()

fo=open("file1.txt","r")
highscore=fo.read()
fo.close()

#password

import tkinter as tk

failure_max=1
passwords=[('rajan','sajan')]
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

def enter(event):
    check_password()
def check_password(failures=[]):
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    print(user.get(), password.get())
    if (user.get(), password.get()) in passwords:
        root.destroy()
        print('Logged in')
        welcome()
        return
    
        
    else:
        pygame.time.delay(100)
        pygame.mixer.music.load("erro.mp3")
        pygame.mixer.music.play()
        
        
        def okay():
            print("ACCESS DENIED")
            root1.destroy()
            
            
        root1=tk.Tk()
        root1.geometry('300x70')
        root1.title("FAILED")
        l1=tk.Label(root1,text='UNAUTHORISED ATTEMPT TO LOGIN INTO GAME',bg='red')
        l1.pack()
        b1=tk.Button(root1,text='OK',width=10,command=okay)
        b1.pack(side=tk.BOTTOM)
        
        
        
    failures.append(1)
    if sum(failures) >= failure_max:
        root.destroy()
        pygame.quit()
        
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))
    root1.mainloop()

root = tk.Tk()
root.geometry('250x250')
root.title('SNAKE GAME')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "User name:", 16, show='*')
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login",bg='red', width=10, pady=8, command=check_password)




def  textscreen(text,color,a,b):
    screen_text=font.render(text,True,color)
    win.blit(screen_text,(a,b))
def plot_snake(win,color,snk_list,snakesize):
    for x1,y1 in snk_list:
        pygame.draw.rect(win,red,[x1,y1,snakesize,snakesize])
        
def welcome():
    run=True
    while run:
        win.blit(front,(0,0))
        textscreen("Welcome to Snakes", black, 140, 200)
        textscreen("Press Space Bar To Play", black, 120, 230)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
                pygame.quit()
                quit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_SPACE):
                    pygame.mixer.music.load("main1.mp3")
                    pygame.mixer.music.play()
                    gameloop()
                    #pygame.display.update()

        pygame.display.update()
        clock.tick(60)
def gameloop():
    x=50
    y=50
    snakesize=20
    xvel=0
    yvel=0
    xfood=random.randint(20,winx/2)
    yfood=random.randint(20,winy/2)
    score=0
    vel=10
    fps=15
    gameover=False
    
    run=True
    snk_list=[]
    snk_length=1

   

    fo=open("file1.txt","r")
    highscore=fo.read()
    fo.close()
    
    while run:
        if gameover:
            fo=open("file1.txt","w")
            fo.write(str(highscore))
            fo.close()
            win.blit(end,(0,0))
            textscreen("Game over!!!! Press Enter to Continue",white,60,430)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    run=False
                    quit()
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RETURN):
                        pygame.init()
                        pygame.mixer.music.load("main1.mp3")
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    run=False
                    quit()
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                xvel=-vel
                yvel=0
            if keys[pygame.K_RIGHT]:
                xvel=vel
                yvel=0
            if keys[pygame.K_UP]:
                yvel=-vel
                xvel=0
            if keys[pygame.K_DOWN]:
                yvel=vel
                xvel=0
            #if keys[pygame.K_SPACE]:
                #score=score+1000
            x=x+xvel
            y=y+yvel
            if(x<0):
                x=winx
            if(x>winx):
                x=0
            if(y<0):
                y=winy
            if(y>winy):
                y=0
            if abs(x-xfood)<13 and abs(y-yfood)<13:
                score=score+10
                xfood=random.randint(0,500/2)
                yfood=random.randint(0,500/2)
                snk_length+=3
                if score>int(highscore):
                    highscore=score
                    """fo=open("file1.txt","w")
                    fo.write(str(highscore))
                    fo.close()"""
            
                
            win.blit(bg2,(0,0))
            textscreen("SCORE:"+str(score) +"      HIGHSCORE:"+str(highscore),(0,255,0),5,5)
            pygame.draw.rect(win,(255,0,255),(xfood,yfood,snakesize,snakesize))
            head=[]
            head.append(x)
            head.append(y)
            snk_list.append(head)
            if(len(snk_list)>snk_length):
                del snk_list[0]
            if head in snk_list[:-1]:
                gameover=True
                pygame.mixer.music.load("hit1.mp3")
                pygame.mixer.music.play()
                
                
            
            plot_snake(win,black,snk_list,snakesize)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    #quit()
#welcome()
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()












