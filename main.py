import json

from flask import Flask,render_template,jsonify,request


app = Flask(__name__)

@app.route("/",methods=["GET"])
def all_users():
    with open("data.json") as file:
        data=json.load(file)
    return jsonify([i["name"] for i in data])
@app.route("/",methods=["POST"])
def register():
    new_data=request.json
    with open("data.json","r")as file:
        data=json.load(file)
        if new_data["name"] not in [i["name"] for i in data]:
            data.append(new_data)
            with open("data.json","w") as file:
                    json.dump(data,file,indent=4)
            return "Account has been created"
    return "choose another username"
@app.route("/",methods=["VIEW"])
def verification():
    data_to_verify=request.json
    with open("data.json","r") as file:
        data=json.load(file)
        for account in data:
            if account ==data_to_verify:
                return "You were verificated successfully"
    return "Incorrect username or password"

@app.route("/",methods=["PUT"])
def change_password():
    new_data: dict[str:str]=request.json #new_data-словарь из имени аккаунта и нового пароля
    with open("data.json","r") as file:
        data=json.load(file)
        for account in data:
            if account["name"]==new_data["name"]:
                account["password"]=new_data["password"]
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)
    return "Password has been changed to %s" %new_data["password"]
@app.route("/",methods=["DELETE"])
def delete_account():
    deleted_account=request.json #deleted_account-словарь из имени аккаунта и его пароля
    with open("data.json","r") as file:
        data= json.load(file)
        for account in data:
            if account==deleted_account:
                data.remove(account)
    with open("data.json","w") as  file:
        json.dump(data,file,indent=4)
    return "Account %s has been successfully deleted"%deleted_account["name"]
if __name__=='__main__':
    app.run(debug=True)