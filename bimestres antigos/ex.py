acesso=input("qual seu cargo? [gerente,analista e estagiario?]: ").lower()
dia_da_semana=input("qual o dia da semana? [segunda,terça,quarta,quinta ou sexta?]: ")

if acesso == "gerente" or acesso == "analista":
    print("acesso concedido")
elif acesso == "estagiario":
    if dia_da_semana in ["segunda", "quarta","sexta"]:
      print(f"acesso liberado para o dia {dia_da_semana}")
    else:
       print("acesso nao autorizado")
else:
 print("nao encontrado")