/****************************
 * 16/03/2020
 * Ajout de la méthode getCoordinates() à la classe City
 * 
 * Classe : City
 * Propriétés : ville, pays, habitants, lat, lon
 * 
 ****************************/
class City {

    // 5 propriétés de l'objet initialisées par le constructeur
    constructor(nomVille, nomPays, nbreHabitants, latitude, longitude) {
        this.ville = nomVille; // String
        this.pays = nomPays; // String
        this.habitants = nbreHabitants; // Integer
        this.lat = latitude; // Number
        this.long = longitude // Number
    }

    // Fonction dédiée à un objet instance de City
    getCoordinates() {
        // Instruction de ma fonction
        // retourne un objet X Y

        return { x: this.long, y: this.lat }
    }

};

// Instanciation d'un premier objet sans preciser de paramètre
let ville0 = new City();

// Instanciation d'un second objet avec paramètres
let ville1 = new City("Marseille", "France", 861635, 43.300000, 5.400000);
console.log(ville1.getCoordinates())

// Déclaration d'un tableaux JS [...]
var monTableau = [
    // 1 er élément
    ville0, // virgule comme séparateur
    // 2nd élément
    ville1,
    // 3ème élément
    new City("Lille", "France", 232741, 50.6365654, 3.0635282) // pas de virgule car dernier
]

// Ajouter un élément : push
monTableau.push(new City("Rio", "Brésil", 6320000, -22.9110137, -43.2093727));

// Afficher le tableau dans la console
console.log(monTableau); // afficher le tableau dans la console

/**
 * propriété 'length' (attribut) du tableau :
 * Retourne le nombre d'élément (entier)
 */
console.log(monTableau.length); // 4 

var index = 0; // index du tableau
while (index < monTableau.length) { // Boucle sur tous les éléments du tableau

    // compléter ici
    try {
        var element = monTableau[index];
        if (element.ville != undefined) { // Exclure les villes 'undefined'
            console.log(element.ville + " ::: x:" + element.getCoordinates().x.toString() + " y:" + element.getCoordinates().y.toString());
        }
    } catch (error) {
        console.log("Erreur rencontrée en parcourant les éléments du tableau");
        console.log(error);
    }

    index++; // Incrémentation de l'index
}

/****************************
 * 20/03/2020
 * Initiation à OpenLayers
 * 
 * Créer une carte - ol.Map
 * Ajouter des fonctionnalités à la carte - ol.control
 * Ajouter des couches à la carte - ol.layer
 * Afficher une popup - ol.Overlay
 ****************************/

// Raster OpenStreetMap
// Instanciation d'un objet type ol.source.OSM
var osm = new ol.source.OSM();

// Map OpenLayers
const map = new ol.Map({

    target: 'map', // nom de la <div> HTML

    // Tableau des couches de la carte
    layers: [
        // 1er élément : Nouvelle couche tuilée OSM
        new ol.layer.Tile({
            source: osm
        })
    ],

    // Tableau des contrôles (fonctionalités)
    controls: ol.control.defaults().extend([
        // 1er élément : mini-map - vue générale
        new ol.control.OverviewMap({
            layers: [
                new ol.layer.Tile({
                    source: osm
                })
            ],
            className: "ol-overviewmap"
        }),
        // 2nd élément : Plein-écran
        new ol.control.FullScreen(),
        // 3ème élément : Echelle
        new ol.control.ScaleLine(),
        // 4ème élément : Coordonnées de la souris
        new ol.control.MousePosition({
            coordinateFormat: ol.coordinate.createStringXY(4),
            projection: 'EPSG:4326',
            className: 'custom-mouse-position',
            target: document.getElementById('mouse-position')
        })
    ]),

    // Tableaux des intercations
    interactions: ol.interaction.defaults().extend([
        new ol.interaction.DragRotateAndZoom() // Rotation
    ]),

    view: new ol.View({ // Vue initiale
        center: ol.proj.fromLonLat([2.294481, 48.858370]), // Paris WGS84
        zoom: 6
    })
});

/**
 * IGN : Service WMTS
 * Retourne des images précalculées (tuiles) suivant une grille prédéfinies 
 */
var resolutions = [];
var matrixIds = [];
var proj3857 = ol.proj.get('EPSG:3857');
var maxResolution = ol.extent.getWidth(proj3857.getExtent()) / 256;

for (var i = 0; i < 18; i++) {
    matrixIds[i] = i.toString();
    resolutions[i] = maxResolution / Math.pow(2, i);
};

var tileGrid = new ol.tilegrid.WMTS({
    origin: [-20037508, 20037508],
    resolutions: resolutions,
    matrixIds: matrixIds
});

var ign = new ol.source.WMTS({
    url: 'https://wxs.ign.fr/pratique/geoportail/wmts',
    layer: 'GEOGRAPHICALGRIDSYSTEMS.MAPS',
    matrixSet: 'PM',
    format: 'image/jpeg',
    projection: 'EPSG:3857',
    tileGrid: tileGrid,
    style: 'normal'
});

map.addLayer(
    new ol.layer.Tile({ source: ign, visible: false })
);

/**
 * ArcGIS REST Service
 * Service de carte tuilé ArcGIS Server
 */
var arcgis = new ol.source.TileArcGISRest({
    url: 'https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer'
});

map.addLayer(
    new ol.layer.Tile({
        extent: [134987.79195151184, 6175929.419557666, 428505.98056670104, 6319172.410564141],
        source: arcgis,
        opacity: 0.7
    })
);

/**
 * Visibilité des couches
 * @param checkbox 
 */
function setVisibility(checkbox) {
    map.getLayers().forEach(function (layer) { // Parcourir les couches
        switch (checkbox.id) { // selon l'id de la checkbox, on agit sur la bonne couche
            case 'cbOSM': // OpenStreetMap
                if (layer.getSource() == osm) {
                    layer.setVisible(checkbox.checked);
                };
                break;
            case 'cbWMTS': // IGN
                if (layer.getSource() == ign) {
                    layer.setVisible(checkbox.checked);
                }
                break;
            case 'cbTileArcGISRest': // ArcGIS
                if (layer.getSource() == arcgis) {
                    layer.setVisible(checkbox.checked);
                }
                break;
        }
    });
}

/**
 * Nouvelle couche vecteur
 */
var vectorLayer = new ol.layer.Vector({
	// Source de la couche vecteur
	source: new ol.source.Vector({
		// tableau d'entités
		features: [
		// Création d’une entité
		// Objet de type ol.Feature initialisé avec une géométrie et un nom
		new ol.Feature({
			geometry: new ol.geom.Point(ol.proj.fromLonLat([2.294481, 48.858370])),
			name: "Paris"
			})
		]
    })
});

map.addLayer(vectorLayer); // Ajout de la couche vecteur à la carte -- method 'addLayer()'*/

/**
 * Création d'un style 'Icon'
 * @type {module:ol/style/Icon~Options}
 */
var iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
		// mon icône
		src: 'data/icon.png'
    })
});
// Parcourir les entités de la couche
// <Array>.forEach (ES6) : parcours du tableau
vectorLayer.getSource().getFeatures().forEach(function (feature) {
    feature.setStyle(iconStyle);
});

/**
 * Ajout d'entités à la couche vecteur
 */
monTableau.forEach(function (element) { // <Array>.forEach (ES6) : parcours du tableau
    // Exclure les villes 'undefined'
    if (element.ville != undefined) {
        // Créer une nouvelle entité instance de la classe Feature
        var feature = new ol.Feature({
            // Propriété geometry : ol.geom.Point
            geometry: new ol.geom.Point(ol.proj.fromLonLat(
                [element.getCoordinates().x, element.getCoordinates().y]
            )),
            // Propriété name : String
            name: element.ville
        })
        // Appliquer le style
        feature.setStyle(iconStyle);
        // Ajouter l'entité à la source de la couche
        vectorLayer.getSource().addFeature(feature);
    }
})

/**
 * Création d'un objet ol.Overlay pour ancrer la popup sur la carte.
 */
var popup = new ol.Overlay({
    element: document.getElementById('popup') // <div>
});
map.addOverlay(popup);

// Fermer la popup
function closePopup() {
    popup.setPosition(undefined); // masquer la popup
}

/**
 * Évènement click sur la carte
 */
map.on('click', function (event) {
    // Récupérer l'entité ol.Feature
    var feature = map.forEachFeatureAtPixel(event.pixel,
        function(feature, layer) {
            if (layer != drawLayer) {
                return feature;
            } else {
                return null;
            }
        }
    );
    if (feature && !drawEnable) { // Si une entité retournée
        var coordinates = feature.getGeometry().getCoordinates();
        popup.setPosition(coordinates); // Position de la popup
        
        //Contenu de la popup
        document.getElementById('popup-content').innerHTML = "<p style='margin:0'>" + feature.get('name').replace(/\n/g, '<br>') + "</p>";
        
        // Ajout des coordonnées EPSG:3857 dans la popup
        let x = coordinates[0].toFixed(2);
        let y = coordinates[1].toFixed(2);
        document.getElementById('popup-content').innerHTML += "<br><p style='margin:0'><b>x : " + x.toString() + ", y : " + y.toString() + "</b></p>";
    
    } else {
        if (document.getElementById('popup') != null) { // popup ouverte
            closePopup();
        }
    }
});

// Control - ZoomSlider
var zoomslider = new ol.control.ZoomSlider();
map.addControl(zoomslider);

// Control - ZoomToExtent
var zoomToExtent = new ol.control.ZoomToExtent({
    extent: [134987.79195151184, 6175929.419557666, 428505.98056670104, 6319172.410564141]
});
map.addControl(zoomToExtent);

/**
 * Widget dessin
 */
var typeSelect = document.getElementById('type');

// Couche dessin
var source = new ol.source.Vector({ wrapX: false });
var drawLayer = new ol.layer.Vector({
    source: source
});
map.addLayer(drawLayer);

var draw;
var drawEnable = false;

function addInteraction() {
    var value = typeSelect.value;
    if (value !== 'None') {
        drawEnable = true;
        draw = new ol.interaction.Draw({
            source: source,
            type: /** @type {ol.geom.GeometryType} */ (typeSelect.value)
        });
        map.addInteraction(draw);
    } else {
        drawEnable = false;
    }
}

/**
 * Handle change event.
 */
typeSelect.onchange = function () {
    map.removeInteraction(draw);
    addInteraction();
};

addInteraction();