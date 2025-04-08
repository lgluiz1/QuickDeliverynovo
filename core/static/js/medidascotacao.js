
document.addEventListener("DOMContentLoaded", function () {
    const wrapper = document.querySelector("#formset-wrapper");
    const addBtn = document.getElementById("add-medida");
    

    addBtn.addEventListener("click", function () {
        const totalForms = document.getElementById("id_medidas-TOTAL_FORMS");
        const currentFormCount = parseInt(totalForms.value);
        const formItems = document.querySelectorAll(".formset-item");

        if (formItems.length === 0) return;

        const lastForm = formItems[formItems.length - 1];
        const newForm = lastForm.cloneNode(true);

        // Limpa os valores dos inputs clonados
        newForm.querySelectorAll("input").forEach(function (input) {
            input.value = "";
        });

        // Atualiza os atributos name e id
        newForm.querySelectorAll("input, label").forEach(function (el) {
            if (el.name) {
                el.name = el.name.replace(/medidas-(\d+)-/, `medidas-${currentFormCount}-`);
            }
            if (el.id) {
                el.id = el.id.replace(/id_medidas-(\d+)-/, `id_medidas-${currentFormCount}-`);
            }
            if (el.htmlFor) {
                el.htmlFor = el.htmlFor.replace(/id_medidas-(\d+)-/, `id_medidas-${currentFormCount}-`);
            }
        });

        wrapper.appendChild(newForm);
        totalForms.value = currentFormCount + 1;
    });

    // Remover medida
    wrapper.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-medida")) {
            const item = e.target.closest(".formset-item");
            item.remove();

            // Reorganiza os índices dos formulários restantes
            const totalForms = document.getElementById("id_medidas-TOTAL_FORMS");
            const items = wrapper.querySelectorAll(".formset-item");

            items.forEach((form, index) => {
                form.querySelectorAll("input, label").forEach(function (el) {
                    if (el.name) {
                        el.name = el.name.replace(/medidas-(\d+)-/, `medidas-${index}-`);
                    }
                    if (el.id) {
                        el.id = el.id.replace(/id_medidas-(\d+)-/, `id_medidas-${index}-`);
                    }
                    if (el.htmlFor) {
                        el.htmlFor = el.htmlFor.replace(/id_medidas-(\d+)-/, `id_medidas-${index}-`);
                    }
                });
            });

            totalForms.value = items.length;
        }
    });
});

