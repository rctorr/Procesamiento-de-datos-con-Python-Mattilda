votos = ['AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'AI', 'AI'
         , 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC',
         'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'AI', 'AI', 'CC', 'AI', 'CC', 'CC',
         'CC', 'AI', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'AI',
         'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'CC',
         'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC',
         'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC',
         'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC',
         'AI', 'AI', 'AI', 'AI', 'CC', 'AI', 'CC', 'AI', 'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC',
         'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC', 'AI', 'AI',
         'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC',
         'AI', 'AI', 'CC', 'CC', 'CC', 'AI', 'AI', 'AI', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC',
         'CC', 'AI', 'AI', 'CC', 'CC', 'AI', 'AI', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI',
         'AI', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC',
         'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC',
         'AI', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'AI', 'CC',
         'AI', 'AI', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'AI',
         'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC',
         'AI', 'AI', 'AI', 'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC', 'CC', 'CC',
         'AI', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'AI',
         'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'AI', 'CC', 'CC',
         'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI', 'CC', 'CC', 'CC', 'CC', 'CC', 'AI', 'CC', 'CC', 'AI', 'CC',
         'AI', 'CC', 'CC', 'CC', 'AI', 'CC', 'AI']

# Obteniendo lista de voto AI
def votos_ai_filtrados(voto):
    return voto == "AI"

votos_ai = list( filter(votos_ai_filtrados, votos) )
print(votos_ai)
print(len(votos_ai))

# Obteniendo lista de votos CC
votos_cc = list( filter(lambda voto: not votos_ai_filtrados(voto), votos) )
print(votos_cc)
print(len(votos_cc))

# Obteniendo lista de votos CC usando sólo lambda
votos_cc_2 = list( filter(lambda voto: voto == "CC", votos) )
print(votos_cc_2)
print(len(votos_cc_2))

# Obteniendo lista de votos CC usando "listas de compresión"
votos_cc_3 = [voto for voto in votos if voto == "CC"]
print(votos_cc_3)
print(len(votos_cc_3))

