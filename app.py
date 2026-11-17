from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Clouddg-eus-app</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                color: #1e293b;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }

            header {
                background: #1e40af;
                color: white;
                padding: 24px 10%;
            }

            header h1 {
                font-size: 26px;
            }

            main {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 40px 20px;
            }

            .container {
                max-width: 700px;
                text-align: center;
                background: white;
                padding: 50px 40px;
                border-radius: 16px;
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
            }

            .container h2 {
                font-size: 36px;
                margin-bottom: 20px;
                color: #1e40af;
            }

            .container p {
                font-size: 17px;
                line-height: 1.7;
                color: #64748b;
                margin-bottom: 30px;
            }

            .button {
                display: inline-block;
                background: #2563eb;
                color: white;
                text-decoration: none;
                padding: 13px 28px;
                border-radius: 8px;
                font-weight: bold;
                transition: background 0.2s;
            }

            .button:hover {
                background: #1d4ed8;
            }

            footer {
                text-align: center;
                padding: 20px;
                color: #94a3b8;
                font-size: 14px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Clouddgeus Customer Portal</h1>
        </header>

        <main>
            <div class="container">
                <h2>Welcome to Clouddgeus!</h2>

                <p>
                    Your application is up and running.
                    This is a simple landing page hosted in Microsoft Azure.
                    More features coming soon!
                </p>

                <a href="#" class="button">Get Started</a>
            </div>
        </main>

        <footer>
            &copy; 2026 Clouddg-eus-app | Powered by Azure
        </footer>

    </body>
    </html>
    """
