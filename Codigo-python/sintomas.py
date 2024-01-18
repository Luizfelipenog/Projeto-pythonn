from playwright.sync_api import sync_playwright
import time


def clicar(pagina):
    # Obter todos os elementos correspondentes
    elementos = pagina.locator('//td[contains(@class, "tdAzulClaro")][contains(@onclick, "adicionarSintomaLista")]')

    # Verificar se há pelo menos um elemento
    if elementos.count() > 0:
        # Passar o mouse sobre o primeiro elemento
        primeiro_elemento = elementos.first
        primeiro_elemento.hover()

        # Aguardar um breve momento para permitir a exibição da dica de ferramenta, se houver
        time.sleep(1)

        # Clicar no elemento
        primeiro_elemento.click()


def sintoma(pagina):
    sintoma_nome = input("Digite o nome do sintoma:\n")
    pagina.locator('xpath=//*[@id="sintomaPesquisa"]').click()
    pagina.fill('xpath=//*[@id="sintomaPesquisa"]', sintoma_nome)
    pagina.locator('xpath=//*[@id="btPesquisaSintoma"]').click()
    clicar(pagina)


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page()
    pagina.goto("https://analisesintomas.com")

    Quantidade = int(input("Digite quantos sintomas deseja inserir:"))

    for _ in range(Quantidade):
        sintoma(pagina)
    pagina.locator('xpath=//*[@id="message_send"]').click()
    # Imprimir o XPath fornecido
    mensagem_xpath = '//*[@id="divResultadoDoencasDir"]/span[1]'
    mensagem_elemento = pagina.locator(mensagem_xpath)
    mensagem_texto = mensagem_elemento.inner_text()  # Correção aqui, usando inner_text() em vez de text_content()
    print(mensagem_texto)
    mensagem_probabilidade = '//*[@id="divResultadoDoencasDir"]/span[2]'
    mensagem_elemento2 = pagina.locator(mensagem_probabilidade)
    mensagem_texto2 = mensagem_elemento2.inner_text()  # Correção aqui, usando inner_text() em vez de text_content()
    print(mensagem_texto2)



    # Aguardar um tempo para observar a interação (opcional)
    time.sleep(5)
