cd C:\OSGeo4W64\bin

REM Intégration shapefile
ogr2ogr -f "PostgreSQL" PG:"host=localhost dbname=postgis user=postgres password=postgres port=5432" "C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab\parcelles.shp" -nln "formation.parcelles" -nlt MULTIPOLYGON

echo Intégration terminée avec succès
