# Análise Topológica BGP: China e Taiwan

## Objetivo do Trabalho
Este projeto investiga a geopolítica de territórios disputados focando na relação entre China e Taiwan sob a ótica da infraestrutura da Internet. O objetivo principal é analisar os dados públicos do protocolo BGP (Border Gateway Protocol) para mapear os Sistemas Autônomos (ASes) estrangeiros que atuam como provedores de trânsito (*upstreams*) para as redes taiwanesas. 

A partir da análise dos caminhos lógicos de roteamento (`AS_PATH`), o projeto avalia o grau de dependência da ilha em relação a infraestruturas internacionais, testando a hipótese de resiliência e quantificando os potenciais vetores de isolamento digital.

---

## Ferramentas e Fontes de Dados
* **Python 3:** Linguagem base para extração, limpeza e visualização.
* **Bibliotecas:** `pandas` (manipulação de dados), `requests` (consumo de APIs), `mrtparse` (leitura de arquivos BGP/MRT), `matplotlib` e `seaborn` (geração de gráficos).
* **RIPE RIS (Routing Information Service):** Fornecedor do *snapshot* bruto da tabela de roteamento global.
* **RIPE stat Data API:** Utilizada para identificar ASNs taiwaneses e descobrir a jurisdição corporativa (país) dos provedores estrangeiros.

> **Nota sobre o dataset original (Tabela RIB):** 
> O arquivo de roteamento bruto extraído do RIPE RIS no formato MRT (com aproximadamente **397 MB** compactado) processado por este projeto **não foi incluído neste repositório** por questões de limite de tamanho de armazenamento. O processamento inicial que gerou os arquivos CSV derivados encontra-se documentado no notebook principal.

---

### Scripts e Notebooks
* `Trabalho_de_Redes.ipynb`: Jupyter Notebook principal contendo o passo a passo da pesquisa. Inclui o script de descompactação e varredura da RIB, as consultas às APIs públicas e a etapa de limpeza e agregação de dados.
* `HHI.py`: Script Python dedicado à fundamentação matemática do trabalho, responsável pelo cálculo do Índice Herfindahl-Hirschman (HHI) para medir o nível de concentração de mercado/tráfego nas mãos de parceiros internacionais.

### Pasta `/dados`
Contém todos os artefatos de dados gerados durante a execução do trabalho:
* `asns_taiwan.txt`: Arquivo de texto contendo os 468 ASNs registrados sob jurisdição de Taiwan. Esta lista foi o alvo da pesquisa e foi obtida realizando buscas de delegação territorial na API do RIPE stat.
* `upstreams_taiwan.csv`: Primeira extração bruta do BGP. Mapeia cada ASN de Taiwan ao seu fornecedor de trânsito imediato (penúltimo salto no `AS_PATH`), contabilizando a frequência (força) da conexão.
* `upstreams_enriquecidos.csv`: Planilha anterior expandida com os resultados da API WHOIS, adicionando a coluna do código do país (`pais_upstream`) de cada provedor.
* `upstreams_internacionais.csv`: Base de dados refinada onde as rotas puramente domésticas (Taiwan fornecendo para Taiwan) foram descartadas, isolando 100% da "fronteira digital estrangeira" da ilha.
* `top_destinos_absolutos.csv`: Planilha agregada listando quais Sistemas Autônomos dentro de Taiwan mais recebem rotas de fora.
* `top_upstreams_absolutos.csv`: Planilha agregada listando o peso absoluto (ranking) de cada provedor estrangeiro único provendo acesso para a ilha.

### Pasta `/graficos`
Imagens geradas em alta resolução (300 DPI) para a composição do relatório acadêmico em LaTeX:
* `grafico_paises.png`: Gráfico de pizza ilustrando a distribuição percentual da nacionalidade dos provedores de trânsito (destaque para o forte domínio do eixo EUA, Hong Kong e Reino Unido).
* `grafico_top_asns.png`: Gráfico de barras horizontais rankeando os 10 Sistemas Autônomos globais (Tier-1 e Tier-2) com maior volume de rotas servindo Taiwan.
* `grafico_us_cn.png`: Gráfico de comparação geopolítica direta escancarando a disparidade de dependência de roteamento entre os Estados Unidos e a China Continental.
* `grafico_comparativo_amplo.png`: Visão panorâmica em barras comparando as rotas fornecidas pelos 10 maiores países parceiros contra as rotas operadas pela infraestrutura chinesa, evidenciando o isolamento topológico deliberado em relação a Pequim.
