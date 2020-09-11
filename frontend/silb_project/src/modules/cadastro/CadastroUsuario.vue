<template>
  <div class="formulario">
      <!-- <form>
        <input type="text" v-model="email">
        <input type="password" v-model="password">
        <button @click.prevent="createUser">enviar</button>
      </form>
      {{email}}
      {{password}} -->
    <b-form>
      <b-form-group
        id="input-group-1"
        label="Endereço de e-mail:"
        label-for="input-1"

      >
        <b-form-input
          id="email"
          v-model="email"
          type="text"
          required
          placeholder="Insira o e-mail..."
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Nome completo:"
        label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="name"
              required
              placeholder="Insira o nome..."
            ></b-form-input>
      </b-form-group>

    <b-form-group
        id="input-group-4"
        label="Senha:"
        label-for="input-4">
           <b-form @submit.stop.prevent>
            <b-input
                type="password"
                id="password"
                v-model="password"
                aria-describedby="password-help-block"
                placeholder="Inisra a senha..."></b-input>
           </b-form>
       </b-form-group>


        <b-form-group
        id="input-group-5"
        label="Função:"
        label-for="input-5"

      >
                <!-- <b-form-select id="input-12" v-model="form.defermentForm" :options="defermentForms" required></b-form-select> -->
              
        <b-form-select
          id="input-5"
          v-model="role"
          class="mb-2 mr-sm-2 mb-sm-0"
          :options="options"
          :value="null"
        ></b-form-select>
      </b-form-group>

       <b-form-group
        id="input-group-6"
        label="Status:"
        label-for="input-6"

      >
        <b-form-select
          id="input-6"
          v-model="status"
          class="mb-2 mr-sm-2 mb-sm-0"
          :options="statusOption"
          :value="null"
        ></b-form-select>
      </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary" @click.prevent="createUser">enviar</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
    </b-form>

    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card> -->
  </div>
</template>
<script>
import firebase from "firebase";

  export default {
    data() {
      return {
          email: '',
          name: '',
          password: '',
          role: null,
          status: null,
        options: [{text: 'selecionar...', value: null},'Pesquisador Jr','Pesquisador Snr', 'Bolsista', 'Coordenador', 'visitante'],
        statusOption: [{text:'selecionar...', value:null},'Ativo', 'inativo'],
        show: true
      }
    },
    methods: {
      createUser () {
        return firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
        .then(
          (user)=>{
            if(user){
              console.log(user)
              user.updateProfile({
                displayName: this.name,
                role: this.role,
                status: this.status,
              })
            }
        })
        .catch(function(error) {
            console.log(error)
            alert(error)
          }
        )
      }
    },
  }
</script>
<style>
    .formulario{
        width: 700px;
        margin: 0 auto;
        margin-top: 10px;
    }
</style>