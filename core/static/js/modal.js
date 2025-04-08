document.addEventListener("DOMContentLoaded", function () {
    const abrirModais = document.querySelectorAll(".cotacao-botao"); // Seleciona TODOS os botões
    const fecharModal = document.querySelector(".modal-cotacao-close"); // Botão de fechar
    const modal = document.querySelector(".modal-cotacao"); // Modal único

    abrirModais.forEach(botao => {
        botao.addEventListener("click", function () {
            modal.classList.add("ativo"); // Adiciona classe para exibir modal
        });
    });

    fecharModal.addEventListener("click", function () {
        modal.classList.remove("ativo"); // Remove classe para esconder modal
    });
});


