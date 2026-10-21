from sympy import Matrix, Rational, diag, pprint, simplify, symbols

LINHA = "─" * 56

def questao(numero, titulo):
    print(f"\n{LINHA}\n QUESTÃO {numero} · {titulo}\n{LINHA}")

def mostrar(nome, matriz):
    print(f"\n{nome} =")
    pprint(matriz)

# ───────────────────────── QUESTÃO 1 ─────────────────────────
questao(1, "Custo consolidado 2A + 3B")

A = Matrix([[1, 0], [2, 1]])
B = Matrix([[0, 2], [6, 1]])

mostrar("2A\n", 2 * A)
mostrar("3B\n", 3 * B)
mostrar("2A + 3B\n", 2 * A + 3 * B)
print("\n Resposta: [[2, 6], [22, 5]]")

# ───────────────────────── QUESTÃO 2 ─────────────────────────
questao(2, "det(3A) = 27·det(A) PORQUE ...")

M = Matrix(3, 3, symbols("a0:9"))          
k = symbols("k")

M_linha = M.copy()
M_linha[0, :] = k * M[0, :]                

I = simplify((3 * M).det() - 27 * M.det()) == 0
II = simplify(M_linha.det() - k * M.det()) == 0

print(f"I  (det(3A) = 3³·det(A) = 27·det(A)) é verdadeira? {I}")
print(f"II (linha × k  →  det × k)           é verdadeira? {II}")
print("3A multiplica as 3 linhas por 3, logo det fica × 3·3·3 = 27: II justifica I.")
print("\n Resposta: A")

# ───────────────────────── QUESTÃO 3 ─────────────────────────
questao(3, "Qual expressão tem determinante 1?  (det A = -2, det B = 4)")

dA, dB = -2, 4
opcoes = {
    "A) det(A³B²)":   Rational(dA) ** 3 * dB ** 2,
    "B) det(A⁻¹Bᵀ)":  Rational(1, dA) * dB,
    "C) det(A⁴B⁻²)":  Rational(dA) ** 4 * Rational(1, dB) ** 2,
    "D) det(3A)":     3 ** 3 * dA,
    "E) det(A²B)":    Rational(dA) ** 2 * dB,
}

for nome, valor in opcoes.items():
    marca = "  ← igual a 1" if valor == 1 else ""
    print(f"{nome:<16} = {str(valor):>5}{marca}")

print("\nC) (det A)⁴ · (det B)⁻² = (-2)⁴ · 4⁻² = 16 · 1/16 = 1")
print("\n Resposta: C")

# ───────────────────────── QUESTÃO 4 ─────────────────────────
questao(4, "Matriz simétrica e transposta")

print("a) Matriz simétrica: matriz quadrada A tal que A = A′  (aᵢⱼ = aⱼᵢ).")
S = Matrix([[2, 5], [5, -3]])
mostrar("Exemplo S\n", S)
mostrar("S′\n", S.T)
print(f"\nS = S′ ?  {S == S.T}  →  S é simétrica")

print("\nb) Demonstração de (A + B)′ = A′ + B′")
X = Matrix(2, 2, symbols("a11 a12 a21 a22"))
Y = Matrix(2, 2, symbols("b11 b12 b21 b22"))
print(f"   Verificação simbólica: {(X + Y).T == X.T + Y.T}")
print("""
   ((A + B)′)ᵢⱼ = (A + B)ⱼᵢ = aⱼᵢ + bⱼᵢ
   (A′ + B′)ᵢⱼ  = (A′)ᵢⱼ + (B′)ᵢⱼ = aⱼᵢ + bⱼᵢ
   As entradas coincidem para todo i, j  ⇒  (A + B)′ = A′ + B′   c.q.d.""")

print(LINHA)
print(" GABARITO:  1) [[2,6],[22,5]]   2) A   3) C   4) ver acima")
print(LINHA)