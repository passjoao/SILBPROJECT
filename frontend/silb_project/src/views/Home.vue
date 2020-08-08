<template>
  <div>
  <div class="header-cover">
  </div>
  <div  class="px-64 py-16 text-justify text-xl">
    A <b class="font-extrabold">PLATAFORMA SILB </b>é uma base de dados contendo informações das sesmarias concedidas pela Coroa portuguesa no mundo atlântico. A Plataforma SILB tem como objetivo facilitar o acesso às informações de
    quase 16 mil cartas de sesmarias concedidas na América portuguesa, tanto por governadores como capitães mores. Pretende-se a curto prazo incluir as sesmarias distribuídas na África e nas Ilhas atlânticas.
    Na petição por uma carta de sesmaria, o requerente devia justificar seu pedido, e quando recebesse a carta de concessão havia uma serie de obrigações entre as quais estava a necessidade do cultivo, da
    demarcação e da confirmação real, embora a maioria das cartas não tenha sido confirmada pelo rei.
  </div>
  <div class="img-ft">
    <div class="row">
      <div class="col">
        <img src="https://i.ibb.co/vYXpNr4/0a4230f2-21a2-45b0-bc14-6361e0fef37e.png" >
      </div>
      <div class="col">  
        <img src="https://i.ibb.co/LpJ3tSL/logocchla.png" >
      </div>
      <div class="col">  
        <img src="https://i.ibb.co/Fw7SXFm/logo.png" class="lehs">
      </div>
    </div>
    <div class="row row2">
      <div class="col">
        <img src="https://i.ibb.co/fpsyW6D/cnpq.gif" >
      </div>
      <div class="col">
        <img src="https://i.ibb.co/gZy76Ps/ppg.png">
      </div>
      <div class="col">
        <img src="https://i.ibb.co/2WVf4rL/ppgh.jpg" class="col-ppgh">
      </div>
    </div>
  </div>
      <!-- <img alt="Vue foot" src="../assets/imagens/roda_pe_home.png"> -->
  </div>
</template>

<style>
.header-cover {
  background-image: url(../assets/imagens/imagen_home.png);
  background-size: cover;
  background-position: center;
  height: 357px;
}

.img-ft{
  width: 900px;
  margin: auto;

}
.lehs{
  margin-top: -20px;
}
.row .col {
  padding: 0 50px;
}
.row2{
  margin-top: 50px;
}
.col-ppgh{
  width: 100px;
  margin: auto;
}
</style>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {

  }
}
</script>
