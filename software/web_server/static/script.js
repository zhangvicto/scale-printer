// Create a simple RESTFul API

//Simple RESTful API
function startPSO() {
    let mode = document.getElementById('mode').value;
    let numIterations = document.getElementById('numIterations').value;
    let tempE = document.getElementById('tempE').value;
    let tempB = document.getElementById('tempB').value;

    let data = {
        mode: mode,
        numIterations: numIterations,
        tempE: tempE,
        tempB: tempB,
        psoCommand: start
    };

    fetch('http://localhost:5000/api/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    .then((res) => {
        return res.text()
    })
    .then((text) => {
        console.log(text)
    }
}