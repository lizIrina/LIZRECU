from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mundo Panda - Llinin</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #ff9a9e 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            padding: 50px;
            max-width: 900px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
        }
        
        h1 {
            text-align: center;
            background: linear-gradient(135deg, #ff6b9d, #c44569);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            margin-bottom: 10px;
        }
        
        .subtitle {
            text-align: center;
            color: #888;
            font-size: 1.2em;
            margin-bottom: 40px;
        }
        
        .info-section {
            background: linear-gradient(135deg, rgba(255, 107, 157, 0.1), rgba(196, 69, 105, 0.1));
            padding: 30px;
            border-radius: 20px;
            margin-bottom: 30px;
            border-left: 5px solid #ff6b9d;
        }
        
        .info-section h2 {
            color: #c44569;
            margin-bottom: 15px;
        }
        
        .info-section p {
            color: #555;
            line-height: 1.8;
            font-size: 1.1em;
        }
        
        .panda-facts {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .fact-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(255, 107, 157, 0.2);
            transition: transform 0.3s ease;
            border: 2px solid transparent;
        }
        
        .fact-card:hover {
            transform: translateY(-10px);
            border-color: #ff6b9d;
        }
        
        .fact-card h3 {
            color: #c44569;
            margin-bottom: 10px;
        }
        
        .fact-card p {
            color: #666;
            font-size: 0.95em;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #888;
            font-style: italic;
        }
        
        .panda {
            display: inline-block;
            animation: bounce 2s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            25% { transform: translateY(-10px) rotate(-5deg); }
            75% { transform: translateY(-10px) rotate(5deg); }
        }
        
        .heart {
            color: #ff6b9d;
            animation: pulse 1.5s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><span class="panda">🐼</span> lizzzzzzz <span class="panda">🐼</span></h1>
        <p class="subtitle">Descubriendo a los adorables gigantes de bambú <span class="heart">💕</span></p>
        
        <div class="info-section">
            <h2>🎋 ¿Por qué amamos a los pandas?</h2>
            <p>
                Los pandas gigantes son una de las criaturas más adorables del planeta. 
                Con su pelaje blanco y negro característico, sus movimientos torpes y su amor 
                por el bambú, estos osos han conquistado los corazones de millones de personas 
                en todo el mundo. Son símbolos de paz, ternura y conservación de la naturaleza.
            </p>
        </div>
        
        <div class="panda-facts">
            <div class="fact-card">
                <h3>🍃 Amantes del Bambú</h3>
                <p>Un panda puede comer hasta 38 kg de bambú al día, pasando 12 horas comiendo.</p>
            </div>
            
            <div class="fact-card">
                <h3>🏔️ Hogar en las Montañas</h3>
                <p>Viven en las montañas de China central, en bosques templados llenos de bambú.</p>
            </div>
            
            <div class="fact-card">
                <h3>👶 Bebés Pequeñitos</h3>
                <p>Los pandas bebés nacen del tamaño de una barra de mantequilla, ¡súper pequeños!</p>
            </div>
            
            <div class="fact-card">
                <h3>🎨 Manchas Únicas</h3>
                <p>Cada panda tiene un patrón único de manchas, como nuestras huellas dactilares.</p>
            </div>
            
            <div class="fact-card">
                <h3>😴 Dormilones Tiernos</h3>
                <p>Duermen entre 2 y 4 horas entre comidas, en cualquier posición adorable.</p>
            </div>
            
            <div class="fact-card">
                <h3>🌍 Símbolo de Conservación</h3>
                <p>Son embajadores mundiales de la protección de especies en peligro de extinción.</p>
            </div>
        </div>
        
        <div class="footer">
            <p>🌸 Proyecto CI/CD - Prueba 🌸</p>
            <p>Desarrollado con amor por Llinin</p>
            <p>Desplegado automáticamente con GitHub Actions + Docker + Traefik</p>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok', 'message': 'Mundo Panda funcionando correctamente'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
