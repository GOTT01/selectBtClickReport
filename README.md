# Geração de Mapas de Polígonos no QGIS

Este script Python foi desenvolvido para gerar imagens de mapas de localização individual para polígonos de lotes, a partir de uma camada específica no QGIS. As imagens geradas incluem informações detalhadas sobre cada lote, como nome, Código IBGE e área em metros quadrados.

# Atenção: Este código é apenas umas base, para uma ideia. Utilize-o da melhor forma, realize mudanças/alterações conforme suas necessidades.
By Edu Longo.

## Funcionalidades

- **Geração de Mapas**: Cria um mapa PNG de cada lote selecionado, exibindo sua localização geográfica.
- **Informações sobre o Lote**: Insere automaticamente no mapa o nome do lote, Código IBGE e área em m² (alterável de acordo com a demanda).
- **Organização da Imagem**: Posiciona o mapa no canto direito da imagem e as informações textuais no lado esquerdo, com um fundo branco para melhor legibilidade.

## Pré-requisitos

- **QGIS**: Este script deve ser executado dentro do QGIS, uma plataforma de código aberto para sistemas de informações geográficas.
- **Camada de Lotes**: O script pressupõe que existe uma camada chamada `gvw_distritos_administrativos` (utilizada no desenvlvimento, mas você pode alterar o código para aceitar outras) carregada no projeto do QGIS, contendo polígonos.

## Como Usar

1. **Selecione os Lotes**:
   - No QGIS, clique para selecionar os lotes/polígonos desejados na camada (No exemplo do código foi o SHP de `gvw_distritos_administrativos` da Prefeitura de FLorianópolis).

2. **Execute o Script**:
   - Abra o console Python dentro do QGIS e cole o código do script.

3. **Verifique as Imagens Geradas**:
   - As imagens PNG serão salvas na pasta `C:\Users\Edu\Documents\worspace_edu\script_mapas_lote\`, cada uma nomeada de acordo com o ID do lote.
