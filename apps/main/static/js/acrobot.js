const filtros = document.querySelector('#filtros')

function addFilter(filtro) {
    fetch(`static/filtros/${filtro}.html`)
    .then(response => response.text())
    .then(htmlString => {
        const parser = new DOMParser();
        const html = parser.parseFromString(htmlString, 'text/html');
        const elemento = html.body.firstChild;
        filtros.appendChild(elemento);
    });
};

function pessoasDict(){
    let pessoas = [];
    document.querySelectorAll('.pessoa').forEach((bloco) => {
        let pessoa = {
            vestimenta: {cor: null,estampa: null,tipo: null},
            tatuagem: {local: null},
            caracteristicasSomaticas: {cabelo: {tipo: null,cor: null,comprimento: null},estatura: null,compleicao: null,olhosCor: null}
        };
      
        bloco.querySelectorAll('input').forEach((input) => {
          if (input.id == 'vestimenta-cor') pessoa.vestimenta.cor = input.value;
          if (input.id == 'vestimenta-estampa') pessoa.vestimenta.estampa = input.value;
          if (input.id == 'vestimenta-tipo') pessoa.vestimenta.tipo = input.value;
          if (input.id == 'tatuagem-local') pessoa.tatuagem.local = input.value;
          if (input.id == 'cabelo-tipo') pessoa.caracteristicasSomaticas.cabelo.tipo = input.value;
          if (input.id == 'cabelo-cor') pessoa.caracteristicasSomaticas.cabelo.cor = input.value;
          if (input.id == 'cabelo-comprimento') pessoa.caracteristicasSomaticas.cabelo.comprimento = input.value;
          if (input.id == 'estatura') pessoa.caracteristicasSomaticas.estatura = input.value;
          if (input.id == 'compleicao') pessoa.caracteristicasSomaticas.compleicao = input.value;
          if (input.id == 'olhos-cor') pessoa.caracteristicasSomaticas.olhosCor = input.value;
        });

        pessoas.push(pessoa);
    })
    return pessoas
}

function veiculosDict(){
    let veiculos = [];
    document.querySelectorAll('.veiculo').forEach((bloco) => {
        let veiculo = {cor: null,modelo: null,marca: null,tipo: null,placa: null};

        bloco.querySelectorAll('input').forEach((input) => {
            if (input.id == 'veiculo-cor') veiculo.cor = input.value;
            if (input.id == 'veiculo-modelo') veiculo.modelo = input.value;
            if (input.id == 'veiculo-marca') veiculo.marca = input.value;
            if (input.id == 'veiculo-tipo') veiculo.tipo = input.value;
            if (input.id == 'veiculo-placa') veiculo.placa = input.value;
        });

        veiculos.push(veiculo);
    })
    return veiculos
}

function localidadesDict(){
    let localidades = [];
    document.querySelectorAll('.localidade').forEach((bloco) => {
        let localidade = {risp: null,municipio: null,distrito: null,aisp: null,bairro: null};
        bloco.querySelectorAll('input').forEach((input) => {
          if (input.id == 'localidade-risp') localidade.risp = input.value;
          if (input.id == 'localidade-municipio') localidade.municipio = input.value;
          if (input.id == 'localidade-distrito') localidade.distrito = input.value;
          if (input.id == 'localidade-aisp') localidade.aisp = input.value;
          if (input.id == 'localidade-bairro') localidade.bairro = input.value;
        });
      
        localidades.push(localidade);
    });
    return localidades
}

function boletimDict(){
    let boletim = {dataFato: null,dataRegistro: null,registro: null,relato: null};
    document.querySelector('.boletim').querySelectorAll('input').forEach((input) => {
          if (input.id == 'data-fato') boletim.dataFato = input.value;
          if (input.id == 'data-registro') boletim.dataRegistro = input.value;
          if (input.id == 'registro') boletim.registro = input.value;
          if (input.id == 'relato') boletim.relato = input.value;
    });
    return boletim
}

function enviarJSON() {
    boletim = boletimDict()
    pessoas = pessoasDict()
    veiculos = veiculosDict()
    localidades = localidadesDict()

    
    let json = {
        boletim:boletim,
        pessoas: pessoas,
        veiculos: veiculos,
        localidades: localidades
    };

    let token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    fetch("/resultado/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: `csrfmiddlewaretoken=${token}&data=${JSON.stringify(json)}`
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}
