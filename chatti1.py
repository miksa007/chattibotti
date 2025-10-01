#!/usr/bin/env python3
"""
ChattiBotti - OpenAI-pohjainen chatbotti

Yksinkertainen suomenkielinen chatbotti, joka käyttää OpenAI:n Chat Completions API:a.
Chatbotti ylläpitää keskusteluhistoriaa ja mahdollistaa sujuvan keskustelun AI:n kanssa.

Vaatimukset:
    - OpenAI API-avain (OPENAI_API_KEY ympäristömuuttujana)
    - openai Python-kirjasto (pip install openai)

Käyttö:
    python chatti1.py

Tekijä: Mika Saari (mika.saari@tuni.fi)
GitHub: @miksa007
Luotu: Lokakuu 2025
Versio: 1.0

Lisenssi: MIT
"""

import os
from openai import OpenAI

# Lue API-avain ympäristömuuttujasta: OPENAI_API_KEY
# esim. macOS/Linux: export OPENAI_API_KEY="sk-..."; Windows (PowerShell): $env:OPENAI_API_KEY="sk-..."
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-5"  # voit vaihtaa saatavilla olevaan malliin

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

        # Kutsu OpenAI:n Chat Completions -APIa
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=1
        )
        reply = resp.choices[0].message.content
        print(f"Botti: {reply}\n")

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
