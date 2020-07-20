import random
print('='*40)
print('Bem Vindo ao Jokenpo Gigante!')
print('='*40)
print('As opcoes sao as seguintes:')
print('Pedra')
print('Fogo')
print('Tesoura')
print('Cobra')
print('Humano')
print('Arvore')
print('Lobo')
print('Esponja')
print('Papel')
print('Ar')
print('Agua')
print('Dragao')
print('Demonio')
print('Trovao')
print('Arma de Fogo')
print('O computador ira escolher um aleatorio')
choose = str(input('Qual voce escolhe? '))
pedra = 'pedra'
fogo = 'fogo'
tesoura = 'tesoura'
cobra = 'cobra'
humano = 'humano'
arvore = 'arvore'
lobo = 'lobo'
esponja = 'esponja'
papel = 'papel'
ar = 'ar'
agua = 'agua'
dragao = 'dragao'
demonio = 'demonio'
trovao = 'trovao'
adf = 'arma de fogo'
list = [pedra, fogo, tesoura, cobra, humano, arvore, lobo, esponja, papel, ar, agua, dragao, demonio, trovao, adf]
listap = [tesoura, cobra, humano, lobo, trovao]
listaf = [humano, esponja, papel, lobo, cobra, adf, arvore]
listat = [humano, esponja, papel, lobo, cobra, arvore]
listac = [humano, demonio, lobo]
listah = [agua, arvore, papel, ar]
listaa = [demonio, dragao, agua, trovao, cobra, lobo, pedra, adf]
listal = [agua, cobra, humano, papel]
listapa = [ar, adf, trovao, demonio, dragao, pedra, arvore]
listaar = [arvore, humano, fogo, demonio, dragao]
listaag = [papel, dragao, demonio, lobo, humano, trovao, cobra, pedra, adf, fogo]
listad = [humano, demonio, arvore, lobo, cobra]
listade = [humano, lobo, cobra]
listatr = [fogo, tesoura, humano, lobo, papel, cobra]
listaadf = [demonio, dragao, papel, cobra, humano, lobo]
cpu = random.choice(list)
if choose == pedra and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu == tesoura:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu == trovao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu == pedra:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == pedra and cpu != listap:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == esponja:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == adf:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu == fogo:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == fogo and cpu != listaf:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == esponja:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu == tesoura:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == tesoura and cpu != listat:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == cobra and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == cobra and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == cobra and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == cobra and cpu == cobra:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == cobra and cpu != listac:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu == agua:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu == ar:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu == humano:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == humano and cpu != listah:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == dragao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == agua:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == trovao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == pedra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == adf:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu == arvore:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == arvore and cpu != listaa:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu == agua:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu == lobo:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == lobo and cpu != listal:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == esponja:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == ar:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == adf:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == trovao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == dragao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == pedra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu == papel:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == papel and cpu != listapa:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == fogo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == dragao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu == ar:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == ar and cpu != listaar:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == trovao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == adf:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == pedra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == fogo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == dragao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu == agua:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == agua and cpu != listaag:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == arvore:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu == dragao:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == dragao and cpu != listad:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == demonio and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == demonio and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == demonio and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == demonio and cpu == demonio:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == demonio and cpu != listade:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == fogo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == tesoura:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu == trovao:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == trovao and cpu != listatr:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == humano:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == lobo:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == cobra:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == papel:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == dragao:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == demonio:
    print('Voce venceu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu == adf:
    print('Empatamos! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))
elif choose == adf and cpu != listaadf:
    print('Voce perdeu! O computador escolheu {} e voce escolheu {}'.format(cpu, choose))