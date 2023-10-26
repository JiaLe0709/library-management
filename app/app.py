from flask import Flask

app = Flask(__name__, template_folder='web')


@app.route('/hello-world')
def root():
    return (
        [
            {
                'id': 1,
                'name': 'hello',
                'hair': 'true',
            }, 
            {
                'id':2,
                'name': 'hi',
                'hair': 'false'
            }
        ]
    )


if __name__ == '__main__':
    app.run()
