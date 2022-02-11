<p align="center">
  <a href="" rel="noopener">
 <img width=500px height=100px src="https://docs.delta.io/latest/_static/delta-lake-logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Delta lake é um projeto de código aberto que permite construir uma arquitetura Lakehouse em cima de sistemas de armazenamento de dados, como S3, ADLS, GCS e HDFS.</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Conteúdo

- [Sobre](#about)
- [Arquitetura](#architeture)
- [Utilização](#usage)
- [Como funciona](#built_using)

## 🧐 Sobre <a name = "about"></a>

## 🔧 Arquitetura MDW com Delta lake <a name = "architeture"></a>

![image](https://live-delta-io.pantheonsite.io/wp-content/uploads/2019/04/Delta-Lake-marketecture-0423c.png)


O Delta lê dados de um sistema de arquivos chamado landing-zone usando dependências deltalake, que são pacotes jars que estão na configuração de sessão do spark, com o qual é possível usar o framework delta lake. após a execução dos script, os dados serão escritos no diretório passado no código, dentro da tabela delta será gravado um diretório chamado _delta_log, que é responsável por armazenar os arquivos incrementais nos metadados da tabela, será algo como
00000000000000000000.json, 0000000000000000000001.json...
O arquivo Json na pasta _delta_log terá as informações como adicionar/remover arquivos parquet (para Atomicidade), stats (para desempenho otimizado e salto de dados), partitionBy (para remoção de partição), readVersions (para viagem no tempo), commitInfo (para auditoria) .

![image](https://miro.medium.com/max/1400/0*5XnRRdbrbuuNGFzJ.png)

lê os dados em formato delta, o que resulta em ganho de performance por ser armazenado em formato parquet e ter uma das grandes vantagens do gerenciamento de metadados _delta_log, são realizadas etapas de processamento em que são removidas colunas desnecessárias e preparação de tabelas com join para MDW modelagem com dados normalizados em formatos de conjunto de dados.

tem a responsabilidade de enriquecer os dados, neste processo é onde tratamos os dados e refinamos para a área de negócios ou quem irá consumir os dados, neste script deixei o exemplo de como utilizar a viagem no tempo utilizando parâmetro passado em a função que declaramos .option("versionAsOf", "0"), abaixo estão as imagens após a ingestão


Este projeto visa fazer um processamento etl simples, usando pyspark com o framework Delta. O trabalho do pyspark consumirá um sistema de arquivos intitulado landing-zone com arquivos no formato json. Usaremos algumas técnicas de viagem no tempo, escrita em formato delta para controle de gerenciamento de tabelas e muito mais.

## 🔧 Upserts Delta Lake <a name = "deltalake"></a>

![image](https://i.ytimg.com/vi/R4f6SKOetB4/maxresdefault.jpg)

Como funciona a lógica do Delta Lake Upserts e como podemos fazer a adoção da nova e moderna Arquitetura Lake House, para isso disponibilizei um notebook jupyter, no qual lemos dados no formato json, que são relacionados aos usuários de um sistema. Nosso principal objetivo é ler esses arquivos no formato Json e convertê-los em uma Tabela Delta. Depois disso podemos acessar os metadados que são gerados dentro de um diretório chamado _delta_log, que podemos acessar através do método DeltaTable.forPath. Após instanciar a Tabela Delta, conseguimos mesclar os novos dados usando whenMatchedUpdateAll usando a condição de que vamos comparar e finalmente atualizar nossa Tabela Delta.