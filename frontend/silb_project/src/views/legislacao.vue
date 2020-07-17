
<template>
    <div class="corpo">
        <div class="text-justify cabecalho">{{textos.header}}</div>
        <div v-for="texto in textos.paragrafos" :key="texto" class="text-justify">
            <h1 class="cabecalho">{{texto.titulo}}</h1>
            <p class="texto">{{texto.conteudo}}</p>
        </div>
    </div>
</template>

<script>
import textos from "../assets/json/legislacao.json";

export default {
name: "Legislacao",
data() {
    return {
        textos: textos
    }
 }
}
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