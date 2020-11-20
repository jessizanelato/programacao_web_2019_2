import React from 'react';
import Topo from './Componentes/Topo'
import Menu from './Componentes/Menu'
import Noticias from './Componentes/Noticias'

function Principal(props) {

	// Categorias a serem apresentadas no menu
	const categorias = [
		{'url': 'geral', 'nome': 'Geral'}, 
		{'url': 'tecnologia', 'nome': 'Tecnologia'},
		{'url': 'saude', 'nome': 'Saúde'},
		{'url': 'negocios', 'nome': 'Negócios'},
		{'url': 'entretenimento', 'nome': 'Entretenimento'},
		{'url': 'esportes', 'nome': 'Esportes'}
	];

	// define a variável categoria ativa
	let categoriaAtiva;
	
	// checa se a categoria da url é diferente de undefined, 
	// se for a define como a categoria ativa
	if(typeof props.match.params.categoria !== 'undefined'){
		categoriaAtiva = props.match.params.categoria;
	} else {
		categoriaAtiva = 'geral';
	}

	return (
		<div class="container">
			<Topo titulo={'Últimas Notícias'} logo={'/logo192.png'} />
			<Menu categorias={categorias} categoriaAtiva={categoriaAtiva}></Menu>
			<Noticias categoriaAtiva={categoriaAtiva}></Noticias>
		</div>
	);
}

export default Principal;
