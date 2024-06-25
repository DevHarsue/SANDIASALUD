import mariadb

class ComprobadorBD:
    def __init__(self):
        pass
    
    def comprobar(self):
        try:
            with open(".env","r") as x:
                datos = tuple(map(lambda y: y.split("=")[1],x.read().replace("'","").split("\n")))
            
            conn = mariadb.connect(user=datos[0],password=datos[1],host=datos[2],port=int(datos[3]),database=datos[4])
            conn.close()    
            return True
        except Exception as e:
            return False
    
    def testear(self,user,password,host,port):
        try:
            conn = mariadb.connect(user=user,password=password,host=host,port=int(port),database="sandia_salud")
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def crear_env(self,user,password,host,port):
        try:
            with open(".env","w") as x:
                x.write(f"USER='{user}'\n")
                x.write(f"PASSWORD='{password}'\n")
                x.write(f"HOST='{host}'\n")
                x.write(f"PORT='{port}'\n")
                x.write(f"DATABASE='sandia_salud'")
            return True
        except Exception as e:
            return False
    