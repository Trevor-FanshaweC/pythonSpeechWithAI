import os, subprocess

class Controller:
    def __init__(self):
        self.confirm = ["yes", "make it so", "affirmative", "si", "yup", "go", "do it", "yeah"]
        self.cancel = ["no", "nope", "cancel", "negative", "negatory", "hellz no"]
    
    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond('My name is Siri. How are you')
        elif "what" in text and "my name" in text:
            self.respond("I do not know your name yet")                         
        
        if "open" or "launch" in text:
            app = text.split(" ", 1)[1]
            print("opening", app)

            self.respond("Opening", app)

            os.system("open -a " + app)

        
        else:
            self.respond("you said " + text)
    
    def respond(self, response):
        print(response)
        subprocess.call('say ' + response, shell=True)
