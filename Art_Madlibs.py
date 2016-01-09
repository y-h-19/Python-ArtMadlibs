#Phase 3: Final project
#Art Madlibs
#Yuna Hahn and Clare Lee

from Tkinter import *
from turtle import*

class Turtlepattern:
    def __init__(self):
        pass
        
    def polygon(self,numSides, sideLength, color, size):
        '''Creates a polygon of a specified number of sides, color, and size'''
        self.numSides = numSides
        self.sideLength = sideLength
        self.color = color
        self.size = size
        pen(pencolor=self.color, pensize=self.size, shown=False, speed=0)
        for i in range (0, self.numSides):
            fd(self.sideLength)
            lt(360.0/self.numSides) 
   
    def star(self,levels, color):
        '''Draws a star pattern  recursively'''
        self.levels = levels
        self.color = color
        pen(pencolor=self.color, pensize=1, shown=False, speed=0)
        if self.levels>0:
            forward(190)
            left(170)
            self.star(self.levels-1, self.color)

    def I(self):
        '''Draws a short simple line pattern'''
        pen(pencolor='black', pensize=1, shown=False, speed=5)
        fd(50)
        right(65)
        fd(50)


    def You(self):
        '''Draws a triangle with blue and dark red colored sides'''
        pen(pencolor='blue',pensize=1,shown=False,speed=0)
        fd(40)
        lt(120)
        pencolor('DarkRed')
        fd(40)
        lt(120)

        fd(40)
        pencolor('DarkMagenta')
        lt(120)
        fd(40) 
        pu()
        rt(100)
        bk(70)
        pd()

        
    def spiral(self,size,color,color2, sidelen, angle, scaleFactor):
        '''Draws a spiral recursively of specified size, scaleFactor, color, and angle'''
        self.size = size
        self.color = color
        self.color2 = color2 
        self.sidelen = sidelen
        self.angle = angle
        self.scaleFactor = scaleFactor
        pen(pencolor=self.color,pensize=self.size, shown=False, speed=0)
        if self.sidelen>=5:
            fd(self.sidelen)
            lt(self.angle)
            self.spiral(self.size,self.color2,self.color,self.sidelen*self.scaleFactor, 
            self.angle, self.scaleFactor)
    
       
    def no(self):
        '''Draws an 'X' pattern'''
        pen(pencolor='black', pensize=1, shown=False, speed=0)
        rt(45)
        fd(90)
        pu()
        lt(135)
        fd(40)
        pd()
        lt(135)
        fd(70)
        pu()
        bk(100)
        pd()
    
    def yes(self):
        '''Draws a '''
        pen(pencolor='coral', pensize=1, shown=False, speed=0)
        for i in range (1,10):
            fd(60)
            lt(135)

    def female(self):
        '''Draws a flower pattern'''
        for i in range(0,7):
            self.polygon(8,20,'violet',2)
            lt(360.0/7)
    

    def male(self):
        '''Draws a fan-like pattern of squares'''
        pu()
        fd(40)
        pd()
        for i in range(0,4):
            self.polygon(4,25,'MidnightBlue',2)
            rt(55)

    def baby(self):
        '''Draws another flower pattern'''
        pu()
        fd(50)
        pd()
        for i in range(0,5):
            self.polygon(5, 20,'coral', 3)
            lt(360.0/5)

    def dance(self,levels, color):
        '''draws a star pattern'''
        self.levels = levels
        self.color = color 
        self.star(self.levels,self.color)
    
    
            

def selectAnimation(lines):
    '''reads in the lyrics, and for each word in each line, 
    it calls a function in the Turtlepattern class that will draw a specific turtle
    graphic'''
    setup(width=800,height=800)
    lovecount=0 
    yeahcount=1
    yescount=0
    icount=0
    saycount=0
    shakecount=0
    T = Turtlepattern() #Turtlepattern class is called
    for line in lines: #for each list in the list of lines
        for w in line: #for each word in the list
            if w in ['oh','ohh','ohhh','oops','wooh','woah','problem','question']:
                #if the word, w, is in this list of words
                T.spiral(2,'navy','navy',120, 110, 0.9) 
                      
            if w in ['yeah','hey','hi','meet','hello','crazy','like']:
                yeahcount+=0.3
                T.spiral(1,'darkgreen','darkgreen',80*yeahcount,90,0.8)
            if w in ['no','wrong','hate',"don't","won't",'not',"can't",'nothing','break', 'breakup']:
                T.no() 
            if w in ['yes','life','right','lips','eyes','face','nose','mouth','hands', 'hand',
            'body','curves']:
                yescount+=1
                pu()
                goto(200+yescount,-60+yescount)
                pd()
                T.yes()
                    
            if w in ['girl','girlfriend','woman','lady','she','her','mom','mama']:
                T.female()
                    
            if w in ['boy','boyfriend','man','guy','him','he','dad','daddy','dude']:
                T.male()
                    
            if w in ['baby','boo','honey','sweet','child','home', 'feel', 'feeling', 'touch']:
                T.baby()
                    
            if w in ['are','is','am','beautiful','pretty','smile','cute','hot','sexy', 'lovely',
            'gorgeous']:
                T.polygon(4,50,'DeepPink', 2)
                    
            if w in ['star','sun','sunshine','moon','moonlight','earth','universe','wide',
            'world','sky','shine', 'diamond', 'dream','fantasy']:
                pu()
                goto(0,0)
                pd()
                T.star(20, 'LightSalmon')   
            if w in ['i','my','me','mine',"i'm",'self', 'selfie','selfish']:
                icount+=10
                pu()
                goto(-200,-50)
                pd()
                T.I()
            if w in ['you','your',"you're",'u', 'thing', 'something', 'nothing']:
                pu()
                goto(50,60)
                pd()
                T.You()
            if w in ['love','kiss','miss','heart','heartbeat','jealous','think', 'thinking']:
                pu()
                goto(0,0)
                pd()
                lovecount+=0.5
                T.spiral(1.5,'HotPink','LightSeaGreen', 60*lovecount,60, 0.9) 
                    
            if w in ['we','us','they','them','everybody','people','their', 'person', 'everyone', 
            'nobody', 'somebody', 'someone', 'noone'] :
                pu()
                bk(50)
                pd()
                T.spiral(1,'Maroon','PeachPuff',70,100, 0.95)
          
                
            if w in ['say','said','talk','tell','told','see','saw','look','watch','says','looks',
            'explain', 'decide', 'problem']:
                pu()
                goto(150,150)
                pd()
                saycount+=10
                T.polygon(5,100+saycount,'RoyalBlue',1)
               
            if w in ['scream','shout','cry','tear','tears','teardrop','teardrops','screw', 'fuck','shit',
            'bitch','hoe','slut','jerk','fucking']:
                T.polygon(9,30,'Aquamarine', 1)
               
            if w in ['shake','dance','shaking','booty','twerk','dancing','bounce','ass','damn', 'fine',
            'wiggle']:
                shakecount+=15
                pu()
                fd(shakecount)
                pd()
                if shakecount%2==0:
                    T.dance(12,'LimeGreen')
                else:
                    T.dance(8,'Tomato')
            if w in ['who', 'what', 'when','why','where','how','up','down','whole','fall','falling',
            'on', 'in', 'out','inside']:
                T.polygon(12, 10,'DodgerBlue',1.5)
            
            if w in ['the','a','and','it','of','off','this','there','that',"that's","it's"]:
                pu()
                goto(100+icount,100+icount)
                pd()
            if line==lines[len(lines)-1] and w==line[len(line)-1]:
                #when the program finishes the analysis and reaches the last word
                #our names will appear in the upper right hand corner
                pu()
                goto(250,300)
                pd()
                pencolor(0,0,0)
                write("By Clare Lee and Yuna Hahn", align='center',font=('Arial',15, 'bold'))
         
            

class lyrics: 
    def __init__(self):
        pass
        
    def lyricsList(self, fileName):
        '''Strips the textfile  line by line and creates a list of words in all 
        lowercase letters'''
        self.fileName = fileName
        lines = open(self.fileName).readlines()
        words = []
        for line in lines: 
            low = line.lower()
            words.append(low.split())
        return words
        
    def lyricAnalysis(self, fileName):
        '''A function that analyzes the text in the file name using other helper 
        functions and  animation'''
        self.fileName = fileName
        words = self.lyricsList(self.fileName)
        selectAnimation(words)
    

    
    
    
class Animationwindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title('Art Madlibs')
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        # Title
       
        titleLabel = Label(self, text='Type in the lyrics of your favorite song:', fg='darkblue', 
        font='Verdana 16 bold')
        titleLabel.grid(row=0,column=1,sticky=N+E+W+S)

        #Text box
        
        self.text= Text(self, height=20, width=40,borderwidth=2,background='lightblue')
        self.text.grid(row=2,column=1)
     
        # Submit Button
        self.submitButton = Button(self, text='Submit', command=self.onSubmitButtonClick)
        self.submitButton.grid(row=4,column=4)
        

        # Quit Button        
        quitButton = Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.grid(row=4,column=0,sticky=W)
    

    def onSubmitButtonClick(self):
        '''Once the submit button is pressed, a file will be created that contains that text that
        the user inputted'''
        textbox= self.text.get(0.0,END)
        self.newfile=open('lyrics','w') #open new file for writing
        self.newfile.write(textbox)
        self.newfile.close()
        L = lyrics()
        L.lyricAnalysis('lyrics')
        
    
    def onQuitButtonClick(self):
        self.destroy()

app = Animationwindow()
app.mainloop()

