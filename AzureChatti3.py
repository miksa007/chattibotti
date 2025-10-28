#!/usr/bin/env python3
"""
ChattiBotti - Azure OpenAI-pohjainen chatbotti

Yksinkertainen suomenkielinen chatbotti, joka käyttää Azure OpenAI:n Chat Completions API:a.
Chatbotti ylläpitää keskusteluhistoriaa ja mahdollistaa sujuvan keskustelun AI:n kanssa.

Vaatimukset:
    - Azure OpenAI -palvelu ja API-avain
    - Deployattu malli (esim. gpt-4o, gpt-35-turbo)
    - openai Python-kirjasto (pip install openai)

Konfigurointi:
    1. Päivitä api_key, azure_endpoint ja api_version
    2. Vaihda MODEL deployment-nimeen joka löytyy Azure-palvelustasi

Käyttö:
    python AzureChatti3.py

Tekijä: Mika Saari (mika.saari@tuni.fi)
GitHub: @miksa007
Luotu: Lokakuu 2025
Versio: 1.0

Lisenssi: MIT
"""

import os
from openai import AzureOpenAI

# Azure OpenAI -konfiguraatio
client = AzureOpenAI(
    api_key="*******",  # Azure OpenAI API-avain
    api_version="2024-08-01-preview",  # Tarkista tuetut versiot Azure-palvelustasi
    azure_endpoint="https://rg-itcai-openai-seints-001.openai.azure.com/"  # Azure endpoint
)

# Lue API-avain ympäristömuuttujasta: AZURE_API_KEY
# esim. macOS/Linux: export AZURE_API_KEY="sk-..."; Windows (PowerShell): $env:AZURE_API_KEY="sk-..."
#client = OpenAI(api_key=os.getenv("AZURE_API_KEY"))

#MODEL = "gpt-4o"  # vaihda Azure deployment-nimeen (esim. "gpt-4o", "gpt-35-turbo")
MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = (
    "You are a helpful, concise Finnish-speaking assistant. "
    "Answer in Finnish unless the user asks otherwise."
)

def main():
    print("Pieni ChatGPT-tyylinen botti. Kirjoita /exit lopettaaksesi.\n")
    # Ylläpidetään keskusteluhistoriaa mallia varten
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user = input("Sinä: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHeippa!")
            break

        if user.lower() in {"/exit", "/quit"}:
            print("Heippa!")
            break
        if not user:
            continue

        messages.append({"role": "user", "content": user})

        try:
            # Kutsu Azure OpenAI:n Chat Completions -APIa
            resp = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=1
            )
            reply = resp.choices[0].message.content
            print(f"Botti: {reply}\n")
        except Exception as e:
            print(f"❌ Virhe: {e}")
            print("💡 Tarkista että deployment-nimi on oikea Azure-palvelussa.")
            print("   Yleisiä deployment-nimiä: gpt-4o, gpt-35-turbo, gpt-4")
            continue

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
