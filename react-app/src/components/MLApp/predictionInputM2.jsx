import styles from "../../pages/MLApp.module.css"
import { httpFileRequest, httpPostRequest } from "../../utils/httpRequests";
import { useState } from "react"
import { Dropzone } from "../DragDrop";

export function PredictionInputModelo2(props){
    let [predictionInputs, setPredictionInputs] = useState([])
    let [inputFile, setInputFile] = useState([])
    
      const handleSubmit = (event) => {
        event.preventDefault();
        
        httpFileRequest("ML/TrainRedesConv/Predict",inputFile).then(data => 
            {
                
                props.setResponseAPI(data)
            })
      }
  
  

    return(
        <div className={styles.DragDropContainer}>
            <form  onSubmit={handleSubmit} className={styles.Form}>
            
            <Dropzone setInputFile={setInputFile} setInputImage={props.setInputImage}/>
            
                <input type="submit" value="Run Model" className={styles.formSubmit}/>
            </form>
            
        </div>
    )
}