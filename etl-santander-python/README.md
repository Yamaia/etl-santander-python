# ETL com Python — Santander Dev Week (Alternativa 2: CSV)

Projeto de portfólio do desafio DIO de Ciência de Dados com Python, focado no fluxo **ETL**.
Como a API da Santander Dev Week pode estar indisponível, usei a **Alternativa 2**: um CSV completo (nome, conta, cartão).

## Fluxo
1. **Extract:** lê `usuarios.csv` com pandas.
2. **Transform:** gera uma mensagem personalizada de incentivo a investimentos para cada cliente (IA via OpenRouter se `OPENROUTER_API_KEY` estiver definida; senão, template local).
3. **Load:** salva o resultado em `usuarios_com_mensagens.csv`.

## Como rodar
```bash
pip install -r requirements.txt
python main.py
# opcional, para usar IA:
export OPENROUTER_API_KEY="sua-chave"
```

## Aprendizados
- Separar Extract, Transform e Load em funções facilita trocar a fonte (API, CSV, lista) sem mexer no resto.
- Ter um fallback (template) evita que o pipeline quebre quando um serviço externo falha.

Desenvolvido por Yamaia — desenvolvedor focado em backend, cloud e arquitetura de soluções.
