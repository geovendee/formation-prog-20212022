cd C:\Program Files\PostgreSQL\12\bin

REM Sauvegarde Base de données
pg_dump --host localhost --port 5432 --username "postgres" --format custom --blobs --file "C:\FORMATION\bdd-postgis.backup" "postgis"

echo Sauvegarde effectuée

pause