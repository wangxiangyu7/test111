# 书签管理器

这是一个基于 Flask 的个人书签管理项目，用来集中保存、检索和整理常用网页链接。项目提供一个简洁的 Web 页面，用户可以添加书签、编辑书签信息、按关键词搜索，也可以通过标签对书签进行分类筛选。

应用数据默认存储在本地 SQLite 数据库中，适合作为 Flask 入门练习、小型个人工具，或后续扩展成多用户收藏夹系统的基础版本。

## 主要功能

- 添加书签：保存标题、URL、描述和标签。
- 编辑书签：修改已保存书签的标题、链接、描述或标签。
- 删除书签：移除不再需要的收藏链接。
- 关键词搜索：支持按标题、URL 和描述搜索。
- 标签筛选：用逗号分隔标签，并在首页按标签过滤书签。
- URL 自动补全：输入没有协议的 URL 时，会自动补上 `https://`。
- 响应式页面：基础页面适配桌面和移动端浏览。

## 技术栈

- Python
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- SQLite
- HTML、CSS、原生 JavaScript

## 项目结构

```text
.
├── README.md
└── bookmark-manager/
    ├── app/
    │   ├── __init__.py          # Flask 应用创建、配置和数据库初始化
    │   ├── models.py            # Bookmark 数据模型
    │   ├── routes.py            # 首页、添加、编辑、删除等路由
    │   ├── static/
    │   │   └── css/
    │   │       └── style.css    # 页面样式
    │   └── templates/
    │       ├── base.html        # 公共布局模板
    │       ├── index.html       # 书签列表、搜索和标签筛选
    │       ├── add.html         # 添加书签页面
    │       └── edit.html        # 编辑书签页面
    ├── README.md                # 子项目说明
    ├── requirements.txt         # Python 依赖
    └── run.py                   # 应用启动入口
```

## 快速开始

进入应用目录：

```bash
cd bookmark-manager
```

建议创建并启用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

启动应用：

```bash
python run.py
```

启动后在浏览器访问：

```text
http://127.0.0.1:5000
```

首次启动时，应用会自动创建 SQLite 数据库和数据表。

## 使用说明

1. 在首页点击“添加书签”。
2. 填写书签标题和 URL，按需填写描述和标签。
3. 回到首页后，可以通过搜索框查找书签。
4. 点击标签可以筛选对应分类下的书签。
5. 每个书签卡片提供编辑和删除入口。

## 配置说明

应用配置位于 `bookmark-manager/app/__init__.py`：

```python
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
```

当前配置适合本地开发。若部署到生产环境，应替换 `SECRET_KEY`，并根据实际需要调整数据库配置。

## 后续可扩展方向

- 用户注册和登录
- 书签导入、导出
- 收藏夹或分组管理
- favicon 显示
- 批量删除或批量打标签
- 排序和分页

## 许可证

当前项目用于学习和个人使用，尚未声明开源许可证。
