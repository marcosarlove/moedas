#! /usr/bin/python3

import requests
import json
import os
import argparse
import re

API = "https://cdn.moeda.info/api/latest.json"
PATH = "latest.json"
CAMBIO = LAST_UPDATE = ""


def getOnlineData():
    global API

    data = requests.get(API)
    data.raise_for_status()
    fp = open(PATH, "w")
    fp.write(data.text)
    fp.close()


def getOfflineData():
    global PATH

    with open(PATH) as fp:
        return fp.read()


def getDataCommandMode():

    try:
        getOnlineData()
    except:
        print("\033[31mErro ao Acessar a Taxa de Câmbio Atual\033[37m")
        print(
            "\033[33mUsando a Taxa de Cambio da Ultima Atualização armazenada\033[37m"
        )

    try:
        data = getOfflineData()
    except FileNotFoundError:
        print("\033[31mA Taxa de Câmbio Não Pode Ser Acessada.")
        print("Porfavor Conecte-se a Internet e Tente Novamente!\033[37m")
        os.abort()
    else: saveData(data)
                   
def saveData(data):
    global CAMBIO, LAST_UPDATE
    string = json.loads(data)
    CAMBIO, LAST_UPDATE = string["rates"], string["lastupdate"]


def getDataScriptMode():
    try:
        getOnlineData()
    except: pass
    saveData(getOfflineData())


def setParams():
    parse = argparse.ArgumentParser(description="Conversor de Moedas")
    parse.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Lista Os Códigos de Todas As Moedas Disponíveis Para A Conversão",
    )
    parse.add_argument(
        "-e", "--exists", type=str, help="Verifica Se Um Código De Moeda Existe"
    )
    parse.add_argument(
        "-s", "--search", type=str, help="Pesquisa A Existência De Um Código De Moeda"
    )

    parse.add_argument("-c", "--convert", type=str, help="Valor A Ser Convertido")

    parse.add_argument("-t", "--to", type=str, help="Código Da Moeda Destino")

    args = parse.parse_args()

    if args.convert and not args.to:
        print("Especifique o código da moeda destino")
        os.abort()
    if args.to and not args.convert:
        print("Especifique o valor seguido do código a ser convertido")
        os.abort()
    return args


def listAllCodes():
    global CAMBIO
    if commandMode:
        print("\n", "-" * 50, "\n")
        for code in CAMBIO.keys(): print(code)
        print("\n", "-" * 50)
    else: return tuple(CAMBIO.keys())


def exists(code):
    global CAMBIO

    if code.upper() in CAMBIO.keys():
        if commandMode:
            print("\n", "-" * 50, "\n")
            print(f"O Código '{code.upper()}' existe!")
            print("\n", "-" * 50)
        else: return True
    else:
        if commandMode:
            print("\n", "-" * 50, "\n")
            print(f"O Código '{code.upper()}' não existe!")
            print("\n", "-" * 50)
        else: return False


def search(code):
    global CAMBIO
    code = code.upper()
    match = [x for x in CAMBIO.keys() if code in x]
    num = len(match)
    if commandMode:
        print("\n", "-" * 50, "\n")
        if not num:
            print("Nenhuma Correspondência Encontrada")
        else:
            print(f"Número de Correspondencias: {num}")
            for i in match: print(i)
        print("\n", "-" * 50)
    else: return (len(match), tuple(match))


def convert(from_, to):
    global CAMBIO
    value, code = from_
    code, to = code.upper(), to.upper()
    result = (value * CAMBIO[to]) / CAMBIO[code]
    if commandMode:
        print("\n", "-" * 50, "\n")
        print(f"{value:.4f} {code} == {result:.4f} {to}")
        print("\n", "-" * 50)
    else:
        return {code:value, to:result}


def splitArgs(string):

    pattern = r"(-?\d*\.?\d+)\s*([a-zA-Z_-]*)"

    result = re.search(pattern, string)

    value = result.group(1)
    code = result.group(2)
    value = float(value)
    return value, code


def printLastUpdate():
    global LAST_UPDATE
    print(f"Data da última atualização: {LAST_UPDATE[:10]} {LAST_UPDATE[11:19]}")


def main():
    args = setParams()
    getDataCommandMode()
    if args.list:
        listAllCodes()
    elif args.exists:
        exists(args.exists)
    elif args.search:
        search(args.search)
    elif args.convert:
        try:
            from_ = splitArgs(args.convert)
        except ValueError:
            print("Digite um valor de moeda válido!")
            os.abort()
        except AttributeError:
            print("Digite o valor a ser convertido!")
            os.abort()

        to = args.to
        try: convert(from_, to)
        except KeyError as e:
            print(f"O código de moeda {e.args[0]} é inválido!")
            os.abort()
    printLastUpdate()


if __name__ == "__main__":
    commandMode = True
    main()
else:
    commandMode = False
    getDataScriptMode()
