from src.utils.MultiPage import MultiPage
from src.apps import first_app, second_app, third_app

app = MultiPage()
app.add_app('App1',first_app.app)
app.add_app('App2',second_app.app)
app.add_app('App3',third_app.app)
app.run()