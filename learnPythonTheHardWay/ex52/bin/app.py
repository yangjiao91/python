import web
import sys
sys.path.append('E:\\yangjiao91\\python\\learnPythonTheHardWay\\ex52')
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls,globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session
    render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()




# import web
#
# web.config.debug = False
#
# urls = (
#     "/count", "count",
#     "/reset", "reset"
# )
# app = web.application(urls, locals())
# store = web.session.DiskStore('sessions')
# session = web.session.Session(app, store, initializer={'count': 0})
#
# class count:
#     def GET(self):
#         session.count += 1
#         return str(session.count)
#
# class reset:
#     def GET(self):
#         session.kill()
#         return ""
#
# if __name__ == "__main__":
#     app.run()
