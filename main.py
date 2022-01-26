import guizero
from replit import audio
app = guizero.App(title="aaaa")
audio.play_file('freddy-freaker.wav')


# stuff

welcome_message=guizero.Text(app, text="freddy freaker", font="Monsterrat", size="50")
text_box = guizero.TextBox(app, width=20)

def thefreaker():
  welcome_message.value= text_box.value

def textsizecahnge(sliderval):
  welcome_message.size = sliderval

callfreaker=guizero.PushButton(app, command=thefreaker, text="Call The Freaker!")
textslider = guizero.Slider(app,command=textsizecahnge,start=10,end=80)

freddyimg = guizero.Picture(app,image="freddy.gif")


app.display()