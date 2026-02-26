import random
import time
import os

# --- CONFIGURAÇÕES DO JOGO ---
SIMBOLOS = {
    '💎': {'nome': 'Diamante', 'valor': 50, 'chance': 5},
    '⭐': {'nome': 'Estrela',  'valor': 20, 'chance': 10},
    '🔔': {'nome': 'Sino',     'valor': 10, 'chance': 20},
    '🍋': {'nome': 'Limão',    'valor': 5,  'chance': 30},
    '🍒': {'nome': 'Cereja',   'valor': 2,  'chance': 35}
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabela_precos():
    print("\n--- TABELA DE PAGAMENTOS (3 IGUAIS) ---")
    for sim, dados in SIMBOLOS.items():
        print(f"{sim} : {dados['valor']}x a aposta")
    print("2 IGUAIS: Ganha 1.5x a aposta")
    print("-" * 40)

def girar_slots():
    opcoes = list(SIMBOLOS.keys())
    pesos = [SIMBOLOS[s]['chance'] for s in opcoes]
    return random.choices(opcoes, weights=pesos, k=3)

def calcular_premio(resultado, aposta):
    # 3 iguais
    if resultado[0] == resultado[1] == resultado[2]:
        multiplicador = SIMBOLOS[resultado[0]]['valor']
        return aposta * multiplicador, "JACKPOT!"
    # 2 iguais
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        return int(aposta * 1.5), "SORTE PEQUENA!"
    return 0, ""

def main():
    saldo = 500
    historico_ganhos = 0
    
    limpar_tela()
    print("🎰 BEM-VINDO AO SUPREMO CASSINO PYTHON 🎰")
    exibir_tabela_precos()
    
    while saldo > 0:
        print(f"\n💰 SALDO ATUAL: R${saldo:.2f} | 🏆 TOTAL GANHO: R${historico_ganhos:.2f}")
        entrada = input("Quanto deseja apostar? (ou 'tabela' para ver prêmios / 'sair'): ").lower()

        if entrada == 'sair':
            break
        if entrada == 'tabela':
            exibir_tabela_precos()
            continue
            
        try:
            aposta = int(entrada)
        except ValueError:
            print("❌ Digite um número válido.")
            continue

        if aposta > saldo:
            print("❌ Saldo insuficiente!")
            continue
        if aposta <= 0:
            print("❌ Aposta deve ser maior que zero.")
            continue

        saldo -= aposta
        print("\n🎰 GIRANDO OS ROLOS...")
        
        # Efeito de animação simples
        for _ in range(3):
            time.sleep(0.4)
            print("  [ ? ]", end="\r")
            time.sleep(0.4)
            
        resultado = girar_slots()
        print(f"  [ {resultado[0]} ] [ {resultado[1]} ] [ {resultado[2]} ]")
        
        ganho, mensagem = calcular_premio(resultado, aposta)
        
        if ganho > 0:
            saldo += ganho
            historico_ganhos += ganho
            print(f"✅ {mensagem} Você recebeu R${ganho:.2f}!")
        else:
            print("❌ Não foi dessa vez. Tente novamente!")

        if saldo <= 0:
            print("\n💸 Você faliu! O Cassino sempre vence.")
            break

    print(f"\nObrigado por jogar! Você saiu com R${saldo:.2f}")

if __name__ == "__main__":
    main()
