from qgis.core import QgsProject, QgsVectorLayer, QgsMapSettings, QgsLayout, QgsLayoutItemMap, QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsLayoutExporter, QgsLayoutItemLabel
from PyQt5.QtGui import QFont, QColor

# Definir o caminho para salvar os mapas
output_folder = 'C:/Users/Edu/Documents/worspace_edu/script_mapas_lote/'

# Carregar o projeto atual
project = QgsProject.instance()

# Carregar a camada de lotes (a partir do nome "gvw_distritos_administrativos")
lotes_layer = QgsProject.instance().mapLayersByName("gvw_distritos_administrativos")[0]

# Verificar se a camada foi carregada corretamente
if not lotes_layer.isValid():
    print("Erro ao carregar a camada de lotes")
else:
    print("Camada de lotes carregada com sucesso")

# Obter as feições selecionadas (feições clicadas no QGIS)
selected_features = lotes_layer.selectedFeatures()

# Iterar sobre as feições selecionadas
for feature in selected_features:
    lote_id = feature['id']  # Supondo que "id" é o campo identificador de cada lote, ajuste conforme necessário
    lote_nome = feature['nome']  # Nome do lote
    codigo_ibge = feature['codigo_ibg']  # Código IBGE
    area_m2 = feature['area_m2']  # Área em metros quadrados

    # Criar um novo layout
    layout = QgsLayout(project)
    layout.initializeDefaults()

    # Criar item de mapa no layout
    map_item = QgsLayoutItemMap(layout)
    map_item.setRect(0, 0, 150, 150)  # Ajuste as dimensões do item de mapa

    # Configurar a extensão do mapa para o lote
    feature_extent = feature.geometry().boundingBox()  # Obter a extensão do polígono
    map_item.setExtent(feature_extent)  # Definir a extensão do item de mapa para o bounding box do lote

    # Ajustar a escala do mapa para que a extensão do polígono ocupe a área do layout
    map_item.setScale(1.5 * map_item.scale())  # Ajuste fino para aumentar o espaço ao redor do polígono

    # Centralizar o item de mapa no layout
    layout.addLayoutItem(map_item)
    layout_size = layout.pageCollection().pages()[0].pageSize()

    # Mover o mapa para o canto direito do layout
    map_item.attemptMove(QgsLayoutPoint(layout_size.width() - map_item.sizeWithUnits().width() - 10, 10, QgsUnitTypes.LayoutMillimeters))

    # Adicionar título (nome do lote) ao selo
    title_label = QgsLayoutItemLabel(layout)
    title_label.setText(f"Lote: {lote_nome}")
    title_label.setFont(QFont("Arial", 12, QFont.Bold))  # Negrito
    title_label.adjustSizeToText()
    title_label.setBackgroundColor(QColor(255, 255, 255))  # Fundo branco
    layout.addLayoutItem(title_label)
    title_label.attemptMove(QgsLayoutPoint(10, layout_size.height() - 80, QgsUnitTypes.LayoutMillimeters))  # Posicionar no canto inferior esquerdo

    # Adicionar Código IBGE ao selo
    codigo_ibge_label = QgsLayoutItemLabel(layout)
    codigo_ibge_label.setText(f"Código IBGE: {codigo_ibge}")
    codigo_ibge_label.setFont(QFont("Arial", 10))
    codigo_ibge_label.adjustSizeToText()
    codigo_ibge_label.setBackgroundColor(QColor(255, 255, 255))  # Fundo branco
    layout.addLayoutItem(codigo_ibge_label)
    codigo_ibge_label.attemptMove(QgsLayoutPoint(10, layout_size.height() - 65, QgsUnitTypes.LayoutMillimeters))  # Posição abaixo do título

    # Adicionar Área em m² ao selo
    area_label = QgsLayoutItemLabel(layout)
    area_label.setText(f"Área: {area_m2} m²")
    area_label.setFont(QFont("Arial", 10))
    area_label.adjustSizeToText()
    area_label.setBackgroundColor(QColor(255, 255, 255))  # Fundo branco
    layout.addLayoutItem(area_label)
    area_label.attemptMove(QgsLayoutPoint(10, layout_size.height() - 50, QgsUnitTypes.LayoutMillimeters))  # Posição abaixo do Código IBGE

    # Definir o nome do arquivo de saída
    output_path = f"{output_folder}mapa_lote_{lote_id}.png"

    # Exportar o layout como imagem usando QgsLayoutExporter
    exporter = QgsLayoutExporter(layout)
    result = exporter.exportToImage(output_path, QgsLayoutExporter.ImageExportSettings())

    if result == QgsLayoutExporter.Success:
        print(f"Mapa do lote {lote_id} salvo com sucesso em: {output_path}")
    else:
        print(f"Erro ao exportar o mapa do lote {lote_id}")
