<template>
<div class="content">
    <p class="header">Equipe responsável pela Plataforma SILB - Sesmarias do Império Luso Brasileiro</p>
    <div class="equipe">
    <div>
        <h1 class="header">Coordenação</h1>
        <div v-for="pessoa in equipe.coordenacao" :key="pessoa" class="coordenacao">
            <td>
              <ul class="nome">{{pessoa.nome}}</ul>
              <ul>{{pessoa.tilulacao}}</ul>
             </td>
        </div>
    </div>
    <div>
        <h1 class="header">Pesquisadores</h1>
        <div v-for="pessoa in equipe.colaboracao" :key="pessoa" class="Colaboradores">
            <td>
              <ul class="nome">{{pessoa.nome}}</ul>
              <ul>{{pessoa.tilulacao}}</ul>
             </td>
        </div>
    </div>
    <div>
        <h1 class="header">Desenvolvimento</h1>
        <div v-for="pessoa in equipe.desenvolvimento" :key="pessoa" class="desenvolvimento">
            <td>
              <ul class="nome">{{pessoa.nome}}</ul>
              <ul>{{pessoa.tilulacao}}</ul>
             </td>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import equipe from "../assets/json/equipe.json";

export default {
name: "Equipe",
data() {
    return {
        equipe: equipe
    }
 }
}
</script>

<style scoped>
.content{
    margin: 30px auto;
    width: 900px;
}
.header{
    font-weight: bold;
    margin: 10px auto;
}
.nome{
    font-weight: bold;
}
.equipe{
    margin: 0 auto;
    width: 800px;
}
.coordenacao{
    margin: 0 auto;
    width: 750px;
}
.Colaboradores{
    margin: 0 auto;
    width: 750px;
}
.desenvolvimento{
    margin: 0 auto;
    width: 750px;
}
</style>