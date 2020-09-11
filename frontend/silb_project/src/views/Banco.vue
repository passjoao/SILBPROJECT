<template>
<div class="content">
  <b-card no-body>
    <b-tabs card>
      <b-tab title="Dados Gerais">
        <label form="pesquisar">Pesquisar </label>
        <input type="text" name="pesquisar" id="pesquisar" placeholder="">
        <div class="tabela white-100">
        
        <table class="table-auto">
          <thead>
          <tr>
            <th class="px-4 py-2">Referência</th>
            <th class="px-4 py-2">Capitania</th>
            <th class="px-4 py-2">Sesmeiros</th>
            <th class="px-4 py-2">Ocupação</th>
            <th class="px-4 py-2">Data Requerimento</th>
            <th class="px-4 py-2">Data de Concessão</th>
            <th class="px-4 py-2">Localidade</th>
            <th class="px-4 py-2">Área (léguas)</th>
            <th class="px-4 py-2">Data de Confirmação Régia</th>
            <th class="px-4 py-2">Histórico da Terra</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(iten) in itens" v-bind:key="iten.id">
            <td>{{ iten.record_id.reference}}</td> <!-- add referencia -->
            <td>{{ iten.record_id}}</td> <!-- add Capitania -->
            <td>{{ iten.owners}}</td> <!-- add nome -->
            <td>{{ iten.owners}}</td><!-- add ocupação -->
            <td>{{ iten.dateRequest | formatDate }}</td>
            <td>{{ iten.confirmation }}</td> <!-- add data concessão  add '| formatDate' -->
            <td>{{ iten.record_id }}</td> <!-- add localidade -->
            <td>{{ iten.record_id }}</td> <!-- add área -->
            <td>{{ iten.confirmation }}</td> <!-- add data de confirmação --> <!-- add '| formatDate' -->
            <td>{{ iten.record_id }}</td> <!-- add histórico da terra -->


          </tr>
          </tbody>
        </table>  
      </div>
      </b-tab>

      <b-tab title="Sesmeiros">
          <!-- colocar nova tabela aqui -->
      </b-tab>

      <b-tab title="Gráficos">
        <!-- colocar nova tabela aqui -->
      </b-tab>
    </b-tabs>
  </b-card>
</div>
</template>

<script>
import urlBase from "../main";
const axios = require('axios');

export default {
name: "Banco",
  data () {
    return {
      itens: null
    }
  },
  mounted() {
    console.log(urlBase)
    axios.get(urlBase+'request/')
    .then(res=>(this.itens=res.data, console.log(res.data)))
    .catch(erro=>{
      console.log(erro)
      })
  },
  methods:{
    
  }

}
</script>

<style scoped>
.tabela{
  overflow-x: scroll;
  word-wrap: all;
}
.table-auto{
  border-collapse: collapse;
}
.table-auto, td, th, tr{
  border: 0.5px solid #d3d3d3;
  white-space: nowrap;
}
thead{
  background-color: theme('colors.blue.100');
}

.content{
  margin: 10px auto;
  width: 1200px;
}
.card{
  background-color: theme('colors.white');
}
.tabela::-webkit-scrollbar
{
  height: 7px;
}
</style>
