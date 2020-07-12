<template>
  <div id="app">
    <div id="nav">
      <nav class="flex items-center bg-gray-600 p-3 flex-wrap">
        <a href="" class="p-2 mr-4 inline-flex items-center">
          SILB
        </a>
        <button class="text-white flex-initial p-3 hover:bg-gray-900 rounded lg:hidden">
          <b-icon icon="list"  variant="secondary" >menu</b-icon>
        </button>
        <div class="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto" id="navigation">
          <div class="lg:inline-flex lg:flex-row lg:ml-auto">
            <a href="" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Banco
              </span>
            </a>
            <a href="" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Sobre
              </span>
            </a>
            <a href="" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-400">
              <span>
                Contato
              </span>
            </a>
          </div>
        </div>
      </nav>
    </div>
    <router-view/>
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

#nav {
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
