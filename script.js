function sendGuess(){

let guess = document.getElementById("guessInput").value;

fetch("/guess", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({guess: guess})
})
.then(res => res.json())
.then(data => {

let msg = document.getElementById("message");

if(data.result === "low"){
msg.innerText = "Too low ⬇️";
msg.style.color = "blue";
}
else if(data.result === "high"){
msg.innerText = "Too high ⬆️";
msg.style.color = "red";
}
else{
msg.innerText = "🎉 Correct!";
msg.style.color = "green";
}

});
}