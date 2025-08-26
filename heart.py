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
            background: linear-gradient(135deg, pink, lightpink, mistyrose);
            overflow: hidden;
            margin: 0;
          }

          /* Floating hearts in background */
          .floating-heart {
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(255, 0, 0, 0.5);
            transform: rotate(-45deg);
            animation: float 8s linear infinite;
          }

          .floating-heart::before,
          .floating-heart::after {
            content: "";
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(255, 0, 0, 0.5);
            border-radius: 50%;
          }

          .floating-heart::before {
            top: -10px;
            left: 0;
          }

          .floating-heart::after {
            left: 10px;
            top: 0;
          }

          @keyframes float {
            0% {
              transform: translateY(100vh) rotate(-45deg) scale(0.5);
              opacity: 0;
            }
            30% {
              opacity: 1;
            }
            100% {
              transform: translateY(-10vh) rotate(-45deg) scale(1);
              opacity: 0;
            }
          }

          /* Main perfect heart */
          .heart {
            position: relative;
            width: 150px;   /* base square */
            height: 150px;
            background: red;
            transform: rotate(-45deg);
            animation: beat 1.5s infinite ease-in-out;
            z-index: 5;
          }

          .heart::before,
          .heart::after {
            content: "";
            position: absolute;
            width: 150px;   /* equal size to square */
            height: 150px;
            background: red;
            border-radius: 50%;
          }

          .heart::before {
            top: -75px; /* half the height */
            left: 0;
          }

          .heart::after {
            left: 75px; /* half the width */
            top: 0;
          }

          /* Name inside */
          .name {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            color: white;
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: 26px;
            text-align: center;
            z-index: 10;
            pointer-events: none;
            animation: glow 1.5s infinite ease-in-out;
          }

          /* Heart beat animation */
          @keyframes beat {
            0%, 100% {
              transform: rotate(-45deg) scale(1);
              box-shadow: 0 0 20px rgba(255, 105, 180, 0.5),
                          0 0 40px rgba(255, 0, 0, 0.4),
                          0 0 60px rgba(255, 255, 255, 0.3);
            }
            50% {
              transform: rotate(-45deg) scale(1.15);
              box-shadow: 0 0 40px rgba(255, 105, 180, 1),
                          0 0 80px rgba(255, 0, 0, 0.8),
                          0 0 100px rgba(255, 255, 255, 0.8);
            }
          }

          /* Name glow in sync */
          @keyframes glow {
            0%, 100% {
              text-shadow: 0 0 5px white, 0 0 10px hotpink, 0 0 15px red;
            }
            50% {
              text-shadow: 0 0 15px white, 0 0 30px hotpink, 0 0 40px red;
            }
          }
        </style>
      </head>
      <body>
        <!-- floating background hearts -->
        <div class="floating-heart" style="left:10%; animation-delay: 0s; animation-duration: 7s;"></div>
        <div class="floating-heart" style="left:25%; animation-delay: 2s; animation-duration: 9s;"></div>
        <div class="floating-heart" style="left:40%; animation-delay: 4s; animation-duration: 6s;"></div>
        <div class="floating-heart" style="left:60%; animation-delay: 1s; animation-duration: 10s;"></div>
        <div class="floating-heart" style="left:80%; animation-delay: 3s; animation-duration: 8s;"></div>

        <!-- main heart -->
        <div class="heart">
          <div class="name">Gissel</div>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
