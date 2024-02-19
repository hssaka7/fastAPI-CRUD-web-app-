console.log("Form test")
const form = document.getElementById('sign-in');

function sendData(){
    console.log(form)
    const form_data = new FormData(form);

    for (let [key, value] of form_data.entries()) { 
        console.log(key, value);
    }
      
    console.log(form_data.get('username'))
    console.log(form_data)
}


form.addEventListener('submit', (event)=>{
    event.preventDefault()
    console.log("Button pressed");
    sendData()
})