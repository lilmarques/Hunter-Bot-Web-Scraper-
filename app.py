import requests
from bs4 import BeautifulSoup
import time

# Exemplo simples rastreando o site 'RemoteOK' (API pública simulada via JSON)
def buscar_vagas_remote():
    url = "https://remoteok.com/api"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    print("🔍 Iniciando varredura por vagas de Python...")
    try:
        response = requests.get(url, headers=headers)
        vagas = response.json()
        
        encontradas = []
        for vaga in vagas:
            # Pula metadados que não são vagas
            if 'title' not in vaga: continue
            
            titulo = vaga.get('title', '').lower()
            tags = vaga.get('tags', [])
            
            # Filtro: Tem Python no título ou nas tags?
            if 'python' in titulo or 'python' in tags:
                encontradas.append({
                    'titulo': vaga['title'],
                    'empresa': vaga.get('company', 'N/A'),
                    'link': vaga.get('url', '#'),
                    'data': vaga.get('date', 'N/A')
                })
        
        return encontradas
    except Exception as e:
        print(f"Erro na busca: {e}")
        return []

def main():
    vagas = buscar_vagas_remote()
    print(f"\n🎯 Encontrei {len(vagas)} vagas para Python!\n")
    
    for i, v in enumerate(vagas[:5]): # Mostra as top 5
        print(f"[{i+1}] {v['titulo']} na {v['empresa']}")
        print(f"    🔗 Link: {v['link']}\n")

if __name__ == "__main__":
    main()