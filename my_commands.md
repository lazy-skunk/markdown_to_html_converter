# よく利用するコマンド / Frequently Used Commands

## 仮想環境の作成 / Creating a Virtual Environment
```
PowerShell Set-ExecutionPolicy RemoteSigned CurrentUser  
python -m venv my_venv
```

## 仮想環境の起動 / Activating the Virtual Environment
```
.\my_venv\Scripts\Activate.ps1
```

## 依存関係 / Managing Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.txt
```

## プログラム実行 / Running the Program
```
python markdown_to_html_converter.py
```

## テスト実行 / Running Tests
```
pytest --cov=markdown_to_html_converter --cov-report=html tests/
```

## 仮想環境の終了 / Deactivating the Virtual Environment
```
deactivate
```