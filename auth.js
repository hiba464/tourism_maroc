window.onload = function () {

    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const name = document.getElementById("name");

    if (email) {
        email.value = "";
    }

    if (password) {
        password.value = "";
    }

    if (name) {
        name.value = "";
    }

};


console.log("Luxury Auth Loaded ✨");

const card = document.querySelector(".card");

if (card) {

    document.addEventListener("mousemove", (e) => {

        let x =
            (window.innerWidth / 2 - e.pageX) / 30;

        let y =
            (window.innerHeight / 2 - e.pageY) / 30;

        card.style.transform =
            `rotateY(${x}deg) rotateX(${-y}deg)`;

    });

}

// LOGIN
function login() {

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if(email === "" || password === ""){
        alert("Fill all fields");
        return;
    }

    fetch("http://127.0.0.1:5000/login",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            email:email,
            password:password
        })
    })

    .then(res => res.json())

    .then(data => {

        if(data.success){

            document.getElementById("email").value="";
            document.getElementById("password").value="";

           if(data.role === "admin"){

    window.location.href =
    "admin.html";

    }else{

    window.location.href =
    "index.html";

}

        }else{

            alert(data.message);

        }

    })

    .catch(err => {

        console.log(err);
        alert("Server Error");

    });

}


// REGISTER
function register(){

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if(name === "" || email === "" || password === ""){

        alert("Fill all fields");
        return;

    }

    fetch("http://127.0.0.1:5000/register",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            name:name,
            email:email,
            password:password

        })

    })

    .then(res => res.json())

    .then(data => {

        if(data.success){

            document.getElementById("name").value="";
            document.getElementById("email").value="";
            document.getElementById("password").value="";

            alert("Account Created Successfully");

            window.location.href="login.html";

        }else{

            alert(data.message);

        }

    })

    .catch(err => {

        console.log(err);
        alert("Server Error");

    });

}
