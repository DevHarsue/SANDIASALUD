import mariadb
import os
from dotenv import load_dotenv

class BaseDatos:
    def __init__(self):
        load_dotenv()
        self.configuracion = {
            "user":os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "database": os.getenv("DATABASE")}
    
    def crear_conexion(self):
        conexion = mariadb.connect(**self.configuracion)
        return conexion,conexion.cursor()
    
    def consultar(self,sql) -> list:
        try:
            conexion,cursor = self.crear_conexion()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except Exception as e:
            print(e)
    
    def ejecutar(self,sql) ->bool:
        try:
            conexion,cursor = self.crear_conexion()
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
            return True
        except Exception as e:
            print(e)
            return False
            
class Tabla:
    def __init__(self,nombre_tabla) -> None:
        self.bd = BaseDatos()
        self.nombre_tabla = nombre_tabla
        self.definir()
    
    def definir(self):
        self.columnas = [x[0] for x in self.bd.consultar(f"DESCRIBE {self.nombre_tabla}")]
        self.columna_id = self.columnas[0]
    
    def select(self,id=-1):
        if id <= 0:
            condicion = "True"
        else:
            condicion = f"{self.columna_id}={id}"
        sql = f"SELECT * FROM {self.nombre_tabla} WHERE {condicion};"
        return self.bd.consultar(sql)
    
    def insert(self,*datos):
        self.columnas.pop(0)
        if len(datos)!=len(self.columnas):
            print(len(datos))
            print(len(self.columnas))
            return False
        sql = f"INSERT INTO {self.nombre_tabla} ({','.join(self.columnas)}) VALUES('{"','".join(datos)}')"
        self.columnas.insert(0,self.columna_id)
        return self.bd.ejecutar(sql)
    
    def update(self,id,datos):
        columnas_existen = all(tuple(map(lambda x: tuple(filter(lambda y: x==y,self.columnas)),datos.keys())))
        if not columnas_existen:
            return False
        datos = str([str(x)+"="+f"'{y}'" for x,y in zip(datos.keys(),datos.values())])[1:-1].replace('"',"")
        sql = f"UPDATE {self.nombre_tabla} SET {datos} WHERE {self.columna_id}={id};"
        return self.bd.ejecutar(sql)

    def delete(self,id):
        sql = f"DELETE FROM {self.nombre_tabla} WHERE {self.columna_id}={id}"
        return self.bd.ejecutar(sql)
        