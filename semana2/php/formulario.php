<?php

function preprocessa($entrada) {
    // remove espaços vazios
    $entrada = trim($entrada);
    // adiciona barras antes de caracteres que precisam ser escapados
    // como aspas simples, aspas duplas e barra invertida
    $entrada = addslashes($entrada);   
    return $entrada;
}

$dados = $_POST;

$nome = preprocessa($dados['nome']);
$idade = preprocessa($dados['idade']);
$telefone = preprocessa($dados['telefone']);

$mensagem = "<p>Nome: " . $nome . "</p><p>Idade: " . $idade . "</p><p>Telefone: " . $telefone . "</p>";
echo $mensagem;

?>