<template>
  <div id="app">
    <div id="nav">
      <nav class="flex items-center bg-white-500 navbar p-3 flex-wrap shadow">
        <a href="/" class="p-2 mr-4 inline-flex items-center">
          SILB
        </a>
        <button class="text-white flex-initial p-3 hover:bg-gray-900 rounded lg:hidden">
          <b-icon icon="list"  variant="secondary" >menu</b-icon>
        </button>
        <div class="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto" id="navigation">
          <div class="lg:inline-flex lg:flex-row lg:ml-auto">
            <a href="/banco" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Banco
              </span>
            </a>
            <a href="/equipe" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Equipe
              </span>
            </a>
            <a href="/contact" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Contato
              </span>
            </a>
            <a href="/legislacao" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Legislação
              </span>
            </a>
          </div>
        </div>
      </nav>
    </div>
    <div class="bg-gray-200">
        <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  //text-align: center;
  color: #2c3e50;
}
.nav{
    background-color:#fff;
}


#nav {
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
body{
  background-color: theme('colors.gray.200');
}
::-webkit-scrollbar-track
{
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  border-radius: 2px;
  background-color: #F5F5F5;
  height: 10px;
  cursor: grab;
}

::-webkit-scrollbar
{
  width: 2px;
  background-color: #F5F5F5;
  height: 10px;
  cursor: grab;
}

::-webkit-scrollbar-thumb
{
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
  background-color: theme('colors.gray.500');
  cursor: grab;
}
</style>
