uvicorn src.main:app --reload --host 0.0.0.0 --port 8000


# until nc -z -x -w30 db 5432
# do
# echo "Waiting for database connection"
# sleep 5
# done