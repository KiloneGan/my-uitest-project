# GLD 登录 UI 自动化（Python 3.10 + Playwright + pytest）

## 1) 安装

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

## 2) 配置环境变量（PowerShell）

```powershell
$env:BASE_URL="http://www.qzdatasoft.com:8084/gld/"
$env:LOGIN_USERNAME="qzkj"
$env:LOGIN_PASSWORD="123456"

# 按实际页面调整以下选择器
$env:LOGIN_USERNAME_SELECTOR="input[name='username']"
$env:LOGIN_PASSWORD_SELECTOR="input[type='password']"
$env:LOGIN_SUBMIT_SELECTOR="button[type='submit']"

# 成功断言：二选一（推荐文本断言更明确）
$env:LOGIN_SUCCESS_TEXT="首页"
# 或
$env:LOGIN_SUCCESS_SELECTOR=".main-container"

# 失败断言
$env:LOGIN_ERROR_SELECTOR=".el-message--error"

# 是否无头执行（true/false）
$env:HEADLESS="false"
```

## 3) 执行测试

```bash
pytest
```

## 4) 定位器获取建议

如果默认选择器不匹配，先执行：

```bash
python -m playwright codegen http://www.qzdatasoft.com:8084/gld/
```

在打开的录制器中操作登录流程，复制稳定的 CSS/XPath/Role 定位器后替换环境变量。
