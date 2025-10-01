# chatti2.py - Ollama-pohjainen chatbotti
"""
Chatbotti, joka käyttää paikallista Ollama-palvelinta OpenAI:n API:n sijaan.
Tämä esimerkki näyttää miten voit käyttää omaa AI-mallia ilman pilvipalvelua.

Vaatimukset:
- Ollama asennettu ja käynnissä (http://localhost:11434)
- Malli ladattu Ollamaan (esim. ollama pull llama3)
- requests-kirjasto (pip install requests)

Käyttö:
    python chatti2.py
"""

import requests

def main():
    """
    Pääfunktio, joka käynnistää chatbotin ja käsittelee käyttäjän syötteet.
    
    Chatbotti käyttää Ollama-palvelinta (localhost:11434) ja ylläpitää
    keskusteluhistoriaa koko session ajan.
    """
    # Ollama API:n chat-endpoint
    url = "http://localhost:11434/api/chat"
    
    # Käytettävä AI-malli (vaihda haluamaasi malliin)
    # Yleisiä vaihtoehtoja: "llama3", "mistral", "codellama"
    model = "hf.co/mradermacher/Llama-Poro-2-8B-Instruct-GGUF:Q4_K_M"  # Suomenkielinen malli
    
    # Keskusteluhistoria: aloitetaan system-promptilla
    messages = [{"role": "system", "content": "Puhu suomeksi ja ole avulias."}]
    
    print("🤖 Ollama Chatbotti käynnistetty!")
    print("💡 Kirjoita viestisi ja paina Enter. Lopeta '/exit' tai '/quit' komennolla.\n")

    # Pääsilmukka: käsittelee käyttäjän syötteet kunnes lopetus
    while True:
        try:
            # Lue käyttäjän syöte
            user = input("Sinä: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Keskustelu keskeytetty. Heippa!")
            break
        
        # Tarkista lopetuskomennot
        if user.lower() in {"/exit", "/quit"}:
            print("👋 Heippa!")
            break
        
        # Ohita tyhjät syötteet
        if not user:
            continue
        
        # Lisää käyttäjän viesti keskusteluhistoriaan
        messages.append({"role": "user", "content": user})

        try:
            # Lähetä pyyntö Ollama-palvelimelle
            # stream=False varmistaa että saamme koko vastauksen kerralla
            resp = requests.post(
                url, 
                json={
                    "model": model, 
                    "messages": messages, 
                    "stream": False
                },
                timeout=30  # 30 sekunnin aikakatkaisu
            )
            
            # Tarkista HTTP-vastauskoodi
            if resp.status_code != 200:
                print(f"❌ HTTP-virhe {resp.status_code}: {resp.text}")
                continue
            
            # Parsii JSON-vastaus
            data = resp.json()
            reply = data["message"]["content"]
            print(f"🤖 Botti: {reply}\n")
            
            # Lisää botin vastaus keskusteluhistoriaan
            messages.append({"role": "assistant", "content": reply})
            
        except requests.exceptions.JSONDecodeError as e:
            print(f"❌ JSON-parsintavirhe: {e}")
            print(f"📄 Palvelimen vastaus: {resp.text[:500]}...")
            continue
        except requests.exceptions.RequestException as e:
            print(f"❌ Verkkovirhe: {e}")
            print("💡 Varmista että Ollama on käynnissä: http://localhost:11434")
            continue
        except KeyError as e:
            print(f"❌ Odottamaton vastausrakenne: puuttuva avain {e}")
            print(f"📄 Vastaus: {data}")
            continue

if __name__ == "__main__":
    """
    Käynnistyspiste: ajetaan main-funktio vain jos tiedosto suoritetaan suoraan.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Ohjelma keskeytetty. Heippa!")
    except Exception as e:
        print(f"❌ Odottamaton virhe: {e}")
        print("💡 Käynnistä ohjelma uudelleen tai tarkista Ollama-asetukset.")