# **Análise de Fundos de Investimento - CVM**

Este repositório contém um script automatizado em Python para o download, extração e processamento de dados de fundos de investimento disponibilizados pela Comissão de Valores Mobiliários (CVM). O código utiliza as bibliotecas Pandas e Requests para processar de forma eficiente os dados dos fundos.

## **Índice**
- Contexto
- Funcionalidades
- Estrutura do Projeto
- Instalação
- Uso
- Contribuição
- Licença

## **Contexto**
Este projeto visa automatizar o processo de download, tratamento e análise dos dados de fundos de investimento disponibilizados pela CVM. A partir dos dados processados, é possível realizar análises sobre o comportamento dos fundos, como variações de patrimônio e número de cotistas ao longo do tempo, utilizando a biblioteca Pandas.

## **Funcionalidades**
- **Download automatizado:** Baixa arquivos `.zip` contendo dados dos fundos de investimento disponíveis no site da CVM.
- **Extração e leitura:** Extrai e processa arquivos `.csv` diretamente dos arquivos `.zip` baixados.
- **Limpeza e transformação dos dados:** Limpa e formata os dados de forma eficiente para facilitar a análise.
- **Exemplo de análise:** Inclui um exemplo de análise de variação do patrimônio e número de cotistas entre datas específicas.

## **Estrutura do Projeto**
```
dados_fundos_cvm/
│
├── src/
│   ├── data_processing.py    # Funções para download e processamento dos dados
│   └── main.py               # Script principal que executa a análise dos dados
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do projeto
└── .gitignore                # Arquivos a serem ignorados pelo Git
```

## **Instalação**
### Pré-requisitos
- Python 3.8+
As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute o seguinte comando:
```
pip install -r requirements.txt
```

### **Bibliotecas utilizadas**
- **Pandas:** Para manipulação e análise de dados.
- **Requests:** Para download de arquivos da web.
- **Zipfile:** Para descompactação de arquivos `.zip`.
- **OS:** Para operações no sistema de arquivos.

## **Uso**
### Baixar o repositório
Clone o repositório para sua máquina local:
```
git clone https://github.com/seu-usuario/analise-fundos-cvm.git
cd analise-fundos-cvm
```
### **Executar o script**
Após instalar as dependências, execute o script principal:
```
python src/main.py
```
### **Dados processados**
O script baixa e processa os dados dos fundos de investimento, criando um DataFrame consolidado com as informações extraídas.

### **Exemplo de Análise**
O script inclui um exemplo de análise que calcula a variação do patrimônio e do número de cotistas dos fundos entre duas datas específicas.

## **Contribuição**
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um *pull request*.

Para contribuir:

1. Faça um *fork* do projeto.
2. Crie uma nova *branch* para sua funcionalidade:
```
git checkout -b feature/nova-funcionalidade
```
3. Faça suas alterações e faça um *commit*:
```
git commit -m 'Adiciona nova funcionalidade'
```
4. Envie as alterações para o repositório principal:
```
git push origin feature/nova-funcionalidade
```
5. Abra um *pull* request para revisão.

## **Licença**
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
