
import django
django.setup()

from restaurantly_app.seed import run

if __name__== '__main__':
    run()