<template>
    <div class="formulario">
        <b-form-group id="input-group-2" label="Nome completo:" label-for="input-2"> 
            <b-form-input id="input-2" v-model="name" required placeholder="Insira o nome..."></b-form-input>
      </b-form-group>
    
    <b-form-group id="input-group-4" label="Senha:" label-for="input-4"> 
           <b-form @submit.stop.prevent>
                <b-input type="password" id="password" v-model="password" aria-describedby="password-help-block" placeholder="Inisra a senha..."></b-input>
           </b-form>
       </b-form-group>

    <b-form-group id="input-group-5" label="Função:" label-for="input-5">              
        <b-form-select id="input-5" v-model="role" class="mb-2 mr-sm-2 mb-sm-0" :options="options" :value="null">
        </b-form-select>
      </b-form-group>

       <b-form-group id="input-group-6" label="Status:" label-for="input-6">
        <b-form-select id="input-6" v-model="status" class="mb-2 mr-sm-2 mb-sm-0" :options="statusOption" :value="null">
        </b-form-select>
      </b-form-group>

      <b-button-group>
          <b-button type="submit" variant="primary" @click.prevent="updateUser">enviar</b-button>
          <b-button type="reset" variant="danger" onclick="window.location.href='/dashboard'">Cancelar</b-button>
        </b-button-group>
    </div>
</template>

<script>
import firebase from 'firebase'
export default {
    data() {
        return {
            selected:null,
            name: null,
            password: null,
            role: null,
            status: null,
            options: [{text: 'selecionar...', value: null, disabled: true},'Pesquisador Jr','Pesquisador Snr', 'Bolsista', 'Coordenador', 'visitante'],
            statusOption: [{text:'selecionar...', value:null, disabled: true},'Ativo', 'inativo'],
            user: null,
        }
    },
    mounted() {
        this.user = firebase.auth().currentUser;
        console.log(this.user)
    },
    methods: {
        async updateUser(){
            console.log(this.user)
            await this.user.updateProfile({
                displayName: this.name,
                // password: this.password,
                // role: this.role,
                // status: this.status
            }).then(function() {
                alert("Cadastro atualizado com sucesso");
            }).catch(function(error) {
                console.log(error);
                console.log("aaaaaa")
            });
        }
    },
}
</script>