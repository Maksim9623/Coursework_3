from project.config import config
# from project.models import Genre
from project.server import create_app, db


if __name__ == '__main__':
    application = create_app(config)
    application.run(port=25000)



#@app.shell_context_processor
#def shell():
    #return {
        #"Genre": Genre,
    #}
