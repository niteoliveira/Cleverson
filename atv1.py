import math
from scipy.stats import norm

def calcular_intervalo_confianca(desvio_padrao_populacional, tamanho_amostra, nivel_confianca, media_amostral=None):
    alfa = 1 - nivel_confianca
    z_score = norm.ppf(1 - alfa / 2)
    erro_padrao = desvio_padrao_populacional / math.sqrt(tamanho_amostra)
    margem_de_erro = z_score * erro_padrao

    if media_amostral is not None:
        limite_inferior = media_amostral - margem_de_erro
        limite_superior = media_amostral + margem_de_erro
        return margem_de_erro, limite_inferior, limite_superior
    else:
        return margem_de_erro

desvio_padrao_sigma = 0.10
tamanho_amostra_n = 50
nivel_confianca_perc = 0.95

margem_erro_calculada = calcular_intervalo_confianca(desvio_padrao_sigma, tamanho_amostra_n, nivel_confianca_perc)

print(f"--- Cálculo da Margem de Erro ---")
print(f"Desvio Padrão Populacional (σ): {desvio_padrao_sigma} m")
print(f"Tamanho da Amostra (n): {tamanho_amostra_n}")
print(f"Nível de Confiança: {nivel_confianca_perc*100}%")
print(f"Valor Crítico (z-score): {norm.ppf(1 - (1 - nivel_confianca_perc) / 2):.2f}")
print(f"Margem de Erro (ME): {margem_erro_calculada:.4f} m")

print("\n--- Exemplo de Cálculo do Intervalo de Confiança ---")
media_amostral_exemplo = 1.75

margem_erro, lim_inferior, lim_superior = calcular_intervalo_confianca(
    desvio_padrao_sigma,
    tamanho_amostra_n,
    nivel_confianca_perc,
    media_amostral_exemplo
)

print(f"Se a média amostral (x̄) fosse: {media_amostral_exemplo} m")
print(f"O Intervalo de Confiança de {nivel_confianca_perc*100}% seria: ({lim_inferior:.4f} m, {lim_superior:.4f} m)")
print(f"Isso significa que estamos {nivel_confianca_perc*100}% confiantes de que a verdadeira média populacional das alturas está entre {lim_inferior:.4f} m e {lim_superior:.4f} m.")
