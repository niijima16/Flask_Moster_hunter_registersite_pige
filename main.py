from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/info/register', methods=['GET', "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        weapon = request.form.get("weapon")
        experience = request.form.get("experience")
        box = request.form.getlist("box")

        print(user, pwd, gender, weapon, experience, box)
        return "登録成功！"


if __name__ == '__main__':
    app.run()
