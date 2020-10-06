<template>
	<div class="login">
	<form action="post">
    <p class="h4 text-center mb-4">Entrar na SILB</p>
    <label for="defaultFormLoginEmailEx" class="grey-text">E-mail:</label>
    <input type="text" id="defaultFormLoginEmailEx" class="form-control" placeholder="E-mail" v-model="email" />
    <br/>
    <label for="defaultFormLoginPasswordEx" class="grey-text">Senha:</label>
    <input type="password" id="defaultFormLoginPasswordEx" class="form-control" placeholder="Senha" v-model="senha" />
    <router-link to='/'>esqueceu a senha </router-link>
    <div class="text-center mt-4 blue">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" @click.prevent="login">Entrar</button>
    </div>
  </form>
  </div>
</template>

<script>
import firebase from "firebase";
	export default{
		name: "Login",
		data() {
			return {
				email: '',
				senha: '',
        erro:{"auth/wrong-password":"A senha é inválida ou o usuário não possui uma senha",
          "auth/invalid-email":"E-mail Invalido",
          "auth/user-not-found":"User Não Existe"
        }
			};
		},
		methods: {
      login () {
        return firebase.auth().signInWithEmailAndPassword(this.email,this.senha).then(
            ()=>{
              window.location.href="/dashboard";
            },
            err => {
              alert(this.erro[err.code]);
              console.log(err);
            }
        )
      }
    },
    mounted() {
    },  
			
		
	};
</script>

<style scoped>
	.login{
		margin: 30px auto;
		width: 500px;
	}
</style>