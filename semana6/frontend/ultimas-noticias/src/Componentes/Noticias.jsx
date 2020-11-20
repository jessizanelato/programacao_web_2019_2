import React, { Component } from 'react';
import axios from 'axios';
import CardNoticia from './CardNoticia';

class Noticias extends Component {
    constructor(){
		super();
		
		// endereço da API
		this.urlAPI = 'http://localhost:8000/api/';
        this.state = {
            noticias: []
        }
        this.style = {
            corNomeOrigemNoticia: "#8DB5E9"
        }
    }

	// método principal que faz a chamada na API e define o estado das notícias
    definirNoticias(){
        // axios.get(this.urlAPI + this.props.categoriaAtiva)
        let url = this.urlAPI + 'artigos/?categoria=' + this.props.categoriaAtiva
        axios.get(url, {auth: {username: 'admin', password: 'admin123'}})
		.then(response => {
			this.setState({ noticias: response.data });
		})
		.catch(error => {
			console.log(error)
		})
    }	
	// método chamado quando o componente termina de atualizar (clique no link)
    componentDidUpdate(prevProps) {
        if(prevProps.categoriaAtiva !== this.props.categoriaAtiva){
            this.definirNoticias();
        }
	}
	// método chamado no carregamento da página (refresh)
    componentDidMount() {
        this.definirNoticias();
    }
    render() {
        if(this.state.noticias.length){
			return (<div className="row mb-2">
				{this.state.noticias.map((noticia, i) => (
					<CardNoticia key={i} titulo={noticia.titulo} fonte={noticia.fonte} resumo={noticia.resumo}></CardNoticia>
				))}
				</div>);
        }else{
            return (<div>Não há notícias nessa categoria.</div>);
        }
    }

}

export default Noticias;