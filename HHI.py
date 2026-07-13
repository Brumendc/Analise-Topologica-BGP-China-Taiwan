# Dados do Gráfico 4 do relatório
dados_paises = {
    "Estados Unidos": 51525,
    "Hong Kong": 37332,
    "Reino Unido": 18610,
    "Japão": 14406,
    "Singapura": 3271,
    "Malásia": 1579,
    "SE (Suécia)": 667,
    "Coreia do Sul": 578,
    "Austrália": 542,
    "China": 11
}

# Desconhecidos representam 10.748 rotas.
# O total da amostra é a soma de tudo
total_rotas = sum(dados_paises.values()) + 10748 

hhi_total = 0

print("Cálculo do HHI por País:\n ")
for pais, rotas in dados_paises.items():
    # Calcula a porcentagem de cada país
    share = (rotas / total_rotas) * 100
    
    
    hhi_parcial = share ** 2
    

    hhi_total += hhi_parcial
    
    print(f"{pais}: {share:.2f}% -> Contribuição no HHI: {hhi_parcial:.2f}")
print("\n")
print(f"HHI Total: {hhi_total:.2f}")
