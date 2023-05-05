
let login = $("#login"),
email= $("#email"),
password = $("#password"),
rpassword = $("#rpassword");

class Registration{
constructor(){
    this.APIRegistration = "/api/v1/registration";
}

registrate = async () => {
    return await Request.post(this.APIRegistration, {
        "login" : login[0].value,
        "email" : email[0].value,
        "password" : password[0].value,
        "rpassword" : rpassword[0].value,
    })
}
}

$("#reg").click(async (e)=>{
e.preventDefault();
let registration = new Registration();
let result = await registration.registrate();
result = JSON.parse(result);
console.log(result);
if (result == 0){
    location.href="";
}else{
    console.log("Ошибка данных");
}
})