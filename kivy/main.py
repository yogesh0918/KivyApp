from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button,Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pymysql
#from kivy.uix.popup import Popup


class MainWindow(Screen):
    pass
    
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


class Gamee(Screen):
    namee:ObjectProperty(None)
    password:ObjectProperty(None)
    conf_password: ObjectProperty(None)
    def btn(self):
        if self.conf_password.text==self.password.text:
            if self.password.text.isalnum() :
                con=pymysql.connect(host="localhost",user="root",password="",db="test")
                print("Name:",self.namee.text,"Password:",self.password.text)
                mycur=con.cursor()
                query="select username from register where username= %s"
                ans=mycur.execute(query,self.namee.text)
                #print(ans)
                if not ans:
                    query="INSERT INTO register(username,password,password2) VALUES(%s,%s,%s)"
                    vl=(self.namee.text,self.password.text,self.password.text)
                    mycur.execute(query,vl)
                    con.commit()
                    con.close()
                else:
                    print("Username is Taken :",self.namee.text)
                    
            else:
                print("Enter Values")
        else:
            print("Error",self.conf_password.text)
    pass

class my(App):
        def build(self):
            img=Image(source="pic.jpg")
            kv = Builder.load_file("my.kv")
            return kv

my().run()

"""
    def __init__(self,**kwargs):
        super(Gamee,self).__init__(**kwargs)
        self.cols=1    # Fisrt it will set no. of column

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text='UserName'))
        self.inside.add_widget(TextInput(multiline=False))

        self.inside.add_widget(Label(text='Password'))
        self.inside.add_widget(TextInput(multiline=False))

        self.inside.add_widget(Label(text='Conform Password'))
        self.inside.add_widget(TextInput(multiline=False))

        # This is seqence of printing
        self.add_widget(self.inside)   # To add self.inside= GridLayout()
        self.add_widget(Button(text='Submit'))  # For Button
        """
"""class GameApp(App):
    def build(self):
        return Gamee()
        
GameApp().run()

"""