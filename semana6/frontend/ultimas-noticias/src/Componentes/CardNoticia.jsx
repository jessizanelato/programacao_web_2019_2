import React from 'react';

function CardNoticia(props) {
	return (		
		<div className="col-md-6">
			<div className="card flex-md-row mb-4 shadow-sm h-md-200">
				<div className="card-body d-flex flex-column align-items-start">
					<strong className="d-inline-block mb-2">{props.fonte}</strong>
					<h4 className="mb-0">
						{props.titulo}
					</h4>
					<small>{props.resumo}</small>
				</div>
			</div>
		</div>
	);
}

export default CardNoticia;