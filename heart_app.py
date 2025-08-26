from flask import Flask
import os

app = Flask(__name__)

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
            width: 150px;
            height: 135px;
            background: red;
            transform: rotate(-45deg);
            margin: 0 auto;
            animation: beat 1s infinite;
          }

          .heart::before,
          .heart::after {
            content: "";
            position: absolute;
            width: 150px;
            height: 150px;
            background: red;
            border-radius: 50%;
          }

          .heart::before {
            top: -75px;
            left: 0;
          }

          .heart::after {
            left: 75px;
            top: 0;
          }

          .name {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg); /* undo heart rotation */
            color: white;
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: 24px;
            white-space: nowrap;
          }

          @keyframes beat {
            0%, 100% {
              transform: rotate(-45deg) scale(1);
            }
            25% {
              transform: rotate(-45deg) scale(1.1);
            }
            50% {
              transform: rotate(-45deg) scale(1.2);
            }
            75% {
              transform: rotate(-45deg) scale(1.1);
            }
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
