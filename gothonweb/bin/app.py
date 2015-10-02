import web

urls = (
  '/', 'index'
)

app = web.application(urls,globals())

class index:
    def GET(self):
        greeting = "Hello world"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
