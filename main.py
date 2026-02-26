class Produto:
    def __init__(self, nome, codigo, categoria, quantidade, preco, descricao, fornecedor, estoque_minimo=5):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.estoque_minimo = estoque_minimo

    def adicionar(self, qtd):
        if qtd > 0:
            self.quantidade += qtd
            print(f"✅ {qtd} unidades adicionadas. Novo saldo de '{self.nome}': {self.quantidade}")
        else:
            print("❌ Quantidade inválida.")

    def remover(self, qtd):
        if 0 < qtd <= self.quantidade:
            self.quantidade -= qtd
            print(f"📉 {qtd} unidades removidas. Novo saldo de '{self.nome}': {self.quantidade}")
            self.verificar_alerta()
        else:
            print("❌ Quantidade inválida ou estoque insuficiente para a operação.")

    def atualizar_manualmente(self, nova_qtd):
        if nova_qtd >= 0:
            self.quantidade = nova_qtd
            print(f"🔄 Estoque de '{self.nome}' atualizado forçadamente para: {self.quantidade}")
            self.verificar_alerta()
        else:
            print("❌ O estoque não pode ser negativo.")

    def verificar_alerta(self):
        # A lógica de alerta embutida na própria classe garante que o produto "grite" quando necessário.
        if self.quantidade <= self.estoque_minimo:
            print(f"⚠️ ALERTA: O estoque de '{self.nome}' (Cód: {self.codigo}) está baixo! Restam apenas {self.quantidade} unidades.")


class GerenciadorEstoque:
    def __init__(self):
        self.catalogo = {} # Dicionário para buscas ultra-rápidas pelo código do produto

    def cadastrar_produto(self, produto):
        if produto.codigo in self.catalogo:
            print("❌ Produto com este código já existe no sistema.")
        else:
            self.catalogo[produto.codigo] = produto
            print(f"📦 Produto '{produto.nome}' cadastrado com sucesso!")

    def relatorio_estoque(self):
        print("\n--- 📊 RELATÓRIO DE ESTOQUE ---")
        if not self.catalogo:
            print("O estoque está vazio.")
            return
        
        # O uso do loop 'for' para iterar sobre os objetos instanciados
        for codigo, produto in self.catalogo.items():
            print(f"[{codigo}] {produto.nome} | Qtd: {produto.quantidade} | R$ {produto.preco:.2f} | Fornecedor: {produto.fornecedor}")
            produto.verificar_alerta()
        print("-------------------------------\n")


# === Área de Execução e Testes (Uso de Loops) ===
def iniciar_sistema():
    sistema = GerenciadorEstoque()
    
    # Cadastrando alguns objetos iniciais
    p1 = Produto("Notebook Pro", "NOTE01", "Eletrônicos", 10, 4500.00, "Notebook 16GB RAM", "TechCorp", estoque_minimo=3)
    p2 = Produto("Camiseta Básica", "CAM01", "Vestuário", 5, 49.90, "100% Algodão", "Malharia X", estoque_minimo=10)
    
    sistema.cadastrar_produto(p1)
    sistema.cadastrar_produto(p2)

    # Loop principal para simular o funcionamento contínuo do sistema
    while True:
        print("\n1. Ver Estoque | 2. Vender (Remover) | 3. Receber (Adicionar) | 4. Balanço (Atualizar) | 5. Sair")
        opcao = input("Escolha uma ação: ")

        if opcao == '1':
            sistema.relatorio_estoque()
        
        elif opcao in ['2', '3', '4']:
            cod = input("Digite o código do produto: ")
            if cod in sistema.catalogo:
                produto = sistema.catalogo[cod]
                qtd = int(input("Digite a quantidade: "))
                
                if opcao == '2':
                    produto.remover(qtd)
                elif opcao == '3':
                    produto.adicionar(qtd)
                elif opcao == '4':
                    produto.atualizar_manualmente(qtd)
            else:
                print("❌ Produto não encontrado.")
                
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida.")

# Descomente a linha abaixo para rodar o menu interativo no seu terminal
iniciar_sistema()