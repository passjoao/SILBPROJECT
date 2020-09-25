<template>
    <div class="formStyle">
      <h1 class="titleForm text-center">Adicionar Confirmação Régia</h1>
        <div>
            <b-form-group id="references" label="Sesmaria" label-for="reference-ipt">
                <b-form-select id="reference-ipt" v-model="form.request_id" :options="request" required search>
                </b-form-select>
              </b-form-group>

            <b-form-group id="register" label="Referência do registro" label-for="register-ipt">
                <b-form-select id="register-ipt" v-model="form.register" :options="registers" required search></b-form-select>
              </b-form-group>

            <b-form-group id date-conf label="Data de Confirmação" label-for="date-conf-ipt">
                <b-form-input id="date-conf-ipt" v-model="form.dateConfirmation" type="date" required ></b-form-input>
            </b-form-group>

            <b-form-checkbox id="concessionPresential-ipt" v-model="form.concessionPresential" name="concessionPresential-checkbox" true-value="Y" false-value="N">
                O requerimento da concessão está presente na carta de confirmação
            </b-form-checkbox>

            <b-form-checkbox id="concessionPresential-ipt" v-model="form.concessionPresential" name="concessionPresential-checkbox" true-value="Y" false-value="N">
                O requerimento da confirmação está presente na carta de confirmação
            </b-form-checkbox>

            <b-form-checkbox id="lisbon-ipt" v-model="form.confirmationLisbon" name="confirmationLisbon-checkbox" true-value="Y" false-value="N">
                A carta confirmada em lisboa foi registrada na capitania onde se localiza
            </b-form-checkbox>

            <b-form-checkbox id="concessionEqual-ipt" v-model="form.concessionEqual" name="concessionEqual-checkbox" true-value="Y" false-value="N">
                O requerimento da concessão é igual ao da confirmação
            </b-form-checkbox>

            <b-form-group id="kingName" label="Rei mencionado na carta" label-for="kingName" class="group">
                <b-form-input id="kingName" v-model="form.kingName" type="text" required placeholder="Nome do Rei"></b-form-input>
            </b-form-group>

            <b-form-group id="treasurerName" label="Tesoureiro" label-for="treasurerName" class="group">
                <b-form-input id="treasurerName" v-model="form.treasurerName" type="text" required placeholder="Nome do Tesoureiro"></b-form-input>
            </b-form-group>

            <b-form-group id="scrivener" label="Escrivão da carta de confirmação" label-for="scrivener" class="group">
                <b-form-input id="scrivener" v-model="form.scrivener" type="text" required placeholder="Nome do escrivão"></b-form-input>
            </b-form-group>

            <b-form-checkbox id="registerMeiasAnatas-ipt" v-model="form.registerMeiasAnatas" name="registerMeiasAnatas-checkbox" true-value="Y" false-value="N">
               Houve meias anatas?
            </b-form-checkbox>

            <b-form-group id="anatas" label="Valor cobrado da meias anatas" label-for="meiasAnatas" class="md-6">
                <b-form-input id="meiasAnatas" v-model="form.meiasAnatas" type="number" required placeholder="Meias Anatas"></b-form-input>
            </b-form-group>

            <b-form-group id="values" label="outros valores cobrados" label-for="meiasAnatas" class="md-6">
                <b-form-input id="otherValue" v-model="form.otherValue" type="number" required placeholder="outros valores"></b-form-input>
            </b-form-group>

            <b-form-group id="comments" label="Observações" label-for="comments-9">
                <b-form-textarea id="comments-9" v-model="form.comments" type="text" required placeholder="Observações"></b-form-textarea>
            </b-form-group>

            <b-button variant="primary" @click="submitPost">Enviar</b-button>
            <b-button type="reset" variant="danger">Cancelar</b-button>
        </div>
    </div>
</template>
<script>
import urlBase from '@/main.js'
const axios = require('axios')
export default {
    data() {
        return {
            selected:null,
            request: [],
            registers: [{text:"selecionar...", value:null, disabled: true}, "Chancelaria", "Registro Geral de Merces", "Conselho Ultramarino"],
            form:{
                dateConfirmation: null,
                confirmationLisbon: false,
                confirmationPresential: false,
                concessionPresential: false,
                concessionEqual: false,
                kingName: null,
                treasurerName: null,
                scrivener: null,
                register:null,
                registerMeiasAnatas: false,
                meiasAnatas: null,
                otherValue: null,
                comments: null,
                request_id: null
            }
        }
    },
    mounted() {
        axios.get(urlBase + 'request/').then(res=>{
        this.request.push({'text':"selecionar....", 'value': null, disabled:true}) 
        res.data.forEach(
         (d)=>{
           this.request.push({'text':d.reference.toString(), 'value': d.id})
         }
        )      
      }).catch(erro=>{          
          console.log(erro)
      })
    },
     methods: {
      async submitPost(){
        await axios.post(urlBase+'confirmation/',{
            "dateConfirmation": this.form.dateConfirmation,
            "confirmationLisbon": this.form.confirmationLisbon,
            "concessionPresential": this.form.concessionPresential,
            "concessionEqual": this.form.concessionEqual,
            "kingName": this.form.kingName,
            "treasurerName": this.form.treasurerName,
            "scrivener": this.form.scrivener,
            "register": this.form.register,
            "registerMeiasAnatas": this.form.registerMeiasAnatas,
            "meiasAnatas": this.form.meiasAnatas,
            "otherValue": this.form.otherValue,
            "comments": this.form.comments,
            "request_id": this.form.request_id
          }
        ).then(res=>{
          console.log(res.id)
        }).catch(err=>{
          console.log(err)
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
  .group{
      margin: 10px 0;
  }
</style>