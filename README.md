# Criptografia

Trabalho prático da disciplina de Criptografia (CI1017)

UFPR Ciência da Computação 2021 - ERE

### Esteganografia

- Implementação de uma forma de esteganografia na computação.
- Ideia: Técnica LSB, sendo que o byte da imagem codificada tem o tamanho da mensagem (tamanho máximo 255), e os últimos X bits da imagem tem o byte (aleatório) que a mensagem começa.

#### Instalação de bibliotecas

```
pip3 install -r requirements.txt
```

#### Execução

```
python3 steg.py [-e/-d] img.png
```

### Autoria

Maria Teresa Andrioli

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/mariateresaandrioli/) &nbsp; [![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/mariaandrioli)