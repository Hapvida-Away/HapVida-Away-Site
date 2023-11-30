
function enviar(){
    
    let nome = document.getElementById('nome').value;
    let email = document.getElementById('email').value;

    if(nome == '' || email == ''){
        alert("Por favor preencha com seus dados !")
    }else{
        document.getElementById("nome").innerText = ""
        document.getElementById("email").innerText = ""
        alert("Agradecemos o contato!")  
    }
}
