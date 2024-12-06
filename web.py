from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/register")
def index():

    return render_template("register.html")

@app.route("/do/reg")
def do_reg():
    username = request.args.get('user')
    password = request.args.get('pwd')
    role = request.args.get('role')
    gender = request.args.get('gender')
    print(username,password,role)
    with open('account.txt', mode='a',encoding='utf-8') as f:
        line = "{}|{}|{}|{}\n".format(username, password,role,gender)
        f.write(line)
    return "提交成功"
if __name__ == "__main__":
    app.run()