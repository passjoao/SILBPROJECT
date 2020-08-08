
<template>
    <div class="corpo" id="butao1">
        <div class="text-justify cabecalho">{{textos.header}}</div>
         <b-button v-on:click="evento" v-b-toggle.collapse-1 variant="secondary"><span id="myButton">Expandir</span></b-button>
        <b-collapse id="collapse-1" class="mt-2">
                <b-card class="card-text">
                    <div v-for="texto in textos.paragrafos" :key="texto" class="text-justify">
                        <h1 class="cabecalho">{{texto.titulo}}</h1>
                        <p class="texto">{{texto.conteudo}}</p>
                    </div>
            </b-card>
        </b-collapse>
    </div>
</template>


<script>
import textos from "../assets/json/legislacao.json";

export default {
name: "Legislacao",
data() {
    return {
        textos: textos,
        evento: function() {
            var elem = document.getElementById("myButton");
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
</style>