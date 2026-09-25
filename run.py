import os
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[INFO] Starting EstateIQ PropTech Intelligence Server on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
