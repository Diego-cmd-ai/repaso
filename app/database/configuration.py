# datos para la conexion a la base de datos

dataBaseName="repasodb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion 
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"
print(dataBaseConnection)