<template>
  <div class="content">
    <div class="inline-flex buttons">
    <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-l">
      Imagens
    </button>
    <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r">
      Documentos
    </button>
    <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded-r">
      Download
    </button>
  </div>
    <table class="table-auto">
    <td colspan="2" class="text-center bg-gray-100 font-bold">Sesmaria</td>
    <tr>
      <td class="border px-4 py-2">Referência</td>
      <td class="border px-4 py-2">RN 0000</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Referência antiga <span> <br>referência da sesmaria da antoga SILB</span></td>
      <td class="border px-4 py-2">RN 0000</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Localização</td>
      <td class="border px-4 py-2">{{location}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Ribeira</td>
      <td class="border px-4 py-2">{{nearest_river}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Área (em hectáres)</td>
      <td class="border px-4 py-2">{{hectare_area}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Histórico da terra</td>
      <td class="border px-4 py-2">{{landHistory}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Tipo de terra</td>
      <td class="border px-4 py-2">{{land_record_type}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Capitania</td>
      <td class="border px-4 py-2">{{captaincy}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Limitantes</td>
      <td class="border px-4 py-2">{{limits}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Comentários</td>
      <td class="border px-4 py-2">{{comments}}</td>
    </tr>
   <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Sesmeiros{{owner}}</td>
    </tr>
    <!-- um for para cada sesmeiro -->
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Nome</td>
      <td class="border px-4 py-2">{{name}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Sexo</td>
      <td class="border px-4 py-2">{{gender}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Nome do cônjuge</td>
      <td class="border px-4 py-2">{{spouse_name}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Índigena</td>
      <td class="border px-4 py-2">{{indian}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Ocupação</td>
      <td class="border px-4 py-2">{{occupation}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Capitania em que reside</td>
      <td class="border px-4 py-2">{{captaincy_resident_name}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Estado civíl</td>
      <td class="border px-4 py-2">{{matrialStatus}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Clero secular</td>
      <td class="border px-4 py-2">{{secular_clergy}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Clero regular</td>
      <td class="border px-4 py-2">{{regular_clergy}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Ordem Religiosa</td>
      <td class="border px-4 py-2">{{religious_order}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Comentários</td>
      <td class="border px-4 py-2">{{comments}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Requisição</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Data da requisição</td>
      <td class="border px-4 py-2">{{dateRequest}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Solicitou divisão igualitária</td>
      <td class="border px-4 py-2">{{same_measure}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Referência</td>
      <td class="border px-4 py-2">{{record_id}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">link</td>
      <td class="border px-4 py-2">{{link}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">comentários</td>
      <td class="border px-4 py-2">{{privileged_observations}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Confirmação</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Data de confirmação</td>
      <td class="border px-4 py-2">{{dateConfirmation}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Data de concessão</td>
      <td class="border px-4 py-2">{{dateConcession}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Confirmada em Lisboa</td>
      <td class="border px-4 py-2">{{confirmationLisbon}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Confirmação presencial</td>
      <td class="border px-4 py-2">{{concessionPresential}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Concessão igualitária</td>
      <td class="border px-4 py-2">{{concessionEqual}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Nome do rei</td>
      <td class="border px-4 py-2">{{kingName}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Nome do tesoureiro</td>
      <td class="border px-4 py-2">{{treasurerName}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Escrivão</td>
      <td class="border px-4 py-2">{{scrivener}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Registro geral de merces</td>
      <td class="border px-4 py-2">generalRegisterMercesgeneralRegisterMercesgeneralRegisterMercesgeneralRegisterMerces</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Registro de meias anatas</td>
      <td class="border px-4 py-2">{{registerMeiasAnatas}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Meias Anatas valor</td>
      <td class="border px-4 py-2">{{meiasAnatas}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2">Outros valores</td>
      <td class="border px-4 py-2">{{otherValue}}</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Comentários</td>
      <td class="border px-4 py-2">{{comments}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Tramitações</td>
    </tr>

    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Passou por provedor</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>
    
    <tr>
      <td class="border px-4 py-2">Nome do provedor</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Passou pela câmara</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Nome do camarário</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Passou por escrivão</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Nome do escrivão</td>
      <td class="border px-4 py-2">{{pendingProvider}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Justificativa</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Justificativas</td>
      <td class="border px-4 py-2">{{justification}}</td>
    </tr>

    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Exigências</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Exigências</td>
      <td class="border px-4 py-2">{{demands}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2 text-center font-bold" colspan="2">Deferimento</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Foi deferido</td>
      <td class="border px-4 py-2">{{defered}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Deferimento favorável</td>
      <td class="border px-4 py-2">{{favorable}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Escrivão do deferimento</td>
      <td class="border px-4 py-2">{{scriviner}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Data do registro</td>
      <td class="border px-4 py-2">{{dateRegister}}</td>
    </tr>
    <tr class="bg-gray-100">
      <td class="border px-4 py-2">Fonte</td>
      <td class="border px-4 py-2">{{sources}}</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Autoridade</td>
      <td class="border px-4 py-2">{{authority}}</td>
    </tr>

</table>
</div>
</template>

<script>

</script>

<style scoped>
.content{
    margin: 30px auto;
}
.table-auto{
    margin: 0 auto;
}

.modal {
    transition: opacity 0.25s ease;
}
body.modal-active {
    overflow-x: hidden;
    overflow-y: visible !important;
}
.buttons{
    margin: 10px a;
    padding: 10px;
}
</style>