<template>
  <div class="formulario">
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


        
        <b-button-group>
          <b-button type="submit" variant="primary" @click.prevent="createUser">enviar</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
    </b-form>
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