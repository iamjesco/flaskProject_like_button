from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

all_likes = 0
user = {
    'name': 'Jack',
    'like': 0
}


@app.route('/')
def home():
    return render_template('button.html', likes=all_likes, user=user)


@app.route('/increase')
def increase_likes():
    user['like'] = user.get('like') + 1
    global all_likes
    all_likes = all_likes + 1
    return redirect(url_for('home'))


@app.route('/decrease')
def decrease_likes():
    user['like'] = user.get('like') - 1
    global all_likes
    all_likes = all_likes - 1
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
