from aiohttp import web
import function_s as fu
import os

APP_DIR = os.path.dirname(os.path.realpath(__file__))


async def handle(request: web.Request) -> web.StreamResponse:
    css = """<style>
         body {
        background-color: #87ceeb
        }
        h1 {
          color: White;
          text-align: center
        } 
        h2 {
          color: black;
          text-align: center
        } 

        </style>
        </head>
        <body>"""
    text = f'''<!DOCTYPE html>
    <html>
    {css}
    <h1>"Выберите задачу"<h1/>
    <form action="/stipendion" target="_blank">
       <button>Расчет стипендии</button>
    </form>
    <form action="/triangle" target="_blank">
       <button>Расчет треугольников</button>
    </form>
    
    </html>'''

    return web.Response(text=text, content_type='text/html')

async def stipendion(request: web.Request) -> web.StreamResponse:
    name = request.match_info.get("name", "name")
    css = """<style>
    body {
      background-color: white;
    }
    h1 {
      color: red;
      text-align: center
    } 
    h2 {
      color: black;
      text-align: center
    } 
    </style>
    </head>
    <body>"""
    text = f'''<!DOCTYPE html>
<html>
<form action="/stipendion" method="POST">
   Пожалуйста, введите исходные данные:<br>
   <input type="text" name="d1" value="" placeholder="оценка 1" required><br>
   <input type="text" name="d2" value="" placeholder="оценка 1" required><br>
   <input type="text" name="session" value="" placeholder="сессия сдана вовремя (y/n)" required><br>
   <input type="text" name="d4" value="" placeholder="размер полной стипендии" required><br>
   <input type="submit" value="Войти на сайт">
</form>
</html>'''

    return web.Response(text=text, content_type='text/html')


async def triangle(request: web.Request) -> web.StreamResponse:
    css = """<style>
        body {
          background-color: white;
        }
        h1 {
          color: red;
          text-align: center
        } 
        h2 {
          color: black;
          text-align: center
        } 
        </style>
        </head>
        <body>"""
    text = f'''<!DOCTYPE html>
    <html>
    <form action="/triangle" method="POST">
       Пожалуйста, введите исходные данные:<br>
       <input type="text" name="k1" value="" placeholder="сторона 1" required><br>
       <input type="text" name="k2" value="" placeholder="сторона 2" required><br>
       <input type="text" name="h1" value="" placeholder="сторона 3 " required><br>
       <input type="submit" value="Проверить">
    </form>
    </html>'''
    return web.Response(text=text, content_type='text/html')

async def triangle1(request) -> web.StreamResponse:
    a = await request.post()
    print(a)

    k1 = int(a["k1"])
    k2 = int(a["k2"])
    h1 = int(a["h1"])
    print(a)
    data = fu.triaangle(k1, k2, h1)
    css = """<style>
        body {
          background-color: white;
        }
        h1 {
          color: red;
          text-align: center
        } 
        h2 {
          color: black;
          text-align: center
        } 
        </style>
        </head>
        <body>"""
    text = f'''<!DOCTYPE html>
    <html>
    <h1>{data}<h1/>
    <form action="/" target="_blank">
   <button>Переход по ссылке</button>
    </form>
    </html>'''
    return web.Response(text=text, content_type='text/html')


async def stipendion1(request) -> web.StreamResponse:

    a = await request.post()
    print(a)

    a1 = int(a["d1"])
    b1 = int(a["d2"])
    c1 = a["session"]
    n = int(a["d4"])
    print(a1)
    data = fu.stipendion(a1, b1, c1, n)
    css = """<style>
    body {
      background-color: white;
    }
    h1 {
      color: red;
      text-align: center
    } 
    h2 {
      color: black;
      text-align: center
    } 
    </style>
    </head>
    <body>"""
    text = f'''<!DOCTYPE html>
<html>
<h1>{data}<h1/>
<form action="/" target="_blank">
   <button>Переход по ссылке</button>
</form>
</html>'''

    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes(
    [web.get("/", handle), web.get("/stipendion", stipendion), web.post("/stipendion", stipendion1), web.get("/triangle", triangle), web.post("/triangle", triangle1), web.get("/{name}", handle)])

web.run_app(app)
