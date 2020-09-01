<template>
	<div class="login">
	<form>
    <p class="h4 text-center mb-4">Entrar na SILB</p>
    <label for="defaultFormLoginEmailEx" class="grey-text">E-mail:</label>
    <input type="email" id="defaultFormLoginEmailEx" class="form-control" placeholder="E-mail" v-model="email" />
    <br/>
    <label for="defaultFormLoginPasswordEx" class="grey-text">Senha:</label>
    <input type="password" id="defaultFormLoginPasswordEx" class="form-control" placeholder="Senha" v-model="senha" />
    <router-link to='/'>esqueceu a senha </router-link>
    <div class="text-center mt-4 blue">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" @click="login">Entrar</button>
    </div>
  </form>
  </div>
</template>

<script>
	
	export default{
		name: "login",
		data() {
			return {
				email: '',
				senha: ''
			};
		},
		methods: {
		}
			
		
	};
</script>

<style scoped>
	.login{
		margin: 30px auto;
		width: 500px;
	}
</style>