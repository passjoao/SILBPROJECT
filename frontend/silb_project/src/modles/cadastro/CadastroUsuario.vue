<template>
  <div class="formulario">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Endereço de e-mail:"
        label-for="input-1"

      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
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
              v-model="form.name"
              required
              placeholder="Insira o nome..."
            ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Usuário:"
        label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.user"
              type="text"
              required
              placeholder="Insira o nome de usuário..."
            ></b-form-input>
      </b-form-group>

    <b-form-group
        id="input-group-4"
        label="Senha:"
        label-for="input-4">
           <b-form @submit.stop.prevent>
            <b-input
                type="password"
                id="input-4"
                v-model="form.password"
                aria-describedby="password-help-block"
                placeholder="Inisra a senha..."></b-input>
           </b-form>
       </b-form-group>


        <b-form-group
        id="input-group-5"
        label="Função:"
        label-for="input-5"

      >
        <b-form-select
          id="input-5"
          v-model="form.role"
          class="mb-2 mr-sm-2 mb-sm-0"
          :options="[{ text: 'Escolha uma função...', value: null }]"
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
          v-model="form.status"
          class="mb-2 mr-sm-2 mb-sm-0"
          :statusOption="[{ text: 'Status do usuário...', value: null }]"
          :value="null"
        ></b-form-select>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card> -->
  </div>
</template>
<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          user: '',
          password: '',
          role: null,
          status: null
        },
        options: ['Pesquisador Jr','Pesquisador Snr', 'Bolsista', 'Coordenador', 'visitante'],
        statusOption: ['Ativo', 'inativo'],
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.user = ''
        this.form.password = ''
        this.form.role = null
        this.form.status = null
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>
<style>
    .formulario{
        width: 700px;
        margin: 0 auto;
    }
</style>