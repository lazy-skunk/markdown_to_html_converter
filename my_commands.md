# よく利用するコマンド / Frequently Used Commands

## Docker
```
docker images -a
docker-compose down --rmi all
docker-compose build --no-cache
docker-compose up -d
docker-compose ps
docker-compose exec app bash
docker-compose stop
docker-compose down
```

## プログラム実行 / Running the Program
```
python markdown_to_html_converter.py
```

## テスト実行 / Running Tests
```
pytest --cov=src.markdown_to_html_converter --cov-report=html tests/
```

## 仮想環境の終了 / Deactivating the Virtual Environment
```
deactivate
```