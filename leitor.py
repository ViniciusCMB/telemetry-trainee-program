import sys, csv, os

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 leitor.py <arquivo.csv>")
        return

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Erro: arquivo '{path}' nao encontrado")
        return

    a=0
    b=0
    c=999999999
    amostras = []

    with open(path, 'r') as f:
        reader=csv.DictReader(f)
        for linha in reader:
            try:
                alt=float(linha['altitude_m'])
                amostras.append(alt)
                if alt > b:
                    b=alt
                if alt < c:
                    c=alt
                a+=1
            except (ValueError, KeyError):
                pass

    if a == 0:
        print("CSV vazio ou sem dados validos")
        return

    media = sum(amostras) / a
    print(f"Arquivo: {path}")
    print(f"Amostras: {a}")
    print(f"Altitude media: {media:.2f} m")
    print(f"Altitude max:   {b:.2f} m")
    print(f"Altitude min:   {c:.2f} m")

    with open('resumo.txt', 'w') as f:
        f.write(f"Arquivo: {path}\n")
        f.write(f"Amostras: {a}\n")
        f.write(f"Altitude media: {media:.2f} m\n")
        f.write(f"Altitude max:   {b:.2f} m\n")
        f.write(f"Altitude min:   {c:.2f} m\n")

if __name__ == "__main__":
    main()
