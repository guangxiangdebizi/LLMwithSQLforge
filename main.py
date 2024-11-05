from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sql_generator import generate_sql
from database import execute_sql
from answer_generator import generate_answer
from api_config import client, MODEL_NAME
import os

app = FastAPI()

# 设置模板文件夹路径
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")


@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    # 读取 index.html 文件内容
    with open(os.path.join(TEMPLATES_DIR, "index.html"), encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get("/man/", response_class=HTMLResponse)
async def get_manual_page():
    # 读取 manual.html 文件内容
    with open(os.path.join(TEMPLATES_DIR, "manual.html"), encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


class Question(BaseModel):
    text: str


@app.post("/ask")
async def ask_question(question: Question):
    # 记录用户请求日志
    print(f"收到用户请求: {question.text}")

    # 生成 SQL 查询
    generated_sql = generate_sql(question.text)
    print(f"生成的 SQL 查询语句: {generated_sql}")

    # 执行 SQL 查询
    query_results = execute_sql(generated_sql)
    print(f"数据库返回的结果: {query_results}")

    # 生成最终回答
    if query_results == [("数据库连接失败，返回默认信息",)]:
        final_answer = f"很抱歉，目前无法提供今天的天气情况，因为数据库连接失败，返回了默认信息。请您稍后再试或联系客户获取帮助。"
    else:
        final_answer = generate_answer(question.text, query_results)
        print(f"生成的回答: {final_answer}")

    return {"answer": final_answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
