<template>
    <div class="formStyle">
      <h1 class="titleForm text-center">Adicionar Nova Sesmaria</h1>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <div>
          <b-card no-body>
          <b-tabs pills card vertical nav-wrapper-class="w-25" end>
            <b-tab title="Sesmaria" active >
              <fieldset>
              <b-form-group id="reference" label="Nova Referência" label-for="input-1">
                <b-form-input id="input-1" v-model="form.reference" type="text" required placeholder="Referência"></b-form-input>
              </b-form-group>

              <b-form-group id="owners" label="Sesmeiros" label-for="owner">
                <b-form-input id="input-2" v-model="form.owners" required placeholder="Selecione o(s) sesmeiro(s)"></b-form-input>
              </b-form-group>

              <b-form-group id="captaincy" label="Capitanias:" label-for="input-3">
                <b-form-select id="input-3" v-model="form.captaincy" :options="capitanias" required></b-form-select>
              </b-form-group>

              <b-form-group id="landHistory" label="Histórico da terra:" label-for="input-4">
                <b-form-select id="input-4" v-model="form.landHistory" :options="landHistorys" required></b-form-select>
              </b-form-group>

              <b-form-group id="requestType" label="Tipo de Requerimento:" label-for="input-5">
                <b-form-select id="input-5" v-model="form.requestType" :options="requestTypes" required></b-form-select>
              </b-form-group>

              <b-form-group id="sesmaria" label="Data de Requisição" label-for="input-13">
                <b-form-input id="input-13" v-model="form.dateRequest" type="date" required placeholder="Referência"></b-form-input>
              </b-form-group>
              </fieldset>
              
              <hr>
              
              <b-form-group id="location" label="Localidade" label-for="input-6">
                <b-form-input id="input-6" v-model="form.location" type="text" required placeholder="Localidade"></b-form-input>
              </b-form-group>
              
              <b-form-group id="nearest_river" label="Ribeira" label-for="input-7">
                <b-form-input id="input-7" v-model="form.nearest_river" type="text" required placeholder="Ribeira"></b-form-input>
              </b-form-group>
              
              <b-form-group id="same_measure" label="Tipo de Requerimento:" label-for="input-06">
                <b-form-select id="input-06" v-model="form.same_measure" :options="same_measures" required></b-form-select>
              </b-form-group>

              <b-form-group id="area" label="Área em hectar" label-for="input-8" class="md-6">
                <b-form-input id="input-8" v-model="form.area" type="number" required placeholder="Área"></b-form-input>
                <b-form-text id="input-8-help">
                  Insira a área da sesmaria em hectáres
                </b-form-text>
              </b-form-group>
              
              <b-form-group id="hectar" label="Tipo de área" label-for="input-9">
                <b-form-select id="input-9" :options="[{ text: 'Léguas Quadradas' }, 'Braças Quadradas']" :value="null"></b-form-select>
              </b-form-group>

              <hr>
              <b-form-group id="confrotants" label="Confrontates" label-for="input-9">
                <b-form-input id="input-9" v-model="form.confrotants" type="text" required placeholder="Ribeira"></b-form-input>
              </b-form-group>
              <hr>
              <b-form-group id="comments" label="Observações" label-for="input-9">
                <b-form-input id="input-9" v-model="form.comments" type="text" required placeholder="Ribeira"></b-form-input>
              </b-form-group>
              <b-form-group id="privileged_observations" label="Observações Privilegiadas" label-for="input-9">
                <b-form-input id="input-9" v-model="form.privileged_observations" type="text" required placeholder="Ribeira"></b-form-input>
              </b-form-group>
            </b-tab>
            
            <b-tab title="Documentos">              
              <b-form-group id="files" label="Adicionar Documentos" label-for="input-10">
                <b-form-file multiple :file-name-formatter="formatNames" placeholder="Arquivos..."></b-form-file>
              </b-form-group>

              <b-form-group id="images" label="Adicionar Imagens" label-for="input-11">
                <b-form-file multiple :file-name-formatter="formatNames" placeholder="Imagens..."></b-form-file>
              </b-form-group>
            </b-tab>
            <b-tab title="Deferimentos">

              <b-form-group id="hectar" label="Foi Deferido" label-for="input-12">
                <b-form-select id="input-12" :options="[{ text: 'Selecionar', value: null }, {text: 'Sim', value: true}, {text:'Não', value: false}]" required></b-form-select>
              </b-form-group>

              <b-form-group id="hectar" label="Forma de deferimento" label-for="input-12">
                <b-form-select id="input-12" v-model="form.defermentForm" :options="defermentForms" required></b-form-select>
              </b-form-group>

              <b-form-group id="sesmaria" label="Data de Confirmação" label-for="input-13">
                <b-form-input id="input-13" v-model="form.dateConfirmation" type="date" required></b-form-input>
              </b-form-group>

              <b-form-group id="sesmaria" label="Data de Concessão" label-for="input-13">
                <b-form-input id="input-13" v-model="form.dateConcession" type="date" required ></b-form-input>
              </b-form-group>
              
              <hr>
              
              <b-form-group id="sesmaria" label="Autoridade" label-for="input-13">
                <b-form-input id="input-13" v-model="form.authority" type="text" required ></b-form-input>
              </b-form-group>
              <b-form-group id="hectar" label="Título da Autoridade" label-for="input-12">
                <b-form-select id="input-12" :options="[{ text: 'Selecionar', value: null }, 'Capitão-mor', 'Governador']" required></b-form-select>
              </b-form-group>

              <b-form-group id="scriviner" label="Nome do Escrivão" label-for="owner">
                <b-form-input id="input-2" v-model="form.scriviner" required placeholder="Escrivão..."></b-form-input>
              </b-form-group>

              <b-form-group id="source" label="Fonte" label-for="owner">
                <b-form-input id="input-2" v-model="form.source" required placeholder="Fonte..."></b-form-input>
              </b-form-group>

            </b-tab>
            <b-tab title="Justificativas">
              <b-form-select v-model="selected" :options="justifications" multiple search :select-size="4"></b-form-select>
            </b-tab>
            <b-tab title="Exigências">
              <b-form-select v-model="selected" :options="demands" multiple search :select-size="4"></b-form-select>
            </b-tab>
          </b-tabs>
          </b-card>
        </div>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </div>
</template>

<script>
export default {
    data() {
      return {
        form: {
          reference: '',
          owners: '',
          capitania: null,
          landHistory: null,
          requestType: null,
        },
        capitanias: [{ text: 'Selecionar Capitania', value: null }, 'Rio Grande', 'Ceara', 'Pernambuco', '...'],
        landHistorys: [{ text: 'Selecionar Histórico da terra', value: null }, 'Rio Grande', 'Ceara', 'Pernambuco', '...'],
        requestTypes: [{ text: 'Selecionar Tipo de Requerimento', value: null }, 'Concessão', 'Confirmação', 'Não Encontrado'],
        same_measures: [{ text: 'Selecione...', value: null }, {text: 'Sim', value: true},  {text: 'Não', value: false}],
        defermentForms: [{ text: 'Selecionar Forma de Deferimento', value: null }, 'Provisão', 'Carta Régia', 'Carta de Doação'],
        justifications:['teste1', 'teste 2'],
        demands:['teste3', 'teste4'],
        show: true
      }
    },
    methods: {
      formatNames(files) {
        if (files.length === 1) {
          return files[0].name
        } else {
          return `${files.length} files selected`
        }
      },
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form value
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style scoped>
  .formStyle{
    max-width: 900px;
    padding: 10px 20px;
    background: #f4f7f8;
    margin: 10px auto;
    padding: 20px;
    background: #f4f7f8;
    border-radius: 8px;
    font-size: 1.1em;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .titleForm{
    font-size: 2.5em;
    margin: 20px auto;
  }
  .subtitleForm {
    font-size: 1.5em;
  }
  .formStyle fieldset{
    border: none;
  }
  .formStyle legend{
    font-size: 1.4em;
    margin-bottom: 10px;
  }
  hr {
    margin: 10px auto;
  }
</style>