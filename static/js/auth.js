
let login = $("#login"),
password = $("#password")

class Authorization{
constructor(){
    this.APIAuthorization = "/api/v1/authorization";
}

authorize = async () => {
    return await Request.post(this.APIAuthorization , {
        "login" : login[0].value,
        "password" : password[0].value
    })
}
}

$("#auth").click(async (e)=>{
e.preventDefault();
let authorization = new Authorization();
let result = await authorization.authorize();
result = JSON.parse(result);
console.log(result);
if (result == 0){
    location.href="";
}else{
    console.log("Ошибка данных");
}
})