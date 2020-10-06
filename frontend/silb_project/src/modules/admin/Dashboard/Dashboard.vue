<template>
<div>
    <UsersFields>
        <UserName><UserLabel>Logado como: </UserLabel> {{nameuser}} </UserName>
        <UserMenu>
            <a href="/AtualizarUsuario"><ButtonUser>Perfil</ButtonUser></a>
            <a @click="logout"><ButtonUser>Sair</ButtonUser></a>
        </UserMenu>
    </UsersFields>
    <Content>
        <Tittle>BEM VINDOS À PLATAFORMA SILB ADMIN</Tittle>
        <div class="text-center">
        <ButtonGroup>
            <a href="/addsesmaria"><Button>+ Adicionar Sesmaria</Button></a>
            <a href="/addsesmeiro"><Button>+ Adicionar Sesmeiro</Button></a>
            <a href="/addconfirmacao"><Button>+ Adicionar Confirmação</Button></a>
        </ButtonGroup>
        </div>
        <Graphics>
            <GraphicsRow>
                <GraphicsCard>
                    <Subtitle>Sesmeiros adicionados</Subtitle>
                </GraphicsCard>
                <GraphicsCard>
                    <Subtitle>Sesmarias adicionadas</Subtitle>
                </GraphicsCard>
                <GraphicsCard>
                    <Subtitle>Confirmações adicionadas</Subtitle>
                </GraphicsCard>
            </GraphicsRow>
            <GraphicsRow>
            </GraphicsRow>
        </Graphics>
    </Content>
</div>
</template>

<script>
import firebase from 'firebase';
// import urlBase from '@/main.js';
// const axios = require('axios');
import {Button,Content,Tittle, ButtonGroup, GraphicsCard, Subtitle, Graphics, GraphicsRow, UsersFields, UserName, UserLabel, UserMenu, ButtonUser} from '@/modules/admin/Dashboard/style';
export default {
    name: "Dashboard",
    components:{
        Button,
        Content,
        Tittle,
        ButtonGroup,
        GraphicsCard,
        Subtitle,
        Graphics,
        GraphicsRow,
        UsersFields,
        UserName,
        UserLabel,
        UserMenu,
        ButtonUser,
    },
    data() {
        return {
            nameuser: null,
            table:{
                sesmarias: null,
            }
        }
    },
    mounted() {
        firebase.auth().onAuthStateChanged(user=>{
            console.log(user)
            if (user){
                this.nameuser = user.displayName
            } else{
                window.location.href="/admin";
            }
        });
    },
    methods: {
        logout(){
            firebase.auth().signOut().then(()=> {
                window.location.href="/";
            }).catch(function(error) {
                console.log(error)
            });            
        }
    },
}
</script>

<style scoped>
body, .app, template{
    background-color: aliceblue;
}
</style>