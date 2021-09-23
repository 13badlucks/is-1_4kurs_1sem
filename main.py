from aiohttp import web

def stipendion(a, b, c, n):

    # a = int(input("Введите оценку 1: "))
    # b = int(input("Введите оценку 2: "))
    # c = int(input("Введите одно значение из 2-х (y или n, где y - сессия сдана вовремя, а n - после указанного срока): "))

    if (a > 3) and (b > 3) and (c=="y"):
        if (a == 4) and (b == 4):
            pays = n
            data = f"Студент будет получать стипендию в размере: {pays} р."
            # print(data)
    if (a == 4 and b == 5) or (a == 5 and b == 4):
        pays = ( n + ((n/100)*25))
        data = f"Студент будет получать стипендию в размере: {pays}р."
        # print(data)
    if (a == 5 and b == 5):
        pays = (n + ((n/100)*50))
        data = f"Студент будет получать стипендию в размере: {pays}р."
        # print(data)
    if (a < 4) or (b < 4) or (c == "n"):
        data = "Студент не будет получать стипендию"
        # print(data)

    return str(data)

async def handle(request: web.Request) -> web.StreamResponse:
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
<form action="/" method="POST">
   Пожалуйста, введите исходные данные:<br>
   <input type="text" name="d1" value="" placeholder="оценка 1" required><br>
   <input type="text" name="d2" value="" placeholder="оценка 1" required><br>
   <input type="text" name="session" value="" placeholder="сессия сдана вовремя (y/n)" required><br>
   <input type="text" name="d4" value="" placeholder="размер полной стипендии" required><br>
   <input type="submit" value="Войти на сайт">
</form>
</html>'''

    return web.Response(text=text, content_type='text/html')

async def handle1(request) -> web.StreamResponse:

    a = await request.post()
    print(a)

    a1 = int(a["d1"])
    b1 = int(a["d2"])
    c1 = a["session"]
    n = int(a["d4"])
    print(a1)
    data = stipendion(a1, b1, c1, n)
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
    [web.get("/", handle), web.post("/", handle1), web.get("/{name}", handle)])

web.run_app(app)
