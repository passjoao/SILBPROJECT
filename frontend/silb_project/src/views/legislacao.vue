
<template>
    <div class="corpo" id="butao1">
        <div class="item">
        <div class="text-justify cabecalho">{{textos.header}}</div>
         <b-button v-on:click="evento1" v-b-toggle.collapse-1 variant="secondary"><span id="btn1">Expandir</span></b-button>
        <b-collapse id="collapse-1" class="mt-2">
                <b-card class="card-text">
                    <div v-for="texto in textos.paragrafos" :key="texto" class="text-justify">
                        <h1 class="cabecalho">{{texto.titulo}}</h1>
                        <p class="texto">{{texto.conteudo}}</p>
                    </div>
            </b-card>
        </b-collapse>
        </div>
        <div class="item">
            <div class="text-justify cabecalho">Ordenações Afonsinas</div>
            <b-button v-on:click="evento2" v-b-toggle.collapse-2 variant="secondary"><span id="btn2">Expandir</span></b-button>
          <b-collapse id="collapse-2">
            <b-card>Download do PDF: <a class="link" href="PDFs/ordenacoesafonsinas.pdf">Ordenações Afonsinas</a> </b-card>
          </b-collapse>
        </div>
        <div class="item">
            <div class="text-justify cabecalho">Ordenações Filipinas</div>
            <b-button v-on:click="evento3" v-b-toggle.collapse-3 variant="secondary"><span id="btn3">Expandir</span></b-button>
          <b-collapse id="collapse-3">
            <b-card>Download do PDF: <a class="link" href="PDFs/ordenacoesfilipinas.pdf">Ordenações Filipinas</a> </b-card>
          </b-collapse>
        </div>
        <div class="item">
            <div class="text-justify cabecalho">Ordenações Manuelinas</div>
            <b-button v-on:click="evento4" v-b-toggle.collapse-4 variant="secondary"><span id="btn4">Expandir</span></b-button>
          <b-collapse id="collapse-4">
            <b-card>Download do PDF: <a class="link" href="PDFs/ordenacoesmanuelinas.pdf">Ordenações Manuelinas</a> </b-card>
          </b-collapse>
        </div>
        <div class="item">
            <div class="text-justify cabecalho">Tabela das Ordens Régias Complementares</div>
            <b-button v-on:click="evento5" v-b-toggle.collapse-5 variant="secondary"><span id="btn5">Expandir</span></b-button>
          <b-collapse id="collapse-5">
            <b-card>Download do PDF: <a class="link" href="PDFs/tabelanova.pdf">Tabela das Ordens Régias Complementares</a> </b-card>
          </b-collapse>
        </div>
        <div class="item">
            <div class="text-justify cabecalho">Tabela comparativa das leis de sesmarias</div>
            <b-button v-on:click="evento6" v-b-toggle.collapse-6 variant="secondary"><span id="btn6">Expandir</span></b-button>
          <b-collapse id="collapse-6">
            <b-card>Download do PDF: <a class="link" href="PDFs/tabelmon.pdf">Tabela comparativa das leis de sesmarias</a> </b-card>
          </b-collapse>
        </div>
    </div>
</template>


<script>
import textos from "../assets/json/legislacao.json";


export default {
name: "Legislacao",
components: {
  },
data() {
    return {
        textos: textos,
        evento1: function() {
            var elem = document.getElementById("btn1");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        },
        evento2: function() {
            var elem = document.getElementById("btn2");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        },
        evento3: function() {
            var elem = document.getElementById("btn3");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        },
        evento4: function() {
            var elem = document.getElementById("btn4");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        },
        evento5: function() {
            var elem = document.getElementById("btn5");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        },
        evento6: function() {
            var elem = document.getElementById("btn6");
            if(elem.textContent == "Fechar") elem.textContent = "Expandir";
            else elem.textContent = "Fechar";        
        }
    }
 }
};
</script>

<style scoped>
.corpo{
    margin: 40px auto;
    width: 900px;
} .cabecalho{
    font-weight: bold;
    font-size:20px;
    margin: 10px 0;
}
.texto{
    margin: 30px 0;
    text-indent: 50px;
}
.item{
    margin: 10px
}
.link{
    color: blueviolet;
}
</style>