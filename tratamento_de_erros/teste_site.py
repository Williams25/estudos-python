import urllib
import urllib.request


def conexaoSite(url):
    try:
        site = urllib.request.urlopen(url)
    except Exception as erro:
        print(f"Erro {erro.__class__}, o site não esta acessivel")
    else:
        print("Site acessivel")
        print(site.read())


conexaoSite("https://www.youtube.com/")
