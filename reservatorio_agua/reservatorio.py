# Importar a biblioteca colorama
from colorama import init, Fore, Style
 # Inicializar a colorama
init(autoreset=True)
 # 📌 Lista com os níveis, mensagens e cores
niveis_reservatorio = [
     {
         "nivel": 1,
         "situacao": "Nível muito baixo — CRÍTICO!",
         "cor": Fore.RED
     },
     {
         "nivel": 2,
         "situacao": "Nível baixo — Atenção.",
         "cor": Fore.YELLOW
     },
     {
         "nivel": 3,
         "situacao": "Nível médio — Situação normal.",
         "cor": Fore.GREEN
     },
     {
         "nivel": 4,
         "situacao": "Nível alto — Fique atento.",
         "cor": Fore.CYAN
     },
     {
         "nivel": 5,
         "situacao": "Nível muito alto — Verificar transbordamento!",
         "cor": Fore.BLUE
     }
 ]
 # 📌 Função para definir e exibir a mensagem com a cor correta
def exibir_alerta(nivel):
     """Exibe a mensagem de alerta com a cor correspondente ao nível informado"""
     for item in niveis_reservatorio:
         if item["nivel"] == nivel:
             mensagem = f"[Nível {item['nivel']}] {item['situacao']}"
             print(f"{item['cor']}{mensagem}{Style.RESET_ALL}")
             return
     # Se o nível não for encontrado
     print(Fore.RED + "⚠️ Nível inválido! Informe um valor entre 1 e 5." + Style.RESET_ALL)
 # 📌 Programa principal — Simulação dos níveis
print("=" * 55)
print("        💧 SISTEMA DE MONITORAMENTO — RESERVATÓRIO")
print("=" * 55)
print()
 # Simulando diferentes níveis (pode alterar o número aqui!)
nivel_atual = 1  # ← TROQUE AQUI: 1, 2, 3, 4 ou 5!
print(f"📊 Situação atual do reservatório:")
exibir_alerta(nivel_atual)
print()
print("=" * 55)
print("✅ Leitura concluída.")
print("=" * 55)