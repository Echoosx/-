# import sys
# sys.path.append("../")
import Kernel

Seyana = Kernel.Kernel()

Seyana.learn("other.aiml")
Seyana.learn("wxAndroid-life.aiml")

def dialogue(Content):
    response=Seyana.respond(Content)
    if response=="":
        response="对不起，我没明白您在说什么"
    return response
