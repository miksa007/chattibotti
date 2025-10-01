# ChattiBotti

Yksinkertainen suomenkielinen chatbotti, joka käyttää OpenAI:n API:a keskustelujen käsittelyyn.

## Ominaisuudet

### Kaksi erilaista toteutusta:

**Esimerkki 1 (chatti1.py) - OpenAI Cloud API:**
- Suomenkielinen käyttöliittymä
- Keskusteluhistorian ylläpito
- OpenAI:n tehokkaat mallit (GPT-4o, GPT-3.5-turbo)
- Vaatii internetyhteyden ja API-avaimen

**Esimerkki 2 (chatti2.py) - Paikallinen Ollama:**
- Toimii täysin offline (ei internetyhteyttä tarvita)
- Tietosuojallinen (kaikki data pysyy omalla koneella)
- Suomenkieliset mallit (Llama-Poro)
- Ilmainen käyttö (ei API-kuluja)
- Parannettu virheenkäsittely ja käyttöliittymä

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

### Esimerkki 1: OpenAI-pohjainen chatbotti (chatti1.py)

Käynnistä OpenAI-chatbotti:
```bash
python chatti1.py
```

### Esimerkki 2: Ollama-pohjainen chatbotti (chatti2.py)

Käynnistä paikallinen chatbotti:
```bash
python chatti2.py
```

Lopeta keskustelu molemmissa kirjoittamalla `/exit` tai `/quit`.

## Konfigurointi

### OpenAI-chatbotti (chatti1.py)

Voit muuttaa käytettävää AI-mallia muokkaamalla `MODEL`-muuttujaa koodissa. Tuetut mallit löytyvät [OpenAI:n dokumentaatiosta](https://platform.openai.com/docs/models).

### Ollama-chatbotti (chatti2.py)

**Vaatimukset:**
1. Asenna Ollama: [https://ollama.ai](https://ollama.ai)
2. Asenna requests-kirjasto:
   ```bash
   pip install requests
   ```

**Konfigurointi:**

1. Käynnistä Ollama-palvelin:
   ```bash
   ollama serve
   ```

2. Lataa haluamasi malli (esimerkiksi):
   ```bash
   # Suomenkielinen malli
   ollama pull hf.co/mradermacher/Llama-Poro-2-8B-Instruct-GGUF:Q4_K_M
   
   # Tai yleinen englanninkielinen malli
   ollama pull llama3
   ollama pull mistral
   ```

3. Muokkaa `chatti2.py`:ssä `model`-muuttujaa vastaamaan lataamaasi mallia:
   ```python
   model = "llama3"  # tai muu ladattu malli
   ```

**Mallisuositukset:**
- **Suomenkieliseen käyttöön:** `hf.co/mradermacher/Llama-Poro-2-8B-Instruct-GGUF:Q4_K_M`
- **Englanninkieliseen käyttöön:** `llama3`, `mistral`, `phi3`
- **Koodaukseen:** `codellama`, `codegemma`

**Vianetsintä:**
- Varmista että Ollama on käynnissä: avaa [http://localhost:11434](http://localhost:11434)
- Tarkista ladatut mallit: `ollama list`
- Jos malli ei vastaa, kokeile eri mallia tai käynnistä Ollama uudelleen

## Vertailu: OpenAI vs Ollama

| Ominaisuus | OpenAI (chatti1.py) | Ollama (chatti2.py) |
|------------|---------------------|---------------------|
| **Kustannukset** | Maksullinen API | Ilmainen |
| **Internetyhteys** | Vaaditaan | Ei vaadita |
| **Tietosuoja** | Data lähetetään OpenAI:lle | Data pysyy paikallisena |
| **Mallin laatu** | Erittäin korkea | Hyvä, riippuu mallista |
| **Asennus** | Helppo (vain API-avain) | Vaatii Ollama-asennuksen |
| **Suomenkieli** | Erinomainen | Hyvä (Llama-Poro mallilla) |
| **Nopeus** | Nopea | Riippuu koneesta |

## Lisätietoja

**OpenAI:**
- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
- [OpenAI Python SDK dokumentaatio](https://github.com/openai/openai-python)

**Ollama:**
- [Ollama virallinen sivusto](https://ollama.ai)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Llama-Poro suomenkielinen malli](https://huggingface.co/LumiOpen/Llama-Poro-Chat-7B-v0.1)

## Tekijä & Tekniikka

**Toteutus:**
- OpenAI Chat Completions API (pilvipalvelu)
- Ollama + Poro-2 paikallinen AI-järjestelmä
- Python 3.x + requests/openai kirjastot

**Kehittäjä:**
- **GitHub:** [@miksa007](https://github.com/miksa007)
- **Sähköposti:** mika.saari@tuni.fi

---

*Projekti on toteutettu opetuskäyttöön ja demonstroi kahta erilaista lähestymistapaa AI-chatbottien rakentamiseen.*
