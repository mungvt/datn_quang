let labels = ['model'],
    fullLabel = ['thoi_tiet', 'csphat_olt', 'csthu_olt', 'csphat_tbc', 'csthu_tbc', 'sh_download', 'sh_upload', 'kc_tb', 'model'],
    phanLop = {0: "Tốt", 1: "Đạt", 2: "Kém"},
    mauSac = {0: "#4CAF50", 1: "#eedd08", 2: "#fc0000"};

$(document).ready(function () {
    loadDuLieu()
    loadTuongQuan()
});


function loadDuLieu() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function (evt) {
        let response = JSON.parse(xhttp.responseText)
        // document.getElementById("demo").innerHTML = this.responseText;
        labels.forEach(label => {
            let labelName = "#" + label,
                select = $(labelName)
            response[label].forEach(item => {
                select.append(new Option(item["value"], item["key"]))
            })
            // select.formSelect();
        })
    }
    xhttp.open("GET", "/getdata", true);
    xhttp.send();
}

function loadTuongQuan() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function (evt) {
        let response = JSON.parse(xhttp.responseText)
        let table = $("#tqTable")
        response.forEach((item,index) => {
            let row = `<tr><th scope="row">` + (index + 1) +  `</th><td>` + item.label + `</td><td>` + item.value + `</td></tr>`
            table.append(row)
            // select.formSelect();
        })
    }
    xhttp.open("GET", "/gettuongquan", true);
    xhttp.send();
}
