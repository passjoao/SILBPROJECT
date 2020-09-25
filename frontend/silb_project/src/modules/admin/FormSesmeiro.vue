<template>
    <div class="formStyle">
      <h1 class="titleForm text-center">Adicionar Novo Sesmeiro</h1>
          <div>              
            <b-form-group id="name" label="Nome do Sesmeiro" label-for="nome-ipt">
                <b-form-input id="nome-ipt" v-model="form.name" type="text" required placeholder="Nome"></b-form-input>
            </b-form-group>

            <b-form-group id="original_name" label="Nome original do Sesmeiro" label-for="original_name-ipt">
                <b-form-input id="original_name-ipt" v-model="form.original_name" type="text" required placeholder="Nome original"></b-form-input>
            </b-form-group>

            <b-form-group id="spouse_name" label="Nome do conjuge" label-for="spouse_name-ipt">
                <b-form-input id="spouse_name-ipt" v-model="form.spouse_name" type="text" required placeholder="Nome do conjuge"></b-form-input>
            </b-form-group>

            <b-form-group id="gender" label="Sexo" label-for="gender-ipt">
                <b-form-select id="gender-ipt" v-model="form.gender" :options="this.genders" required></b-form-select>
            </b-form-group>

            <b-form-group id="occupation" label="Ocupação" label-for="occupation-ipt">
                <b-form-input id="occupation-ipt" v-model="form.occupation" type="text" required placeholder="Ocupação"></b-form-input>
            </b-form-group>
            
            <b-form-checkbox id="indian-ipt" v-model="form.indian" name="indian-checkbox" value="true" unchecked-value="false">
                Indigena
            </b-form-checkbox>
            
            <b-form-checkbox id="captaincy_resident-ipt" v-model="form.captaincy_resident" name="captaincy_resident-checkbox" value="true" unchecked-value="false">
                Reside na capitania
            </b-form-checkbox>

            <b-form-group id="captaincy_resident_name" label="Capitanias:" label-for="captaincy_resident_name-ipt">
                <b-form-select v-model="form.captaincy_resident_name" :options="this.capitanias"></b-form-select>
            </b-form-group>

            <b-form-group id="matrialStatus" label="Estado civil" label-for="matrialStatus-ipt">
                <b-form-select id="matrialStatus-ipt" v-model="form.matrialStatus" :options="this.listMatrialStatus" required></b-form-select>
            </b-form-group>
            
            <b-form-checkbox id="secular_clergy-ipt" v-model="form.secular_clergy" name="secular_clergy-checkbox" value="true" unchecked-value="false">
                Clero secular
            </b-form-checkbox>

            <b-form-checkbox id="regular_clergy-ipt" v-model="form.regular_clergy" name="regular_clergy-checkbox" value="true" unchecked-value="false">
                Clero regular
            </b-form-checkbox>

            <b-form-group id="religiousorder" label="Ordem Religiosa:" label-for="religiousorder-ipt">
                <b-form-select v-model="form.religious_order" :options="this.religiousorders">
                </b-form-select>
            </b-form-group>

            <b-form-group id="comments" label="Comentário" label-for="comments-ipt">
                <b-form-input id="comments-ipt" v-model="form.comments" type="text" required placeholder="Comentário"></b-form-input>
            </b-form-group>

            <b-form-group id="privileged_observations" label="Observações privilegiadas" label-for="privileged_observations-ipt">
                <b-form-input id="privileged_observations-ipt" v-model="form.privileged_observations" type="text" required placeholder="Observações privilegiadas"></b-form-input>
            </b-form-group>   
          </div>
        <b-button variant="primary" @click="ownerPost">Enviar</b-button>
        <b-button type="reset" variant="danger">Cancelar</b-button>
  
    </div>    
</template>

<script>
import urlBase from '@/main.js'
const axios = require('axios')
export default {
    data() {
        return {
            options:[],
            selected: null,
            form:{
                name: null,
                original_name: null,
                spouse_name: null,
                gender: null,
                occupation: null,
                indian: false,
                captaincy_resident: false,
                matrialStatus: null,
                secular_clergy: false,
                regular_clergy: false,
                comments: null,
                privileged_observations: null,
                captaincy_resident_name: null,
                religious_order: null,
            },
            genders: [{text: 'Selecionar', value: null, disabled: true}, {text: 'Homem', value: 'MALE'}, {text: 'Mulher', value: 'FEMALE'} ,  {text: 'NA', value: 'NA'}],
            listMatrialStatus: [{text: 'Selecionar', value: null, disabled: true}, {value:'CASADO', text:'Casado'}, {value: 'SOLTEIRO', text: 'Solteiro'}, {value: 'VIUVO', text: 'Viúvo'}],
            capitanias: [{ text: 'Selecione...', value: null, disabled: true}],
            religiousorders: [{ text: 'Selecione...', value: null, disabled: true}],
        }
    },
    mounted () {
      axios.get(urlBase + 'captaincy/').then(res=>{
        res.data.forEach(
         (d)=>{
           this.capitanias.push({'text':d.name.toString(), 'value': d.id})
         }
        )
        console.log(this.capitanias)       
      }).catch(erro=>{          
          console.log(erro)
      }),
      axios.get(urlBase + 'religiousorder/').then(res=>{
        res.data.forEach(
         (d)=>{
           this.religiousorders.push({'text':d.name.toString(), 'value': d.id})
         }
        )
        console.log(this.capitanias)       
      }).catch(erro=>{          
          console.log(erro)
      })
    },
    methods: {
        async ownerPost() {
            await axios.post(urlBase+'owner/',{
                "name": this.form.name,
                "original_name": this.form.original_name,
                "spouse_name": this.form.spouse_name,
                "gender": this.form.gender,
                "occupation": this.form.occupation,
                "indian": this.form.indian,
                "captaincy_resident": this.form.captaincy_resident,
                "matrialStatus": this.form.matrialStatus,
                "secular_clergy": this.form.secular_clergy,
                "regular_clergy": this.form.regular_clergy,
                "comments": this.form.comments,
                "privileged_observations": this.form.privileged_observations,
                "captaincy_resident_name": this.form.captaincy_resident_name,
                "religious_order": this.form.religious_order
            }).then(res=>{
              alert("Sesmeiro adicionado com sucesso!!" + res.data.name)
            })
            .catch(erro=>{      
                console.log(this.form)    
                console.log(erro)
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