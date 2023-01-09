// Create a simple RESTFul API

//Simple RESTful API
function startPSO() {
    let mode = document.getElementById('mode').value;
    let data = {
        mode: mode
    };

    fetch('http://localhost:5000/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then((res) => {
        return res.text();
    })
    .then((text) => {
    }
}