

$( document ).ready(function() {
    console.log("index.js");

    const updateButton = $('#update-button');
    if (updateButton.length) {
        updateButton.click(update);
    } else {
        prepareTotalUpdate();
    }
});


function updateTotal(index) {
    const transportationCostEl = $('#id_form-'+index+'-transportation_cost');
    const productionCostEl = $('#id_form-'+index+'-production_cost');
    const total = parseInt(transportationCostEl.val()) + parseInt(productionCostEl.val());

    const totalEl = productionCostEl.parent().siblings('.dynamic-total')[0];
    console.log(
        transportationCostEl.value,
        productionCostEl.attr('value'),
        totalEl
    )
    totalEl.innerText = total;
}

function prepareTotalUpdate() {
    const total = $('#id_form-TOTAL_FORMS').attr('value');

    for (let i = 0; i < total; i++) {
        let transportationCost = $('#id_form-'+i+'-transportation_cost');
        let productionCostEl = $('#id_form-'+i+'-production_cost');

        transportationCost.on('change', function (){
            updateTotal(i);
        });
        productionCostEl.on('change', function (){
            updateTotal(i);
        });
    }
}

function update() {
    $('#cancel-button').removeClass('hidden');
    $('#save-button').removeClass('hidden');

    $('#form-table').removeClass('readonly').addClass('editable');

    $(this).remove();
    prepareTotalUpdate();
}
