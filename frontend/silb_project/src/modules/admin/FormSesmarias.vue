<template>
    <div class="formStyle">
      <h1 class="titleForm text-center">Adicionar Nova Sesmaria</h1>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <div>
          <b-card no-body>
          <b-tabs pills card vertical nav-wrapper-class="w-25" end>
            <b-tab title="Sesmaria" active >
              <fieldset>

              <b-form-group id="reference" label="Referência Antiga" label-for="input-18">
                <b-form-input id="input-18" v-model="form.oldReference" maxlength=7 type="text" required placeholder="Referência"></b-form-input>
                <b-form-text id="input-8-help">
                  Referência da silb antiga, tamanho máximo 7 caracteres
                </b-form-text>
              </b-form-group>

              <b-form-group id="owners" label="Sesmeiros" label-for="owners-ipt">
                <b-form-select id="owners-ipt" v-model="form.owners" :options="owners" required multiple search></b-form-select>
              </b-form-group>
              
              <b-form-group id="captaincyLabel" label="Capitanias:" label-for="captaincy">
                <b-form-select v-model="form.captaincy" :options="this.capitanias">
                </b-form-select>
              </b-form-group>

              <b-form-group id="landHistory" label="Histórico da terra:" label-for="input-4">
                <b-form-select id="input-4" v-model="form.landHistory" :options="landHistorys" required>
                </b-form-select>
              </b-form-group>

              <b-form-group id="requestType" label="Tipo de Requerimento:" label-for="input-5">
                <b-form-select id="input-5" v-model="form.requestType" :options="requestTypes" required></b-form-select>
              </b-form-group>

              <b-form-group id="sesmaria" label="Data de Requisição" label-for="input-13">
                <b-form-input id="input-13" v-model="form.dateRequest" type="date" required placeholder="Referência"></b-form-input>
              </b-form-group>
              </fieldset>
              
              <b-form-group id="comments" label="Observações" label-for="input-9">
                <b-form-textarea id="input-9" v-model="form.comments" type="text" required placeholder="Observações"></b-form-textarea>
              </b-form-group>

              <b-form-group id="privileged_observations" label="Observações privilegiadas" label-for="privileged_observations-ipt">
                <b-form-textarea id="privileged_observations-ipt" v-model="form.privileged_observations" type="text" required placeholder="Observações privilegiadas"></b-form-textarea>
              </b-form-group>
              <!--  -->
              
              <hr>
              
              <b-form-group id="location" label="Localidade" label-for="input-6">
                <b-form-input id="input-6" v-model="form.location" type="text" required placeholder="Localidade"></b-form-input>
              </b-form-group>
              
              <b-form-group id="nearest_river" label="Ribeira" label-for="input-7">
                <b-form-input id="input-7" v-model="form.nearest_river" type="text" required placeholder="Ribeira"></b-form-input>
              </b-form-group>

              <b-form-group id="area" label="Área em hectar" label-for="input-8" class="md-6">
                <b-form-input id="input-8" v-model="form.area" type="number" required placeholder="Área"></b-form-input>
                <b-form-text id="input-8-help">
                  Insira a área da sesmaria em hectáres
                </b-form-text>
              </b-form-group>
              
              <b-form-group id="hectar" label="Tipo de área" label-for="input-9">
                <b-form-select id="input-9" v-model="form.areaType" :options="areaTypes" :value="null"></b-form-select>
              </b-form-group>

              <hr>
              <b-form-group id="confrotants" label="Confrontates" label-for="input-9">
                <b-form-input id="input-9" v-model="form.confrotants" type="text" required placeholder="Confrotantes"></b-form-input>
              </b-form-group>
              <hr>
              <b-form-group id="comments" label="Observações" label-for="input-9">
                <b-form-textarea id="input-9" v-model="form.comments_land" type="text" required placeholder="Observações"></b-form-textarea>
              </b-form-group>

            </b-tab>
            
            <b-tab title="Documentos">              
              <b-form-group id="files" label="Adicionar Documentos" label-for="input-10">
                <b-form-file multiple :file-name-formatter="formatNames" v-model="form.files" placeholder="Arquivos..."></b-form-file>
              </b-form-group>

              <b-form-group id="images" label="Adicionar Imagens" label-for="input-11">
                <b-form-file multiple :file-name-formatter="formatNames" v-model="form.images" placeholder="Imagens..."></b-form-file>
              </b-form-group>
            </b-tab>
            <b-tab title="Deferimentos">

              <b-form-group id="hectar" label="Foi Deferido" label-for="input-12">
                <b-form-select id="input-12" v-model="form.defered" :options="defereds" required></b-form-select>
              </b-form-group>

              <b-form-group id="hectar" label="Deferimento favorável" label-for="input-12">
                <b-form-select id="input-12" v-model="form.favorable" :options="defermentForms" required></b-form-select>
              </b-form-group>

              <b-form-checkbox id="secular_clergy-ipt" v-model="form.same_measure" name="same_measure-checkbox" true-value="Y" false-value="N">
                Mesma medida
              </b-form-checkbox>

              <b-form-group id="sesmaria" label="Data de Concessão" label-for="input-13">
                <b-form-input id="input-13" v-model="form.dateConcession" type="date" required ></b-form-input>
              </b-form-group>
              
              <hr>
              <b-row>
                <b-col sm="7">
                  <b-form-group id="sesmaria" label="Autoridade" label-for="input-13">
                    <b-form-input id="input-13" v-model="form.authority" type="text" required ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col sm="5">
                  <b-form-group id="hectar" label="Título da Autoridade" label-for="input-12">
                    <b-form-select v-model="form.authorityTitle" id="input-12" :options="[{ text: 'Selecionar', value: null }, 'Capitão-mor', 'Governador']" required></b-form-select>
                  </b-form-group>
                </b-col>
                <button @click.prevent="authorityPost">add</button>
              </b-row>
              {{authoritysNames}}
              <hr>
              <!-- checkbox tramitações -->
              <h2 class="text-center subtitleForm">Tramitações</h2>
              <b-row>
                <b-col sm="6">
                  <b-form-checkbox id="checkbox-1" v-model="form.pendingProvider" name="provider-checkbox" true-value="Y" false-value="N">
                    Passou por provedor
                    <b-form-input id="input-20" v-model="form.ProviderName" required placeholder="Nome Provedor"></b-form-input>
                  </b-form-checkbox>
                </b-col>
                <b-col sm="6">
                  <b-form-checkbox id="checkbox-2" v-model="form.pendingAssembly" name="assembly-checkbox" true-value="Y" false-value="N">
                    Passou por Câmara
                    <b-form-input id="input-21" v-model="form.assemblyName" required placeholder="Nome Camarário"></b-form-input>
                  </b-form-checkbox>
                </b-col>
              </b-row>
              <b-row>
                <b-col sm="5">
                  <b-form-checkbox id="checkbox-23" v-model="form.pendingScriviner" name="assembly-checkbox" true-value="Y" false-value="N">
                    Passou por Escrivão
                    <b-form-input id="input-23" v-model="form.scrivinerName" required placeholder="Nome Escrivão"></b-form-input>
                  </b-form-checkbox>
                </b-col>
              </b-row>
              
              <hr>

              <b-form-group id="source" label="Fonte de registro" label-for="source-ipt">
                <b-form-input id="source-ipt" v-model="form.source" required placeholder="Fonte..."></b-form-input>
                <b-form-text id="input-2-help">
                  Insira a Fonte do documento físico. 
                </b-form-text>
              </b-form-group>

              <b-form-group id="link" label="Links de referência" label-for="link-ipt">
                <b-form-input id="link-ipt" v-model="form.link" required placeholder="Link..."></b-form-input>
                <b-form-text id="link-2-help">
                  Insira um link externo caso tenha de refeência a sesmaria.
                </b-form-text>
              </b-form-group>

              <b-form-group id="scriviner" label="Escrivão" label-for="scriviner-ipt">
                <b-form-input id="scriviner-ipt" v-model="form.scriviner" required placeholder="Escrivão..."></b-form-input>
                <b-form-text id="scriviner-2-help">
                  Insira o Nome do escrivão da carta
                </b-form-text>
              </b-form-group>
              
              <b-form-group id="comments" label="Observações" label-for="input-coment-deferment">
                <b-form-textarea id="input-coment-deferment" v-model="form.comments_deferment" type="text" required placeholder="Observações"></b-form-textarea>
              </b-form-group>

              <b-form-group id="comments" label="Observações privilegiadas" label-for="input-coment-deferment">
                <b-form-textarea id="input-coment-deferment" v-model="form.privileged_observations_deferment" type="text" required placeholder="Observações"></b-form-textarea>
              </b-form-group>

            </b-tab>
            <b-tab title="Justificativas">


                <multiselect
                  v-model="form.justifications"
                  :options="justifications"
                  :multiple="true"
                  :close-on-select="false"
                  placeholder="Selecionar"
                  label="text"
                  :key="value">
                </multiselect>
            </b-tab>
            <b-tab title="Exigências">
              <multiselect
                  v-model="form.demands"
                  :options="demands"
                  :multiple="true"
                  :close-on-select="false"
                  placeholder="Selecionar"
                  label="text"
                  :value="value">
                </multiselect>
            </b-tab>
          </b-tabs>
          </b-card>
        </div>
        <b-button variant="primary" @click="submitPost">Enviar</b-button>
        <b-button type="reset" variant="danger" onclick="window.location.href='/dashboard'">Cancelar</b-button>
      </b-form>
    </div>
</template>

<script>
 import Multiselect from 'vue-multiselect'
import firebase from 'firebase'
import listLandHistory from '@/util/const.js'
import urlBase from '@/main.js'
const axios = require('axios')

export default {
    components: { Multiselect },
    data() {
      return {
        options:["a", "b"],
        selected: null,
        search:null,
        form: {
          reference: null,
          oldReference: null,
          owners: [],
          captaincy: null,
          landHistory: null,
          requestType: null,
          dateRequest: null,
          location: null,
          nearest_river: null,
          same_measure: false,
          area: null,
          areaType: null,
          confrotants:null,
          files: null,
          images: null,
          defered: null,
          dateConcession: null,
          authority: null,
          authoritys: [],
          authorityTitle: null,
          source: null,
          justifications: null,
          demands: null,
          pendingProvider: false,
          ProviderName: "NA",
          pendingAssembly: false,
          assemblyName: "NA",
          pendingScriviner: false,
          scrivinerName: "NA",
          scriviner:null,
          comments:null,
          comments_land:null,
          privileged_observations:null,
          comments_deferment: null,
          privileged_observations_deferment:null,
          link: null,
          favorable:null,
        },
        owners: [],
        authoritysNames: [],    
        defereds: [{ text: 'Selecionar', value: null }, {text: 'Sim', value: true}, {text:'Não', value: false}],
        capitanias: [{ text: 'Selecione...', value: null, disabled: true}],
        landHistorys: listLandHistory,
        defermentForms:[{ text: 'Selecionar Tipo de Requerimento', value: null, disabled: true}, {text: 'Sim', value: true},  {text: 'Não', value: false}],
        requestTypes: [{ text: 'Selecionar Tipo de Requerimento', value: null, disabled: true}, 'Concessão', 'Confirmação', 'Não Encontrado'],
        same_measures: [{ text: 'Selecione...', value: null, disabled: true}, {text: 'Sim', value: true},  {text: 'Não', value: false}],
        areaTypes: ['Léguas Quadradas' , 'Braças Quadradas'],
        justifications:[],
        demands:[],
        just:[],
        deman:[],
        show: true,
        record_id: null,
        tramitations: null,
        deferment:null,
      }
    },
    watch: {
      search:function(val, oldVal){
        this._search()
        val;
        oldVal;
      }
    },
    mounted () {
      firebase.auth().onAuthStateChanged(user=>{
            console.log(user)
            if (user){
                this.nameuser = user.displayName
            } else{
                alert("Faça login para acessar essa página!!"); 
                window.location.href="/admin";
            }
        });
      axios.get(urlBase + 'captaincy/').then(res=>{
        res.data.forEach(
         (d)=>{
           this.capitanias.push({'text':d.name.toString(), 'value': d.id})
         }
        )      
      }).catch(erro=>{          
          console.log(erro)
      }),
      axios.get(urlBase+'justifications/').then(res=>{
      res.data.forEach(
         (d)=>{
           this.justifications.push({value: d.id, text: d.justification})
         }
        )
      }).catch(erro=>{          
          console.log(erro)
      }),
      axios.get(urlBase+'demands/').then(res=>{
      res.data.forEach(
         (d)=>{
           this.demands.push({text:d.demands, value:d.id})
         }
        )    
      }).catch(erro=>{          
          console.log(erro)
      }),
      axios.get(urlBase+'owner/').then(res=>{
      res.data.forEach(
         (d)=>{
           this.owners.push({text: d.name, value: d.id})
         }
        )    
      }).catch(erro=>{          
          console.log(erro)
      })
    },
    methods: {
      _search(){
        // this.justifications.map();
        if(this.search){
        return this.justifications.filter((item)=>{
          return item.text.startsWith(this.search);
        })
        }else{
          return this.justifications;
        }
      },
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
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      async authorityPost(){
          await axios.post(urlBase+'authority/',{
            "name": this.form.authority,
            "title": this.form.authorityTitle
          }
        ).then(res=>{
          this.form.authoritys.push(res.data.id)
          this.authoritysNames.push(res.data.name)
        }).catch(err=>{
          console.log(err)
        })
      },
      async submitPost(){
        this.form.demands.forEach(res => {
          this.deman.push(res.value);
        });
        this.form.justifications.forEach(res => {
          this.just.push(res.value);
        });
        console.log(this.deman)
        await axios.post(urlBase+'landrecord/',{
          "location": this.form.location,
          "nearest_river": this.form.nearest_river,
          "hectare_area": parseFloat(this.form.area),
          "type_area": this.form.areaType,
          "landHistory": this.form.landHistory,
          "comments": this.form.comments_land,
          "published": true,
          "captaincy": this.form.captaincy,
          "limits": []
        }).then(res=>{
          this.record_id = res.data.id
          console.log("record_id: " + res.data.id)
        }).catch(err=>{
          console.log(err)
        }),
        await axios.post(urlBase+'tramitations/', {
          "pendingProvider": this.form.pendingProvider,
          "ProviderName": this.form.ProviderName,
          "pendingAssembly": this.form.pendingAssembly,
          "assemblyName": this.form.assemblyName,
          "pendingScriviner": this.form.pendingScriviner,
          "scrivinerName": this.form.scrivinerName
        }).then(res=>{
          this.tramitations = res.data.id
          console.log("tramitations: " + res.data.id)
          console.log(Date.now())
        }).catch(err=>{
          console.log(err)
        }),
        await axios.post(urlBase+'deferment/', {
          "defered": this.form.defered,
          "favorable": this.form.favorable,
          "scriviner": this.form.scriviner,
          "dateRegister": "2020-12-31",
          "comments": this.form.comments_deferment,
          "privileged_observations": this.form.privileged_observations_deferment,
          "sources": this.form.source,
          "authority": this.form.authoritys,
          "tramitations": this.form.tramitations,
        }).then(res=>{
          this.deferment = res.data.id
          console.log("deferment: " + res.data.id)
        }).catch(err=>{
          console.log(err)
        }),
        console.log(this.form.reference, this.form.oldReference, this.form.dateRequest),
        console.log(this.form.dateConcession, this.form.dateConcession, this.form.same_measure),
        console.log(this.form.requestType, this.form.comments, this.form.privileged_observations),
        console.log(this.form.link, this.form.owners, this.form.justifications, this.form.demands),
        await axios.post(urlBase+'request/', {
          "reference": this.form.reference,
          "oldReference": this.form.oldReference,
          "dateRequest": this.form.dateRequest,
          "dateConcession": this.form.dateConcession,
          "same_measure": this.form.same_measure,
          "requestType": this.form.requestType,
          "comments": this.form.comments,
          "privileged_observations": this.form.privileged_observations,
          "link": this.form.link,
          "record_id": this.record_id,
          "deferment": this.deferment,
          "medias": [1],
          "files": [1],
          "owners": this.form.owners,
          "justification": this.just,
          "demands": this.deman,
        }).then(
        ).catch(err=>{
          console.log(err)
        })
      }      
    }
  }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
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