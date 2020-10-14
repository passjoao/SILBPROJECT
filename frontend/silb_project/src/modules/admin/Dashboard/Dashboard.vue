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
        {{table.captaincy}}
        <Graphics>
            <GraphicsRow>
                <GraphicsCard>
                    <Subtitle>Sesmarias adicionados</Subtitle>
                    <table>
                        <thead class="thead-dark">
                            <tr>
                                <th>Capitania</th>
                                <th>Quantidade</th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr v-for="sesmaria in table.sesmarias" :key="sesmaria.id">
                            <td>{{sesmaria.location}}</td>
                            <td>{{sesmaria.captaincy}}</td>
                        </tr>
                        </tbody>
                    </table>
                </GraphicsCard>
                <GraphicsCard>
                    <Subtitle>Sesmeiros adicionados</Subtitle>
                    <table>
                        <thead class="thead-dark">
                            <tr>
                                <th>Capitania</th>
                                <th>Quantidade</th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr v-for="confi in table.sesmeiros" :key="confi.id">
                            <td>{{confi.name}}</td>
                            <td>{{confi.location}}</td>
                        </tr>
                        </tbody>
                    </table>
                </GraphicsCard>
                <GraphicsCard>
                    <Subtitle>Confirmações adicionadas</Subtitle>
                    <table>
                        <thead class="thead-dark">
                            <tr>
                                <th>Capitania</th>
                                <th>Quantidade</th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr v-for="confi in table.confirmacoes" :key="confi.id">
                            <td>{{confi.confirmationReference}}</td>
                            <td>{{confi.location}}</td>
                        </tr>
                        </tbody>
                    </table>
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
import urlBase from '@/main.js';
const axios = require('axios');
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
                sesmarias: [],
                sesmeiros: [],
                confirmacoes: [],
                captaincy: [],
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
        //importando as Sesmarias
        axios.get(urlBase+'landrecord/').then(res=>{
        res.data.forEach(
            (d)=>{
            this.table.sesmarias.push(d)
            }
            )
        }).catch(erro=>{          
            console.log(erro)
        });
        axios.get(urlBase+'captaincy/').then(res=>{
        res.data.forEach(
            (d)=>{
            this.table.captaincy.push(d)
            }
            )
        }).catch(erro=>{          
            console.log(erro)
        });

        //importando os sesmeiros
        axios.get(urlBase+'owner/').then(res=>{
        res.data.forEach(
            (d)=>{
            this.table.sesmeiros.push(d)
            }
            )    
        }).catch(erro=>{          
            console.log(erro)
        });
        //importando as confirmações
        axios.get(urlBase+'confirmation/').then(res=>{
        res.data.forEach(
            (d)=>{
            this.table.confirmacoes.push(d)
            }
            )    
        }).catch(erro=>{          
            console.log(erro)
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
table{
    width: 90%;
    margin: 0 auto;
}
th{
    text-align: center;
}
td{
    text-align: center;
    margin: auto;
    border: solid 1px;
}
</style>