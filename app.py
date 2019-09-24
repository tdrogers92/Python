from flask import Flask, render_template, request, url_for, redirect, session
import forms
import ldap_functions as ldap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'panduem48fp4mfod'


@app.route('/')
def index():
    form = forms.LdapForm()
    return render_template('main.html', title="FTP LDAP", form=form)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        listofvals = {
            "company": request.form['company'],
            "username": request.form['username'],
            "firstname": request.form['firstname'],
            "surname": request.form['surname'],
            "password": request.form['password'],
            "function": request.form['dropdown']
            }

        if listofvals["function"] == 'adduser':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                result = ldap.searchcompany(listofvals['company'])
                return render_template('test.html', result=result)

        elif listofvals["function"] == 'addcompany':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                return render_template('test.html', listofvals=listofvals)

        elif listofvals["function"] == 'searchuser':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                return render_template('test.html', listofvals=listofvals)

        elif listofvals["function"] == 'searchcompany':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                return render_template('test.html', listofvals=listofvals)

        elif listofvals["function"] == 'removeuser':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                return render_template('test.html', listofvals=listofvals)

        elif listofvals["function"] == 'removecompany':
            if check_minimum_requirements(listofvals['function'], listofvals) is True:
                return render_template('test.html', listofvals=listofvals)

        else:
            return render_template('error.html')


def check_minimum_requirements(function, listofvals):
    if function is 'adduser':
        minimum_requirements = ['company', 'username', 'firstname', 'surname',
                                'password']
        for requirement in minimum_requirements:
            if not listofvals[requirement]:
                return False
            else:
                return True

    elif function in {'addcompany', 'searchcompany', 'removecompany'}:
        minimum_requirements = ['company']
        for requirement in minimum_requirements:
            if not listofvals[requirement]:
                return False
            else:
                return True

    elif function is 'searchuser':
        minimum_requirements = ['username']
        for requirement in minimum_requirements:
            if not listofvals[requirement]:
                return False
            else:
                return True

    elif function is 'removeuser':
        minimum_requirements = ['username', 'company']
        for requirement in minimum_requirements:
            if not listofvals[requirement]:
                return False
            else:
                return True


if __name__ == '__main__':
    app.run()
