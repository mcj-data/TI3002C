import styles from "../../pages/MLApp.module.css"
import { useState } from "react"
import { httpPostRequest } from "../../utils/httpRequests";
export function PredictionInputModelo1(){
    let [predictionInputs, setPredictionInputs] = useState([])
    let [responseAPI, setResponseAPI] = useState()

    const handleChange = (event) => {
        event.preventDefault();
        const name = event.target.name;
        const value = event.target.value;
        setPredictionInputs(values => ({...values, [name]: value}))
        console.log(predictionInputs)
      }
      const handleSubmit = (event) => {
        event.preventDefault();
        var processedInputs = {"X":[Object.values(predictionInputs).map(x=>parseInt(x))]}
        console.log(JSON.stringify(processedInputs))
        
        httpPostRequest("ML/predictWithModel",processedInputs).then(data => 
            {
                console.log(data)
                setResponseAPI(data.toString())
            })
      }
      var response
      if (responseAPI){
        response = "API response is..." + responseAPI
      }else{
        response = "No Response"
      }
    return(
        <div className={styles.PredictionContainer}>
            <form  onSubmit={handleSubmit} className={styles.Form}>
            <label>
                X1:<input type="text" name="X1" onChange={handleChange}/>
            </label>
            <label>
                X2:<input type="text" name="X2" onChange={handleChange}/>
            </label>
            <label>
                X3:<input type="text" name="X3" onChange={handleChange}/>
            </label>
            <label>
                X4:<input type="text" name="X4" onChange={handleChange}/>
            </label>
                <input type="submit" value="Submit" />
            </form>
            {response}
        </div>
    )
}