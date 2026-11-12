"""ETL simples: CSV (Extract) -> mensagens personalizadas (Transform) -> CSV (Load).

Se a variável OPENROUTER_API_KEY existir, a mensagem é gerada por IA.
Caso contrário, usa um template local (o fluxo ETL funciona do mesmo jeito).
"""
import os
import pandas as pd
import requests

ENTRADA = "usuarios.csv"
SAIDA = "usuarios_com_mensagens.csv"


# ---------- EXTRACT ----------
def extract(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)


# ---------- TRANSFORM ----------
def mensagem_template(u: pd.Series) -> str:
    return (
        f"{u['nome']}, investir hoje constrói o seu amanhã. "
        f"Seu cartão da conta {u['conta']} tem limite de R$ {u['cartao']:.2f}: use com consciência!"
    )


def mensagem_ia(u: pd.Series, api_key: str) -> str:
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Você é um especialista em marketing bancário."},
                {"role": "user", "content": f"Crie uma mensagem de até 100 caracteres para {u['nome']} sobre a importância dos investimentos."},
            ],
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip('"')


def transform(df: pd.DataFrame) -> pd.DataFrame:
    api_key = os.getenv("OPENROUTER_API_KEY")
    gerar = (lambda u: mensagem_ia(u, api_key)) if api_key else mensagem_template
    df = df.copy()
    df["mensagem"] = df.apply(gerar, axis=1)
    return df


# ---------- LOAD ----------
def load(df: pd.DataFrame, caminho: str) -> None:
    df.to_csv(caminho, index=False, encoding="utf-8")


if __name__ == "__main__":
    dados = extract(ENTRADA)
    dados = transform(dados)
    load(dados, SAIDA)
    print(dados[["nome", "mensagem"]].to_string(index=False))
