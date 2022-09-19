export function httpRequest(path){
    const root = "http://127.0.0.1:8000/api/v1/"
    let data =  fetch(root+path).then(data => data.json())
    return data
}
export function httpPostRequest(path,data){
    const root = "http://127.0.0.1:8000/api/v1/"
    let response =  fetch(root+path,{
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(data => data.json())
    return response
}
export function httpFileRequest(path,file){
    var formData = new FormData()
    formData.append("file", file);
    const root = "http://127.0.0.1:8000/api/v1/"
    let response =  fetch(root+path,{
        method: "POST", 
        body: formData
    }).then(data => data.json())
    return response
}