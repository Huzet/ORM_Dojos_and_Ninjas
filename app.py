from config import app
import routes
from models import ninjas, dojos

if __name__ == '__main__':
    app.run(debug=True)