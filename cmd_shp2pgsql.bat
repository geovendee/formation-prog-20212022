cd C:\Program Files\PostgreSQL\12\bin

REM Intégration shapefile
shp2pgsql -d -s 2154 "C:\FORMATION\Cours_Programmation_20212022\ressources\administratif_commune.shp" "formation.administratif_commune" | psql -h localhost -d postgis -U postgres -p 5432

pause