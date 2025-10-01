# ChattiBotti

Yksinkertainen suomenkielinen chatbotti, joka käyttää OpenAI:n API:a keskustelujen käsittelyyn.

## Ominaisuudet

- Suomenkielinen käyttöliittymä
- Keskusteluhistorian ylläpito
- Konfiguroitava AI-malli
- Yksinkertainen komentorivi-interface

## Asennus

1. Asenna OpenAI Python SDK:
   ```bash
   pip install --upgrade openai
   ```

2. Hanki OpenAI API-avain [OpenAI Platform](https://platform.openai.com/):sta

3. Aseta API-avain ympäristömuuttujaan:

   **macOS / Linux:**
   ```bash
   export OPENAI_API_KEY="sk-...YOUR_KEY..."
   ```

   **Windows PowerShell:**
   ```powershell
   $env:OPENAI_API_KEY="sk-...YOUR_KEY..."
   ```

## Käyttö

Käynnistä chatbotti:
```bash
python chatti.py
```

Lopeta keskustelu kirjoittamalla `/exit` tai `/quit`.

## Konfigurointi

Voit muuttaa käytettävää AI-mallia muokkaamalla `MODEL`-muuttujaa koodissa. Tuetut mallit löytyvät [OpenAI:n dokumentaatiosta](https://platform.openai.com/docs/models).

## Lisätietoja

- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
- [OpenAI Python SDK dokumentaatio](https://github.com/openai/openai-python)

## Tekijä

Toteutettu OpenAI:n Chat Completions API:n avulla.
