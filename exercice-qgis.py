# Exercice QGIS & Python
# ----------------------------------------------------

# Afficher l'aide ur l'interface iface
help(iface)

# Charger une couche vecteur (La façon la plus rapide d’ouvrir et d’afficher une couche vectorielle avec QGIS est la fonction addVectorLayer de QgisInterface:)
vlayer = iface.addVectorLayer(r"C:\FORMATION\Cours_Programmation_20212022\ressources\administratif_commune.shp", "Communes", "ogr")

# Exporter une couche : utiliser la fonction writeAsVectorFormat de la classe QgsVectorFileWriter
QgsVectorFileWriter.writeAsVectorFormat(vlayer,r"C:\temp\export_communes.shp","utf-8",QgsProject.instance().crs(),"ESRI Shapefile",False)

# Carte
map = QgsProject.instance()
map.count() # retourne le nombre de couche
map.crs() # retourne la projection
map.mapLayers() # retourne une liste (dictionnaire) des couches de la carte

# Couche
vlayer.id() # 'Communes administratif_commune'
vlayer.name() # 'Communes_076ca82d_5507_42a3_a5cd_b723cf059c69'
vlayer.extent() # <QgsRectangle: 276123.70000000001164153 6582709.09999999962747097, 545050 6834664.40000000037252903>
vlayer.isEditable() # False
vlayer.isSpatial() # True
vlayer.isValid() # True
vlayer.maximumScale() # 0.0
vlayer.minimumScale() # 100000000.0
vlayer.source() #'C:\\Users\\martin.delsinne\\Desktop\\Cours Programmation\\2020-2021\\ressources\\administratif_commune.shp'
vlayer.type() # <QgsMapLayerType.VectorLayer: 0>

# Vecteur
vlayer.featureCount() #1238
vlayer.fields() # <qgis._core.QgsFields object at 0x000002859B4F5DC8>
vlayer.geometryType() # 2
vlayer.selectedFeatures() # [<qgis._core.QgsFeature object at 0x000002859B4F53A8>, <qgis._core.QgsFeature object at 0x000002859B4F5678>, etc.]



#---------------------------------------------------------------
# Autre façon de charger une couche vectorielle

## 1. SHAPEFILE 

# chemin vers le shapefile
path_shp = r"C:\FORMATION\Cours_Programmation_20212022\ressources\administratif_commune.shp"

# Pour charger une couche vectorielle, 
# spécifier l’identifiant de la source de données de la couche, un nom pour la couche et le nom du fournisseur
shpLayer = QgsVectorLayer(path_shp, "Communes", "ogr")
if not shpLayer.isValid():
    print("Layer failed to load!")
else:
    # Ajout de la couche Shapefile
    QgsProject.instance().addMapLayer(shpLayer)

## 2. DXF
#uri = "testdata/sample.dxf|layername=entities|geometrytype=Polygon"
#vlayer = QgsVectorLayer(uri, "layer_name_you_like", "ogr")
#QgsProject.instance().addMapLayer(vlayer)


## 3. PostGIS

# La source des données est une chaîne de caractères contenant toutes les informations nécessaires pour créer une connexion à la base de données PostGIS,
# la classe QgsDataSourceURI peut générer cette chaîne pour vous.

uri = QgsDataSourceUri()
# set host name, port, database name, username and password
uri.setConnection("localhost", "5432", "postgis", "postgres", "postgres")
# set database schema, table name, geometry column
uri.setDataSource("formation", "administratif_departement", "geom")

# Init couche vecteur PostGIS
pgLayer = QgsVectorLayer(uri.uri(True), "Departements", "postgres")

# Ajout de la couche PostGIS à la carte
QgsProject.instance().addMapLayer(pgLayer, True)

# Exporter la couche au format Shapefile
QgsVectorFileWriter.writeAsVectorFormat(pgLayer,r"c:\temp\export_departements.shp","utf-8",QgsProject.instance().crs(),"ESRI Shapefile",False)

  