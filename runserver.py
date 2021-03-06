import os
from flask import Flask
from example_apps.basic_app import create_app

app = create_app()



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# app.run(host='0.0.0.0', port=5000, debug=True)

