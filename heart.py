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
            height: 18px;
            background: rgba(255, 0, 0, 0.6);
            transform: rotate(-45deg);
            animation: float 8s linear infinite;
          }

          .floating-heart::before,
          .floating-heart::after {
            content: "";
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(255, 0, 0, 0.6);
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

          .heart {
            position: relative;
            width: 200px;
            height: 180px;
            background: red;
            transform: rotate(-45deg);
            margin: 0 auto;
            animation: beat 1.5s infinite ease-in-out;
            z-index: 5;
          }

          .heart::before,
          .heart::after {
            content: "";
            position: absolute;
            width: 200px;
            height: 200px;
            background: red;
            border-radius: 50%;
          }

          .heart::before {
            top: -100px;
            left: 0;
          }

          .heart::after {
            left: 100px;
            top: 0;
          }

          .name {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            color: white;
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: 28px;
            white-space: nowrap;
            text-align: center;
            z-index: 10;
            pointer-events: none;
            animation: glow 1.5s infinite ease-in-out;
          }

          @keyframes beat {
            0%, 100% {
              transform: rotate(-45deg) scale(1);
              box-shadow: 0 0 20px rgba(255, 105, 180, 0.5),
                          0 0 40px rgba(255, 0, 0, 0.4),
                          0 0 60px rgba(255, 255, 255, 0.3);
            }
            30% {
              transform: rotate(-45deg) scale(1.08);
              box-shadow: 0 0 30px rgba(255, 105, 180, 0.8),
                          0 0 60px rgba(255, 0, 0, 0.6),
                          0 0 80px rgba(255, 255, 255, 0.5);
            }
            60% {
              transform: rotate(-45deg) scale(1.15);
              box-shadow: 0 0 40px rgba(255, 105, 180, 1),
                          0 0 80px rgba(255, 0, 0, 0.9),
                          0 0 100px rgba(255, 255, 255, 0.9);
            }
            80% {
              transform: rotate(-45deg) scale(1.08);
              box-shadow: 0 0 30px rgba(255, 105, 180, 0.8),
                          0 0 60px rgba(255, 0, 0, 0.6),
                          0 0 80px rgba(255, 255, 255, 0.5);
            }
          }

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
        <!-- floating hearts -->
        <div class="floating-heart" style="left:10%; animation-delay: 0s;"></div>
        <div class="floating-heart" style="left:30%; animation-delay: 2s;"></div>
        <div class="floating-heart" style="left:50%; animation-delay: 4s;"></div>
        <div class="floating-heart" style="left:70%; animation-delay: 1s;"></div>
        <div class="floating-heart" style="left:90%; animation-delay: 3s;"></div>

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
