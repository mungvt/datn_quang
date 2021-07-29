
async function duDoan() {

    let data = {},
        flag = true
    fullLabel.forEach(label => {
        let idName = "#" + label,
            val = $(idName).val()
        data[label] = val ? parseFloat(val) : 0
        if (val === null || val === "")
            flag = false
    })

    if (flag) {
        let xhttp = new XMLHttpRequest();
        xhttp.onload = function () {
            let response = xhttp.responseText,
                kq = JSON.parse(response)
            $("#panelKetQua").show()
            let ketqua = $("#ketqua")
            ketqua.text(phanLop[kq])
            ketqua.css('color', mauSac[kq]);
        }
        xhttp.open('POST', '/dudoan', true);
        xhttp.setRequestHeader('Content-Type', 'application/json');
        xhttp.send(JSON.stringify(data));
    } else
        alert("Vui lòng nhập đầy đủ thông tin")

}

function loadLai() {
    labels.forEach(label => {
        let labelName = "#" + label,
            select = $(labelName)
        select.val(null)
    })
    $("#panelKetQua").hide()
}
