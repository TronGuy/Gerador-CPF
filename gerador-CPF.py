'''
  -------------------- Gerador de CPF ------------------

  -> Este script foi feito para fins educativos. Não assumo a responsabilidade por qualquer
     mal uso do mesmo. Use com sabedoria.

   __author__ = LouizF
   __License__ = GPLv3
   __GitHub__ = github.com/TronGuy

'''
from random import randint
print(''' 
  ==================================================================================
  
                                        GERADOR DE CPF

  ==================================================================================
  
  ''')

print(' -> Este script foi feito para fins educacionais. Não me responsabilizo pelo mal uso do mesmo.\n')


while True:
  print('digite S para sim e N para não.\n')
  print('Deseja gerar o CPF? ')
  resposta = input('R: ').strip()
  if resposta == 's' or resposta == 'S':
        #Declaração de variáveis
        valores = str(randint(100000000,999999999)) #cpf aleatório
        valores = list(valores) #conversão para iterável
        tot = 0
        tot2 = 0
        #digito 1
        for n,values in enumerate(range(10,1,-1)):
          tot += int(valores[n]) * values
        tot = abs(11 - (tot % 11))
        tot = 0 if tot > 9 else tot
        valores.append(tot)

        #digito 2
        for n,values in enumerate(range(11,1,-1)):
          tot2 += int(valores[n]) * values
        tot2 = abs(11 - (tot2 % 11))
        tot2 = 0 if tot2 > 9 else tot2
        valores.append(tot2)

        #desempacotamento
        cpf_gerado = ''
        for i in valores:
          cpf_gerado += str(i)

        #Hadouken 
        print(f'CPF GERADO: {cpf_gerado[0:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:12]}') 
  else:
    break 
