import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
# password = os.environ.get("MYSQL_PASSWORD", '12345678')
password = os.environ.get("MYSQL_PASSWORD", 'p29Am6vX')
# db_address = os.environ.get("MYSQL_ADDRESS", '127.0.0.1:3306')
# 正式环境的域名以及端口
db_address = os.environ.get("MYSQL_ADDRESS", 'sh-cynosdbmysql-grp-333sy8t0.sql.tencentcdb.com:26849')
# print(username, password, db_address)

app_id = "wx599f8fadc6580b39"
app_secrt = "e7b85aed291a6b792e82dc0d10d68eaa"