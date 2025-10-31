# ChattiBotti

Yksinkertainen suomenkielinen chatbotti, joka käyttää OpenAI:n API:a keskustelujen käsittelyyn.

## Ominaisuudet

### Kolme erilaista toteutusta:

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

**Esimerkki 3 (AzureChatti3.py) - Azure OpenAI:**
- Yritysluokan tietoturva ja compliance
- Azure-integraatio (SSO, RBAC, logging)
- Datan sijainti EU:ssa (GDPR-yhteensopiva)
- Vakaa SLA ja enterprise-tuki
- Kustannushallinta ja käyttörajoitukset

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

### Esimerkki 2: PORO-2 -pohjainen chatbotti (chatti2.py)

Käynnistä paikallinen chatbotti:
```bash
python chatti2.py
```

### Esimerkki 3: Azure OpenAI-pohjainen chatbotti (AzureChatti3.py)

Käynnistä Azure-chatbotti:
```bash
python AzureChatti3.py
```

Lopeta keskustelu kaikissa kirjoittamalla `/exit` tai `/quit`.

## Konfigurointi

### OpenAI-chatbotti (chatti1.py)

Voit muuttaa käytettävää AI-mallia muokkaamalla `MODEL`-muuttujaa koodissa. Tuetut mallit löytyvät [OpenAI:n dokumentaatiosta](https://platform.openai.com/docs/models).

### PORO-2 + Ollama-chatbotti (chatti2.py)

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

### Azure OpenAI-chatbotti (AzureChatti3.py)

**Vaatimukset:**
1. Azure-tili ja Azure OpenAI -palvelu
2. Deployattu AI-malli Azure OpenAI:ssa
3. OpenAI Python SDK: `pip install openai`

**Konfigurointi:**

1. **Luo Azure OpenAI -resurssi:**
   - Kirjaudu [Azure Portal](https://portal.azure.com):iin
   - Luo "Azure OpenAI" -resurssi
   - Kopioi API-avain ja endpoint-osoite

2. **Deployaa malli:**
   - Siirry Azure OpenAI Studio:on
   - Valitse "Deployments" → "Create new deployment"
   - Valitse malli (esim. gpt-4o, gpt-35-turbo)
   - Anna deployment-nimi (esim. "gpt-4o")

3. **Päivitä koodi:**
   ```python
   client = AzureOpenAI(
       api_key="YOUR_API_KEY",
       api_version="2024-08-01-preview",
       azure_endpoint="https://your-resource.openai.azure.com/"
   )
   MODEL = "your-deployment-name"  # Deployment-nimi, ei mallin nimi!
   ```

**Yleisiä deployment-nimiä:**
- `gpt-4o` tai `gpt-4o-deployment`
- `gpt-35-turbo` tai `gpt35`
- `gpt-4` tai `gpt4`

**Vianetsintä:**
- **404 Error:** Tarkista deployment-nimi Azure Portal:ista
- **401 Error:** Tarkista API-avain ja oikeudet
- **Endpoint:** Varmista että endpoint päättyy `.openai.azure.com/`
- **API-versio:** Kokeile `2024-02-01` tai `2023-12-01-preview`

## Vertailu: OpenAI vs Ollama vs Azure OpenAI

| Ominaisuus | OpenAI (chatti1.py) | Ollama (chatti2.py) | Azure OpenAI (AzureChatti3.py) |
|------------|---------------------|---------------------|-------------------------------|
| **Kustannukset** | Maksullinen API | Ilmainen | Maksullinen, yrityshinnoittelu |
| **Internetyhteys** | Vaaditaan | Ei vaadita | Vaaditaan |
| **Tietosuoja** | Data → OpenAI | Paikallinen | Data → Azure (EU-alue) |
| **Mallin laatu** | Erittäin korkea | Hyvä | Erittäin korkea |
| **Asennus** | Helppo | Vaatii Ollaman | Keskitaso (Azure-setup) |
| **Suomenkieli** | Erinomainen | Hyvä (Poro-malli) | Erinomainen |
| **Nopeus** | Nopea | Riippuu koneesta | Nopea |
| **Yritysominaisuudet** | Perus | Ei | Edistynyt (SSO, RBAC, SLA) |
| **GDPR/Compliance** | Rajoitettu | Täysi | Korkea (EU-data) |
| **Skaalautuvuus** | Hyvä | Paikallinen rajoitus | Erittäin hyvä |

## Lisätietoja

**OpenAI:**
- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
- [OpenAI Python SDK dokumentaatio](https://github.com/openai/openai-python)

**Ollama:**
- [Ollama virallinen sivusto](https://ollama.ai)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Llama-Poro suomenkielinen malli](https://huggingface.co/LumiOpen/Llama-Poro-Chat-7B-v0.1)

**Azure OpenAI:**
- [Azure OpenAI Service dokumentaatio](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Azure OpenAI Studio](https://oai.azure.com/)
- [Azure OpenAI Python SDK](https://github.com/openai/openai-python#microsoft-azure-openai)
- [Azure OpenAI hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)

## Tekijä & Tekniikka

**Toteutus:**
- OpenAI Chat Completions API (pilvipalvelu)
- PORO-2 + Ollama paikallinen AI-järjestelmä  
- Azure OpenAI Service (yritysluokan pilvipalvelu)
- Python 3.x + requests/openai kirjastot

**Kehittäjä:**
- **GitHub:** [@miksa007](https://github.com/miksa007)
- **Sähköposti:** mika.saari@tuni.fi

---

*Projekti on toteutettu opetuskäyttöön ja demonstroi kolmea erilaista lähestymistapaa AI-chatbottien rakentamiseen: kuluttaja-API (OpenAI), paikallinen ratkaisu (Ollama) ja yritysluokan pilvipalvelu (Azure OpenAI).*
