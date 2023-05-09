
let nam = $("#name"),
    price = $("#price"),
    manufacturer = $("#manufacturer"),
    date = $("#date"),
    cpu = $("#cpu"),
    sdd = $("#sdd"),
    ram = $("#ram"),
    gpu = $("#gpu");

class Computering{
constructor(){
    this.APIComputering = "/api/v1/computering";
}

compit = async () => {
    return await Request.post(this.APIComputering, {
        "name" : nam[0].value,
        "price" : price[0].value,
        "manufacturer" : manufacturer[0].value,
        "date" : date[0].value,
        "cpu" : cpu[0].value,
        "sdd" : sdd[0].value,
        "ram" : ram[0].value,
        "gpu" : gpu[0].value,
    })
}
}

$("#comp").click(async (e)=>{
e.preventDefault();
let computering = new Computering();
let result = await computering.compit();
result = JSON.parse(result);
console.log(result);
if (result == 0){
    location.href="";
}else{
    console.log("Ошибка данных");
}
})