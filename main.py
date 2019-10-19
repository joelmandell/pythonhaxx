from flask import request, Flask
import json

class MinKlass:
    def __init__(self, number, liter):
        self.number = number
        self.liter = liter
    def cool(self):
        return self.number*self.liter
    def convertMPG(self,liter, region="US"):
        if region == "UK":
            return 284.48/liter
        else:
            return 235.21/liter
    def kmph_to_mps(self, kmph):
        return kmph*3.6
form = """
<form method="POST">
<input type="number" min="1" name="add1"></input>
<input type="number" min="1" name="add2"></input>
<input type="submit"></input>
</form>
"""

app = Flask(__name__)
@app.route('/test', methods=["GET", "POST"])
def hello():
    add1 = request.form.get("add1")
    add2 = request.form.get("add2")
        
    if request.method == "GET":
        return form
    return str(MinKlass(1 if add1 == None else float(add1),1 if add2 == None else float(add2)).cool())

@app.route('/mpg', methods=["GET", "POST"])
def mpg():
    mpgnr = request.form.get("add1")
    region = request.args.get("region")# Vad har du då? Stationär en gammal i7 cpu o så :tummen upp: :)
    #:) sla testa kmph konverteraren...
    
    
    if request.method == "GET":
        return form 
    return str(MinKlass(0,0).convertMPG(1 if mpgnr == None else float(mpgnr),region))

@app.route('/kmph', methods=["GET", "POST"])
def kmph():
    kmph = request.form.get("add1")
    
    if request.method == "GET":
        return form 
    return str(MinKlass(0,0).kmph_to_mps(1 if kmph == None else float(kmph)))

#Nä men nu tycker jag vi bygger en form-builder... :)
@app.route('/formtest', methods=["GET", "POST"])
def formtest():
    return FormBuilder(["add1|text","add2|number"]).renderForm()

class FormBuilder:
    def __init__(self, inputs):
        self.form = ""
        for input in inputs:
            name = input.split("|")[0]
            type = input.split("|")[1]
            self.form += f"""
            <input type="{type}" name="{name}" />
            """
    def renderForm(self):
        return self.form

cla