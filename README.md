# ETL com Python — Santander Dev Week (Alternativa 2: CSV)

Projeto de portfólio do desafio da DIO de Ciência de Dados com Python, focado no fluxo **ETL** (Extração, Transformação e Carregamento).

Como a API da Santander Dev Week pode estar indisponível, usei a **Alternativa 2**: um CSV completo com nome, conta e cartão dos clientes.

## Fluxo

1. **Extract:** lê o arquivo `usuarios.csv` com pandas.
2. **Transform:** gera uma mensagem personalizada de incentivo a investimentos para cada cliente. Se a variável `OPENROUTER_API_KEY` estiver definida, a mensagem é gerada por IA; caso contrário, usa um template local.
3. **Load:** salva o resultado em `usuarios_com_mensagens.csv`.

## Estrutura

```
etl-santander-python/
├── main.py
├── usuarios.csv
├── usuarios_com_mensagens.csv
├── requirements.txt
└── README.md
```

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

Para usar IA na geração das mensagens (opcional):

```bash
export OPENROUTER_API_KEY="sua-chave"
python main.py
```

## Tecnologias

- Python
- pandas
- requests
- OpenRouter (opcional)

## Aprendizados

- Separar Extract, Transform e Load em funções facilita trocar a fonte de dados (API, CSV, lista) sem mexer no resto do código.
- Ter um fallback (template local) evita que o pipeline quebre quando um serviço externo falha.

## Autor

Desenvolvido por Yamaia, desenvolvedor focado em backend, cloud e arquitetura de soluções.
