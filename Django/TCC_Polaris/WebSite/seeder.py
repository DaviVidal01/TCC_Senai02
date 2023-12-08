from .models import Barra_Pesquisa, Pedido, Produtos_BD, Tipo_BD, Marca_BD, Tecido_BD, Tamanho_BD
from django.utils import timezone

agora = timezone.now()

def DadosHighFashionBD():
    # --- Tamanhos
    Tamanho_BD.objects.create(tamanho='PP')
    Tamanho_BD.objects.create(tamanho='P')
    Tamanho_BD.objects.create(tamanho='M')
    Tamanho_BD.objects.create(tamanho='G')
    Tamanho_BD.objects.create(tamanho='GG')
    Tamanho_BD.objects.create(tamanho='XGG')
    # --- Tipos
    Tipo_BD.objects.create(tipo='Camisa')
    Tipo_BD.objects.create(tipo='Calça')
    Tipo_BD.objects.create(tipo='Casaco/Blusa')
    Tipo_BD.objects.create(tipo='Vestido')
    Tipo_BD.objects.create(tipo='Short')
    Tipo_BD.objects.create(tipo='Bermuda')
    Tipo_BD.objects.create(tipo='Jaqueta')
    Tipo_BD.objects.create(tipo='Íntima')
    Tipo_BD.objects.create(tipo='Banho')
    Tipo_BD.objects.create(tipo='Social')
    Tipo_BD.objects.create(tipo='Esportiva')
    Tipo_BD.objects.create(tipo='Kit')
    # --- Marcas
    Marca_BD.objects.create(marca='High Fashion')
    Marca_BD.objects.create(marca='Nike')
    Marca_BD.objects.create(marca='Adidas')
    Marca_BD.objects.create(marca='Zara')
    Marca_BD.objects.create(marca="Levi's")
    Marca_BD.objects.create(marca="Gucci")
    Marca_BD.objects.create(marca="Chanel")
    Marca_BD.objects.create(marca="Calvin Klein")
    Marca_BD.objects.create(marca="Bob Nature")
    Marca_BD.objects.create(marca="Puma")
    # --- Tecidos
    Tecido_BD.objects.create(tecido='Algodão')
    Tecido_BD.objects.create(tecido='Jeans')
    Tecido_BD.objects.create(tecido='Lã')
    Tecido_BD.objects.create(tecido='Legging')
    Tecido_BD.objects.create(tecido='Seda')
    Tecido_BD.objects.create(tecido='Linho')
    Tecido_BD.objects.create(tecido='Sintéticos')
    Tecido_BD.objects.create(tecido='Microfibra')
    # --- Produtos
    Produtos_BD.objects.create(
        titulo="Terno Azul Gucci",
        foto="images/13_vMXu88c.png",
        descricao= "Terno Azul da marca Gucci usando tecido de lã", 
        preco="900", 
        data_foto=agora, 
        autor_id="1",
        marca_id="30",
        tamanho_id="23",
        tecido_id="22",
        tipo_id="46",
        genero="Masculino",
    )
    Produtos_BD.objects.create(
        titulo="Terno Cinza Chanel",
        foto="images/12.png",
        descricao= "Terno cinza da Chanel usando tecidos de lã", 
        preco="850", 
        data_foto=agora, 
        autor_id="1",
        marca_id="31",
        tamanho_id="23",
        tecido_id="22",
        tipo_id="46",
        genero="Masculino",
    )
    Produtos_BD.objects.create(
        titulo="Terno Bege Calvin Klein",
        foto="images/11_H0GTVms.png",
        descricao= "Terno bege da Calvin Klein usando tecido de lã", 
        preco="500", 
        data_foto=agora, 
        autor_id="1",
        marca_id="32",
        tamanho_id="23",
        tecido_id="22",
        tipo_id="46",
        genero="Masculino",
    )
    Produtos_BD.objects.create(
        titulo="Vestido Branco Zara",
        foto="images/7_FOc1rR1.png",
        descricao= "Vestido branco da marca Zara e tecido Linho", 
        preco="200", 
        data_foto=agora, 
        autor_id="1",
        marca_id="28",
        tamanho_id="23",
        tecido_id="25",
        tipo_id="40",
        genero="Feminino",
    )
    Produtos_BD.objects.create(
        titulo="Vestido Cinza Zara",
        foto="images/6_hPALumE.png",
        descricao= "Vestido cinza da marca Zara tecido Linho", 
        preco="230", 
        data_foto=agora, 
        autor_id="1",
        marca_id="28",
        tamanho_id="23",
        tecido_id="25",
        tipo_id="40",
        genero="Feminino",
    )
    Produtos_BD.objects.create(
        titulo="Vestido Azul Claro Zara",
        foto="images/10_CnlDA5K.png",
        descricao= "Vestido azul claro da marca Zara usando tecido Seda", 
        preco="220", 
        data_foto=agora, 
        autor_id="1",
        marca_id="28",
        tamanho_id="23",
        tecido_id="24",
        tipo_id="40",
        genero="Feminino",
    )
    Produtos_BD.objects.create(
        titulo="Calça Jeans rasgo joelho",
        foto="images/8_RQjn6EU.png",
        descricao= "Calça Jeans rasgada", 
        preco="123", 
        data_foto=agora, 
        autor_id="1",
        marca_id="33",
        tamanho_id="23",
        tecido_id="21",
        tipo_id="38",
        genero="Unisex",
    )
    Produtos_BD.objects.create(
        titulo="Camisa Estampada Preta",
        foto="images/9_Q1qaKx1.png",
        descricao= "Camisa estampada preta com mão de caveira, camisa feminino e masculino da marca High Fashion", 
        preco="150", 
        data_foto=agora, 
        autor_id="1",
        marca_id="25",
        tamanho_id="23",
        tecido_id="20",
        tipo_id="37",
        genero="Unisex",
    )
    Produtos_BD.objects.create(
        titulo="Camisa Estampada Vermelha",
        foto="images/camisavermelha_Rd9xiCX.png",
        descricao= "Camisa estampada da cor vermelha da marca High Fashion", 
        preco="123", 
        data_foto=agora, 
        autor_id="1",
        marca_id="25",
        tamanho_id="23",
        tecido_id="20",
        tipo_id="37",
        genero="Unisex",
    )
    Produtos_BD.objects.create(
        titulo="Calvin Klein Esportiva",
        foto="images/4_fV2nPkg.png",
        descricao= "Calvin Klein Esportiva feminina do tecido de legging", 
        preco="300", 
        data_foto=agora, 
        autor_id="1",
        marca_id="32",
        tamanho_id="23",
        tecido_id="23",
        tipo_id="47",
        genero="Feminino",
    )