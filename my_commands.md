# よく利用するコマンド / Frequently Used Commands

## Docker
```
docker-compose images
docker-compose ps
docker-compose build --no-cache
docker-compose up -d
docker-compose exec app bash
docker-compose stop
docker-compose down --rmi all
```

## プログラム実行 / Running the Program
```
python src/app.py
```

## テスト実行 / Running Tests
```
pytest --cov=src --cov-config=.coveragerc --cov-report=html tests/
```