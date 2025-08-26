from flask import Flask

app = Flask(__name__)  # <-- make sure it has the underscores!

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Heart for Gissel</title>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: pink;
            margin: 0;
          }
          .heart {
            position: relative;
            width: 100px;
            height: 90px;
            background: red;
            transform: rotate(-45deg);
            margin: 0 auto;
          }
          .heart::before,
          .heart::after {
            content: "";
            position: absolute;
            width: 100px;
            height: 100px;
            background: red;
            border-radius: 50%;
          }
          .heart::before {
            top: -50px;
            left: 0;
          }
          .heart::after {
            left: 50px;
            top: 0;
          }
          .name {
            position: absolute;
            top: 35%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            color: white;
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: 20px;
          }
        </style>
      </head>
      <body>
        <div class="heart">
          <div class="name">Gissel</div>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)