# LLMwithSQLforge
这是一个基于MySQL数据库和LLM的一个前端后端交互的项目
This is a frontend-backend interactive project based on a MySQL database and LLM.
# README.md

## 项目简介 (Project Introduction)

### 简介 (Introduction)

这是一个基于 FastAPI 和 OpenAI GLM 模型的智能问答系统。用户可以在前端页面输入问题，系统将通过后端服务自动生成 SQL 查询，从 MySQL 数据库中获取相关信息，并生成详细的回答。同时，系统还支持日志窗口，用户可以查看数据处理的每一个步骤，包括生成的 SQL 查询和数据库返回的结果。

This is an intelligent question-answering system based on FastAPI and OpenAI GLM model. Users can input questions in the front-end page, and the system will automatically generate SQL queries in the backend, retrieve related information from the MySQL database, and generate a detailed answer. The system also supports a log window where users can view each step of data processing, including the generated SQL queries and database results.

### 功能 (Features)
- 用户可以在前端页面输入问题，系统自动生成 SQL 查询语句并执行。
- 前端界面包含问答窗口和日志窗口，日志窗口用于显示查询过程的详细步骤。
- 用户可以访问 `/man/` 页面查看使用手册，了解如何使用问答系统。
- 置顶框支持一键跳转到手册页面，便于用户快速获取帮助。

- Users can input questions in the front-end page, and the system automatically generates and executes SQL queries.
- The front-end interface includes a Q&A box and a log box, where the log box shows detailed steps of the query process.
- Users can access the `/man/` page to view the user manual and learn how to use the Q&A system.
- The top bar includes a quick access button for the manual page, allowing users to easily get help.

## 文件结构 (File Structure)

```
txt2sqltest/
├── main.py                    # 主程序入口，定义 FastAPI 应用并启动服务
├── sql_generator.py           # SQL生成逻辑，使用GLM模型生成SQL查询语句
├── answer_generator.py        # 回答生成逻辑，使用GLM模型结合查询结果生成回答
├── database.py                # 数据库访问层，执行生成的SQL查询
├── api_config.py              # API配置文件，包含API密钥和模型调用选择
├── templates/                 # 存放HTML模板文件的文件夹
│   ├── index.html             # HTML界面文件，包含问答和日志窗口
│   └── manual.html            # HTML手册页面，包含系统使用说明和指南
└── requirements.txt           # 项目依赖文件
```

```
txt2sqltest/
├── main.py                    # Main program entry, defines FastAPI app and starts service
├── sql_generator.py           # SQL generation logic, using GLM model to generate SQL queries
├── answer_generator.py        # Answer generation logic, using GLM model and query results to generate answers
├── database.py                # Database access layer, executing the generated SQL queries
├── api_config.py              # API configuration file, containing API key and model settings
├── templates/                 # Folder for storing HTML templates
│   ├── index.html             # HTML interface for Q&A and log windows
│   └── manual.html            # HTML manual page for system usage instructions
└── requirements.txt           # Project dependency file
```

## 安装与运行 (Installation and Running)

### 环境要求 (Requirements)
- Python 3.8 及以上版本
- MySQL 数据库
- 需要有 OpenAI API 的访问权限

- Python 3.8 or above
- MySQL database
- Access to OpenAI API

### 安装步骤 (Installation Steps)
1. 克隆此项目到本地：

   Clone this project to your local environment:
   ```bash
   git clone https://github.com/guangxiangdebizi/LLMwithSQLforge.git
   ```

2. 进入项目目录并创建虚拟环境：

   Enter the project directory and create a virtual environment:
   ```bash
   cd txt2sqltest
   python -m venv .venv
   source .venv/bin/activate  # Windows 使用 `.venv\Scripts\activate`
   ```

3. 安装依赖库：

   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. 配置数据库连接与 API 密钥：

   Configure database connection and API key in `api_config.py` and `database.py`.

5. 启动服务：

   Start the server:
   ```bash
   python main.py
   # 或者使用 uvicorn 启动
   uvicorn main:app --reload
   ```

### 访问服务 (Accessing the Service)
- 在浏览器中打开 `http://127.0.0.1:8000` 访问问答系统。
- 点击页面顶部的按钮可以跳转到 `/man/` 页面查看使用手册。

- Open `http://127.0.0.1:8000` in your browser to access the Q&A system.
- Click the button on the top of the page to navigate to `/man/` page for the user manual.

## 使用说明 (Usage Guide)
1. **输入问题**：在页面的输入框中输入你想要咨询的问题，然后点击“发送”按钮。
2. **查看日志**：在右侧的日志窗口中查看系统处理该问题的每一个步骤，包括生成的 SQL 查询语句和查询结果。
3. **查看手册**：点击置顶栏中的“使用手册”按钮可以跳转到手册页面，获取更多系统的使用信息。

1. **Input Questions**: Enter your question in the input box on the page, then click the "Send" button.
2. **View Logs**: Check the log window on the right to see every step the system takes, including generated SQL queries and results.
3. **View Manual**: Click the "User Manual" button in the top bar to navigate to the manual page for more information on using the system.

## 贡献 (Contributing)
欢迎贡献代码和改进建议！请通过 GitHub 提交 Pull Request 或创建 Issue。

Contributions are welcome! Please submit a Pull Request or create an Issue via GitHub.

## 许可证 (License)
MIT 许可证。详情请参阅 LICENSE 文件。

Licensed under the MIT License. See LICENSE file for details.

## 鸣谢 (Acknowledgements)
- [FastAPI](https://fastapi.tiangolo.com/) - Web 框架
- [OpenAI](https://www.openai.com) - 提供的 API 接口
- [Uvicorn](https://www.uvicorn.org/) - ASGI 服务器

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [OpenAI](https://www.openai.com) - API services
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

