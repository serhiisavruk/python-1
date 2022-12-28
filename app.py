from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        'Id': 1,
        'Name': 'User1',
        'Age': 10,
        'activated': False
    },
    {
        'Id': 2,
        'Name': 'User2',
        'Age': 20,
        'activated': False
    }
]


@app.route('/users', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': users})


if __name__ == '__main__':
    app.run()
