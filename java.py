# 使用flask模块 里面的工具Flask
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import config

# 实例化工具的对象  __name__时必须的
app = Flask(__name__)
# 给app去配置数据库连接  但app不可以直接操作数据库
app.config.from_object(config)
# 需要用到SQLAlchemy工具   把app当做参数穿进去
db = SQLAlchemy(app)

# 更新
@app.route("/")
def index():
    return render_template("gg.html")


#代码入口
if __name__ == '__main__':
    app.run(port=8888, debug=True)
