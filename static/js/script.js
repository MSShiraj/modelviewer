const form = document.querySelector("form"),
fileInput = form.querySelector("#file-input"),
progressArea=document.querySelector (".progress-area"),
uploadedArea=document.querySelector(".uploaded-area");

form.addEventListener("click", ()=>{
fileInput.click();
});

console.log("Just checking bruh...")
fileInput.onchange = ({target}) =>{
    let file = target.files[0]; 
    if(file){ //if file is selecte
        let fileName=file.name;
        console.log(fileName," from script");
    }
}
