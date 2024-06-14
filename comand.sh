docker compose run --user 1000  app sh -c 'alembic init migrations'

docker compose run --user 1000  app sh -c 'alembic revision --autogenerate -m "add categories table"' # gerar migrations

docker compose run --user 1000  app sh -c 'alembic upgrade head' # executa migrations


docker exec -it postgresql psql --version

docker-compose up --scale postgres-test=0