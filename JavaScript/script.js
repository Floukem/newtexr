// Inicializa EmailJS
emailjs.init({
    publicKey: "azDURjcyHJTjdLjye",
});

// Captura o submit do formulário
document.getElementById("meuForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Coleta os dados do formulário
    const formData = {
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value
    };

    console.table(formData);

    const serviceID = "service_6f7s3vc";
    const templateID = "template_jkps4ko";

    // Envia o e-mail
    emailjs.send(serviceID, templateID, formData)
        .then(function(response) {
            console.log("E-mail enviado com sucesso!", response.status, response.text);
            document.getElementById("status").innerText = "E-mail enviado com sucesso!";
        })
        .catch(function(error) {
            console.error("Erro ao enviar e-mail:", error);
            document.getElementById("status").innerText = "Erro ao enviar o e-mail.";
        });
});
